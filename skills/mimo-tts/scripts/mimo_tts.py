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


API_URL = "https://api.xiaomimimo.com/v1/chat/completions"
DEFAULT_OUTPUT_ROOT = Path("audio-outputs")
DEFAULT_ENV_FILE = Path(".mimo.env")
VALID_MODELS = {
    "mimo-v2.5-tts",
    "mimo-v2.5-tts-voicedesign",
    "mimo-v2.5-tts-voiceclone",
}


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
        raise SystemExit("MIMO_PROXY 仍是占位地址，请填写真实代理，或删除该配置以直连。")
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


def make_voice(args: argparse.Namespace) -> str | None:
    if args.model == "mimo-v2.5-tts":
        return args.voice or "mimo_default"
    if args.model == "mimo-v2.5-tts-voicedesign":
        return None
    if not args.voice_sample:
        raise SystemExit("voiceclone 模型必须通过 --voice-sample 指定 mp3 或 wav 音色样本。")
    sample = Path(args.voice_sample)
    if sample.suffix.lower() not in {".mp3", ".wav"}:
        raise SystemExit("音色样本只支持 .mp3 或 .wav。")
    encoded = base64.b64encode(sample.read_bytes()).decode("ascii")
    if len(encoded) > 10 * 1024 * 1024:
        raise SystemExit("音色样本的 Base64 字符串不能超过 10 MB。")
    mime = "audio/mpeg" if sample.suffix.lower() == ".mp3" else "audio/wav"
    return f"data:{mime};base64,{encoded}"


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
    install_proxy(proxy)
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"MiMo API HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        route = f"代理 {proxy}" if proxy else "直连"
        hint = "如网络受限，请在 .mimo.env 中配置 MIMO_PROXY。" if not proxy else "请检查代理地址、端口和代理服务状态。"
        raise RuntimeError(f"通过{route}无法连接 MiMo API: {exc.reason}。{hint}") from exc
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
    parser.add_argument("--model", default="mimo-v2.5-tts", choices=sorted(VALID_MODELS))
    parser.add_argument("--voice", help="预置音色 ID，例如 冰糖、茉莉、苏打、白桦、Milo")
    parser.add_argument("--instruction", help="自然语言音色/情绪/语速指导")
    parser.add_argument("--voice-sample", help="voiceclone 的 mp3/wav 音色样本")
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT))
    parser.add_argument("--env-file", default=str(DEFAULT_ENV_FILE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_env(Path(args.env_file))
    api_key = os.environ.get("MIMO_API_KEY")
    if not api_key:
        raise SystemExit(f"未找到 MIMO_API_KEY，请在 {args.env_file} 中配置，或先导出环境变量。")
    proxy = os.environ.get("MIMO_PROXY") or None
    text = read_text(args).strip()
    if not text:
        raise SystemExit("待合成文字为空。")
    voice = make_voice(args)
    title = clean_title(args.title or text)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = Path(args.output_root) / f"{title}-{stamp}"
    output_dir.mkdir(parents=True, exist_ok=False)
    audio = request_audio(api_key, args.model, text, args.instruction, voice, proxy)
    audio_path = output_dir / "narration.wav"
    audio_path.write_bytes(audio)
    manifest = {
        "model": args.model,
        "voice": args.voice or ("voiceclone-sample" if args.voice_sample else "mimo_default"),
        "instruction": args.instruction,
        "source": args.input or "inline",
        "text": text,
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
