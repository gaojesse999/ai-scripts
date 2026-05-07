#!/usr/bin/env python3
"""Prepare text context for bilibili-analyzer.

Pipeline:
1. Prefer platform subtitles when available.
2. Fall back to image-only mode when subtitles are unavailable.

Outputs are written into the analysis output directory.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0.0.0 Safari/537.36"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare subtitle text for bilibili-analyzer")
    parser.add_argument("url", help="Bilibili single-page video URL, explicit ?p= page URL, or BV id")
    parser.add_argument("-o", "--output", default=".", help="Output directory")
    return parser.parse_args()


def fetch_json(url: str, referer: str) -> dict:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Referer": referer,
            "Accept": "application/json, text/plain, */*",
        },
    )
    with urlopen(request) as response:
        return json.load(response)


def fetch_text_json(url: str, referer: str) -> dict:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Referer": referer,
            "Accept": "application/json, text/plain, */*",
        },
    )
    with urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_bvid(url: str) -> str:
    match = re.search(r"BV[a-zA-Z0-9]{10}", url)
    if not match:
        raise ValueError(f"Unable to extract BV id from: {url}")
    return match.group(0)


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
            "Multi-page video requires an explicit '?p=' URL. Resolve the target first (for example via resolve_scope.py) before calling text_prepare.py."
        )

    cid = info.get("cid")
    for page in pages:
        if page.get("cid") == cid:
            return page

    if not pages:
        return {"page": 1, "part": info.get("title"), "duration": info.get("duration"), "cid": cid}
    return pages[0]


def normalize_subtitle_url(url: str) -> str:
    if not url:
        return url
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        return "https://api.bilibili.com" + url
    return url


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def get_video_context(url: str) -> tuple[str, str, dict, dict]:
    bvid = extract_bvid(url)
    referer = f"https://www.bilibili.com/video/{bvid}"
    view_data = fetch_json(f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}", referer)
    if view_data.get("code") != 0:
        raise RuntimeError(f"view API failed: {view_data.get('message')}")

    info = view_data["data"]
    page = select_page(info, extract_page_number(url))
    return bvid, referer, info, page


def fetch_subtitle_entries(bvid: str, cid: int, referer: str) -> list[dict]:
    player_data = fetch_json(f"https://api.bilibili.com/x/player/v2?bvid={bvid}&cid={cid}", referer)
    if player_data.get("code") != 0:
        raise RuntimeError(f"player/v2 API failed: {player_data.get('message')}")

    subtitle = (player_data.get("data") or {}).get("subtitle") or {}
    return subtitle.get("subtitles") or []


def subtitle_segments_from_payload(payload: dict) -> list[dict]:
    body = payload.get("body") or []
    segments = []
    for index, item in enumerate(body, start=1):
        text = (item.get("content") or "").strip()
        if not text:
            continue
        segments.append(
            {
                "index": index,
                "start": round(float(item.get("from", 0.0)), 3),
                "end": round(float(item.get("to", 0.0)), 3),
                "text": text,
                "source": "subtitle",
            }
        )
    return segments


def save_subtitle_artifacts(output_dir: Path, subtitle_meta: dict, subtitle_payload: dict, segments: list[dict]) -> dict:
    subtitles_json_path = output_dir / "subtitles.json"
    subtitles_txt_path = output_dir / "subtitles.txt"
    text_segments_path = output_dir / "text_segments.json"

    write_json(
        subtitles_json_path,
        {
            "source": "subtitle",
            "selected_subtitle": subtitle_meta,
            "segment_count": len(segments),
            "segments": segments,
            "raw_payload": subtitle_payload,
        },
    )
    write_text(subtitles_txt_path, "\n".join(segment["text"] for segment in segments) + ("\n" if segments else ""))
    write_json(
        text_segments_path,
        {
            "mode": "subtitle",
            "segment_count": len(segments),
            "segments": segments,
        },
    )
    return {
        "mode": "subtitle",
        "subtitle_count": len(segments),
        "files": {
            "subtitles_json": str(subtitles_json_path),
            "subtitles_txt": str(subtitles_txt_path),
            "text_segments_json": str(text_segments_path),
        },
    }


def image_only_result(reason: str) -> dict:
    return {
        "mode": "image_only",
        "reason": reason,
    }


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    bvid, referer, info, page = get_video_context(args.url)
    cid = page["cid"]

    print(f"[INFO] Preparing text context for {bvid}")
    print(f"[INFO] Page {page.get('page', 1)}: {page.get('part')}")

    subtitle_entries = fetch_subtitle_entries(bvid, cid, referer)
    usable_subtitles = [entry for entry in subtitle_entries if normalize_subtitle_url(entry.get("subtitle_url", ""))]

    if usable_subtitles:
        selected = usable_subtitles[0]
        subtitle_url = normalize_subtitle_url(selected.get("subtitle_url", ""))
        print(f"[INFO] Using subtitle track: {selected.get('lan_doc') or selected.get('lan') or 'unknown'}")
        subtitle_payload = fetch_text_json(subtitle_url, referer)
        segments = subtitle_segments_from_payload(subtitle_payload)
        result = save_subtitle_artifacts(output_dir, selected, subtitle_payload, segments)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print("[INFO] No platform subtitle available")
    result = image_only_result("subtitle_unavailable")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        raise SystemExit(1)
