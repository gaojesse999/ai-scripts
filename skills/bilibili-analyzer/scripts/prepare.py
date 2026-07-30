#!/usr/bin/env python3

import argparse
import json
import math
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

import cv2
from PIL import Image
import imagehash

import bili_common
from bili_common import (
    USER_AGENT,
    build_headers,
    ensure_network,
    merge_streams,
    pick_dash_streams,
    stream_base_url,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fallback Bilibili prepare pipeline")
    parser.add_argument("url", help="Bilibili single-page video URL, explicit ?p= page URL, or BV id")
    parser.add_argument("-o", "--output", default=".", help="Output directory")
    parser.add_argument("--fps", type=float, default=1.0, help="Target extracted frames per second")
    parser.add_argument(
        "--similarity",
        type=float,
        default=0.80,
        help="Adjacent-frame similarity threshold for deduplication",
    )
    parser.add_argument("--no-dedup", action="store_true", help="Disable adjacent-frame deduplication")
    parser.add_argument(
        "--max-height",
        type=int,
        default=1080,
        help="Cap DASH video resolution (e.g. 1080). Use 0 for the absolute best (4K/HDR).",
    )
    return parser.parse_args()


def extract_bvid(url: str) -> str:
    match = re.search(r"BV[a-zA-Z0-9]{10}", url)
    if not match:
        raise ValueError(f"Unable to extract BV id from: {url}")
    return match.group(0)


def extract_episode_id(url: str) -> int | None:
    match = re.search(r"/ep(\d+)", url)
    if not match:
        return None
    return int(match.group(1))


def extract_page_number(url: str) -> int | None:
    parsed = urlparse(url)
    values = parse_qs(parsed.query).get("p")
    if not values:
        return None
    try:
        page = int(values[0])
        return page if page > 0 else None
    except ValueError:
        return None


def fetch_json(url: str, referer: str) -> dict:
    request = Request(url, headers=build_headers(referer))
    with urlopen(request) as response:
        return json.load(response)


def fetch_playurl(url: str, referer: str) -> dict:
    request = Request(url, headers=build_headers(referer))
    with urlopen(request) as response:
        return json.load(response)


def select_page(info: dict, page_number: int | None) -> dict:
    pages = info.get("pages") or []
    if page_number is not None:
        if not pages:
            raise ValueError("This video does not expose page metadata")
        if not (1 <= page_number <= len(pages)):
            raise ValueError(f"Requested page {page_number} is out of range; available pages: 1-{len(pages)}")
        return pages[page_number - 1]

    if len(pages) > 1:
        raise ValueError(
            "Multi-page video requires an explicit '?p=' URL. Resolve the target first (for example via resolve_scope.py) before calling prepare.py."
        )

    cid = info.get("cid")
    for page in pages:
        if page.get("cid") == cid:
            return page

    if not pages:
        return {"page": 1, "part": info.get("title"), "duration": info.get("duration"), "cid": cid}
    return pages[0]


def normalize_duration(value: object) -> float | int | None:
    if not isinstance(value, (int, float)):
        return value
    if value > 10000:
        return round(value / 1000.0, 3)
    return value


def get_bangumi_context(url: str) -> tuple[str, str, dict, dict]:
    ep_id = extract_episode_id(url)
    if ep_id is None:
        raise ValueError(f"Unable to extract episode id from: {url}")

    referer = f"https://www.bilibili.com/bangumi/play/ep{ep_id}"
    season_data = fetch_json(f"https://api.bilibili.com/pgc/view/web/season?ep_id={ep_id}", referer)
    if season_data.get("code") != 0:
        raise RuntimeError(f"pgc season API failed: {season_data.get('message')}")

    result = season_data.get("result") or {}
    episodes = result.get("episodes") or []
    if not episodes:
        raise RuntimeError("No episode metadata returned by pgc season API")

    episode = None
    for item in episodes:
        try:
            if int(item.get("ep_id") or 0) == ep_id:
                episode = item
                break
        except (TypeError, ValueError):
            continue
    if episode is None:
        episode = episodes[0]

    info = {
        "title": result.get("title") or result.get("name") or episode.get("title") or f"EP{ep_id}",
        "season_id": result.get("season_id"),
        "ep_id": ep_id,
    }
    page = {
        "page": 1,
        "part": episode.get("share_copy") or episode.get("title") or info["title"],
        "duration": normalize_duration(episode.get("duration") or episode.get("duration_ms") or 0),
        "cid": episode.get("cid"),
        "ep_id": ep_id,
    }
    return f"EP{ep_id}", referer, info, page


def download_video(video_url: str, output_path: Path, referer: str) -> None:
    request = Request(video_url, headers=build_headers(referer, accept="*/*"))
    with urlopen(request) as response, output_path.open("wb") as file_handle:
        total_bytes = int(response.headers.get("Content-Length", "0") or 0)
        downloaded = 0
        last_reported = -1
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            file_handle.write(chunk)
            downloaded += len(chunk)
            if total_bytes:
                progress = math.floor(downloaded * 100 / total_bytes)
                if progress != last_reported and (progress % 10 == 0 or progress == 100):
                    print(f"[INFO] Download progress: {progress}%")
                    last_reported = progress


def extract_frames(video_path: Path, raw_dir: Path, target_fps: float) -> tuple[list[dict], float]:
    capture = cv2.VideoCapture(str(video_path))
    if not capture.isOpened():
        raise RuntimeError(f"Unable to open video: {video_path}")

    native_fps = capture.get(cv2.CAP_PROP_FPS) or 25.0
    if native_fps <= 0:
        native_fps = 25.0
    frame_interval = max(native_fps / target_fps, 1.0)

    saved = []
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
    return saved, native_fps


def phash_for(path: Path) -> imagehash.ImageHash:
    with Image.open(path) as image:
        return imagehash.phash(image, hash_size=8)


def deduplicate_frames(raw_dir: Path, final_dir: Path, frames: list[dict], threshold: float) -> list[dict]:
    kept = []
    previous_hash = None

    for index, frame in enumerate(frames):
        source = raw_dir / frame["file"]
        current_hash = phash_for(source)
        keep = index == 0
        if previous_hash is not None:
            distance = previous_hash - current_hash
            similarity = 1.0 - (distance / 64.0)
            keep = similarity <= threshold
            frame["adjacent_similarity"] = round(similarity, 4)
        else:
            frame["adjacent_similarity"] = None

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
                "adjacent_similarity": frame["adjacent_similarity"],
            }
        )

    return kept


