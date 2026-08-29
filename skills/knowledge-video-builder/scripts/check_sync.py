#!/usr/bin/env python3
"""Gate that audio, captions and motion still refer to the same take.

Runs after alignment and before rendering. The failure this exists to catch
is silent: a script line gets edited, that chapter is not re-recorded, and
every downstream number stays plausible while the voice says something else.
Alignment makes it measurable — a line whose characters the recogniser
cannot find is either misrecognised or not in the audio at all.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from align_audio import (  # noqa: E402
    DROP_CHARS,
    UNSUPPORTED_CONTROL_RE,
    canon,
    script_digest,
)
from apply_voice_plan import chapter_pauses, pause_digest  # noqa: E402
from apply_timing import literal_times  # noqa: E402
from derive_script_artifacts import (  # noqa: E402
    build_chapters,
    narration_line_error,
    parse_script,
)
from produce_voice import (  # noqa: E402
    plan_digest,
    reference_voice_sha256,
    settings as voice_settings,
    text_sha256,
    trailing_extra,
)

BLOCK_RE = re.compile(r"/\* timing:start.*?/\* timing:end \*/", re.DOTALL)
BEAT_REF_RE = re.compile(r"\b(?:B|BE|W|WE)\(\s*[\"']([^\"']+)[\"']")

CRITICAL, HIGH, MEDIUM = "Critical", "High", "Medium"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def heard_as(units: list[dict], asr_text: str) -> dict[str, str]:
    """Recover what the recogniser heard in each unit's span."""
    script, owner = [], []
    for index, unit in enumerate(units):
        for c in unit["text"]:
            if c not in DROP_CHARS:
                script.append(c)
                owner.append(index)
    matcher = difflib.SequenceMatcher(
        None, canon(asr_text), canon("".join(script)), autojunk=False
    )
    lo: dict[int, int] = {}
    hi: dict[int, int] = {}
    for a, b, size in matcher.get_matching_blocks():
        for k in range(size):
            u = owner[b + k]
            lo[u] = min(lo.get(u, a + k), a + k)
            hi[u] = max(hi.get(u, a + k), a + k)
    # Anchors only cover what matched, so a misheard tail would be invisible
    # in the report. Extend each unit up to where the next one starts.
    placed = sorted(lo)
    for cur, nxt in zip(placed, placed[1:]):
        hi[cur] = max(hi[cur], lo[nxt] - 1)

    return {
        unit["id"]: asr_text[lo[index]: hi[index] + 1]
        for index, unit in enumerate(units) if index in lo
    }


