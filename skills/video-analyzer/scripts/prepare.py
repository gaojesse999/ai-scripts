#!/usr/bin/env python3
"""Local video prepare pipeline: extract frames + adjacent-frame dedup.

Reads a single local video file, samples frames at the requested fps into
`<out>/images_raw/`, then deduplicates adjacent near-duplicates via pHash and
copies the kept frames into `<out>/images/`, renumbered.

Output directory rules:
- If `-o/--output` is provided, use it verbatim.
- Otherwise, default to a sibling directory of the video named after the video
  filename (without extension).
- If the resolved output directory already exists, append `_YYYYMMDD-HHMMSS`
  to preserve previous results.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import shutil
import sys
from pathlib import Path

import cv2
from PIL import Image
import imagehash


DEFAULT_VIDEO_EXTS = {".mp4", ".mkv", ".mov", ".webm", ".m4v"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Local video prepare pipeline")
    parser.add_argument("video", help="Path to a local video file")
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output directory (default: <video parent>/<video stem>/)",
    )
    parser.add_argument("--fps", type=float, default=1.0, help="Target extracted frames per second")
    parser.add_argument(
        "--similarity",
        type=float,
        default=0.80,
        help="Adjacent-frame similarity threshold for deduplication (0-1)",
    )
    parser.add_argument(
        "--no-dedup",
        action="store_true",
        help="Disable adjacent-frame deduplication",
    )
    return parser.parse_args()


def resolve_output_dir(video_path: Path, explicit: str | None) -> Path:
    if explicit:
        base = Path(explicit).resolve()
    else:
        base = (video_path.parent / video_path.stem).resolve()

    if not base.exists():
        return base

    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = base.with_name(f"{base.name}_{stamp}")
    # In the extremely unlikely event the stamped path also exists, append a counter.
    counter = 1
    while candidate.exists():
        counter += 1
        candidate = base.with_name(f"{base.name}_{stamp}_{counter}")
    return candidate


def extract_frames(video_path: Path, raw_dir: Path, target_fps: float) -> tuple[list[dict], dict]:
    capture = cv2.VideoCapture(str(video_path))
    if not capture.isOpened():
        raise RuntimeError(
            f"Unable to open video: {video_path}. "
            "OpenCV+ffmpeg backend may not support this container; try converting to .mp4."
        )

    native_fps = capture.get(cv2.CAP_PROP_FPS) or 25.0
    if native_fps <= 0:
        native_fps = 25.0
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH) or 0)
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    duration = total_frames / native_fps if native_fps else 0.0

    frame_interval = max(native_fps / target_fps, 1.0)

    saved: list[dict] = []
    next_capture = 0.0
    frame_index = 0.0

    while True:
        ok, frame = capture.read()
        if not ok:
            break
        if frame_index + 1e-9 >= next_capture:
            timestamp = capture.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
            file_name = f"frame_{len(saved) + 1:04d}.jpg"
            file_path = raw_dir / file_name
            if not cv2.imwrite(str(file_path), frame):
                raise RuntimeError(f"Unable to save frame: {file_path}")
            saved.append({"file": file_name, "timestamp": round(timestamp, 3)})
            next_capture += frame_interval
        frame_index += 1.0

    capture.release()
    info = {
        "native_fps": native_fps,
        "width": width,
        "height": height,
        "duration": round(duration, 3),
        "source_total_frames": total_frames,
    }
    return saved, info


def phash_for(path: Path) -> imagehash.ImageHash:
    with Image.open(path) as image:
        return imagehash.phash(image, hash_size=8)


def deduplicate_frames(
    raw_dir: Path,
    final_dir: Path,
    frames: list[dict],
    threshold: float,
) -> list[dict]:
    kept: list[dict] = []
    previous_hash = None
    for index, frame in enumerate(frames):
        source = raw_dir / frame["file"]
        current_hash = phash_for(source)
        if previous_hash is None:
            keep = True
            similarity = None
        else:
            distance = previous_hash - current_hash
            similarity = 1.0 - (distance / 64.0)
            keep = similarity <= threshold
        previous_hash = current_hash
        if not keep:
            continue
        target_name = f"frame_{len(kept) + 1:04d}.jpg"
        shutil.copy2(source, final_dir / target_name)
        kept.append(
            {
                "file": target_name,
                "source_file": frame["file"],
                "timestamp": frame["timestamp"],
                "adjacent_similarity": (round(similarity, 4) if similarity is not None else None),
            }
        )
    return kept


def copy_without_dedup(raw_dir: Path, final_dir: Path, frames: list[dict]) -> list[dict]:
    copied: list[dict] = []
    for frame in frames:
        source = raw_dir / frame["file"]
        target_name = frame["file"]
        shutil.copy2(source, final_dir / target_name)
        copied.append(
            {
                "file": target_name,
                "source_file": target_name,
                "timestamp": frame["timestamp"],
                "adjacent_similarity": None,
            }
        )
    return copied


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    video_path = Path(args.video).expanduser().resolve()
    if not video_path.is_file():
        raise FileNotFoundError(f"Video file not found: {video_path}")
    ext = video_path.suffix.lower()
    if ext not in DEFAULT_VIDEO_EXTS:
        print(
            f"[WARN] Extension '{ext}' is outside the supported default set "
            f"{sorted(DEFAULT_VIDEO_EXTS)}. Proceeding; will error out if OpenCV cannot decode.",
            file=sys.stderr,
        )

    output_dir = resolve_output_dir(video_path, args.output)
    raw_dir = output_dir / "images_raw"
    final_dir = output_dir / "images"
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)
    final_dir.mkdir(parents=True, exist_ok=True)

    print(f"[INFO] Video: {video_path}")
    print(f"[INFO] Output: {output_dir}")
    print(f"[INFO] Extracting frames at {args.fps} fps")
    raw_frames, source_info = extract_frames(video_path, raw_dir, args.fps)
    print(f"[INFO] Extracted {len(raw_frames)} raw frames")

    if args.no_dedup:
        kept_frames = copy_without_dedup(raw_dir, final_dir, raw_frames)
    else:
        kept_frames = deduplicate_frames(raw_dir, final_dir, raw_frames, args.similarity)
    print(f"[INFO] Retained {len(kept_frames)} frames after dedup")

    metadata = {
        "source_path": str(video_path),
        "source_name": video_path.name,
        "output_dir": str(output_dir),
        "fps_target": args.fps,
        "native_fps": source_info["native_fps"],
        "width": source_info["width"],
        "height": source_info["height"],
        "duration": source_info["duration"],
        "source_total_frames": source_info["source_total_frames"],
        "raw_frame_count": len(raw_frames),
        "final_frame_count": len(kept_frames),
        "similarity_threshold": (None if args.no_dedup else args.similarity),
        "dedup_enabled": not args.no_dedup,
    }
    write_json(output_dir / "metadata.json", metadata)
    write_json(output_dir / "frames.json", {"frames": kept_frames})

    summary = {
        "output_dir": str(output_dir),
        "raw_frame_count": len(raw_frames),
        "final_frame_count": len(kept_frames),
    }
    print("[OK] " + json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"[ERROR] {exc}", file=sys.stderr)
        raise SystemExit(1)
