#!/usr/bin/env python3
"""Forced alignment of narration audio against the known script.

Recognises the audio with timestamps, then aligns the recognised character
stream to the authoritative script text with an edit-distance match.
Recognition errors are tolerated: correctly recognised characters act as
anchors and everything between them is interpolated.

Recognition runs on Groq's hosted whisper-large-v3. Output is a per-chapter
alignment file whose unit boundaries are measured from the audio rather than
estimated from character counts.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from dataclasses import dataclass, field
from pathlib import Path

# Stripped before alignment: punctuation carries no audio of its own.
DROP_CHARS = set(
    "，。？！：；、,.?!:;\"'“”‘’《》〈〉（）()[]【】…—-～~·「」/\\|*#_`\n\r\t "
)

UNSUPPORTED_CONTROL_RE = re.compile(r"<#[^#>]+#>")
SENTENCE_END = "。？！?!"

GROQ_URL = "https://api.groq.com/openai/v1/audio/transcriptions"
GROQ_MODEL = "whisper-large-v3"
# The published ceiling is 25 MB; stay under it so multipart framing cannot
# push a borderline upload over.
GROQ_UPLOAD_LIMIT = 24 * 1024 * 1024
# 16 kHz mono FLAC runs about 20 KB/s, so this window is far inside the limit
# while keeping the number of round trips low.
GROQ_WINDOW_SECONDS = 600.0
GROQ_RETRY_STATUS = {408, 409, 429, 500, 502, 503, 504}
GROQ_ATTEMPTS = 4

# Anything ffmpeg can decode is acceptable input; these are the extensions a
# chapter take is looked up under when the project stores something other than
# the wav the TTS pipeline writes.
AUDIO_EXTENSIONS = (
    ".wav", ".flac", ".mp3", ".m4a", ".ogg", ".opus", ".aac", ".mp4", ".webm",
)


def script_digest(segments: list[dict]) -> str:
    """Fingerprint the text a chapter was aligned against.

    Lets a later gate tell "the script moved on" apart from "the recogniser
    misheard a word", which look identical in a match rate alone.
    """
    body = "\u0000".join(seg.get("text", "") for seg in segments)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()

# Recognition and script routinely disagree on surface form without
# disagreeing on what was said: "Skill" vs "skill", "八点" vs "8点".
# Folding both sides costs nothing when they already agree, and recovers
# anchors when they do not. Every mapping is 1:1 so character indices,
# which carry the unit ownership, survive.
CANON = str.maketrans("〇零一二三四五六七八九", "00123456789")


def canon(text: str) -> str:
    return text.lower().translate(CANON)


@dataclass
class Unit:
    """One narration line or sentence: the granularity motion cues attach to."""

    id: str
    segment: str
    text: str
    kind: str = "line"
    start: float | None = None
    end: float | None = None
    anchors: int = 0
    # Per-character times, so a caption may be split at any point in the line
    # without falling back to a character-count estimate.
    chars: list[dict] = field(default_factory=list)


def to_pcm16k(wav: Path, dest: Path) -> Path:
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(wav),
         "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", str(dest)],
        check=True,
    )
    return dest


def engineering_root() -> Path:
    """The directory holding .cursor/skills and the single .skill.env."""
    return Path(__file__).resolve().parents[4]


def load_env(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    values = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def media_duration(audio: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(audio)],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    return float(out)


def to_flac16k(audio: Path, dest: Path, start: float | None = None,
               end: float | None = None) -> Path:
    """Encode an upload copy: 16 kHz mono FLAC, optionally a window of it.

    The service downsamples to 16 kHz mono anyway, so sending anything richer
    only buys upload time — on one 104 s take this is 2.1 MB instead of 20 MB.
    """
    window = []
    if start is not None:
        window += ["-ss", f"{start:.3f}"]
    if end is not None:
        window += ["-to", f"{end:.3f}"]
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", *window, "-i", str(audio),
         "-ar", "16000", "-ac", "1", "-map", "0:a", "-c:a", "flac", str(dest)],
        check=True,
    )
    return dest


def silence_midpoints(audio: Path) -> list[float]:
    out = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", str(audio), "-af",
         "silencedetect=n=-35dB:d=0.25", "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    starts = [float(v) for v in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(v) for v in re.findall(r"silence_end: ([\d.]+)", out)]
    return [(s + e) / 2 for s, e in zip(starts, ends)]


def upload_windows(audio: Path, tmp: Path) -> list[tuple[float, Path]]:
    """Encoded uploads with their offset into the take.

    A single file is the normal case. Only a take long enough to exceed the
    upload limit is split, and then at the middle of a detected silence so the
    seam does not land inside a word.
    """
    whole = to_flac16k(audio, tmp / "upload.flac")
    if whole.stat().st_size <= GROQ_UPLOAD_LIMIT:
        return [(0.0, whole)]
    whole.unlink()

    duration = media_duration(audio)
    silences = silence_midpoints(audio)
    cuts: list[float] = []
    target = GROQ_WINDOW_SECONDS
    while target < duration:
        near = min(silences, key=lambda t: abs(t - target), default=None)
        floor = (cuts[-1] if cuts else 0.0) + 1.0
        usable = near is not None and abs(near - target) <= 30.0 and near > floor
        cut = near if usable else target
        cuts.append(cut)
        target = cut + GROQ_WINDOW_SECONDS

    bounds = [0.0, *cuts, duration]
    windows = []
    for index, (start, end) in enumerate(zip(bounds, bounds[1:])):
        part = to_flac16k(audio, tmp / f"upload-{index:02d}.flac", start, end)
        windows.append((start, part))
    return windows


def groq_post(part: Path, language: str, model: str, api_key: str,
              proxy: str) -> dict:
    boundary = uuid.uuid4().hex
    fields = [
        ("model", model),
        ("response_format", "verbose_json"),
        ("timestamp_granularities[]", "word"),
        ("timestamp_granularities[]", "segment"),
        ("temperature", "0"),
    ]
    if language:
        fields.append(("language", language))

    body = bytearray()
    for name, value in fields:
        body += (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
            f"{value}\r\n"
        ).encode("utf-8")
    body += (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{part.name}"\r\n'
        "Content-Type: audio/flac\r\n\r\n"
    ).encode("utf-8")
    body += part.read_bytes()
    body += f"\r\n--{boundary}--\r\n".encode("utf-8")

    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy} if proxy else {})
    )
    request = urllib.request.Request(
        GROQ_URL, data=bytes(body), method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            # The default urllib agent is refused at the edge with a bare
            # "error code: 1010" that looks nothing like an auth failure.
            "User-Agent": "knowledge-video-builder/1.0",
        },
    )

    delay = 2.0
    for attempt in range(1, GROQ_ATTEMPTS + 1):
        try:
            with opener.open(request, timeout=300) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:400]
            if exc.code not in GROQ_RETRY_STATUS or attempt == GROQ_ATTEMPTS:
                raise RuntimeError(f"groq transcription failed ({exc.code}): {detail}")
            wait = float(exc.headers.get("retry-after") or delay)
        except urllib.error.URLError as exc:
            if attempt == GROQ_ATTEMPTS:
                raise RuntimeError(
                    f"groq transcription unreachable: {exc.reason}. "
                    "Check SKILL_PROXY in .skill.env."
                )
            wait = delay
        time.sleep(wait)
        delay *= 2
    raise RuntimeError("groq transcription failed")


def groq_tokens(payload: dict) -> list[tuple[str, float, float]]:
    """Timed tokens from a verbose_json response, forced monotonic.

    Word timestamps come back overlapping now and then — on one 104 s take,
    16 of 451 words started before the previous word ended. Clamping each
    start to the running cursor keeps the character stream in order, which is
    what the edit-distance alignment assumes.
    """
    items = payload.get("words") or []
    if not items:
        # No word granularity means the take was short or silent enough that
        # only segments came back; segment spans still place the text.
        items = [
            {"word": seg.get("text", ""), "start": seg.get("start"), "end": seg.get("end")}
            for seg in payload.get("segments") or []
        ]

    limit = float(payload.get("duration") or 0.0)
    tokens: list[tuple[str, float, float]] = []
    cursor = 0.0
    for item in items:
        text = str(item.get("word") or "").strip()
        if not text:
            continue
        start = max(float(item.get("start") or 0.0), cursor)
        end = max(float(item.get("end") or start), start)
        if limit:
            start, end = min(start, limit), min(end, limit)
        cursor = end
        tokens.append((text, start, end))
    return tokens


def transcribe(audio: Path, language: str, model: str, api_key: str,
               proxy: str) -> list[tuple[str, float, float]]:
    """Return (token_text, start, end) triples with word-level timestamps."""
    with tempfile.TemporaryDirectory() as tmp:
        tokens: list[tuple[str, float, float]] = []
        for offset, part in upload_windows(audio, Path(tmp)):
            tokens += [
                (text, start + offset, end + offset)
                for text, start, end in groq_tokens(
                    groq_post(part, language, model, api_key, proxy)
                )
            ]
    return tokens


@dataclass
class Recognizer:
    """Groq's hosted Whisper, resolved once and passed to whatever needs it."""

    model: str
    api_key: str
    proxy: str

    @property
    def source(self) -> str:
        return "groq forced alignment"

    def transcribe(self, audio: Path, language: str) -> list[tuple[str, float, float]]:
        return transcribe(audio, language, self.model, self.api_key, self.proxy)


