#!/usr/bin/env python3
"""Derive machine-readable artifacts from the approved narration article.

`script/SCRIPT.md` is the single source of spoken text. This turns it into
`timing/chapters.json` and refreshes the narration side of
`script/scene-plan.json`, leaving hand-authored visual fields untouched, so a
narration edit costs one command instead of three hand-synced copies.

Parsing is a white list: every line is a chapter heading, a blank separator, or
a narration line, and anything else stops the run. A black list would only
reject the markdown we happened to think of, and narration reaches TTS
verbatim — an unrecognised line must never be guessed at or silently dropped.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CHAPTER_RE = re.compile(r"^##\s+(S\d{2})\s+(\S.*?)\s*$")
CONTROL_RE = re.compile(r"<#[^#>]+#>|\[pause(?::[^\]]+)?\]", re.IGNORECASE)
ORDERED_LIST_RE = re.compile(r"^\d+[.)]\s")
LINK_RE = re.compile(r"\[[^\]]*\]\([^)]*\)")
ANCHOR_RE = re.compile(r"\banchor:\s*[\"']?([A-Za-z0-9]+\.\d+)")
LEADING_MARKERS = "#>|`-*+"

# What a derived scene skeleton carries so build_review and build_hyperframes
# can read it before anyone has written the art direction.
SCENE_SKELETON = {
    "title": "",
    "purpose": "",
    "evidence_ids": [],
    "screen_text": [],
    "visual_type": "",
    "visual_description": "",
    "visual_beats": [],
    "layout": "",
    "visual_data": {},
    "motion": [],
    "caption": {"mode": "bottom-pill", "max_lines": 2},
    "assets": [],
    "estimated_duration": 0.0,
    "transition": "hard-cut",
}


def narration_line_error(line: str) -> str | None:
    """Why this line cannot be spoken text, or None when it is valid.

    produce_voice.py imports this so a hand-edited or legacy chapters.json is
    rejected before the first paid provider call, not only at derivation time.
    """
    text = line.strip()
    if not text:
        return "a blank line cannot be spoken narration"
    if text.startswith("#"):
        return ("narration cannot start with '#'; a chapter heading must be "
                "written as `## S01 chapter name`")
    if text[0] in LEADING_MARKERS:
        return (f"narration cannot start with {text[0]!r}; markdown structure "
                "is not spoken content")
    if ORDERED_LIST_RE.match(text):
        return "narration cannot start with an ordered list marker"
    if "**" in text:
        return "narration cannot contain the bold marker **"
    if "`" in text:
        return "narration cannot contain backticks"
    if "<!--" in text or "-->" in text:
        return "narration cannot contain an HTML comment"
    if LINK_RE.search(text):
        return "narration cannot contain a markdown link"
    control = CONTROL_RE.search(text)
    if control:
        return (f"narration contains the inline control token {control.group(0)!r}; "
                "use script/voice-plan.json for exact pauses")
    return None


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_script(text: str, source: str) -> tuple[list[dict], list[str]]:
    """SCRIPT.md -> [{id, title, segments: [[line, ...], ...]}] plus errors."""
    chapters: list[dict] = []
    errors: list[str] = []
    current: dict | None = None
    block: list[str] = []
    seen: dict[str, int] = {}

    def flush() -> None:
        nonlocal block
        if block and current is not None:
            current["segments"].append(block)
        block = []

    for lineno, raw in enumerate(text.splitlines(), 1):
        heading = CHAPTER_RE.match(raw)
        if heading:
            flush()
            chapter_id, title = heading.group(1), heading.group(2)
            if not 1 <= int(chapter_id[1:]) <= 9:
                errors.append(
                    f"{source}:{lineno} chapter number {chapter_id} is outside S01-S09; "
                    "a two-digit chapter would collide with derived segment ids"
                )
            if chapter_id in seen:
                errors.append(
                    f"{source}:{lineno} chapter {chapter_id} already appears on "
                    f"line {seen[chapter_id]}"
                )
            seen[chapter_id] = lineno
            current = {"id": chapter_id, "title": title, "segments": []}
            chapters.append(current)
            continue
        if not raw.strip():
            flush()
            continue
        if current is None:
            errors.append(
                f"{source}:{lineno} narration appears before the first chapter "
                f"heading\n    {raw}"
            )
            continue
        problem = narration_line_error(raw)
        if problem:
            errors.append(f"{source}:{lineno} {problem}\n    {raw}")
            continue
        block.append(raw.strip())
    flush()

    for chapter in chapters:
        if not chapter["segments"]:
            errors.append(f"{source} chapter {chapter['id']} has no narration")
    if not chapters:
        errors.append(f"{source} has no `## S01 chapter name` heading")
    return chapters, errors


def segment_id(chapter_id: str, index: int) -> str:
    return f"S{int(chapter_id[1:])}{index}"


def build_chapters(parsed: list[dict], gap: float) -> dict:
    chapters = {}
    for chapter in parsed:
        segments = [
            {
                "id": segment_id(chapter["id"], index),
                "text": "\n".join(block),
                "start": 0.0,
                "end": 0.0,
                "duration": 0.0,
            }
            for index, block in enumerate(chapter["segments"], 1)
        ]
        chapters[chapter["id"]] = {"duration": 0.0, "segments": segments, "pause": gap}
    return {
        "chapters": chapters,
        "estimate_only": True,
        "note": "derived from script/SCRIPT.md; forced alignment overwrites these times",
    }


def carry_measured_timing(derived: dict, previous: dict) -> list[str]:
    """Keep measured times for segments whose text did not change.

    Re-deriving after a render must not throw away alignment results for the
    chapters nobody edited. Returns the chapters that did change.
    """
    stale: list[str] = []
    for chapter_id, chapter in derived["chapters"].items():
        old = (previous.get("chapters") or {}).get(chapter_id)
        if not old:
            stale.append(chapter_id)
            continue
        old_segments = {item.get("id"): item for item in old.get("segments", [])}
        unchanged = len(old_segments) == len(chapter["segments"])
        for segment in chapter["segments"]:
            prior = old_segments.get(segment["id"])
            if prior and prior.get("text") == segment["text"]:
                for key in ("start", "end", "duration"):
                    if key in prior:
                        segment[key] = prior[key]
            else:
                unchanged = False
        if unchanged:
            chapter["duration"] = old.get("duration", 0.0)
        else:
            stale.append(chapter_id)
    return stale


def is_placeholder(scene: dict) -> bool:
    """A template scene nobody has authored yet, safe to replace silently."""
    return not (scene.get("narration") or scene.get("visual_description")
                or scene.get("visual_beats") or scene.get("screen_text"))


def new_scene(scene_id: str) -> dict:
    scene = {"id": scene_id, "chapter": "", "narration": ""}
    scene.update(json.loads(json.dumps(SCENE_SKELETON)))
    return scene


def update_scene_plan(plan: dict, parsed: list[dict]) -> tuple[list[str], list[str]]:
    """Refresh the chapter map and narration; never touch visual authoring."""
    existing = {}
    for scene in plan.get("scenes", []):
        if scene.get("id") and not is_placeholder(scene):
            existing[scene["id"]] = scene

    scenes: list[dict] = []
    chapter_map: list[dict] = []
    created: list[str] = []
    for chapter in parsed:
        ids = []
        for index, block in enumerate(chapter["segments"], 1):
            sid = segment_id(chapter["id"], index)
            ids.append(sid)
            scene = existing.pop(sid, None)
            if scene is None:
                scene = new_scene(sid)
                created.append(sid)
            scene["chapter"] = f"{chapter['id']} · {chapter['title']}"
            scene["narration"] = "\n".join(block)
            scenes.append(scene)
        chapter_map.append({"id": chapter["id"], "title": chapter["title"], "scenes": ids})

    plan["chapters"] = chapter_map
    plan["scenes"] = scenes
    return created, sorted(existing)


def unit_texts(chapters: dict) -> dict[str, str]:
    units = {}
    for chapter in (chapters.get("chapters") or {}).values():
        for segment in chapter.get("segments", []):
            for index, line in enumerate(segment.get("text", "").split("\n"), 1):
                units[f"{segment.get('id')}.{index}"] = line
    return units


def moved_units(previous: dict, derived: dict) -> list[str]:
    """Unit ids whose spoken line changed, including ids that disappeared.

    Inserting one line mid-segment renumbers everything after it, which
    silently repoints voice-plan pauses and motion anchors at other sentences.
    """
    before, after = unit_texts(previous), unit_texts(derived)
    return sorted(uid for uid, line in before.items() if after.get(uid) != line)


def anchor_references(project: Path, units: set[str]) -> list[str]:
    hits: list[str] = []
    plan = load_json(project / "script/voice-plan.json", {}) or {}
    for pause in plan.get("pauses", []):
        if pause.get("after_unit") in units:
            hits.append(
                f"script/voice-plan.json pause {pause.get('id')} "
                f"after_unit={pause.get('after_unit')}"
            )
    motion = project / "motion/motion-plan.yaml"
    if motion.exists():
        for lineno, line in enumerate(motion.read_text(encoding="utf-8").splitlines(), 1):
            match = ANCHOR_RE.search(line)
            if match and match.group(1) in units:
                hits.append(f"motion/motion-plan.yaml:{lineno} anchor={match.group(1)}")
    return hits


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", required=True, type=Path)
    ap.add_argument("--write", action="store_true",
                    help="write the derived files; the default is a dry run")
    ap.add_argument("--force", action="store_true",
                    help="allow changes that invalidate recorded audio or drop authored scenes")
    args = ap.parse_args()

    project: Path = args.project
    script = project / "script/SCRIPT.md"
    if not script.exists():
        raise SystemExit(f"missing {script}")

    parsed, errors = parse_script(script.read_text(encoding="utf-8"), "script/SCRIPT.md")
    if errors:
        for problem in errors:
            print(problem)
        print(f"\n{len(errors)} structural problem(s); nothing was written.")
        sys.exit(1)

    config = load_json(project / "project-config.json", {}) or {}
    gap = float((config.get("audio") or {}).get("scene_gap_seconds", 0.8))

    previous = load_json(project / "timing/chapters.json", {}) or {}
    derived = build_chapters(parsed, gap)
    stale = carry_measured_timing(derived, previous)
    recorded = [
        chapter_id for chapter_id in stale
        if (project / f"audio/segments/{chapter_id}.wav").exists()
    ]

    plan_path = project / "script/scene-plan.json"
    plan = load_json(plan_path)
    created: list[str] = []
    orphans: list[str] = []
    if plan is not None:
        created, orphans = update_scene_plan(plan, parsed)

    segments = sum(len(c["segments"]) for c in derived["chapters"].values())
    print(f"{len(parsed)} chapter(s), {segments} segment(s)")
    for chapter in parsed:
        ids = ", ".join(
            segment_id(chapter["id"], index)
            for index in range(1, len(chapter["segments"]) + 1)
        )
        print(f"  {chapter['id']} {chapter['title']}: {ids}")

    shifted = moved_units(previous, derived)
    if shifted:
        preview = ", ".join(shifted[:12]) + (" ..." if len(shifted) > 12 else "")
        print(f"\n{len(shifted)} unit id(s) now carry different words: {preview}")
        for hit in anchor_references(project, set(shifted)):
            print(f"  recheck: {hit}")
    if created:
        print(f"\nnew scene skeleton(s): {', '.join(created)}")

    blocked: list[str] = []
    if recorded and not args.force:
        blocked.append(
            "these chapters are already recorded but no longer match the script, "
            "so they need re-recording; pass --force to accept that:\n    "
            + ", ".join(recorded)
        )
    if orphans and not args.force:
        blocked.append(
            "these scenes hold authored visuals but SCRIPT.md no longer references "
            "them; pass --force to delete them:\n    " + ", ".join(orphans)
        )
    if blocked:
        print()
        for reason in blocked:
            print(reason)
        print("\nNothing was written.")
        sys.exit(1)

    if orphans:
        print(f"\nremoved orphaned scene(s): {', '.join(orphans)}")
    if recorded:
        print(f"\ndropped measured times, re-record: {', '.join(recorded)}")

    if not args.write:
        print("\nDry run. Add --write once this looks right.")
        return

    write_json(project / "timing/chapters.json", derived)
    print("\nwrote timing/chapters.json")
    if plan is not None:
        write_json(plan_path, plan)
        print("updated the chapter map and narration in script/scene-plan.json")
    else:
        print("no script/scene-plan.json found; skipped the scene update")


if __name__ == "__main__":
    main()
