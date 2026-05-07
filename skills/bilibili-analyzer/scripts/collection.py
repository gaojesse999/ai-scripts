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


def find_series_for_bvid(mid: str, bvid: str) -> dict | None:
    """Check if a video belongs to any series of the given user.

    Fetches the user's series list via seasons_series_list API, then checks each
    series for the target bvid using the series/archives API.
    Returns series info dict if found, None otherwise.
    """
    referer = f"https://space.bilibili.com/{mid}"

    # Fetch user's seasons & series list
    series_list_url = (
        f"https://api.bilibili.com/x/polymer/web-space/seasons_series_list"
        f"?mid={mid}&page_num=1&page_size=20"
    )
    try:
        list_data = fetch_json(series_list_url, referer)
    except Exception:
        return None

    if list_data.get("code") != 0:
        return None

    items_lists = (list_data.get("data") or {}).get("items_lists") or {}
    series_items = items_lists.get("series_list") or []
    if not series_items:
        return None

    # Check each series for the target bvid
    for item in series_items:
        meta = item.get("meta", {})
        series_id = str(meta.get("series_id", ""))
        if not series_id:
            continue

        # First do a quick check in the archives already returned in the list response
        inline_archives = item.get("archives") or []
        found_inline = any(arch.get("bvid") == bvid for arch in inline_archives)
        if found_inline:
            # Fetch full archive list for this series
            return _fetch_full_series(mid, series_id, meta.get("name", "未知系列"))

        # If not found inline but series has more videos, check the full list
        total_in_series = meta.get("total", 0)
        if total_in_series > len(inline_archives):
            series_referer = f"https://space.bilibili.com/{mid}/channel/seriesdetail?sid={series_id}"
            archives_url = (
                f"https://api.bilibili.com/x/series/archives"
                f"?mid={mid}&series_id={series_id}&pn=1&ps=100"
            )
            try:
                arch_data = fetch_json(archives_url, series_referer)
            except Exception:
                continue

            if arch_data.get("code") != 0:
                continue

            archives = (arch_data.get("data") or {}).get("archives") or []
            if any(arch.get("bvid") == bvid for arch in archives):
                return _build_series_result(meta.get("name", "未知系列"), archives)

    return None


def _fetch_full_series(mid: str, series_id: str, series_title: str) -> dict:
    """Fetch full video list for a series and return as collection result."""
    series_referer = f"https://space.bilibili.com/{mid}/channel/seriesdetail?sid={series_id}"
    archives_url = (
        f"https://api.bilibili.com/x/series/archives"
        f"?mid={mid}&series_id={series_id}&pn=1&ps=100"
    )
    try:
        arch_data = fetch_json(archives_url, series_referer)
        if arch_data.get("code") == 0:
            archives = (arch_data.get("data") or {}).get("archives") or []
            return _build_series_result(series_title, archives)
    except Exception:
        pass
    return {"type": "collection", "source": "series_page", "collection_title": series_title, "total": 0, "videos": []}


def _build_series_result(series_title: str, archives: list) -> dict:
    """Build a series collection result from archive list."""
    videos = []
    for a in archives:
        a_bvid = a.get("bvid", "")
        videos.append({
            "bvid": a_bvid,
            "title": a.get("title", ""),
            "url": f"https://www.bilibili.com/video/{a_bvid}",
            "duration": a.get("duration", 0),
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

    # Check for series membership by searching the user's series list
    series_result = find_series_for_bvid(owner_mid, bvid) if owner_mid else None

    # Determine what to return
    if ugc_result:
        ugc_result["also_in_series"] = series_result is not None
        if series_result:
            ugc_result["series_info"] = {
                "collection_title": series_result["collection_title"],
                "total": series_result["total"],
            }
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
