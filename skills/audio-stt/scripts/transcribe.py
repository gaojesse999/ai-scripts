#!/usr/bin/env python3
"""Audio Speech-to-Text transcription via Groq Whisper-large-v3.

Self-contained: requires only Python >= 3.9 standard library and ffmpeg.
No external third-party Python packages (e.g. numpy) required.

Usage:
  Single file:    transcribe.py --input path/to/audio.mp3
  Directory:      transcribe.py --input-dir path/to/folder [--pattern "*.mp3"]
  Language:       transcribe.py --input audio.mp3 --language en
  Skip existing:  transcribe.py --input-dir path/ --skip-existing
  Specify env:    transcribe.py --env-file /path/to/.skill.env

Output:
  Saved as same-name .txt file next to source audio (or in --output-dir).
  Each speech segment is written as one line.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

# ── Fix encoding on Windows consoles ──────────────────────────────────────────
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if hasattr(sys.stderr, "buffer"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# ── Groq API Constants ────────────────────────────────────────────────────────
GROQ_URL = "https://api.groq.com/openai/v1/audio/transcriptions"
GROQ_MODEL = "whisper-large-v3"
GROQ_UPLOAD_LIMIT = 24 * 1024 * 1024  # 24 MB safe ceiling
GROQ_WINDOW_SECONDS = 600.0           # 10 minutes max window for splitting
GROQ_RETRY_STATUS = {408, 409, 429, 500, 502, 503, 504}
GROQ_ATTEMPTS = 4

# Extensions ffmpeg can decode
AUDIO_EXTENSIONS = {".mp3", ".wav", ".flac", ".m4a", ".ogg", ".opus", ".aac", ".webm", ".mp4"}

# Drop segments where Whisper predicts high probability of no speech (hallucination)
NO_SPEECH_THRESHOLD = 0.80


# ── Audio Processing Helpers (pure ffmpeg / subprocess) ─────────────────────────

def check_ffmpeg() -> None:
    """Verify ffmpeg and ffprobe are available on PATH."""
    missing = []
    if not shutil.which("ffmpeg"):
        missing.append("ffmpeg")
    if not shutil.which("ffprobe"):
        missing.append("ffprobe")
    if missing:
        sys.exit(
            f"ERROR: Missing required command-line tool(s): {', '.join(missing)}\n"
            "Please install ffmpeg and make sure it is accessible via your system PATH."
        )


def media_duration(audio: Path) -> float:
    """Get audio duration in seconds via ffprobe."""
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(audio)],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    return float(out)


def to_flac16k(audio: Path, dest: Path, start: float | None = None,
               end: float | None = None) -> Path:
    """Downsample to 16 kHz mono FLAC to minimize upload size."""
    window = []
    if start is not None:
        window += ["-ss", f"{start:.3f}"]
    if end is not None:
        window += ["-to", f"{end:.3f}"]
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", *window, "-i", str(audio),
         "-ar", "16000", "-ac", "1", "-map", "0:a", "-c:a", "flac", str(dest)],
        check=True,
    )
    return dest


def silence_midpoints(audio: Path) -> list[float]:
    """Detect silence timestamps to split long audio safely at natural pauses."""
    out = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", str(audio), "-af",
         "silencedetect=n=-35dB:d=0.25", "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    starts = [float(v) for v in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(v) for v in re.findall(r"silence_end: ([\d.]+)", out)]
    return [(s + e) / 2 for s, e in zip(starts, ends)]


def upload_windows(audio: Path, tmp: Path) -> list[tuple[float, Path]]:
    """Convert audio to FLAC and slice into windows if size exceeds Groq limit."""
    whole = to_flac16k(audio, tmp / "upload.flac")
    if whole.stat().st_size <= GROQ_UPLOAD_LIMIT:
        return [(0.0, whole)]
    whole.unlink()

    duration = media_duration(audio)
    silences = silence_midpoints(audio)
    cuts: list[float] = []
    target = GROQ_WINDOW_SECONDS
    while target < duration:
        near = min(silences, key=lambda t: abs(t - target), default=None)
        floor = (cuts[-1] if cuts else 0.0) + 1.0
        usable = near is not None and abs(near - target) <= 30.0 and near > floor
        cut = near if usable else target
        cuts.append(cut)
        target = cut + GROQ_WINDOW_SECONDS

    bounds = [0.0, *cuts, duration]
    windows = []
    for index, (start, end) in enumerate(zip(bounds, bounds[1:])):
        part = to_flac16k(audio, tmp / f"upload-{index:02d}.flac", start, end)
        windows.append((start, part))
    return windows


# ── Environment & Config ──────────────────────────────────────────────────────

def find_engineering_root() -> Path:
    """Find engineering root by searching upward from script location for .skill.env or .git."""
    curr = Path(__file__).resolve().parent
    for parent in [curr, *curr.parents]:
        if (parent / ".skill.env").exists() or (parent / ".git").exists():
            return parent
    # Default to 4 levels up (.agents/skills/audio-stt/scripts/ -> root)
    return Path(__file__).resolve().parents[3]


def load_env(env_path: Path | None = None) -> dict[str, str]:
    if env_path is None:
        root = find_engineering_root()
        env_path = root / ".skill.env"

    if not env_path.exists():
        return {}

    values: dict[str, str] = {}
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


class Recognizer:
    def __init__(self, model: str, api_key: str, proxy: str = ""):
        self.model = model
        self.api_key = api_key
        self.proxy = proxy


def resolve_recognizer(env_file: Path | None = None) -> Recognizer:
    """Resolve API key and proxy from .skill.env or system environment."""
    env = load_env(env_file)
    api_key = env.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        env_location = env_file or (find_engineering_root() / ".skill.env")
        sys.exit(
            f"ERROR: GROQ_API_KEY not found in {env_location} or environment variables.\n"
            "Please create a .skill.env file with GROQ_API_KEY=gsk_... or export GROQ_API_KEY.\n"
            "Get an API key for free at: https://console.groq.com/keys"
        )
    proxy = (
        env.get("SKILL_PROXY")
        or os.environ.get("HTTPS_PROXY")
        or os.environ.get("https_proxy", "")
    )
    return Recognizer(model=GROQ_MODEL, api_key=api_key, proxy=proxy)


# ── Transcription Engine ──────────────────────────────────────────────────────

def transcribe_audio(audio_path: Path, asr: Recognizer, language: str) -> list[str]:
    """Transcribe an audio file using Groq Whisper. Returns list of lines."""
    lines: list[str] = []

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        windows = upload_windows(audio_path, tmp)

        for _offset, part in windows:
            boundary = uuid.uuid4().hex
            fields = [
                ("model", asr.model),
                ("response_format", "verbose_json"),
                ("timestamp_granularities[]", "segment"),
                ("temperature", "0"),
            ]
            if language:
                fields.append(("language", language))

            body = bytearray()
            for name, value in fields:
                body += (
                    f"--{boundary}\r\n"
                    f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
                    f"{value}\r\n"
                ).encode("utf-8")
            body += (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="file"; filename="{part.name}"\r\n'
                "Content-Type: audio/flac\r\n\r\n"
            ).encode("utf-8")
            body += part.read_bytes()
            body += f"\r\n--{boundary}--\r\n".encode("utf-8")

            opener = urllib.request.build_opener(
                urllib.request.ProxyHandler({"http": asr.proxy, "https": asr.proxy} if asr.proxy else {})
            )
            req = urllib.request.Request(
                GROQ_URL,
                data=bytes(body),
                method="POST",
                headers={
                    "Authorization": f"Bearer {asr.api_key}",
                    "Content-Type": f"multipart/form-data; boundary={boundary}",
                    "User-Agent": "audio-stt-skill/1.0",
                },
            )

            delay = 2.0
            resp_data: dict | None = None
            for attempt in range(1, GROQ_ATTEMPTS + 1):
                try:
                    with opener.open(req, timeout=300) as response:
                        resp_data = json.loads(response.read().decode("utf-8"))
                        break
                except urllib.error.HTTPError as exc:
                    detail = exc.read().decode("utf-8", "replace")[:400]
                    if exc.code not in GROQ_RETRY_STATUS or attempt == GROQ_ATTEMPTS:
                        raise RuntimeError(
                            f"NETWORK BLOCKED\n"
                            f"  Process : {sys.executable}\n"
                            f"  URL     : {GROQ_URL}\n"
                            f"  Error   : HTTP {exc.code} — {detail}"
                        )
                    wait = float(exc.headers.get("retry-after") or delay)
                    time.sleep(wait)
                    delay *= 2
                except urllib.error.URLError as exc:
                    if attempt == GROQ_ATTEMPTS:
                        raise RuntimeError(
                            f"NETWORK BLOCKED\n"
                            f"  Process : {sys.executable}\n"
                            f"  URL     : {GROQ_URL}\n"
                            f"  Error   : {type(exc).__name__}: {exc.reason}"
                        )
                    time.sleep(delay)
                    delay *= 2

            if not resp_data:
                raise RuntimeError("Groq transcription returned empty response.")

            segments = resp_data.get("segments") or []
            if segments:
                for seg in segments:
                    # Filter out hallucinated silence segments
                    if float(seg.get("no_speech_prob") or 0.0) >= NO_SPEECH_THRESHOLD:
                        continue
                    txt = str(seg.get("text") or "").strip()
                    if txt:
                        lines.append(txt)
            else:
                raw = str(resp_data.get("text") or "").strip()
                if raw:
                    lines.append(raw)

    return lines


def collect_audio_files(path: Path, pattern: str) -> list[Path]:
    """Collect audio files matching supported extensions and glob pattern."""
    return sorted(
        f for f in path.glob(pattern)
        if f.suffix.lower() in AUDIO_EXTENSIONS
    )


# ── Main Entrypoint ───────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Transcribe audio file(s) to text using Groq Whisper-large-v3."
    )
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", type=Path, help="Single audio file to transcribe.")
    group.add_argument("--input-dir", type=Path, dest="input_dir",
                       help="Directory of audio files to transcribe (batch mode).")
    ap.add_argument("--pattern", default="*",
                    help="Glob pattern for batch mode (default: '*', matched against audio extensions).")
    ap.add_argument("--language", default="zh",
                    help="Language code for Whisper (default: zh). E.g. 'en', 'ja', etc.")
    ap.add_argument("--skip-existing", action="store_true", dest="skip_existing",
                    help="Skip files whose .txt already exists.")
    ap.add_argument("--output-dir", type=Path, dest="output_dir",
                    help="Save .txt files to a different directory (default: same directory as audio).")
    ap.add_argument("--env-file", type=Path, dest="env_file",
                    help="Path to custom .skill.env file (default: searches in project root).")
    args = ap.parse_args()

    check_ffmpeg()
    asr = resolve_recognizer(args.env_file)
    print(f"Groq STT ready  model={asr.model}  proxy={'set' if asr.proxy else 'none'}", flush=True)

    if args.input:
        if not args.input.is_file():
            sys.exit(f"ERROR: File not found: {args.input}")
        audio_files = [args.input]
    else:
        if not args.input_dir.is_dir():
            sys.exit(f"ERROR: Directory not found: {args.input_dir}")
        audio_files = collect_audio_files(args.input_dir, args.pattern)
        if not audio_files:
            print(f"No supported audio files found in {args.input_dir}", flush=True)
            return
        print(f"Found {len(audio_files)} audio file(s) in {args.input_dir}:", flush=True)
        for f in audio_files:
            print(f"  {f.name}", flush=True)

    success, skipped, failed = 0, 0, 0
    for idx, audio_file in enumerate(audio_files, 1):
        out_dir = args.output_dir or audio_file.parent
        txt_file = out_dir / (audio_file.stem + ".txt")

        if args.skip_existing and txt_file.exists():
            print(f"[{idx}/{len(audio_files)}] Skip (exists): {audio_file.name}", flush=True)
            skipped += 1
            continue

        print(f"[{idx}/{len(audio_files)}] Transcribing: {audio_file.name} ...", flush=True)
        t0 = time.time()
        try:
            lines = transcribe_audio(audio_file, asr, args.language)
            out_dir.mkdir(parents=True, exist_ok=True)
            txt_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
            elapsed = time.time() - t0
            print(
                f"  → {txt_file.name}  "
                f"({len(lines)} lines, {txt_file.stat().st_size} bytes, {elapsed:.1f}s)",
                flush=True,
            )
            success += 1
        except RuntimeError as net_err:
            print(f"\n[STOPPED] Network access blocked during: {audio_file.name}", flush=True)
            print(str(net_err), flush=True)
            print("\nPlease configure your firewall/proxy and retry.", flush=True)
            failed += 1
            sys.exit(1)
        except Exception as exc:
            print(f"  ERROR: {exc}", file=sys.stderr, flush=True)
            failed += 1

    print(
        f"\nDone — success: {success}, skipped: {skipped}, failed: {failed}",
        flush=True,
    )


if __name__ == "__main__":
    main()
