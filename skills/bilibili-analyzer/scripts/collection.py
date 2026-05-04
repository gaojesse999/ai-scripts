#!/usr/bin/env python3
"""Detect whether a Bilibili URL points to a single video or a collection,
and output the result as JSON to stdout.

Usage:
    python collection.py "<URL>"

Exit codes:
    0 - success
    1 - error (message printed to stderr)
"""

import json
import re
import sys
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0.0.0 Safari/537.36"
)


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


def resolve_short_url(url: str) -> str:
    """Resolve b23.tv short links to their real URL."""
    if "b23.tv" not in url:
        return url
    request = Request(url, headers={"User-Agent": USER_AGENT})
    request.method = "HEAD"
    # Follow redirects manually to get the final URL
    from urllib.request import build_opener, HTTPRedirectHandler

    class NoRedirect(HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    opener = build_opener(NoRedirect)
    try:
        opener.open(request)
    except Exception:
        pass
    # Use urlopen which follows redirects by default
    request2 = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request2) as response:
        return response.url


def extract_bvid(url: str) -> str | None:
    match = re.search(r"BV[a-zA-Z0-9]{10}", url)
    return match.group(0) if match else None


def parse_space_collection_url(url: str) -> dict | None:
    """Parse space.bilibili.com collection/series URLs.

    Patterns:
      space.bilibili.com/{mid}/channel/collectiondetail?sid={season_id}
      space.bilibili.com/{mid}/channel/seriesdetail?sid={series_id}
    """
    parsed = urlparse(url)
    if "space.bilibili.com" not in parsed.netloc:
        return None

    mid_match = re.search(r"space\.bilibili\.com/(\d+)", url)
    if not mid_match:
        return None
    mid = mid_match.group(1)

    qs = parse_qs(parsed.query)
    sid_values = qs.get("sid")
    if not sid_values:
        return None
    sid = sid_values[0]

    if "collectiondetail" in parsed.path:
        return {"mid": mid, "season_id": sid, "type": "collection"}
    elif "seriesdetail" in parsed.path:
        return {"mid": mid, "series_id": sid, "type": "series"}
    return None


def fetch_collection_videos(mid: str, season_id: str) -> dict:
    """Fetch all videos from a UGC collection (合集) using the seasons API."""
    referer = f"https://space.bilibili.com/{mid}/channel/collectiondetail?sid={season_id}"
    all_archives = []
    collection_title = ""
    page_num = 1

    while True:
        api_url = (
            f"https://api.bilibili.com/x/polymer/web-space/seasons_archives_list"
            f"?mid={mid}&season_id={season_id}&page_num={page_num}&page_size=100"
        )
        data = fetch_json(api_url, referer)
        if data.get("code") != 0:
            raise RuntimeError(f"seasons_archives_list API failed: {data.get('message')}")

        result = data.get("data", {})
        if not collection_title:
            meta = result.get("meta", {})
            collection_title = meta.get("name", "未知合集")

        archives = result.get("archives", [])
        if not archives:
            break
        all_archives.extend(archives)

        total = result.get("page", {}).get("total", 0)
        if len(all_archives) >= total:
            break
        page_num += 1

    videos = []
    for arch in all_archives:
        bvid = arch.get("bvid", "")
        videos.append({
            "bvid": bvid,
            "title": arch.get("title", ""),
            "url": f"https://www.bilibili.com/video/{bvid}",
            "duration": arch.get("duration", 0),
        })

    return {
        "type": "collection",
        "source": "collection_page",
        "collection_title": collection_title,
        "total": len(videos),
        "videos": videos,
    }


