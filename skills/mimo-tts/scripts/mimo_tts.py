#!/usr/bin/env python3
"""Generate WAV speech with Xiaomi MiMo V2.5 TTS."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from wave import Error as WaveError
from wave import open as wave_open


API_URL = "https://api.xiaomimimo.com/v1/chat/completions"
VALID_MODELS = {
    "mimo-v2.5-tts",
    "mimo-v2.5-tts-voicedesign",
    "mimo-v2.5-tts-voiceclone",
}


def find_project_root() -> Path:
    """Find the project root, never the Skill or script directory."""
    forced = os.environ.get("SKILL_PROJECT_ROOT")
    if forced:
        return Path(forced).expanduser().resolve()
    starts = [Path.cwd().resolve(), Path(__file__).resolve().parent]
    checked: set[Path] = set()
    for start in starts:
        current = start if start.is_dir() else start.parent
        for parent in (current, *current.parents):
            if parent in checked:
                continue
            checked.add(parent)
            if (parent / ".skill.env").is_file():
                return parent
    return Path.cwd().resolve()


PROJECT_ROOT = find_project_root()
DEFAULT_OUTPUT_ROOT = PROJECT_ROOT / "audio-outputs"
DEFAULT_ENV_FILE = PROJECT_ROOT / ".skill.env"


def load_env(path: Path) -> None:
    """Load simple KEY=VALUE pairs without adding a dependency."""
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip().strip("\"'")
        if key and key not in os.environ:
            os.environ[key] = value


def install_proxy(proxy: str | None) -> None:
    """Use a configured proxy; otherwise keep urllib's direct connection."""
    if proxy and ("xxx.xxx.xxx.xxx" in proxy or "xxxx" in proxy):
        raise ValueError("SKILL_PROXY 仍是占位地址。")
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler(
            {"http": proxy, "https": proxy} if proxy else {}
        )
    )
    urllib.request.install_opener(opener)


def clean_title(text: str) -> str:
    first = next((line.strip() for line in text.splitlines() if line.strip()), text.strip())
    first = re.sub(r"^#+\s*", "", first)
    first = re.split(r"[。！？.!?；;，,]", first, maxsplit=1)[0].strip()
    first = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", first, flags=re.UNICODE)
    first = re.sub(r"-+", "-", first).strip("-_")
    return (first[:40] or "语音合成").strip()


