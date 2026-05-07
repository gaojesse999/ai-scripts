#!/usr/bin/env python3
"""Resolve a Bilibili URL into concrete analysis targets for bilibili-analyzer.

This script centralizes scope resolution for the skill's two modes:

- single: analyze one concrete unit only
- collection: analyze a multi-unit scope (full collection / all pages of a BV)

It resolves short URLs, detects collection/series roots, inspects multi-page BVs,
and returns a structured JSON payload describing the exact units to process.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Any
from urllib.request import Request, urlopen

import collection as collection_script

USER_AGENT = collection_script.USER_AGENT


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resolve analysis scope for bilibili-analyzer")
    parser.add_argument("url", help="Bilibili URL or BV id")
    parser.add_argument("--mode", choices=["single", "collection"], required=True, help="Requested analysis mode")
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


def extract_bvid(url: str) -> str:
    match = re.search(r"BV[a-zA-Z0-9]{10}", url)
    if not match:
        raise ValueError(f"Unable to extract BV id from: {url}")
    return match.group(0)


def extract_page_number(url: str) -> int | None:
    from urllib.parse import parse_qs, urlparse

    parsed = urlparse(url)
    values = parse_qs(parsed.query).get("p")
    if not values:
        return None
    try:
        page = int(values[0])
        return page if page > 0 else None
    except ValueError:
        return None


def fetch_view_info(bvid: str) -> dict:
    referer = f"https://www.bilibili.com/video/{bvid}"
    payload = fetch_json(f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}", referer)
    if payload.get("code") != 0:
        raise RuntimeError(f"view API failed: {payload.get('message')}")
    return payload["data"]


def build_page_targets(bvid: str, info: dict) -> list[dict[str, Any]]:
    pages = info.get("pages") or []
    if not pages:
        cid = info.get("cid")
        return [
            {
                "kind": "page",
                "bvid": bvid,
                "page": 1,
                "part": info.get("title") or "第1P",
                "duration": info.get("duration"),
                "cid": cid,
                "url": f"https://www.bilibili.com/video/{bvid}?p=1",
            }
        ]

    targets = []
    for index, page in enumerate(pages, start=1):
        page_number = page.get("page") or index
        targets.append(
            {
                "kind": "page",
                "bvid": bvid,
                "page": page_number,
                "part": page.get("part") or f"第{page_number}P",
                "duration": page.get("duration"),
                "cid": page.get("cid"),
                "url": f"https://www.bilibili.com/video/{bvid}?p={page_number}",
            }
        )
    return targets


def build_video_target(bvid: str, info: dict, original_url: str | None = None) -> dict[str, Any]:
    return {
        "kind": "video",
        "bvid": bvid,
        "title": info.get("title") or bvid,
        "duration": info.get("duration"),
        "url": original_url or f"https://www.bilibili.com/video/{bvid}",
        "page_count": len(info.get("pages") or []),
    }


def expand_video_entry(video: dict[str, Any]) -> dict[str, Any]:
    bvid = video["bvid"]
    info = fetch_view_info(bvid)
    pages = build_page_targets(bvid, info)
    return {
        "kind": "video",
        "bvid": bvid,
        "title": video.get("title") or info.get("title") or bvid,
        "url": video.get("url") or f"https://www.bilibili.com/video/{bvid}",
        "duration": video.get("duration") or info.get("duration"),
        "page_count": len(pages),
        "is_multi_p": len(pages) > 1,
        "pages": pages,
    }


def classify_bv_link(info: dict, page_number: int | None) -> str:
    page_count = len(info.get("pages") or [])
    if page_count > 1 and page_number is not None:
        return "current_p"
    if page_count > 1:
        return "multi_p_root"
    return "video"


def fetch_collection_root(space_info: dict) -> dict[str, Any]:
    if space_info["type"] == "collection":
        return collection_script.fetch_collection_videos(space_info["mid"], space_info["season_id"])
    return collection_script.fetch_series_videos(space_info["mid"], space_info["series_id"])


def descend_first_analyzable_unit(video: dict[str, Any], reason: str) -> tuple[dict[str, Any], list[str], list[dict[str, Any]]]:
    info = fetch_view_info(video["bvid"])
    pages = build_page_targets(video["bvid"], info)
    notes = [reason, f"First video selected: {video.get('title') or video['bvid']}"]
    if len(pages) > 1:
        notes.append(f"First video is multi-page, descending to P1: {pages[0]['part']}")
        return pages[0], notes, pages
    return build_video_target(video["bvid"], info, video.get("url")), notes, pages


def single_mode_from_space_root(url: str) -> dict[str, Any]:
    space_info = collection_script.parse_space_collection_url(url)
    if not space_info:
        raise ValueError(f"Unsupported space URL: {url}")

    root = fetch_collection_root(space_info)
    videos = root.get("videos") or []
    if not videos:
        raise RuntimeError("Collection or series is empty")

    target, notes, pages = descend_first_analyzable_unit(videos[0], "Detected collection/series root in single mode")
    return {
        "mode": "single",
        "normalized_url": url,
        "input_link_type": "collection_root" if space_info["type"] == "collection" else "series_root",
        "resolved_scope": "single_page" if target["kind"] == "page" else "single_video",
        "display_logic": {
            "recognized_as": "合集 / 系列总链接",
            "rule": "Single mode descends to the first analyzable unit",
            "final_target": target,
            "notes": notes,
        },
        "collection_context": {
            "source": root.get("source"),
            "collection_title": root.get("collection_title"),
            "total": root.get("total"),
        },
        "targets": [target],
        "first_video_pages": pages,
    }


def collection_mode_from_space_root(url: str) -> dict[str, Any]:
    space_info = collection_script.parse_space_collection_url(url)
    if not space_info:
        raise ValueError(f"Unsupported space URL: {url}")

    root = fetch_collection_root(space_info)
    expanded_videos = [expand_video_entry(video) for video in (root.get("videos") or [])]
    total_expanded_units = sum(video["page_count"] if video["is_multi_p"] else 1 for video in expanded_videos)

    return {
        "mode": "collection",
        "normalized_url": url,
        "input_link_type": "collection_root" if space_info["type"] == "collection" else "series_root",
        "resolved_scope": "full_collection",
        "display_logic": {
            "recognized_as": "合集 / 系列总链接",
            "rule": "Collection mode processes the entire collection or series",
            "notes": ["Nested multi-page child videos are expanded in the targets list."],
        },
        "collection_context": {
            "source": root.get("source"),
            "collection_title": root.get("collection_title"),
            "total": root.get("total"),
            "total_expanded_units": total_expanded_units,
        },
        "targets": expanded_videos,
    }


def resolve_single_mode_bv(url: str) -> dict[str, Any]:
    bvid = extract_bvid(url)
    info = fetch_view_info(bvid)
    page_number = extract_page_number(url)
    page_targets = build_page_targets(bvid, info)
    input_link_type = classify_bv_link(info, page_number)

    if input_link_type == "current_p":
        target = page_targets[page_number - 1]
        return {
            "mode": "single",
            "normalized_url": url,
            "input_link_type": input_link_type,
            "resolved_scope": "single_page",
            "display_logic": {
                "recognized_as": "当前P链接",
                "rule": "Single mode keeps the current page only",
                "final_target": target,
                "notes": [],
            },
            "targets": [target],
        }

    if input_link_type == "multi_p_root":
        target = page_targets[0]
        return {
            "mode": "single",
            "normalized_url": url,
            "input_link_type": input_link_type,
            "resolved_scope": "single_page",
            "display_logic": {
                "recognized_as": "多P总链接",
                "rule": "Single mode descends to P1",
                "final_target": target,
                "notes": [f"Detected {len(page_targets)} pages, descending to the first page."],
            },
            "targets": [target],
            "all_pages": page_targets,
        }

    target = build_video_target(bvid, info, url)
    membership = collection_script.detect_collection_from_bvid(bvid)
    return {
        "mode": "single",
        "normalized_url": url,
        "input_link_type": input_link_type,
        "resolved_scope": "single_video",
        "display_logic": {
            "recognized_as": "普通视频链接",
            "rule": "Single mode keeps the current video only",
            "final_target": target,
            "notes": [],
        },
        "membership": membership,
        "targets": [target],
    }


def resolve_collection_mode_bv(url: str) -> dict[str, Any]:
    bvid = extract_bvid(url)
    info = fetch_view_info(bvid)
    page_number = extract_page_number(url)
    page_targets = build_page_targets(bvid, info)
    input_link_type = classify_bv_link(info, page_number)
    membership = collection_script.detect_collection_from_bvid(bvid)

    if len(page_targets) > 1:
        return {
            "mode": "collection",
            "normalized_url": url,
            "input_link_type": input_link_type,
            "resolved_scope": "all_pages_of_current_bv",
            "display_logic": {
                "recognized_as": "当前 BV 为多P视频",
                "rule": "Collection mode resolves to all pages of the current BV",
                "final_target": {"bvid": bvid, "page_count": len(page_targets)},
                "notes": [
                    "Current BV itself is multi-page.",
                    "Per collection-mode bottom-layer rule, all pages of the current BV are selected.",
                ],
            },
            "membership": membership,
            "targets": page_targets,
        }

    if membership.get("type") == "collection":
        expanded_videos = [expand_video_entry(video) for video in (membership.get("videos") or [])]
        total_expanded_units = sum(video["page_count"] if video["is_multi_p"] else 1 for video in expanded_videos)
        return {
            "mode": "collection",
            "normalized_url": url,
            "input_link_type": input_link_type,
            "resolved_scope": "full_collection",
            "display_logic": {
                "recognized_as": "合集成员视频",
                "rule": "Collection mode resolves to the full parent collection",
                "final_target": {"collection_title": membership.get("collection_title")},
                "notes": ["Nested multi-page child videos are expanded in the targets list."],
            },
            "collection_context": {
                "source": membership.get("source"),
                "collection_title": membership.get("collection_title"),
                "total": membership.get("total"),
                "total_expanded_units": total_expanded_units,
            },
            "targets": expanded_videos,
        }

    target = build_video_target(bvid, info, url)
    return {
        "mode": "collection",
        "normalized_url": url,
        "input_link_type": input_link_type,
        "resolved_scope": "single_video_fallback",
        "display_logic": {
            "recognized_as": "普通单视频链接",
            "rule": "No collection/series membership and not multi-page; fall back to the current video only",
            "final_target": target,
            "notes": ["Requested collection mode, but the input does not resolve to a collection, series, or multi-page BV."],
        },
        "membership": membership,
        "targets": [target],
    }


def main() -> int:
    args = parse_args()
    url = args.url.strip()

    if "b23.tv" in url:
        url = collection_script.resolve_short_url(url)

    space_info = collection_script.parse_space_collection_url(url)
    if space_info:
        result = single_mode_from_space_root(url) if args.mode == "single" else collection_mode_from_space_root(url)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    result = resolve_single_mode_bv(url) if args.mode == "single" else resolve_collection_mode_bv(url)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        raise SystemExit(1)