def fetch_series_videos(mid: str, series_id: str) -> dict:
    """Fetch all videos from a series (系列) using the series API."""
    referer = f"https://space.bilibili.com/{mid}/channel/seriesdetail?sid={series_id}"
    all_archives = []
    series_title = ""
    pn = 1

    while True:
        api_url = (
            f"https://api.bilibili.com/x/series/archives"
            f"?mid={mid}&series_id={series_id}&pn={pn}&ps=100"
        )
        data = fetch_json(api_url, referer)
        if data.get("code") != 0:
            raise RuntimeError(f"series/archives API failed: {data.get('message')}")

        result = data.get("data", {})
        archives = result.get("archives", [])
        if not archives:
            break
        all_archives.extend(archives)

        total = result.get("page", {}).get("total", 0)
        if len(all_archives) >= total:
            break
        pn += 1

    # Fetch series title
    try:
        meta_url = f"https://api.bilibili.com/x/series/series?series_id={series_id}"
        meta_data = fetch_json(meta_url, referer)
        if meta_data.get("code") == 0:
            series_title = meta_data.get("data", {}).get("meta", {}).get("name", "未知系列")
    except Exception:
        series_title = "未知系列"

    videos = []
    for arch in all_archives:
        bvid = arch.get("bvid", "")
        videos.append({
            "bvid": bvid,
            "title": arch.get("title", ""),
            "url": f"https://www.bilibili.com/video/{bvid}",
            "duration": arch.get("duration", 0),
        })

    return {
        "type": "collection",
        "source": "series_page",
        "collection_title": series_title,
        "total": len(videos),
        "videos": videos,
    }


def detect_collection_from_bvid(bvid: str) -> dict:
    """Check if a BV video belongs to a UGC collection or series via the view API."""
    referer = f"https://www.bilibili.com/video/{bvid}"
    api_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    data = fetch_json(api_url, referer)

    if data.get("code") != 0:
        raise RuntimeError(f"view API failed: {data.get('message')}")

    info = data["data"]
    ugc_season = info.get("ugc_season")
    owner_mid = str(info.get("owner", {}).get("mid", ""))

    # Check for UGC season
    ugc_result = None
    if ugc_season:
        collection_title = ugc_season.get("title", "未知合集")
        videos = []
        sections = ugc_season.get("sections", [])
        for section in sections:
            episodes = section.get("episodes", [])
            for ep in episodes:
                ep_bvid = ep.get("bvid", "")
                videos.append({
                    "bvid": ep_bvid,
                    "title": ep.get("title", ""),
                    "url": f"https://www.bilibili.com/video/{ep_bvid}",
                    "duration": ep.get("arc", {}).get("duration", ep.get("page", {}).get("duration", 0)),
                })
        ugc_result = {
            "type": "collection",
            "source": "ugc_season",
            "collection_title": collection_title,
            "total": len(videos),
            "videos": videos,
        }

    # Check for series membership (via season_id in the view response)
    # Note: This checks if the video has an associated series via the `season` field
    series_result = None
    season_info = info.get("season")  # PGC/series season info (different from ugc_season)
    # For UGC series, we check if there's a series_id hint in the URL or page data
    # The view API doesn't directly expose series membership for UGC series,
    # so series detection from BV URL is limited to ugc_season.

    # Determine what to return
    if ugc_result:
        # If UGC season detected, always return UGC (takes priority per requirements)
        ugc_result["also_in_series"] = series_result is not None
        return ugc_result

    if series_result:
        return series_result

    # Single video, no collection
    return {
        "type": "single",
        "bvid": bvid,
        "title": info.get("title", ""),
        "url": f"https://www.bilibili.com/video/{bvid}",
    }


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python collection.py <URL>", file=sys.stderr)
        return 1

    url = sys.argv[1].strip()

    # Resolve short URLs
    if "b23.tv" in url:
        try:
            url = resolve_short_url(url)
            print(f"[INFO] Resolved short URL to: {url}", file=sys.stderr)
        except Exception as exc:
            print(f"[ERROR] Failed to resolve short URL: {exc}", file=sys.stderr)
            return 1

    # Check if it's a space.bilibili.com collection/series URL
    space_info = parse_space_collection_url(url)
    if space_info:
        if space_info["type"] == "collection":
            result = fetch_collection_videos(space_info["mid"], space_info["season_id"])
        else:
            result = fetch_series_videos(space_info["mid"], space_info["series_id"])
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    # Otherwise, try to extract BV id and check via view API
    bvid = extract_bvid(url)
    if not bvid:
        print(f"[ERROR] Unable to extract BV id from: {url}", file=sys.stderr)
        return 1

    result = detect_collection_from_bvid(bvid)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        raise SystemExit(1)
