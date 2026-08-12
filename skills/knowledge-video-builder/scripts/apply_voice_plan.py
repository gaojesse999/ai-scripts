#!/usr/bin/env python3
"""Insert exact, structured pauses into aligned PCM narration.

The spoken script stays clean. Pause intent lives in script/voice-plan.json,
is resolved against a preliminary forced alignment, and is applied to the WAV
before the final alignment/timing build.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
import wave
from datetime import datetime, timezone
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pause_digest(pauses: list[dict]) -> str:
    body = json.dumps(pauses, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def chapter_pauses(plan: dict, chapter: str) -> list[dict]:
    pauses = [
        item for item in plan.get("pauses", [])
        if item.get("chapter") == chapter and item.get("enabled", True)
    ]
    seen: set[str] = set()
    by_anchor: dict[str, dict] = {}
    for item in pauses:
        pause_id = str(item.get("id", "")).strip()
        if not pause_id:
            raise ValueError(f"{chapter}: pause id is required")
        if pause_id in seen:
            raise ValueError(f"{chapter}: duplicate pause id {pause_id}")
        seen.add(pause_id)
        if not str(item.get("after_unit", "")).strip():
            raise ValueError(f"{pause_id}: after_unit is required")
        seconds = float(item.get("seconds", 0))
        if not 0 < seconds <= 10:
            raise ValueError(f"{pause_id}: seconds must be in (0, 10]")
        if item.get("source", "automatic") not in {"automatic", "user"}:
            raise ValueError(f"{pause_id}: source must be automatic or user")
        anchor = str(item["after_unit"])
        previous = by_anchor.get(anchor)
        if previous is None:
            by_anchor[anchor] = item
        elif previous.get("source") == "user" and item.get("source") != "user":
            continue
        elif item.get("source") == "user" and previous.get("source") != "user":
            by_anchor[anchor] = item
        else:
            raise ValueError(
                f"{chapter}: multiple {item.get('source', 'automatic')} pauses "
                f"target {anchor}; keep one"
            )
    return list(by_anchor.values())


def resolve_pauses(pauses: list[dict], alignment: dict) -> list[dict]:
    units = {unit["id"]: unit for unit in alignment.get("units", [])}
    resolved = []
    for item in pauses:
        unit_id = item["after_unit"]
        if unit_id not in units:
            raise ValueError(f"{item['id']}: alignment has no unit {unit_id}")
        unit = units[unit_id]
        expected = item.get("after_text")
        if expected is not None and expected.strip() != unit["text"].strip():
            raise ValueError(
                f"{item['id']}: after_text no longer matches {unit_id}; "
                "update the voice plan after editing the narration"
            )
        at = unit.get("end")
        if at is None:
            raise ValueError(f"{item['id']}: {unit_id} has no measured end time")
        resolved.append({
            "id": item["id"],
            "after_unit": unit_id,
            "segment": unit["segment"],
            "after_text": unit["text"],
            "seconds": round(float(item["seconds"]), 3),
            "at": round(float(at), 3),
            "source": item.get("source", "automatic"),
            "reason": item.get("reason", ""),
        })
    return sorted(resolved, key=lambda item: (item["at"], item["id"]))


def update_chapter_timing(project: Path, chapter: str, pauses: list[dict]) -> float:
    path = project / "timing/chapters.json"
    data = load_json(path)
    item = data["chapters"][chapter]
    added_by_segment: dict[str, float] = {}
    for pause in pauses:
        segment = pause["segment"]
        added_by_segment[segment] = added_by_segment.get(segment, 0.0) + pause["seconds"]

    cursor = 0.0
    gap = float(item.get("pause", 0))
    for segment in item["segments"]:
        duration = float(segment["duration"]) + added_by_segment.get(segment["id"], 0.0)
        segment["duration"] = round(duration, 3)
        segment["start"] = round(cursor, 3)
        segment["end"] = round(cursor + duration, 3)
        cursor = segment["end"] + gap
    item["duration"] = item["segments"][-1]["end"]
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return float(item["duration"])


def write_with_pauses(source: Path, output: Path, pauses: list[dict]) -> tuple[float, float]:
    with wave.open(str(source), "rb") as wav:
        params = wav.getparams()
        if params.comptype != "NONE":
            raise ValueError("voice-plan input must be uncompressed PCM WAV")
        frames = wav.readframes(wav.getnframes())

    frame_size = params.nchannels * params.sampwidth
    total_frames = len(frames) // frame_size
    by_frame: dict[int, int] = {}
    for pause in pauses:
        frame = round(pause["at"] * params.framerate)
        if frame < 0 or frame > total_frames:
            raise ValueError(
                f"{pause['id']}: pause time {pause['at']:.3f}s is outside "
                f"the {total_frames / params.framerate:.3f}s WAV"
            )
        by_frame[frame] = by_frame.get(frame, 0) + round(
            pause["seconds"] * params.framerate
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    in_place = source.resolve() == output.resolve()
    if in_place:
        handle = tempfile.NamedTemporaryFile(
            prefix=f".{output.name}.", suffix=".tmp", dir=output.parent, delete=False
        )
        handle.close()
        target = Path(handle.name)
    else:
        target = output

    try:
        with wave.open(str(target), "wb") as wav:
            wav.setparams(params)
            cursor = 0
            for frame, silence_frames in sorted(by_frame.items()):
                wav.writeframes(frames[cursor * frame_size: frame * frame_size])
                wav.writeframes(b"\x00" * silence_frames * frame_size)
                cursor = frame
            wav.writeframes(frames[cursor * frame_size:])
        if in_place:
            os.replace(target, output)
    finally:
        if target.exists() and target != output:
            target.unlink(missing_ok=True)

    before = total_frames / params.framerate
    after = before + sum(by_frame.values()) / params.framerate
    return round(before, 6), round(after, 6)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", required=True, type=Path)
    ap.add_argument("--chapter", required=True)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--plan", type=Path)
    ap.add_argument("--alignment", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    project = args.project.resolve()
    plan_path = args.plan or project / "script/voice-plan.json"
    alignment_path = args.alignment or project / f"timing/align/{args.chapter}.json"
    source = args.input or project / f"audio/segments/{args.chapter}.wav"
    output = args.output or source
    application_path = project / "audio/voice-plan-application.json"

    for path in (plan_path, alignment_path, source):
        if not path.exists():
            raise SystemExit(f"missing required input: {path}")

    plan = load_json(plan_path)
    pauses = chapter_pauses(plan, args.chapter)
    if not pauses:
        raise SystemExit(f"{args.chapter}: voice plan contains no enabled pauses")
    alignment = load_json(alignment_path)
    if alignment.get("chapter") != args.chapter:
        raise SystemExit(
            f"alignment chapter is {alignment.get('chapter')}, expected {args.chapter}"
        )
    resolved = resolve_pauses(pauses, alignment)

    with wave.open(str(source), "rb") as wav:
        wav_duration = wav.getnframes() / wav.getframerate()
    aligned_duration = float(alignment.get("duration", 0))
    if abs(wav_duration - aligned_duration) > 0.1:
        raise SystemExit(
            f"{args.chapter}: alignment duration {aligned_duration:.3f}s does not "
            f"match input WAV {wav_duration:.3f}s; re-align the unpaused take first"
        )

    chapter_hash = pause_digest(pauses)
    existing = load_json(application_path) if application_path.exists() else {}
    old = existing.get("chapters", {}).get(args.chapter, {})
    if (
        source.resolve() == output.resolve()
        and old.get("chapter_plan_sha256") == chapter_hash
        and old.get("output_sha256") == sha256(source)
    ):
        raise SystemExit(
            f"{args.chapter}: this voice plan is already applied to {source}"
        )

    if args.dry_run:
        for item in resolved:
            print(
                f"{args.chapter} {item['id']}: insert {item['seconds']:.3f}s "
                f"after {item['after_unit']} at {item['at']:.3f}s"
            )
        return

    source_hash = sha256(source)
    before, after = write_with_pauses(source, output, resolved)
    payload = existing or {"schema_version": "1.0", "chapters": {}}
    payload["voice_plan"] = str(plan_path)
    payload["voice_plan_sha256"] = sha256(plan_path)
    payload["generated_at"] = datetime.now(timezone.utc).isoformat()
    payload.setdefault("chapters", {})[args.chapter] = {
        "chapter_plan_sha256": chapter_hash,
        "input": str(source),
        "input_sha256": source_hash,
        "output": str(output),
        "output_sha256": sha256(output),
        "alignment": str(alignment_path),
        "alignment_sha256": sha256(alignment_path),
        "duration_before": before,
        "duration_after": after,
        "pauses": resolved,
    }
    canonical = project / f"audio/segments/{args.chapter}.wav"
    if output.resolve() == canonical.resolve():
        chapter_duration = update_chapter_timing(project, args.chapter, resolved)
        payload["chapters"][args.chapter]["chapter_duration"] = chapter_duration
    application_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"{args.chapter}: inserted {len(resolved)} pause(s), "
        f"{before:.3f}s -> {after:.3f}s: {output}"
    )


if __name__ == "__main__":
    main()