def resolve_recognizer(model: str = GROQ_MODEL) -> Recognizer:
    env = load_env(engineering_root() / ".skill.env")
    api_key = env.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        sys.exit(
            f"GROQ_API_KEY not found in {engineering_root() / '.skill.env'}; "
            "recognition cannot run"
        )
    proxy = (
        env.get("SKILL_PROXY")
        or os.environ.get("HTTPS_PROXY")
        or os.environ.get("https_proxy", "")
    )
    return Recognizer(model=model, api_key=api_key, proxy=proxy)


def chapter_audio(project: Path, chapter_id: str) -> Path | None:
    base = project / "audio/segments"
    for ext in AUDIO_EXTENSIONS:
        candidate = base / f"{chapter_id}{ext}"
        if candidate.exists():
            return candidate
    return None


def explode(tokens: list[tuple[str, float, float]]) -> tuple[str, list[tuple[float, float]]]:
    """Flatten multi-character tokens into a character stream with times."""
    chars, spans = [], []
    for text, start, end in tokens:
        keep = [c for c in text if c not in DROP_CHARS]
        if not keep:
            continue
        step = (end - start) / len(keep)
        for i, c in enumerate(keep):
            chars.append(c)
            spans.append((start + i * step, start + (i + 1) * step))
    return "".join(chars), spans