def run_timelines(project: Path) -> list[tuple[str, str]]:
    """Execute every composition timeline against a stubbed GSAP.

    An anchor that fails to resolve throws, the timeline never registers, and
    the render then succeeds with every frame showing the initial state. That
    is invisible to lint and expensive to find by watching, so run the code.
    """
    runtime = next((r for r in ("bun", "node") if shutil.which(r)), None)
    if not runtime:
        return [(MEDIUM, "no bun or node available; composition timelines were not executed")]

    runner = Path(__file__).with_name("check_timelines.js")
    comps = project / "hyperframes/compositions"
    result = subprocess.run(
        [runtime, str(runner), str(comps)],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        return []
    detail = (result.stdout + result.stderr).strip()
    return [(CRITICAL, f"a composition timeline failed to build:\n      "
                       + detail.replace("\n", "\n      "))]


def check_derivation(project: Path, config: dict, chapters: dict) -> list[tuple[str, str]]:
    """Confirm timing/chapters.json is still what SCRIPT.md derives to.

    SCRIPT.md is what the user reads and approves; chapters.json is what the
    voice actually speaks. Nothing else notices when the two drift apart,
    because every downstream number stays internally consistent.
    """
    script = project / "script/SCRIPT.md"
    if not script.exists():
        return [(HIGH, "script/SCRIPT.md is missing; the spoken text has no "
                       "single source and timing/chapters.json cannot be verified")]

    body = script.read_text(encoding="utf-8")
    if not any(line.startswith("##") for line in body.splitlines()):
        # Predates the chapter-heading contract, so there is nothing to derive
        # from. Say so instead of blocking a project that already rendered.
        return [(MEDIUM, "script/SCRIPT.md has no chapter headings, so it predates "
                         "the derivation contract and timing/chapters.json cannot be "
                         "verified against it; add `## S01 章节名` headings to bring "
                         "this project under the gate")]

    parsed, errors = parse_script(body, "script/SCRIPT.md")
    if errors:
        return [(HIGH, f"script/SCRIPT.md is not parseable: {problem}") for problem in errors]

    gap = float((config.get("audio") or {}).get("scene_gap_seconds", 0.8))
    expected = build_chapters(parsed, gap)["chapters"]
    issues: list[tuple[str, str]] = []
    for chapter_id in sorted(set(expected) | set(chapters)):
        want, have = expected.get(chapter_id), chapters.get(chapter_id)
        if want is None:
            issues.append((HIGH, f"{chapter_id}: SCRIPT.md no longer has this chapter; "
                                 "run derive_script_artifacts.py"))
            continue
        if have is None:
            issues.append((HIGH, f"{chapter_id}: SCRIPT.md has this chapter but "
                                 "timing/chapters.json does not; "
                                 "run derive_script_artifacts.py"))
            continue
        wanted = {item["id"]: item["text"] for item in want["segments"]}
        held = {item.get("id"): item.get("text", "") for item in have.get("segments", [])}
        drifted = sorted(
            set(wanted) ^ set(held)
            | {sid for sid in set(wanted) & set(held) if wanted[sid] != held[sid]}
        )
        if drifted:
            issues.append((
                HIGH,
                f"{chapter_id}: timing/chapters.json disagrees with SCRIPT.md at "
                f"{', '.join(drifted)}; run derive_script_artifacts.py --write",
            ))
    return issues


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", required=True, type=Path)
    ap.add_argument("--min-chapter-match", type=float, default=None)
    ap.add_argument("--min-unit-match", type=float, default=None)
    # build_timing.py targets 20 and allows a clause to run a little over rather
    # than cut it mid-phrase; this is the point past which it stops reading well.
    ap.add_argument("--cue-limit", type=int, default=30)
    args = ap.parse_args()

    project: Path = args.project
    config = load(project / "project-config.json") if (project / "project-config.json").exists() else {}
    timing_cfg = config.get("timing", {})
    if args.min_chapter_match is None:
        args.min_chapter_match = float(timing_cfg.get("min_chapter_match", 0.90))
    if args.min_unit_match is None:
        args.min_unit_match = float(timing_cfg.get("min_unit_match", 0.75))

    issues: list[tuple[str, str]] = []

    chapters = load(project / "timing/chapters.json")["chapters"]
    issues.extend(check_derivation(project, config, chapters))
    align_dir = project / "timing/align"
    voice_plan_path = project / "script/voice-plan.json"
    voice_plan = load(voice_plan_path) if voice_plan_path.exists() else None
    application_path = project / "audio/voice-plan-application.json"
    application = load(application_path) if application_path.exists() else {}
    tts_plan_path = project / "audio/tts-plan.json"
    production_path = project / "audio/voice-production.json"
    if tts_plan_path.exists():
        tts_plan = load(tts_plan_path)
        if not production_path.exists():
            issues.append((
                HIGH,
                "a bounded TTS plan exists but has not been produced; "
                "run produce_voice.py --generate",
            ))
        else:
            production = load(production_path)
            if production.get("plan_sha256") != plan_digest(tts_plan):
                issues.append((HIGH, "voice production is older than audio/tts-plan.json"))
            current_settings = voice_settings(project)
            current_settings_hash = text_sha256(
                json.dumps(current_settings, ensure_ascii=False, sort_keys=True)
            )
            if production.get("settings_sha256") != current_settings_hash:
                issues.append((HIGH, "voice consistency settings changed after production"))
            try:
                engineering_root = Path(__file__).resolve().parents[4]
                current_voice_hash = reference_voice_sha256(engineering_root)
                if production.get("reference_voice_sha256") != current_voice_hash:
                    issues.append((HIGH, "reference voice changed after production"))
            except RuntimeError as exc:
                issues.append((CRITICAL, str(exc)))

            for chapter_id in tts_plan.get("chapters", {}):
                produced = production.get("chapters", {}).get(chapter_id)
                wav = project / f"audio/segments/{chapter_id}.wav"
                if not produced:
                    issues.append((HIGH, f"{chapter_id}: no voice-production record"))
                    continue
                if (
                    not wav.exists()
                    or produced.get("final_audio_sha256") != sha256(wav)
                ):
                    issues.append((
                        HIGH,
                        f"{chapter_id}: final WAV does not match voice-production record",
                    ))
                previous_rate = None
                for chunk in produced.get("chunks", []):
                    selected = next(
                        (
                            item for item in chunk.get("candidates", [])
                            if item.get("attempt") == chunk.get("selected_attempt")
                        ),
                        None,
                    )
                    metrics = chunk.get("selected_metrics", {})
                    if selected is None or selected.get("rejection_reasons"):
                        issues.append((
                            HIGH,
                            f"{chunk.get('id', chapter_id)}: selected take did not "
                            "pass the recorded candidate gate",
                        ))
                        continue
                    rate = float(metrics.get("chars_per_second", 0))
                    if previous_rate is not None and abs(rate / previous_rate - 1) > (
                        current_settings["adjacent_tolerance"] + 0.001
                    ):
                        issues.append((
                            HIGH,
                            f"{chunk['id']}: selected pace jumps too far from "
                            "the preceding chunk",
                        ))
                    previous_rate = rate
                    lufs = float(metrics.get("normalized_lufs", -999))
                    if abs(lufs - current_settings["target_lufs"]) > (
                        current_settings["lufs_tolerance"] + 0.01
                    ):
                        issues.append((
                            HIGH,
                            f"{chunk['id']}: normalized loudness is outside tolerance",
                        ))
                    peak = float(metrics.get("normalized_true_peak", 999))
                    if peak > current_settings["true_peak"] + 0.1:
                        issues.append((
                            HIGH,
                            f"{chunk['id']}: normalized true peak exceeds target",
                        ))

    for chapter_id in sorted(chapters):
        for segment in chapters[chapter_id]["segments"]:
            marker = UNSUPPORTED_CONTROL_RE.search(segment.get("text", ""))
            if marker:
                issues.append((
                    HIGH,
                    f"{chapter_id}: unsupported inline control marker {marker.group(0)}; "
                    "keep narration clean and use script/voice-plan.json",
                ))
            for line in filter(str.strip, segment.get("text", "").splitlines()):
                problem = narration_line_error(line)
                if problem:
                    issues.append((HIGH, f"{segment.get('id', chapter_id)}: {problem}\n"
                                         f"      {line}"))

        planned_pauses = []
        if voice_plan is not None:
            try:
                planned_pauses = chapter_pauses(voice_plan, chapter_id)
            except ValueError as exc:
                issues.append((CRITICAL, f"voice plan is invalid: {exc}"))
        if planned_pauses:
            applied = application.get("chapters", {}).get(chapter_id)
            wav = project / f"audio/segments/{chapter_id}.wav"
            if not applied:
                issues.append((
                    HIGH,
                    f"{chapter_id}: exact pauses are planned but not applied; "
                    "run apply_voice_plan.py before final alignment",
                ))
            elif applied.get("chapter_plan_sha256") != pause_digest(planned_pauses):
                issues.append((
                    HIGH,
                    f"{chapter_id}: voice plan changed after pauses were applied",
                ))
            elif not wav.exists() or applied.get("output_sha256") != sha256(wav):
                issues.append((
                    HIGH,
                    f"{chapter_id}: narration changed after exact pauses were applied",
                ))

        path = align_dir / f"{chapter_id}.json"
        if not path.exists():
            issues.append((CRITICAL, f"{chapter_id}: no alignment; run align_audio.py"))
            continue
        data = load(path)

        current = script_digest(chapters[chapter_id]["segments"])
        if data.get("script_sha256") not in (None, current):
            issues.append((
                HIGH,
                f"{chapter_id}: the script changed after this alignment; "
                f"re-record if the wording moved, then re-align",
            ))
        wav = project / f"audio/segments/{chapter_id}.wav"
        if wav.exists() and path.stat().st_mtime < wav.stat().st_mtime:
            issues.append((HIGH, f"{chapter_id}: alignment is older than the audio"))

        rate = float(data.get("match_rate", 0))
        if rate < args.min_chapter_match:
            issues.append((
                HIGH,
                f"{chapter_id}: only {rate:.1%} of the script was found in the audio",
            ))

        heard = heard_as(data["units"], data.get("asr_text", ""))
        # Every rate above measures what the recogniser found; none of them
        # measure what it found in addition. A syllable the model voiced after
        # the last line leaves all of them at 100% and still ships.
        recognised = "".join(
            c for c in data.get("asr_text", "") if c not in DROP_CHARS
        )
        unscripted = trailing_extra(
            "".join(unit["text"] for unit in data["units"]), recognised
        )[0]
        if len(unscripted) > 1:
            issues.append((
                HIGH,
                f"{chapter_id}: the audio says {unscripted} after the script "
                f"ends; re-take the final chunk",
            ))
        for unit in data["units"]:
            spoken = sum(1 for c in unit["text"] if c not in DROP_CHARS)
            if spoken < 6:
                continue
            ratio = unit["anchors"] / spoken
            if ratio < args.min_unit_match:
                issues.append((
                    MEDIUM,
                    f"{unit['id']}: {ratio:.0%} matched\n"
                    f"      script: {unit['text']}\n"
                    f"      heard : {heard.get(unit['id'], '(nothing)')}",
                ))
            if unit["start"] is None or unit["end"] is None:
                issues.append((CRITICAL, f"{unit['id']}: missing timing"))
            elif unit["end"] <= unit["start"]:
                issues.append((HIGH, f"{unit['id']}: non-positive duration"))

        cue_path = project / f"timing/cues/{chapter_id}.json"
        if not cue_path.exists():
            issues.append((CRITICAL, f"{chapter_id}: no caption cues; run build_timing.py"))
        else:
            cues = load(cue_path)["cues"]
            duration = float(chapters[chapter_id]["duration"])
            for cue in cues:
                if not cue["text"].strip():
                    issues.append((HIGH, f"{chapter_id}: empty caption cue"))
                if len(cue["text"]) > args.cue_limit:
                    issues.append((
                        MEDIUM,
                        f"{chapter_id}: caption of {len(cue['text'])} characters "
                        f"exceeds the {args.cue_limit} limit: {cue['text']}",
                    ))
                if cue["text"].endswith("…") or cue["text"].endswith("..."):
                    issues.append((HIGH, f"{chapter_id}: caption is truncated: {cue['text']}"))
                if cue["start"] < -0.001 or cue["end"] > duration + 0.5:
                    issues.append((
                        HIGH,
                        f"{chapter_id}: caption {cue['start']:.2f}-{cue['end']:.2f} "
                        f"falls outside the chapter ({duration:.2f}s)",
                    ))
            for cur, nxt in zip(cues, cues[1:]):
                if nxt["start"] < cur["start"] - 0.001:
                    issues.append((HIGH, f"{chapter_id}: caption cues are out of order"))

    beats_path = project / "timing/beats.json"
    known = set(load(beats_path)["beats"]) if beats_path.exists() else set()
    if not known:
        issues.append((CRITICAL, "timing/beats.json is missing; run build_timing.py"))

    for comp in sorted((project / "hyperframes/compositions").glob("*.html")):
        body = BLOCK_RE.sub("", comp.read_text(encoding="utf-8"))
        for ref in BEAT_REF_RE.findall(body):
            if ref not in known:
                issues.append((CRITICAL, f"{comp.name}: references unknown beat {ref}"))
        literals = literal_times(comp)
        if literals:
            issues.append((
                MEDIUM,
                f"{comp.name}: {len(literals)} keyframe(s) still on literal seconds "
                f"({', '.join(literals[:6])}{' ...' if len(literals) > 6 else ''}); "
                f"a re-record will not move them",
            ))

    issues.extend(run_timelines(project))

    order = {CRITICAL: 0, HIGH: 1, MEDIUM: 2}
    issues.sort(key=lambda item: order[item[0]])
    blocking = sum(1 for level, _ in issues if level in (CRITICAL, HIGH))

    if not issues:
        print("Sync gate passed: audio, captions and motion all agree.")
        return
    for level, message in issues:
        print(f"[{level}] {message}")
    print(f"\n{len(issues)} issue(s), {blocking} blocking.")
    if blocking:
        sys.exit(1)


if __name__ == "__main__":
    main()
