#!/usr/bin/env python3
"""Turn forced-alignment output into the project's timing contracts.

Everything downstream — captions, motion anchors, subtitle deliverables —
reads from here, so a re-record only ever changes one set of numbers.

Consumes `timing/align/*.json` (see align_audio.py) and writes:

  timing/beats.json      motion anchors, keyed by unit id
  timing/sentences.json  measured sentence spans
  timing/words.json      per-character spans
  timing/cues/S0X.json   caption cues, chapter-relative
  timing/captions.srt    subtitle deliverable, whole video
  timing/scenes.json     chapter spans on the global timeline
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

# Sized for reading rhythm, not for the box: at 28px in a 1624px content width
# roughly 57 characters would fit, so the limit is what keeps a cue to about one
# clause rather than what prevents overflow. Cues are split, never truncated.
CUE_LIMIT = 20
SLACK = 5

SPLIT_AFTER = "，。？！；：、,.?!;:"
SENTENCE_END = "。？！?!"
NO_TIME = set("，。？！：；、,.?!:;\"'“”‘’《》〈〉（）()[]【】…—-～~·「」/\\|*#_` \n\r\t")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def srt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def is_word_char(c: str) -> bool:
    return c.isascii() and (c.isalnum() or c in "-_.'")


def cut_point(piece: str, limit: int) -> int:
    """Where to break a clause that has no punctuation to break at.

    A Latin term must not be split down the middle: `Markdown` becoming
    `Markdo` reads as a truncation bug even though nothing was lost. When the
    term alone is longer than the limit, the cue overflows instead — the
    caption box holds far more than the limit, which is set for reading
    rhythm rather than for width.
    """
    space = piece.rfind(" ", limit // 2, limit + 1)
    if space > 0:
        return space
    if limit >= len(piece):
        return len(piece)
    if not (is_word_char(piece[limit - 1]) and is_word_char(piece[limit])):
        return limit
    back = limit
    while back > limit // 2 and is_word_char(piece[back - 1]) and is_word_char(piece[back]):
        back -= 1
    if back > limit // 2:
        return back
    forward = limit
    while forward < len(piece) and is_word_char(piece[forward]):
        forward += 1
    return forward


def split_line(text: str, limit: int) -> list[tuple[int, int]]:
    """Break a narration line into caption-sized spans. Never truncates.

    Spans index the original text so each cue can be timed from the
    characters it actually covers.
    """
    spans: list[tuple[int, int]] = []
    pos = 0
    for part in re.split(rf"(?<=[{re.escape(SPLIT_AFTER)}])", text):
        if part:
            spans.append((pos, pos + len(part)))
            pos += len(part)

    merged: list[tuple[int, int]] = []
    for lo, hi in spans:
        # Merging across a full stop puts the tail of one sentence and the head
        # of the next on the same card, which reads as a fragment.
        closed = merged and text[: merged[-1][1]].rstrip().endswith(tuple(SENTENCE_END))
        if merged and not closed and hi - merged[-1][0] <= limit:
            merged[-1] = (merged[-1][0], hi)
        else:
            merged.append((lo, hi))

    # A clause a little over the limit reads better whole than cut mid-phrase,
    # so only split what is clearly too long.
    out: list[tuple[int, int]] = []
    for lo, hi in merged:
        while hi - lo > limit + SLACK:
            cut = lo + cut_point(text[lo:hi], limit)
            out.append((lo, cut))
            lo = cut
        if hi > lo:
            out.append((lo, hi))

    # An overflowing term can leave its trailing punctuation stranded as a cue
    # of its own. Give it back to the line it belongs to.
    joined: list[tuple[int, int]] = []
    for lo, hi in out:
        if joined and not any(c not in NO_TIME for c in text[lo:hi]):
            joined[-1] = (joined[-1][0], hi)
        else:
            joined.append((lo, hi))
    return joined


def cue_span(chars: list[dict], lo: int, hi: int,
             unit: dict) -> tuple[float, float]:
    """Time a slice of a unit from its measured characters."""
    inside = [c for c in chars if lo <= c["i"] < hi]
    if inside:
        return inside[0]["start"], inside[-1]["end"]
    before = [c for c in chars if c["i"] < lo]
    after = [c for c in chars if c["i"] >= hi]
    start = before[-1]["end"] if before else unit["start"]
    end = after[0]["start"] if after else unit["end"]
    return start, max(end, start)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", required=True, type=Path)
    ap.add_argument("--cue-limit", type=int, default=CUE_LIMIT)
    args = ap.parse_args()

    project: Path = args.project
    chapters = load(project / "timing/chapters.json")["chapters"]
    config = load(project / "project-config.json")
    gap = float(config.get("audio", {}).get("scene_gap_seconds", 0.8))

    align_dir = project / "timing/align"
    missing = [c for c in chapters if not (align_dir / f"{c}.json").exists()]
    if missing:
        raise SystemExit(f"no alignment for {', '.join(missing)}; run align_audio.py first")

    cues_dir = project / "timing/cues"
    cues_dir.mkdir(parents=True, exist_ok=True)

    beats: dict[str, dict] = {}
    sentences: list[dict] = []
    words: list[dict] = []
    scenes: list[dict] = []
    srt: list[str] = []
    offset = 0.0
    total_units = 0
    worst_match = 1.0
    sources: set[str] = set()

    for order, chapter_id in enumerate(sorted(chapters)):
        data = load(align_dir / f"{chapter_id}.json")
        duration = float(data["duration"])
        sources.add(data.get("source", "forced alignment"))
        worst_match = min(worst_match, float(data.get("match_rate", 1.0)))
        scenes.append({
            "id": chapter_id, "start": round(offset, 3),
            "end": round(offset + duration, 3), "duration": duration,
        })

        chapter_cues: list[dict] = []
        for unit in data["units"]:
            total_units += 1
            beats[unit["id"]] = {
                "chapter": chapter_id,
                "segment": unit["segment"],
                "text": unit["text"],
                "start": unit["start"],
                "end": unit["end"],
                "global_start": round(offset + unit["start"], 3),
                "anchors": unit["anchors"],
            }
            sentences.append({
                "id": unit["id"], "text": unit["text"],
                "start": round(offset + unit["start"], 3),
                "end": round(offset + unit["end"], 3),
            })
            for ch in unit["chars"]:
                if ch["c"] in NO_TIME:
                    continue
                words.append({
                    "text": ch["c"],
                    "start": round(offset + ch["start"], 3),
                    "end": round(offset + ch["end"], 3),
                    "anchored": ch["a"],
                })

            for lo, hi in split_line(unit["text"], args.cue_limit):
                piece = unit["text"][lo:hi].strip()
                if not piece:
                    continue
                start, end = cue_span(unit["chars"], lo, hi, unit)
                chapter_cues.append({
                    "start": round(start, 3), "end": round(end, 3),
                    "text": piece, "unit": unit["id"],
                })

        # A cue holds until the next one begins, so a gap would otherwise
        # leave the last line of a chapter hanging over silence.
        for cur, nxt in zip(chapter_cues, chapter_cues[1:]):
            cur["end"] = round(max(cur["end"], min(nxt["start"], cur["end"] + 0.4)), 3)
        if chapter_cues:
            chapter_cues[-1]["end"] = round(max(chapter_cues[-1]["end"], duration), 3)

        (cues_dir / f"{chapter_id}.json").write_text(
            json.dumps({"chapter": chapter_id, "duration": duration,
                        "cues": chapter_cues},
                       ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        for cue in chapter_cues:
            srt.append((offset + cue["start"], offset + cue["end"], cue["text"]))

        offset += duration + gap

    total = offset - gap
    source = " + ".join(sorted(sources)) or "forced alignment"

    (project / "timing/beats.json").write_text(
        json.dumps({"source": source,
                    "gap_seconds": gap, "duration": round(total, 3),
                    "beats": beats}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (project / "timing/sentences.json").write_text(
        json.dumps({"granularity": "sentence_aligned",
                    "source": source,
                    "sentences": sentences}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (project / "timing/words.json").write_text(
        json.dumps({"granularity": "character",
                    "source": source,
                    "words": words}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (project / "timing/scenes.json").write_text(
        json.dumps({"audio_file": "audio/narration.wav",
                    "duration": round(total, 3),
                    "timing_status": "forced_aligned",
                    "granularity": "character",
                    "scenes": scenes}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    blocks = []
    for index, (start, end, text) in enumerate(srt, 1):
        blocks.append(f"{index}\n{srt_time(start)} --> {srt_time(end)}\n{text}\n")
    (project / "timing/captions.srt").write_text("\n".join(blocks), encoding="utf-8")

    print(f"chapters {len(scenes)}, units {total_units}, cues {len(srt)}, "
          f"characters {len(words)}")
    print(f"total {total:.2f}s, lowest chapter match {worst_match:.1%}")
    longest = max((len(t) for _, _, t in srt), default=0)
    print(f"longest cue {longest} characters (limit {args.cue_limit})")


if __name__ == "__main__":
    main()