def speech_edges(pcm: Path, min_pause: float = 0.15) -> tuple[list[float], list[float]]:
    """Locate speech onsets and offsets from short-time energy.

    Recognition places a sentence roughly; energy places its first syllable
    exactly. The recogniser puts a segment boundary in the middle of a pause,
    which can sit a few hundred milliseconds before the speaker opens up.
    """
    import wave

    import numpy as np

    with wave.open(str(pcm)) as w:
        sr = w.getframerate()
        samples = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
    x = samples.astype(np.float32) / 32768.0
    hop, win = int(0.01 * sr), int(0.025 * sr)
    frames = max((len(x) - win) // hop, 0)
    if frames == 0:
        return [], []
    energy = np.sqrt(
        np.mean(
            np.lib.stride_tricks.sliding_window_view(x, win)[: frames * hop : hop] ** 2,
            axis=1,
        )
    )
    db = 20 * np.log10(energy + 1e-9)
    # Reference the loud end of the distribution so the threshold tracks the
    # take's own level instead of an absolute dBFS value.
    threshold = float(np.percentile(db, 90)) - 25.0
    silent = db < threshold

    onsets, offsets = [], []
    i, n = 0, len(silent)
    while i < n:
        if silent[i]:
            j = i
            while j < n and silent[j]:
                j += 1
            if (j - i) * 0.01 >= min_pause:
                offsets.append(i * 0.01)
                if j < n:
                    onsets.append(j * 0.01)
            i = j
        else:
            i += 1
    return onsets, offsets


def clamp_chars(units: list[Unit]) -> None:
    """Keep character times inside their unit after boundary adjustments."""
    for unit in units:
        if unit.start is None or unit.end is None:
            continue
        for ch in unit.chars:
            ch["start"] = round(min(max(ch["start"], unit.start), unit.end), 3)
            ch["end"] = round(min(max(ch["end"], ch["start"]), unit.end), 3)


def rescale(unit: Unit, was: tuple[float, float]) -> None:
    """Map character times from the old unit span onto the new one."""
    old_start, old_end = was
    span = old_end - old_start
    if span <= 0 or unit.start is None or unit.end is None:
        return
    factor = (unit.end - unit.start) / span
    for ch in unit.chars:
        ch["start"] = round(unit.start + (ch["start"] - old_start) * factor, 3)
        ch["end"] = round(unit.start + (ch["end"] - old_start) * factor, 3)


def snap(units: list[Unit], onsets: list[float], offsets: list[float],
         window: float) -> int:
    """Pull unit boundaries onto the nearest measured speech edge."""
    import bisect

    moved = 0

    def nearest(points: list[float], t: float) -> float | None:
        if not points:
            return None
        i = bisect.bisect_left(points, t)
        best = None
        for c in (i - 1, i):
            if 0 <= c < len(points) and abs(points[c] - t) <= window:
                if best is None or abs(points[c] - t) < abs(best - t):
                    best = points[c]
        return best

    for idx, unit in enumerate(units):
        if unit.start is None or unit.end is None:
            continue
        was = (unit.start, unit.end)
        # Only the first unit may begin at true zero; others follow a pause.
        cand = nearest(onsets, unit.start) if idx else None
        if cand is not None and abs(cand - unit.start) > 0.02:
            unit.start = round(cand, 3)
            moved += 1
        cand = nearest(offsets, unit.end)
        if cand is not None and cand > unit.start:
            unit.end = round(cand, 3)
        rescale(unit, was)

    for prev, cur in zip(units, units[1:]):
        if prev.end is not None and cur.start is not None and prev.end > cur.start:
            prev.end = cur.start
    clamp_chars(units)
    return moved


def split_units(chapter_id: str, segments: list[dict], sentence_level: bool) -> list[Unit]:
    units: list[Unit] = []
    for seg in segments:
        seg_id = seg.get("id", chapter_id)
        for raw in seg.get("text", "").split("\n"):
            line = raw.strip()
            if not line:
                continue
            if UNSUPPORTED_CONTROL_RE.search(line):
                raise ValueError(
                    f"{seg_id}: unsupported inline control marker in narration: {line}. "
                    "Keep spoken text clean and declare exact pauses in "
                    "script/voice-plan.json."
                )
            pieces = [line]
            if sentence_level:
                pieces = [p for p in re.split(rf"(?<=[{SENTENCE_END}])", line) if p.strip()]
            for piece in pieces:
                units.append(
                    Unit(
                        id=f"{seg_id}.{sum(1 for u in units if u.segment == seg_id) + 1}",
                        segment=seg_id,
                        text=piece.strip(),
                    )
                )
    return units


def align(units: list[Unit], asr_text: str, spans: list[tuple[float, float]],
          duration: float) -> float:
    """Assign measured start/end to every unit. Returns the anchor match rate."""
    script_chars: list[str] = []
    owner: list[tuple[int, int]] = []
    for idx, unit in enumerate(units):
        for pos, c in enumerate(unit.text):
            if c in DROP_CHARS:
                continue
            script_chars.append(c)
            owner.append((idx, pos))
    script_text = "".join(script_chars)
    if not script_text:
        return 0.0

    starts: list[float | None] = [None] * len(script_text)
    ends: list[float | None] = [None] * len(script_text)
    matched = 0
    matcher = difflib.SequenceMatcher(
        None, canon(asr_text), canon(script_text), autojunk=False
    )
    for a, b, size in matcher.get_matching_blocks():
        for k in range(size):
            starts[b + k], ends[b + k] = spans[a + k]
            matched += 1

    # Anchor the ends so interpolation has something to work against.
    if starts[0] is None:
        starts[0] = ends[0] = 0.0
    if starts[-1] is None:
        starts[-1] = ends[-1] = duration

    known = [i for i, v in enumerate(starts) if v is not None]
    for left, right in zip(known, known[1:]):
        gap = right - left
        if gap < 2:
            continue
        t0, t1 = ends[left], starts[right]
        step = (t1 - t0) / gap
        for j in range(1, gap):
            starts[left + j] = t0 + (j - 1) * step
            ends[left + j] = t0 + j * step

    anchored = set(known)
    for idx, unit in enumerate(units):
        mine = [i for i, (u, _) in enumerate(owner) if u == idx]
        if not mine:
            continue
        unit.start = round(min(starts[i] for i in mine), 3)
        unit.end = round(max(ends[i] for i in mine), 3)
        unit.anchors = sum(1 for i in mine if i in anchored)
        unit.chars = [
            {"i": owner[i][1], "c": script_chars[i],
             "start": round(starts[i], 3), "end": round(ends[i], 3),
             "a": i in anchored}
            for i in mine
        ]

    # Monotonicity: a later unit may never start before an earlier one ends.
    for prev, cur in zip(units, units[1:]):
        if cur.start is not None and prev.end is not None and cur.start < prev.end:
            cur.start = prev.end
    clamp_chars(units)

    return matched / len(script_text)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", required=True, type=Path,
                    help="video project root containing timing/chapters.json")
    ap.add_argument("--chapters", nargs="*", help="chapter ids; default all")
    ap.add_argument("--model", default=GROQ_MODEL,
                    help="groq speech-to-text model")
    ap.add_argument("--language", default="zh")
    ap.add_argument("--sentence-level", action="store_true",
                    help="split narration lines further at 。？！")
    ap.add_argument("--no-snap", action="store_true",
                    help="skip energy-based refinement of boundaries")
    ap.add_argument("--snap-window", type=float, default=0.7,
                    help="max seconds a boundary may be pulled to a speech edge")
    ap.add_argument("--out", type=Path, help="output dir; default <project>/timing/align")
    args = ap.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not found")
    asr = resolve_recognizer(args.model)

    chapters = json.loads((args.project / "timing/chapters.json").read_text(encoding="utf-8"))["chapters"]
    out_dir = args.out or (args.project / "timing/align")
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"recogniser: groq ({asr.model})", flush=True)
    summary = []
    for chapter_id in (args.chapters or sorted(chapters)):
        chapter = chapters[chapter_id]
        take = chapter_audio(args.project, chapter_id)
        if take is None:
            print(f"{chapter_id}: no audio in {args.project / 'audio/segments'}",
                  file=sys.stderr)
            continue
        duration = float(chapter["duration"])
        units = split_units(chapter_id, chapter["segments"], args.sentence_level)
        with tempfile.TemporaryDirectory() as tmp:
            pcm = to_pcm16k(take, Path(tmp) / "16k.wav")
            tokens = asr.transcribe(pcm, args.language)
            asr_text, spans = explode(tokens)
            rate = align(units, asr_text, spans, duration)
            moved = 0
            if not args.no_snap:
                onsets, offsets = speech_edges(pcm)
                moved = snap(units, onsets, offsets, args.snap_window)

        payload = {
            "chapter": chapter_id,
            "duration": duration,
            "granularity": "sentence" if args.sentence_level else "line",
            "source": asr.source,
            "model": asr.model,
            "script_sha256": script_digest(chapter["segments"]),
            "match_rate": round(rate, 4),
            "snapped_units": moved,
            "units": [
                {"id": u.id, "segment": u.segment, "text": u.text,
                 "start": u.start, "end": u.end, "anchors": u.anchors,
                 "chars": u.chars}
                for u in units
            ],
            "asr_text": asr_text,
        }
        (out_dir / f"{chapter_id}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        summary.append((chapter_id, len(units), rate))
        print(f"{chapter_id}: {len(units)} units, match {rate:.1%}, snapped {moved}",
              flush=True)

    if summary:
        worst = min(r for _, _, r in summary)
        print(f"\nlowest match rate: {worst:.1%}")


if __name__ == "__main__":
    main()