def read_text(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    if args.input:
        return Path(args.input).read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("请通过 --text、--input 或标准输入提供要合成的文字。")


def split_long_text(text: str, max_chars: int = 700) -> list[str]:
    """Split oversized prose at sentence boundaries before calling the API."""
    if len(text) <= max_chars:
        return [text.strip()]
    sentences = re.split(r"(?<=[。！？!?；;])", text)
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        if current and len(current) + len(sentence) > max_chars:
            chunks.append(current)
            current = ""
        current += sentence
    if current:
        chunks.append(current)
    return chunks or [text.strip()]


def split_slides(text: str) -> list[tuple[str, str]]:
    """Extract ## S01-style slide sections and discard their headings."""
    heading = re.compile(r"^\s*##\s*(S\d+)\s*[·.\-–—]\s*(.*?)\s*$")
    sections: list[tuple[str, str]] = []
    current_id: str | None = None
    current_lines: list[str] = []
    found_slide_heading = False

    for line in text.splitlines():
        match = heading.match(line)
        if match:
            found_slide_heading = True
            if current_id is not None:
                body = "\n".join(current_lines).strip()
                if body:
                    sections.append((current_id, body))
            current_id = match.group(1)
            current_lines = []
        elif current_id is not None:
            current_lines.append(line)

    if current_id is not None:
        body = "\n".join(current_lines).strip()
        if body:
            sections.append((current_id, body))

    if not found_slide_heading:
        return [("TEXT", text.strip())]

    expanded: list[tuple[str, str]] = []
    for section_id, body in sections:
        parts = split_long_text(body)
        for index, part in enumerate(parts, start=1):
            suffix = "" if len(parts) == 1 else f"-{index}"
            expanded.append((f"{section_id}{suffix}", part))
    return expanded


def make_voice(args: argparse.Namespace, model: str,
               voice_sample: str | None) -> str | None:
    if model == "mimo-v2.5-tts":
        return args.voice or "mimo_default"
    if model == "mimo-v2.5-tts-voicedesign":
        return None
    if not voice_sample:
        raise SystemExit(
            "voiceclone 模型必须通过 --voice-sample 或 MIMO_REFERENCE_VOICE "
            "指定 mp3 或 wav 音色样本。"
        )
    sample = Path(voice_sample)
    if not sample.is_absolute():
        sample = PROJECT_ROOT / sample
    sample = sample.resolve()
    if not sample.exists():
        raise SystemExit(f"参考语音文件不存在：{sample}")
    if sample.suffix.lower() not in {".mp3", ".wav"}:
        raise SystemExit("音色样本只支持 .mp3 或 .wav。")
    encoded = base64.b64encode(sample.read_bytes()).decode("ascii")
    if len(encoded) > 10 * 1024 * 1024:
        raise SystemExit("音色样本的 Base64 字符串不能超过 10 MB。")
    mime = "audio/mpeg" if sample.suffix.lower() == ".mp3" else "audio/wav"
    return f"data:{mime};base64,{encoded}"


def write_wav_with_pauses(segment_paths: list[Path], output_path: Path,
                           pause_seconds: float) -> list[float]:
    """Concatenate PCM WAV segments and insert silence between segments."""
    if not segment_paths:
        raise RuntimeError("没有可合并的音频片段。")
    durations: list[float] = []
    try:
        with wave_open(str(segment_paths[0]), "rb") as first:
            params = first.getparams()
            if params.comptype != "NONE":
                raise RuntimeError("MiMo 返回的 WAV 不是未压缩 PCM。")
            with wave_open(str(output_path), "wb") as output:
                output.setparams(params)
                for index, path in enumerate(segment_paths):
                    with wave_open(str(path), "rb") as segment:
                        if (
                            segment.getnchannels() != params.nchannels
                            or segment.getsampwidth() != params.sampwidth
                            or segment.getframerate() != params.framerate
                            or segment.getcomptype() != params.comptype
                        ):
                            raise RuntimeError(f"音频片段格式不一致：{path}")
                        frames = segment.readframes(segment.getnframes())
                        output.writeframes(frames)
                        durations.append(segment.getnframes() / params.framerate)
                    if index < len(segment_paths) - 1 and pause_seconds > 0:
                        silence_frames = round(pause_seconds * params.framerate)
                        output.writeframes(
                            b"\x00" * silence_frames * params.nchannels * params.sampwidth
                        )
    except (WaveError, EOFError) as exc:
        raise RuntimeError("无法解析 MiMo 返回的 WAV 音频。") from exc
    return durations


def request_audio(api_key: str, model: str, text: str, instruction: str | None,
                  voice: str | None, proxy: str | None) -> bytes:
    messages = []
    if instruction or model == "mimo-v2.5-tts-voicedesign":
        messages.append({"role": "user", "content": instruction or ""})
    messages.append({"role": "assistant", "content": text})
    audio = {"format": "wav"}
    if voice is not None:
        audio["voice"] = voice
    if model == "mimo-v2.5-tts-voicedesign":
        audio["optimize_text_preview"] = True
    payload = json.dumps({
        "model": model,
        "messages": messages,
        "audio": audio,
    }, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=payload,
        headers={"api-key": api_key, "Content-Type": "application/json"},
        method="POST",
    )
    strict_proxy = os.environ.get("SKILL_PROXY_STRICT", "").lower() in {"1", "true", "yes"}
    if strict_proxy and not proxy:
        raise RuntimeError("SKILL_PROXY_STRICT=1，但没有配置 SKILL_PROXY。")
    routes = [("proxy", proxy)] if strict_proxy else (
        [("proxy", proxy), ("direct", None)] if proxy else [("direct", None)]
    )
    last_error: Exception | None = None
    body = None
    for route_name, route_proxy in routes:
        try:
            install_proxy(route_proxy)
            with urllib.request.urlopen(request, timeout=180) as response:
                body = json.loads(response.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            if route_proxy is not None and exc.code in {407, 502, 503, 504}:
                last_error = exc
                continue
            raise RuntimeError(f"MiMo API HTTP {exc.code}: {detail}") from exc
        except (urllib.error.URLError, ValueError) as exc:
            last_error = exc
            continue
    else:
        reason = getattr(last_error, "reason", str(last_error))
        if strict_proxy:
            message = (
                f"通过 SKILL_PROXY 连接 MiMo API 失败: {reason}。"
                "严格代理模式已阻止直连，请检查调用方传入的 .skill.env。"
            )
        elif proxy:
            message = (
                "先尝试代理后直连 MiMo API 仍失败"
                f": {reason}。网络可能受限，请在调用方指定的 .skill.env 中配置 SKILL_PROXY。"
            )
        else:
            message = (
                f"直连 MiMo API 失败: {reason}。网络可能受限，"
                "请在调用方指定的 .skill.env 中配置 SKILL_PROXY。"
            )
        raise RuntimeError(message) from last_error

    try:
        encoded = body["choices"][0]["message"]["audio"]["data"]
        return base64.b64decode(encoded)
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise RuntimeError(f"MiMo 返回中没有可用音频: {json.dumps(body, ensure_ascii=False)[:1000]}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="使用 Xiaomi MiMo V2.5 TTS 生成 WAV 音频。")
    parser.add_argument("--text", help="直接提供待合成文字")
    parser.add_argument("--input", help="UTF-8 文本或 Markdown 文件")
    parser.add_argument("--title", help="输出目录标题；不提供时从文字自动提取")
    parser.add_argument(
        "--model",
        default="auto",
        choices=["auto", *sorted(VALID_MODELS)],
        help="默认 auto：根据 MIMO_REFERENCE_VOICE 自动选择普通合成或 clone",
    )
    parser.add_argument("--voice", help="预置音色 ID，例如 冰糖、茉莉、苏打、白桦、Milo")
    parser.add_argument("--instruction", help="自然语言音色/情绪/语速指导")
    parser.add_argument("--voice-sample", help="voiceclone 的 mp3/wav 音色样本")
    parser.add_argument(
        "--pause",
        type=float,
        default=1.0,
        help="不同 slide/片段之间的静音秒数，默认 1.0",
    )
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT))
    parser.add_argument(
        "--env-file",
        default=str(DEFAULT_ENV_FILE),
        help="环境文件，默认读取当前工程根目录的 .skill.env",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_env(Path(args.env_file))
    api_key = os.environ.get("MIMO_API_KEY")
    if not api_key:
        raise SystemExit(f"未找到 MIMO_API_KEY，请在 {args.env_file} 中配置，或先导出环境变量。")
    proxy = os.environ.get("SKILL_PROXY") or os.environ.get("MIMO_PROXY") or None
    reference_voice = os.environ.get("MIMO_REFERENCE_VOICE") or None
    model = args.model
    if model == "auto":
        model = "mimo-v2.5-tts-voiceclone" if reference_voice else "mimo-v2.5-tts"
    voice_sample = args.voice_sample or reference_voice
    text = read_text(args).strip()
    if not text:
        raise SystemExit("待合成文字为空。")
    if args.pause < 0:
        raise SystemExit("--pause 不能小于 0。")
    voice = make_voice(args, model, voice_sample)
    title = clean_title(args.title or text)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = Path(args.output_root) / f"{title}-{stamp}"
    output_dir.mkdir(parents=True, exist_ok=False)
    segments = split_slides(text)
    segment_dir = output_dir / "segments"
    segment_dir.mkdir()
    segment_paths: list[Path] = []
    segment_manifest = []
    for index, (section_id, segment_text) in enumerate(segments, start=1):
        print(f"合成片段 {index}/{len(segments)}: {section_id}", flush=True)
        audio = request_audio(
            api_key, model, segment_text, args.instruction, voice, proxy
        )
        segment_path = segment_dir / f"{section_id}.wav"
        segment_path.write_bytes(audio)
        segment_paths.append(segment_path)
        segment_manifest.append({
            "id": section_id,
            "text": segment_text,
            "audio": str(segment_path),
        })
    audio_path = output_dir / "narration.wav"
    durations = write_wav_with_pauses(segment_paths, audio_path, args.pause)
    for item, duration in zip(segment_manifest, durations):
        item["duration_seconds"] = round(duration, 3)
    manifest = {
        "model": model,
        "voice": args.voice or ("voiceclone-sample" if voice_sample else "mimo_default"),
        "instruction": args.instruction,
        "source": args.input or "inline",
        "pause_seconds": args.pause,
        "segments": segment_manifest,
        "audio": str(audio_path),
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    (output_dir / "tts-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(audio_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
