#!/usr/bin/env python3
"""
local-video-content-analyzer - data-prep entry point.

This script does NOT call any model and has NO model / adapter / API-key
concept. It only:

  1. Discovers local video files,
  2. Loads & normalizes user-provided engagement metadata,
  3. Computes derived metrics (viral_score, engagement rates, etc.),
  4. Builds a ready-to-use analysis prompt per video,
  5. Emits a single `viral-analysis-tasks.json` task list.

The actual multimodal video analysis and the final per-video Markdown report
are produced by the AGENT that runs this skill (i.e. the current Cursor
session model), using the task list as input. See SKILL.md for the full
agent workflow.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


SUPPORTED_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".m4v"}

REQUIRED_FIELDS = ("views", "likes", "author_followers")
RECOMMENDED_FIELDS = ("comments", "saves", "shares")
OPTIONAL_FIELDS = (
    "title", "platform", "publish_time", "video_duration_sec",
    "completion_rate", "ctr", "author", "notes",
)
ALL_KNOWN_FIELDS = REQUIRED_FIELDS + RECOMMENDED_FIELDS + OPTIONAL_FIELDS

# Accept Chinese / platform-native field names and normalize to canonical
# English keys. Douyin uses 收藏 (collect) which is semantically equivalent to
# `saves`.
FIELD_ALIASES: dict[str, str] = {
    "播放": "views", "播放量": "views", "播放数": "views",
    "plays": "views", "play_count": "views", "playCount": "views",
    "点赞": "likes", "点赞数": "likes", "赞": "likes",
    "hearts": "likes", "digg_count": "likes", "diggCount": "likes",
    "评论": "comments", "评论数": "comments",
    "comment_count": "comments", "commentCount": "comments",
    "分享": "shares", "分享数": "shares", "转发": "shares", "转发数": "shares",
    "share_count": "shares", "shareCount": "shares",
    "收藏": "saves", "收藏数": "saves", "收藏量": "saves",
    "bookmarks": "saves",
    "collect": "saves", "collects": "saves",
    "collect_count": "saves", "collectCount": "saves",
    "粉丝": "author_followers", "粉丝数": "author_followers", "粉丝量": "author_followers",
    "followers": "author_followers", "fans": "author_followers",
    "author_fans": "author_followers",
    "标题": "title", "平台": "platform", "账号": "author", "作者": "author",
    "发布时间": "publish_time", "发布日期": "publish_time",
    "时长": "video_duration_sec", "时长秒": "video_duration_sec",
    "duration": "video_duration_sec",
    "完播率": "completion_rate",
    "点击率": "ctr", "封面点击率": "ctr",
    "备注": "notes", "说明": "notes",
}

PROMPT_PATH = (
    Path(__file__).parent / "prompt_templates" / "viral_attribution.md"
)


def normalize_metadata(meta: dict[str, Any]) -> dict[str, Any]:
    """Map Chinese / platform-native field names to canonical English keys."""
    if not meta:
        return {}
    out: dict[str, Any] = {}
    for k, v in meta.items():
        canonical = FIELD_ALIASES.get(k) or FIELD_ALIASES.get(k.lower()) or k
        if v in (None, "") and canonical not in ALL_KNOWN_FIELDS:
            continue
        if canonical in out and canonical != k:
            continue
        out[canonical] = v
    return out


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Prepare local short-form videos + engagement data for the agent "
            "to analyze. Does NOT call any model; outputs a task list."
        )
    )
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--video", "-v", help="Path to a single local video file")
    src.add_argument("--video-dir", "-V", help="Folder containing local videos")

    p.add_argument("--metadata", "-m",
                   help="Path to a unified metadata CSV or JSON. "
                        "If omitted, sidecar <name>.json next to each video is used.")

    p.add_argument("--viral-threshold", type=float, default=5.0,
                   help="views/followers ratio above which a video is tagged "
                        "'breakout' (default: 5.0)")

    p.add_argument("--output", "-o", default="viral-analysis-tasks.json",
                   help="Output task list JSON path "
                        "(default: viral-analysis-tasks.json)")
    p.add_argument("--language", "-l", default="zh", choices=["zh", "en"],
                   help="Language for natural-language fields (default: zh)")
    p.add_argument("--max-videos", "-n", type=int, default=10,
                   help="Max videos to prepare per run (default: 10)")

    return p.parse_args()


# ---------------------------------------------------------------------------
# Video discovery
# ---------------------------------------------------------------------------

def collect_videos(args: argparse.Namespace) -> list[Path]:
    if args.video:
        p = Path(args.video)
        if not p.exists():
            sys.exit(f"Error: video not found: {p}")
        return [p]
    d = Path(args.video_dir)
    if not d.is_dir():
        sys.exit(f"Error: not a directory: {d}")
    videos = sorted(x for x in d.iterdir() if x.suffix.lower() in SUPPORTED_EXTS)
    if not videos:
        sys.exit(f"Error: no supported videos found in {d} "
                 f"(looked for {sorted(SUPPORTED_EXTS)})")
    return videos


# ---------------------------------------------------------------------------
# Metadata loading
# ---------------------------------------------------------------------------

def load_metadata(args: argparse.Namespace, videos: list[Path]) -> dict[str, dict[str, Any]]:
    """Return {filename: metadata_dict}."""
    if args.metadata:
        meta_path = Path(args.metadata)
        if not meta_path.exists():
            sys.exit(f"Error: metadata file not found: {meta_path}")
        if meta_path.suffix.lower() == ".csv":
            return _load_metadata_csv(meta_path)
        if meta_path.suffix.lower() == ".json":
            return _load_metadata_json(meta_path)
        sys.exit(f"Error: unsupported metadata format: {meta_path.suffix}")

    out: dict[str, dict[str, Any]] = {}
    for v in videos:
        sidecar = v.with_suffix(".json")
        if sidecar.exists():
            with open(sidecar, "r", encoding="utf-8") as f:
                out[v.name] = normalize_metadata(json.load(f))
        else:
            out[v.name] = {}
    return out


def _load_metadata_csv(path: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fn = row.get("filename") or row.get("file") or row.get("文件名")
            if not fn:
                continue
            cleaned = {k: _coerce(v) for k, v in row.items() if v not in (None, "")}
            for drop in ("filename", "file", "文件名"):
                cleaned.pop(drop, None)
            out[fn] = normalize_metadata(cleaned)
    return out


def _load_metadata_json(path: Path) -> dict[str, dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        out: dict[str, dict[str, Any]] = {}
        for item in data:
            fn = item.get("filename") or item.get("file") or item.get("文件名")
            if not fn:
                continue
            body = {k: v for k, v in item.items()
                    if k not in ("filename", "file", "文件名")}
            out[fn] = normalize_metadata(body)
        return out
    if isinstance(data, dict):
        return {fn: normalize_metadata(meta or {}) for fn, meta in data.items()}
    sys.exit("Error: metadata JSON must be a list or a dict")


def _coerce(v: str) -> Any:
    try:
        if "." in v:
            return float(v)
        return int(v)
    except (ValueError, TypeError):
        return v


# ---------------------------------------------------------------------------
# Metrics + availability
# ---------------------------------------------------------------------------

def compute_metrics_and_availability(
    meta: dict[str, Any], viral_threshold: float,
) -> tuple[dict[str, Any], dict[str, str], list[str]]:
    """Return (metrics, availability, missing_required)."""
    availability: dict[str, str] = {}
    for f in ALL_KNOWN_FIELDS:
        availability[f] = "available" if meta.get(f) not in (None, "") else "unavailable"

    missing_required = [f for f in REQUIRED_FIELDS if availability[f] == "unavailable"]
    if missing_required:
        return {}, availability, missing_required

    views = float(meta["views"])
    likes = float(meta["likes"])
    followers = float(meta["author_followers"])
    comments = float(meta.get("comments") or 0) if availability["comments"] == "available" else None
    shares = float(meta.get("shares") or 0) if availability["shares"] == "available" else None
    saves = float(meta.get("saves") or 0) if availability["saves"] == "available" else None

    def rate(numer):
        return round(numer / views * 100, 4) if (numer is not None and views > 0) else None

    engagement_numer = likes + (comments or 0) + (shares or 0) + (saves or 0)
    engagement_rate = round(engagement_numer / views * 100, 4) if views > 0 else None

    viral_score = round(views / followers, 2) if followers > 0 else None
    if viral_score is None:
        tier = "unknown"
    elif viral_score >= viral_threshold * 2:
        tier = "breakout"
    elif viral_score >= viral_threshold:
        tier = "viral"
    elif viral_score >= 1:
        tier = "expected"
    else:
        tier = "underperforming"

    metrics = {
        "engagement_rate_pct": engagement_rate,
        "like_rate_pct": rate(likes),
        "comment_rate_pct": rate(comments),
        "share_rate_pct": rate(shares),
        "save_rate_pct": rate(saves),
        "viral_score": viral_score,
        "viral_threshold": viral_threshold,
        "viral_tier": tier,
    }
    return metrics, availability, []


# ---------------------------------------------------------------------------
# Prompt assembly
# ---------------------------------------------------------------------------

def build_prompt(meta: dict[str, Any], metrics: dict[str, Any],
                 availability: dict[str, str], language: str) -> str:
    tpl = PROMPT_PATH.read_text(encoding="utf-8")
    lang_name = {"zh": "Simplified Chinese", "en": "English"}[language]
    return (
        tpl.replace("{LANGUAGE}", lang_name)
           .replace("{METADATA_JSON}", json.dumps(meta, ensure_ascii=False, indent=2))
           .replace("{METRICS_JSON}", json.dumps(metrics, ensure_ascii=False, indent=2))
           .replace("{AVAILABILITY_JSON}", json.dumps(availability, ensure_ascii=False, indent=2))
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    args = parse_args()

    videos = collect_videos(args)
    metadata_all = load_metadata(args, videos)

    run_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    tasks: list[dict[str, Any]] = []
    prepared = 0

    for v in videos:
        if prepared >= args.max_videos:
            print(f"Reached --max-videos={args.max_videos}, stopping.")
            break

        meta = metadata_all.get(v.name, {}) or {}
        metrics, availability, missing = compute_metrics_and_availability(meta, args.viral_threshold)

        if missing:
            reason = f"missing required field(s): {', '.join(missing)}"
            print(f"[SKIP] {v.name}: {reason}")
            tasks.append({
                "file": v.name,
                "video_path": str(v.resolve()),
                "metadata": meta,
                "field_availability": availability,
                "skipped": reason,
            })
            continue

        report_path = v.with_name(f"{v.stem}-{run_timestamp}.md")
        prompt = build_prompt(meta, metrics, availability, args.language)

        print(f"[READY] {v.name} (viral_score={metrics['viral_score']} "
              f"tier={metrics['viral_tier']}) -> agent will write {report_path}")

        tasks.append({
            "file": v.name,
            "video_path": str(v.resolve()),
            "metadata": meta,
            "metrics": metrics,
            "field_availability": availability,
            "language": args.language,
            "prompt": prompt,
            "suggested_report_path": str(report_path),
        })
        prepared += 1

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote task list -> {out_path}")
    print(
        "Next step (for the agent): for each non-skipped task, watch "
        "`video_path`, perform the full viral-attribution analysis using "
        "`prompt`, present the analysis to the user in the chat reply, "
        "and write the SAME content to `suggested_report_path`."
    )


if __name__ == "__main__":
    main()