def copy_without_dedup(raw_dir: Path, final_dir: Path, frames: list[dict]) -> list[dict]:
    copied = []
    for frame in frames:
        source = raw_dir / frame["file"]
        target_name = frame["file"]
        shutil.copy2(source, final_dir / target_name)
        copied.append({"file": target_name, "source_file": target_name, "timestamp": frame["timestamp"]})
    return copied


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def download_playable(play_payload: dict, video_path: Path, referer: str, output_dir: Path, max_height: int | None = 1080) -> None:
    """Download the best available stream.

    Prefers DASH (separate high-quality video + audio, merged with ffmpeg);
    falls back to a progressive durl segment when DASH is unavailable.
    """
    dash = play_payload.get("dash")
    if isinstance(dash, dict) and dash.get("video"):
        selection = pick_dash_streams(dash, max_height=max_height)
        if selection is not None:
            best_video, best_audio = selection
            video_stream = output_dir / "video_stream.m4s"
            print(f"[INFO] Downloading DASH video stream (id={best_video.get('id')})")
            download_video(stream_base_url(best_video), video_stream, referer)

            audio_stream = None
            if best_audio is not None:
                audio_stream = output_dir / "audio_stream.m4s"
                print("[INFO] Downloading DASH audio stream")
                download_video(stream_base_url(best_audio), audio_stream, referer)

            print("[INFO] Merging streams with ffmpeg")
            merge_streams(video_stream, audio_stream, video_path)

            video_stream.unlink(missing_ok=True)
            if audio_stream is not None:
                audio_stream.unlink(missing_ok=True)
            return

    durl = play_payload.get("durl") or play_payload.get("durls") or []
    if not durl:
        raise RuntimeError("No downloadable stream (DASH or durl) returned by playurl API")
    print("[INFO] Downloading progressive stream (durl fallback)")
    download_video(durl[0]["url"], video_path, referer)


