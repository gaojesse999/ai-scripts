#!/usr/bin/env python3
"""Bilibili Video Analyzer - Prepare Script (Python port).

This script is a one-to-one port of `scripts/prepare.cs` from the
`bilibili-analyzer` skill. It downloads a Bilibili video and extracts/dedupes
frames using ffmpeg. CLI arguments, defaults, output structure and console
log messages intentionally mirror the C# version.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
from typing import List, Optional

import requests


# ============================================================================
# Helpers
# ============================================================================


def get_arg_value(args: List[str], *names: str) -> Optional[str]:
    for i in range(len(args) - 1):
        if args[i] in names:
            return args[i + 1]
    return None


def print_help() -> None:
    print(r"""
Bilibili Video Analyzer - Prepare Script

Usage:
        From the skill root:
            python scripts/prepare.py <url> [options]

        From any directory:
            python <path-to-skill>/scripts/prepare.py <url> [options]

Arguments:
  url                    Bilibili video URL (required)
                         Supports multi-part videos: ...?p=4

Options:
  -o, --output <dir>     Output directory (default: current)
  --fps <value>          Frames per second (auto if omitted:
                           <10min: 1.0, 10-30min: 0.5, >30min: 0.2)
  --similarity <value>   Similarity threshold for deduplication (default: 0.65)
  --no-dedup             Disable frame deduplication (still copies to images/)
  --video-only           Only download video, skip frame extraction
    --frames-only          Only extract frames (requires existing video.mp4;
                                                     pass --fps explicitly because auto fps is only
                                                     available when video metadata is fetched)
  -h, --help             Show this help

Output Structure:
  <output>/video.mp4              Downloaded video
  <output>/images_raw/            All extracted frames (raw)
  <output>/images/                Deduplicated frames (for analysis)
  <output>/dedup_manifest.json    Raw-to-output frame mapping

Examples:
    cd <skill-root>
    python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output
    python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=4" -o ./output
    python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --fps 0.5
    python scripts/prepare.py dummy-url -o ./output --frames-only --fps 0.5

Deduplication:
  Each frame is compared against the last kept frame.
  Consecutive similar frames are fully collapsed (only the first is kept).
  Uses ffmpeg SSIM/PSNR for accurate similarity calculation.

Download robustness:
    The downloader uses HTTP/1.1, resume, retry, and backup_url fallback for
    Bilibili CDN interruptions.

Requirements:
  - Python 3.8+ with `requests`
  - ffmpeg: https://ffmpeg.org/download.html
