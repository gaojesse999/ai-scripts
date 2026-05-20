#!/usr/bin/env python3
"""Local video text-track preparation.

Priority chain (each step degrades to the next on failure):
  1. Embedded subtitle track (requires ffmpeg/ffprobe; prefer zh -> en -> first)
  2. External sidecar subtitle file (same dir, same stem; multilang: prefer zh)
  3. image_only fallback

When a subtitle source is found, writes:
  - subtitles.json       (structured segments)
  - subtitles.txt        (plain text)
  - text_segments.json   (unified timeline segments used by the analyzer)
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


SUB_EXTS = [".srt", ".vtt", ".ass", ".ssa"]
LANG_PRIORITY = ["zh", "chi", "zho", "zh-cn", "zh-hans", "zh-tw", "zh-hant", "en", "eng"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Local video text-track preparation")
    parser.add_argument("video", help="Path to the local video file")
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output directory (must be the same dir used by prepare.py)",
    )
    return parser.parse_args()


# ---------- ffmpeg / ffprobe path detection ----------

def find_tool(name: str) -> str | None:
    return shutil.which(name)


# ---------- Subtitle parsers ----------

_TIME_RE_SRT = re.compile(
    r"(\d+):(\d{2}):(\d{2})[,.](\d{1,3})\s*-->\s*(\d+):(\d{2}):(\d{2})[,.](\d{1,3})"
)
_TIME_RE_VTT = _TIME_RE_SRT  # VTT uses '.' but we already accept both.


def _ts_to_seconds(h: str, m: str, s: str, ms: str) -> float:
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms.ljust(3, "0")) / 1000.0


def parse_srt_vtt(text: str) -> list[dict]:
    segments: list[dict] = []
    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Strip WEBVTT header
    if text.lstrip().upper().startswith("WEBVTT"):
        text = text.split("\n", 1)[1] if "\n" in text else ""

    blocks = re.split(r"\n\s*\n", text.strip())
    for block in blocks:
        lines = [ln for ln in block.split("\n") if ln.strip()]
        if not lines:
            continue
        time_line_idx = None
        for i, ln in enumerate(lines):
            if "-->" in ln:
                time_line_idx = i
                break
        if time_line_idx is None:
            continue
        m = _TIME_RE_SRT.search(lines[time_line_idx])
        if not m:
            continue
        start = _ts_to_seconds(m.group(1), m.group(2), m.group(3), m.group(4))
        end = _ts_to_seconds(m.group(5), m.group(6), m.group(7), m.group(8))
        content_lines = lines[time_line_idx + 1 :]
        content = "\n".join(content_lines).strip()
        # Strip simple WEBVTT/SRT inline tags like <i>, <b>, {\an8}
        content = re.sub(r"<[^>]+>", "", content)
        content = re.sub(r"\{\\[^}]+\}", "", content)
        if not content:
            continue
        segments.append({"start": round(start, 3), "end": round(end, 3), "text": content})
    return segments


_ASS_DIALOGUE_RE = re.compile(
    r"^Dialogue:\s*[^,]*,\s*"
    r"(\d+):(\d{2}):(\d{2})\.(\d{1,3}),\s*"
    r"(\d+):(\d{2}):(\d{2})\.(\d{1,3}),"
    r".*?,(?:[^,]*,){5}(.*)$"
)


def parse_ass(text: str) -> list[dict]:
    segments: list[dict] = []
    for line in text.splitlines():
        m = _ASS_DIALOGUE_RE.match(line.strip())
        if not m:
            continue
        start = _ts_to_seconds(m.group(1), m.group(2), m.group(3), m.group(4))
        end = _ts_to_seconds(m.group(5), m.group(6), m.group(7), m.group(8))
        raw = m.group(9)
        content = re.sub(r"\{[^}]*\}", "", raw).replace("\\N", "\n").replace("\\n", "\n").strip()
        if not content:
            continue
        segments.append({"start": round(start, 3), "end": round(end, 3), "text": content})
    return segments


def parse_subtitle_text(text: str, ext: str) -> list[dict]:
    ext = ext.lower()
    if ext in (".srt", ".vtt"):
        return parse_srt_vtt(text)
    if ext in (".ass", ".ssa"):
        return parse_ass(text)
    raise ValueError(f"Unsupported subtitle extension: {ext}")


def read_text_safely(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "utf-16", "gbk", "cp936", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("subtitle", b"", 0, 1, f"Cannot decode {path}")


# ---------- Source 1: embedded subtitle ----------

def _lang_rank(language: str | None, title: str | None) -> int:
    """Lower rank == higher priority."""
    blob = f"{(language or '').lower()} {(title or '').lower()}"
    for i, lang in enumerate(LANG_PRIORITY):
        if lang in blob:
            return i
    return 9999


def try_embedded_subtitle(video_path: Path) -> tuple[list[dict], dict] | None:
    ffprobe = find_tool("ffprobe")
    ffmpeg = find_tool("ffmpeg")
    if not ffprobe or not ffmpeg:
        return None
    try:
        probe = subprocess.run(
            [
                ffprobe,
                "-v",
                "error",
                "-select_streams",
                "s",
                "-show_entries",
                "stream=index:stream_tags=language,title:stream=codec_name",
                "-of",
                "json",
                str(video_path),
            ],
            capture_output=True,
            text=True,
            timeout=60,
            check=True,
        )
    except (subprocess.SubprocessError, OSError):
        return None

    try:
        data = json.loads(probe.stdout or "{}")
    except json.JSONDecodeError:
        return None
    streams = data.get("streams") or []
    if not streams:
        return None

    ranked = sorted(
        enumerate(streams),
        key=lambda kv: (
            _lang_rank((kv[1].get("tags") or {}).get("language"), (kv[1].get("tags") or {}).get("title")),
            kv[0],
        ),
    )

    for stream_order, stream in ranked:
        codec = (stream.get("codec_name") or "").lower()
        # ffmpeg can convert text-based subs to srt; bitmap subs (e.g. dvd_subtitle, hdmv_pgs_subtitle) can't.
        if codec in {"dvd_subtitle", "hdmv_pgs_subtitle", "dvb_subtitle", "xsub"}:
            continue
        try:
            extract = subprocess.run(
                [
                    ffmpeg,
                    "-v",
                    "error",
                    "-i",
                    str(video_path),
                    "-map",
                    f"0:s:{stream_order}",
                    "-f",
                    "srt",
                    "-",
                ],
                capture_output=True,
                timeout=120,
                check=True,
            )
        except (subprocess.SubprocessError, OSError):
            continue
        raw = extract.stdout
        if not raw:
            continue
        try:
            text = raw.decode("utf-8", errors="ignore")
        except Exception:
            continue
        try:
            segments = parse_srt_vtt(text)
        except Exception:
            continue
        if not segments:
            continue
        info = {
            "stream_order": stream_order,
            "codec": codec,
            "language": (stream.get("tags") or {}).get("language"),
            "title": (stream.get("tags") or {}).get("title"),
        }
        return segments, {"source": "embedded", "track": info}
    return None


# ---------- Source 2: external sidecar subtitle ----------

def try_external_subtitle(video_path: Path) -> tuple[list[dict], dict] | None:
    parent = video_path.parent
    stem = video_path.stem
    candidates: list[Path] = []
    try:
        siblings = list(parent.iterdir())
    except OSError:
        siblings = []
    for entry in siblings:
        if not entry.is_file():
            continue
        if entry.suffix.lower() not in SUB_EXTS:
            continue
        name = entry.stem
        if name == stem or name.startswith(stem + "."):
            candidates.append(entry)
    if not candidates:
        return None

    def rank(path: Path) -> tuple[int, int, str]:
        # Lang from segment after stem (e.g. "video.zh.srt" -> "zh")
        suffix = path.stem[len(stem) :].lstrip(".") if path.stem != stem else ""
        lang_rank = _lang_rank(suffix, path.name)
        ext_rank = SUB_EXTS.index(path.suffix.lower())
        return (lang_rank, ext_rank, path.name)

    candidates.sort(key=rank)
    for path in candidates:
        try:
            text = read_text_safely(path)
        except Exception:
            continue
        try:
            segments = parse_subtitle_text(text, path.suffix)
        except Exception:
            continue
        if not segments:
            continue
        return segments, {"source": "external", "file": str(path)}
    return None


# ---------- Output ----------

def write_outputs(output_dir: Path, segments: list[dict], origin: dict) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)

    subtitles_json = {
        "origin": origin,
        "segment_count": len(segments),
        "segments": segments,
    }
    (output_dir / "subtitles.json").write_text(
        json.dumps(subtitles_json, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (output_dir / "subtitles.txt").write_text(
        "\n".join(seg["text"] for seg in segments) + "\n",
        encoding="utf-8",
    )
    (output_dir / "text_segments.json").write_text(
        json.dumps(
            {
                "source": origin.get("source"),
                "segment_count": len(segments),
                "segments": segments,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    return {
        "mode": "subtitle",
        "subtitle_count": len(segments),
        "origin": origin,
        "files": {
            "subtitles_json": str(output_dir / "subtitles.json"),
            "subtitles_txt": str(output_dir / "subtitles.txt"),
            "text_segments_json": str(output_dir / "text_segments.json"),
        },
    }


def main() -> int:
    args = parse_args()
    video_path = Path(args.video).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    if not video_path.is_file():
        raise FileNotFoundError(f"Video file not found: {video_path}")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: embedded
    result = None
    try:
        result = try_embedded_subtitle(video_path)
    except Exception as exc:
        print(f"[WARN] embedded subtitle probe failed: {exc}", file=sys.stderr)

    # Step 2: external
    if result is None:
        try:
            result = try_external_subtitle(video_path)
        except Exception as exc:
            print(f"[WARN] external subtitle probe failed: {exc}", file=sys.stderr)

    if result is None:
        payload = {"mode": "image_only", "reason": "subtitle_unavailable"}
        print(json.dumps(payload, ensure_ascii=False))
        return 0

    segments, origin = result
    payload = write_outputs(output_dir, segments, origin)
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"[ERROR] {exc}", file=sys.stderr)
        raise SystemExit(1)