def main() -> int:
    args = parse_args()
    ensure_network()
    output_dir = Path(args.output).resolve()
    raw_dir = output_dir / "images_raw"
    final_dir = output_dir / "images"
    video_path = output_dir / "video.mp4"

    output_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)
    final_dir.mkdir(parents=True, exist_ok=True)

    episode_id = extract_episode_id(args.url)
    if episode_id is not None:
        bvid, referer, info, page = get_bangumi_context(args.url)
        cid = page["cid"]
        print(f"[INFO] Fetching metadata for {bvid}")
        print(f"[INFO] Title: {info['title']}")
        print(f"[INFO] Page {page.get('page', 1)}: {page.get('part')}")
        print(f"[INFO] Duration: {page.get('duration')} seconds")

        play_data = fetch_playurl(
            f"https://api.bilibili.com/pgc/player/web/playurl?ep_id={episode_id}&cid={cid}&fnval=4048&fourk=1",
            referer,
        )
    else:
        bvid = extract_bvid(args.url)
        referer = f"https://www.bilibili.com/video/{bvid}"

        print(f"[INFO] Fetching metadata for {bvid}")
        view_data = fetch_json(f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}", referer)
        if view_data.get("code") != 0:
            raise RuntimeError(f"view API failed: {view_data.get('message')}")

        info = view_data["data"]
        page = select_page(info, extract_page_number(args.url))
        cid = page["cid"]
        print(f"[INFO] Title: {info['title']}")
        print(f"[INFO] Page {page.get('page', 1)}: {page.get('part')}")
        print(f"[INFO] Duration: {page.get('duration')} seconds")

        play_data = fetch_json(
            f"https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&fnval=4048&fourk=1",
            referer,
        )

    if play_data.get("code") != 0:
        raise RuntimeError(f"playurl API failed: {play_data.get('message')}")

    play_payload = play_data.get("data") or play_data.get("result") or {}
    if isinstance(play_payload.get("result"), dict):
        play_payload = play_payload["result"]

    print("[INFO] Downloading video")
    download_playable(play_payload, video_path, referer, output_dir, max_height=(args.max_height or None))
    print(f"[INFO] Saved video to {video_path}")

    print(f"[INFO] Extracting frames at {args.fps} fps")
    raw_frames, native_fps = extract_frames(video_path, raw_dir, args.fps)
    print(f"[INFO] Extracted {len(raw_frames)} raw frames")

    if args.no_dedup:
        kept_frames = copy_without_dedup(raw_dir, final_dir, raw_frames)
    else:
        kept_frames = deduplicate_frames(raw_dir, final_dir, raw_frames, args.similarity)
    print(f"[INFO] Retained {len(kept_frames)} frames after dedup")

    write_json(
        output_dir / "metadata.json",
        {
            "bvid": bvid,
            "title": info["title"],
            "uploader": info.get("owner", {}).get("name"),
            "page": page,
            "fps": args.fps,
            "native_fps": native_fps,
            "raw_frame_count": len(raw_frames),
            "final_frame_count": len(kept_frames),
            "video_path": str(video_path),
            "images_dir": str(final_dir),
        },
    )
    write_json(output_dir / "frames.json", {"frames": kept_frames})

    print("[OK] Pipeline complete")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"[ERROR] {exc}", file=sys.stderr)
        raise SystemExit(1)