""")


def extract_bvid(url: str) -> Optional[str]:
    # BV ID is exactly 12 characters: BV + 10 alphanumeric chars
    m = re.search(r"BV[a-zA-Z0-9]{10}", url)
    return m.group(0) if m else None


def extract_page_number(url: str) -> int:
    m = re.search(r"[?&]p=(\d+)", url)
    if m:
        try:
            page = int(m.group(1))
            if page > 0:
                return page
        except ValueError:
            pass
    return 1


def find_executable(*names: str) -> Optional[str]:
    for name in names:
        path = shutil.which(name)
        if path:
            return path

    if sys.platform.startswith("win"):
        common_paths = [
            r"C:\ffmpeg\bin",
            r"C:\Program Files\ffmpeg\bin",
            r"C:\tools\ffmpeg\bin",
            os.path.join(os.path.expanduser("~"), "scoop", "shims"),
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "WinGet", "Links"),
        ]
        for base in common_paths:
            for name in names:
                full = os.path.join(base, name)
                if os.path.isfile(full):
                    return full
    return None


def create_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Referer": "https://www.bilibili.com",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
    })
    return s


def clean_directory(directory: str) -> None:
    if os.path.isdir(directory):
        old_files = [f for f in os.listdir(directory) if f.startswith("frame_") and f.endswith(".jpg")]
        if old_files:
            print(f"[INFO] Cleaning {len(old_files)} old frames from {directory}/")
            for f in old_files:
                try:
                    os.remove(os.path.join(directory, f))
                except OSError:
                    pass


# ============================================================================
# Core flow
# ============================================================================


def download_bilibili_video(url: str, output_path: str) -> bool:
    print(f"[INFO] Downloading video: {url}")

    try:
        bvid = extract_bvid(url)
        if not bvid:
            print("[ERROR] Invalid Bilibili URL, cannot extract BV ID")
            return False

        page_num = extract_page_number(url)
        print(f"[INFO] BV ID: {bvid}")
        if page_num > 1:
            print(f"[INFO] Page: P{page_num}")

        session = create_session()

        # Step 1: video info
        print("[INFO] Fetching video info...")
        info_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
        info_resp = session.get(info_url, timeout=60)
        info_resp.raise_for_status()
        info = info_resp.json()

        if info.get("code") != 0:
            print(f"[ERROR] Failed to get video info: {info.get('message')}")
            return False

        data = info["data"]
        title = data.get("title")
        total_duration = int(data.get("duration", 0))
        selected_duration = total_duration

        pages = data.get("pages") or []
        if pages:
            if page_num > len(pages):
                print(f"[ERROR] Page P{page_num} not found, video has {len(pages)} pages")
                return False
            page = pages[page_num - 1]
            cid = int(page["cid"])
            if "part" in page:
                print(f"[INFO] Part: {page['part']}")
            if "duration" in page:
                selected_duration = int(page["duration"])
        else:
            cid = int(data["cid"])

        print(f"[INFO] Title: {title}")
        if selected_duration != total_duration:
            print(f"[INFO] Total BV duration: {total_duration}s ({total_duration / 60.0:.1f} min)")
            print(f"[INFO] Selected page duration: {selected_duration}s ({selected_duration / 60.0:.1f} min)")
        else:
            print(f"[INFO] Duration: {selected_duration}s ({selected_duration / 60.0:.1f} min)")

        # Auto-fps based on selected page duration
        global _fps, _fps_explicit  # noqa: PLW0603
        if not _fps_explicit:
            if selected_duration < 600:
                _fps = 1.0
            elif selected_duration < 1800:
                _fps = 0.5
            else:
                _fps = 0.2
            print(f"[INFO] Auto-selected fps={_fps} based on selected duration")

        print(f"[INFO] CID: {cid}")

        # Step 2: playback URL
        print("[INFO] Fetching playback URL...")
        play_url = f"https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&qn=80&fnval=1"
        play_resp = session.get(play_url, timeout=60)
        play_resp.raise_for_status()
        play = play_resp.json()

        if play.get("code") != 0:
            print(f"[ERROR] Failed to get playback URL: {play.get('message')}")
            return False

        durl = play["data"]["durl"][0]
        video_url = durl.get("url")
        size = int(durl.get("size", 0))

        candidate_urls: List[str] = []
        if video_url:
            candidate_urls.append(video_url)
        for backup in durl.get("backup_url", []) or []:
            if backup and backup not in candidate_urls:
                candidate_urls.append(backup)

        if not candidate_urls:
            print("[ERROR] No playable video URL returned by Bilibili API")
            return False

        print(f"[INFO] Video size: {size / 1024.0 / 1024.0:.1f} MB")
        print(f"[INFO] Candidate download URLs: {len(candidate_urls)}")

        # Step 3: download
        print("[INFO] Downloading video file...")
        if not download_file_with_resume(session, candidate_urls,
                                         f"https://www.bilibili.com/video/{bvid}",
                                         output_path, size):
            return False

        print(f"[OK] Video downloaded: {output_path}")
        return True

    except requests.RequestException as ex:
        print(f"[ERROR] Network error: {ex}")
        return False
    except (ValueError, KeyError) as ex:
        print(f"[ERROR] Failed to parse API response: {ex}")
        return False
    except Exception as ex:  # noqa: BLE001
        print(f"[ERROR] Download failed: {ex}")
        return False


def download_file_with_resume(session: requests.Session,
                              candidate_urls: List[str],
                              referer: str,
                              output_path: str,
                              expected_size: int) -> bool:
    max_attempts = 12
    last_error: Optional[str] = None

    if os.path.exists(output_path) and expected_size > 0:
        existing_size = os.path.getsize(output_path)
        if existing_size == expected_size:
            print("[INFO] Existing video.mp4 already matches expected size, skipping download")
            print("[INFO] Progress: 100%")
            return True
        if existing_size > expected_size:
            print("[WARN] Existing video.mp4 is larger than expected size, restarting download")
            os.remove(output_path)

    for attempt in range(1, max_attempts + 1):
        url = candidate_urls[(attempt - 1) % len(candidate_urls)]
        file_length = os.path.getsize(output_path) if os.path.exists(output_path) else 0

        if expected_size > 0 and file_length == expected_size:
            print("[INFO] Progress: 100%")
            return True

        try:
            resume_note = f"(resuming from {file_length / 1024.0 / 1024.0:.1f} MB)" if file_length > 0 else ""
            print(f"[INFO] Download attempt {attempt}/{max_attempts} {resume_note}")
            if attempt > 1 or len(candidate_urls) > 1:
                print(f"[INFO] Source URL #{((attempt - 1) % len(candidate_urls)) + 1}")

            headers = {"Referer": referer}
            if file_length > 0:
                headers["Range"] = f"bytes={file_length}-"

            with session.get(url, headers=headers, stream=True, timeout=(60, 1800)) as resp:
                if file_length > 0 and resp.status_code == 416:
                    if expected_size > 0 and file_length >= expected_size:
                        print("[INFO] Server reported full file already present locally")
                        print("[INFO] Progress: 100%")
                        return True
                    print("[WARN] Server rejected resume range, restarting from byte 0")
                    os.remove(output_path)
                    file_length = 0
                    continue

                resp.raise_for_status()

                resume_accepted = file_length == 0 or resp.status_code == 206
                if not resume_accepted and file_length > 0:
                    print("[WARN] Server ignored resume request, restarting full download")
                    os.remove(output_path)
                    file_length = 0

                content_len = resp.headers.get("Content-Length")
                content_len_int = int(content_len) if content_len and content_len.isdigit() else 0
                total_bytes = expected_size if expected_size > 0 else content_len_int + file_length
                if total_bytes <= 0:
                    total_bytes = 1

                mode = "ab" if file_length > 0 else "wb"
                total_read = file_length
                last_progress = int(total_read * 100 / total_bytes) if total_bytes > 0 else -1
                if 10 <= last_progress < 100:
                    print(f"[INFO] Progress: {last_progress}%")

                with open(output_path, mode) as f:
                    for chunk in resp.iter_content(chunk_size=81920):
                        if not chunk:
                            continue
                        f.write(chunk)
                        total_read += len(chunk)
                        progress = int(total_read * 100 / total_bytes)
                        if progress != last_progress and (progress % 10 == 0 or progress == 100):
                            print(f"[INFO] Progress: {progress}%")
                            last_progress = progress

                if expected_size > 0 and total_read < expected_size:
                    raise IOError(
                        f"The response ended prematurely, with at least "
                        f"{expected_size - total_read} additional bytes expected."
                    )

                if last_progress != 100:
                    print("[INFO] Progress: 100%")

                return True

        except Exception as ex:  # noqa: BLE001
            last_error = str(ex)
            if attempt < max_attempts:
                print(f"[WARN] Download attempt {attempt} failed: {ex}")
                time.sleep(min(attempt, 5))
            else:
                break

    print(f"[ERROR] Download failed after {max_attempts} attempts: {last_error}")
    return False


def extract_frames(video_path: str, output_dir: str, fps: float) -> bool:
    print(f"[INFO] Extracting frames (fps={fps})")

    ffmpeg = find_executable("ffmpeg", "ffmpeg.exe")
    if ffmpeg is None:
        print("[ERROR] ffmpeg not found!")
        print("        Windows: choco install ffmpeg / scoop install ffmpeg")
        print("        macOS: brew install ffmpeg")
        print("        Linux: sudo apt install ffmpeg")
        return False

    os.makedirs(output_dir, exist_ok=True)
    output_pattern = os.path.join(output_dir, "frame_%04d.jpg")

    try:
        print(f"[INFO] Running ffmpeg: {ffmpeg}")
        # Match C# behavior: pass fps as invariant-culture float (e.g. "0.5", "1.0")
        fps_str = str(fps)

        proc = subprocess.run(
            [ffmpeg, "-i", video_path, "-vf", f"fps={fps_str}", "-q:v", "2", "-y", output_pattern],
            capture_output=True, text=True, check=False,
        )

        if proc.returncode != 0:
            error_lines = proc.stderr.split("\n")[-5:]
            print(f"[ERROR] Frame extraction failed (exit code {proc.returncode}):")
            for line in error_lines:
                line = line.strip()
                if line:
                    print(f"        {line}")
            return False

        frame_count = len([f for f in os.listdir(output_dir)
                           if f.startswith("frame_") and f.endswith(".jpg")])
        if frame_count == 0:
            print("[ERROR] No frames extracted. Check if video file is valid.")
            return False

        print(f"[OK] Frames extracted: {frame_count} images saved to {output_dir}/")
        return True

    except Exception as ex:  # noqa: BLE001
        print(f"[ERROR] Frame extraction failed: {ex}")
        return False


def list_frames(directory: str) -> List[str]:
    return sorted(
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.startswith("frame_") and f.endswith(".jpg")
    )


def write_manifest(output_dir: str,
                   dedup_enabled: bool,
                   threshold: float,
                   raw_count: int,
                   output_count: int,
                   kept_frames: List[dict]) -> None:
    manifest = {
        "deduplicationEnabled": dedup_enabled,
        "similarityThreshold": threshold,
        "rawDirectory": "images_raw",
        "outputDirectory": "images",
        "rawFrameCount": raw_count,
        "outputFrameCount": output_count,
        "keptFrames": kept_frames,
    }
    parent = os.path.dirname(output_dir)
    manifest_path = os.path.join(parent, "dedup_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


def copy_all_frames(source_dir: str, dest_dir: str) -> None:
    print(f"[INFO] Copying all frames from {source_dir}/ to {dest_dir}/ (no dedup)...")
    os.makedirs(dest_dir, exist_ok=True)

    files = list_frames(source_dir)
    manifest: List[dict] = []
    for i, src in enumerate(files):
        dest = os.path.join(dest_dir, f"frame_{i + 1:04d}.jpg")
        shutil.copyfile(src, dest)
        manifest.append({
            "rawFrame": os.path.basename(src),
            "rawIndex": i + 1,
            "outputFrame": f"frame_{i + 1:04d}.jpg",
            "outputIndex": i + 1,
        })

    write_manifest(dest_dir, False, 0.0, len(files), len(files), manifest)
    print(f"[OK] Copied {len(files)} frames to {dest_dir}/")


def deduplicate_frames(raw_dir: str, output_dir: str, threshold: float) -> None:
    print(f"[INFO] Deduplicating similar frames (threshold: {threshold:.0%})...")
    print(f"[INFO] Reading from: {raw_dir}/")
    print(f"[INFO] Writing to: {output_dir}/")

    os.makedirs(output_dir, exist_ok=True)
    files = list_frames(raw_dir)

    if len(files) < 2:
        print("[INFO] Not enough frames to deduplicate")
        for i, src in enumerate(files):
            shutil.copyfile(src, os.path.join(output_dir, f"frame_{i + 1:04d}.jpg"))
        return

    ffmpeg = find_executable("ffmpeg", "ffmpeg.exe")
    if ffmpeg is None:
        print("[WARN] ffmpeg not found, skipping deduplication")
        copy_all_frames(raw_dir, output_dir)
        return

    to_remove: set = set()
    last_kept_index = 0

    for i in range(1, len(files)):
        sim = calculate_frame_similarity(ffmpeg, files[last_kept_index], files[i])
        if sim >= threshold:
            to_remove.add(i)
        else:
            last_kept_index = i

    manifest: List[dict] = []
    output_index = 0
    for i, src in enumerate(files):
        if i in to_remove:
            continue
        output_index += 1
        dest = os.path.join(output_dir, f"frame_{output_index:04d}.jpg")
        shutil.copyfile(src, dest)
        manifest.append({
            "rawFrame": os.path.basename(src),
            "rawIndex": i + 1,
            "outputFrame": f"frame_{output_index:04d}.jpg",
            "outputIndex": output_index,
        })

    write_manifest(output_dir, True, threshold, len(files), output_index, manifest)
    print(f"[OK] Deduplication complete: {len(files)} -> {output_index} frames "
          f"(removed {len(to_remove)} similar frames)")
    print("[OK] Manifest saved: dedup_manifest.json")


def calculate_frame_similarity(ffmpeg: str, file1: str, file2: str) -> float:
    try:
        proc = subprocess.run(
            [ffmpeg, "-i", file1, "-i", file2, "-lavfi", "psnr", "-f", "null", "-"],
            capture_output=True, text=True, check=False,
        )
        stderr = proc.stderr or ""
        m = re.search(r"average:(\d+\.?\d*)", stderr, re.IGNORECASE)
        if m:
            try:
                psnr = float(m.group(1))
            except ValueError:
                return calculate_ssim(ffmpeg, file1, file2)

            # Mirror C# PSNR -> similarity mapping
            if psnr > 100:
                return 1.0
            if psnr > 40:
                return 0.95 + (psnr - 40) * 0.001
            if psnr > 30:
                return 0.80 + (psnr - 30) * 0.015
            if psnr > 20:
                return 0.50 + (psnr - 20) * 0.03
            return psnr * 0.025

        return calculate_ssim(ffmpeg, file1, file2)
    except Exception:  # noqa: BLE001
        return 0.0


def calculate_ssim(ffmpeg: str, file1: str, file2: str) -> float:
    try:
        proc = subprocess.run(
            [ffmpeg, "-i", file1, "-i", file2, "-lavfi", "ssim", "-f", "null", "-"],
            capture_output=True, text=True, check=False,
        )
        stderr = proc.stderr or ""
        m = re.search(r"All:(\d+\.?\d*)", stderr, re.IGNORECASE)
        if m:
            try:
                return float(m.group(1))
            except ValueError:
                return 0.0
        return 0.0
    except Exception:  # noqa: BLE001
        return 0.0


# ============================================================================
# Entry point
# ============================================================================

# Globals (mirroring the C# top-level locals so download_bilibili_video can
# update fps after fetching duration metadata).
_fps: float = 1.0
_fps_explicit: bool = False


def main(argv: List[str]) -> int:
    global _fps, _fps_explicit  # noqa: PLW0603

    if len(argv) == 0 or "-h" in argv or "--help" in argv:
        print_help()
        return 0

    url = argv[0]
    output_dir = get_arg_value(argv, "-o", "--output") or "."
    fps_str = get_arg_value(argv, "--fps")
    _fps_explicit = fps_str is not None
    if fps_str is None:
        fps_str = "1.0"

    try:
        _fps = float(fps_str)
    except ValueError:
        print(f"[ERROR] Invalid fps value: {fps_str}")
        return 1

    similarity_str = get_arg_value(argv, "--similarity") or "0.65"
    try:
        similarity_threshold = float(similarity_str)
    except ValueError:
        print(f"[ERROR] Invalid similarity value: {similarity_str}")
        return 1

    video_only = "--video-only" in argv
    frames_only = "--frames-only" in argv
    no_dedup = "--no-dedup" in argv

    video_path = os.path.join(output_dir, "video.mp4")
    images_raw_dir = os.path.join(output_dir, "images_raw")
    images_dir = os.path.join(output_dir, "images")

    os.makedirs(output_dir, exist_ok=True)

    bar = "=" * 50
    print(bar)
    print("Bilibili Video Analyzer - Prepare Script")
    print(bar)
    print(f"URL: {url}")
    print(f"Output: {output_dir}")
    suffix = "" if _fps_explicit else " (auto, may change after fetching video info)"
    print(f"FPS: {_fps}{suffix}")
    print(f"Similarity Threshold: {similarity_threshold:.0%}")
    print(f"Deduplication: {'Disabled' if no_dedup else 'Enabled'}")
    print(bar)

    if not frames_only:
        if not download_bilibili_video(url, video_path):
            return 1

    if not video_only:
        if not os.path.exists(video_path):
            print(f"[ERROR] Video file not found: {video_path}")
            return 1

        clean_directory(images_raw_dir)
        clean_directory(images_dir)

        if not extract_frames(video_path, images_raw_dir, _fps):
            return 1

        if not no_dedup:
            deduplicate_frames(images_raw_dir, images_dir, similarity_threshold)
        else:
            copy_all_frames(images_raw_dir, images_dir)

    print()
    print(bar)
    print("[OK] Done!")
    print(f"  Video: {video_path}")
    print(f"  Raw frames: {images_raw_dir}/")
    print(f"  Deduped images: {images_dir}/")
    print(bar)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
