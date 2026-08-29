#!/usr/bin/env python3
"""Produce duration-bounded, measured, loudness-matched narration.

This orchestrator keeps provider calls short, generates multiple candidates,
rejects truncation/clipping/pace drift, normalizes selected takes, merges them,
applies structured pauses, and runs final forced alignment. It calls mimo-tts
as an unchanged low-level provider.
"""

from __future__ import annotations

import argparse
import array
import difflib
import hashlib
import json
import math
import os
import re
import subprocess
import tempfile
import wave
from datetime import datetime, timezone
from pathlib import Path

from align_audio import (
    DROP_CHARS,
    GROQ_MODEL,
    canon,
    explode,
    load_env,
    resolve_recognizer,
    to_pcm16k,
)
from apply_voice_plan import chapter_pauses
from derive_script_artifacts import narration_line_error


BREAK_CHARS = set("，、；：。！？!?;:")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def plan_digest(plan: dict) -> str:
    stable = {key: value for key, value in plan.items() if key != "generated_at"}
    return text_sha256(json.dumps(stable, ensure_ascii=False, sort_keys=True))


def pronunciation_rules(project: Path) -> list[tuple[str, str]]:
    """Display-to-spoken substitutions, longest display first.

    Sorting by length keeps a short entry from eating part of a longer one:
    with both `Skill` and `Skill.md` declared, an unsorted pass would rewrite
    the `Skill` inside `Skill.md` and leave a dangling `.md`.
    """
    path = project / "script/pronunciation.json"
    if not path.exists():
        return []
    entries = load_json(path).get("entries", [])
    rules = [
        (str(item["display"]), str(item["spoken"]))
        for item in entries
        if item.get("display") and item.get("spoken") is not None
    ]
    return sorted(rules, key=lambda pair: len(pair[0]), reverse=True)


def apply_pronunciation(text: str, rules: list[tuple[str, str]]) -> str:
    for display, spoken in rules:
        text = text.replace(display, spoken)
    return text


def request_text(chunk: dict) -> str:
    """What the provider is asked to say.

    Only the request differs; `text` stays the authoritative narration so
    alignment, captions, and beats never move because of a pronunciation fix.
    """
    return chunk.get("tts_text") or chunk["text"]


def spoken_text(text: str) -> str:
    return "".join(c for c in canon(text) if c not in DROP_CHARS)


def spoken_count(text: str) -> int:
    return len(spoken_text(text))


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def split_oversized(text: str, max_chars: int) -> list[str]:
    remaining = text.strip()
    out: list[str] = []
    while spoken_count(remaining) > max_chars:
        count = 0
        last_break = -1
        cut = -1
        for index, char in enumerate(remaining):
            if char not in DROP_CHARS:
                count += 1
            if char in BREAK_CHARS and count >= max_chars * 0.55:
                last_break = index + 1
            if count >= max_chars:
                cut = last_break if last_break > 0 else index + 1
                break
        if cut <= 0:
            raise ValueError(f"cannot split TTS text within {max_chars} spoken characters")
        out.append(remaining[:cut].strip())
        remaining = remaining[cut:].strip()
    if remaining:
        out.append(remaining)
    return out


def bounded_chunks(text: str, max_chars: int) -> list[str]:
    pieces: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        # Last gate before the provider. Everything here is billed and spoken
        # aloud, so a chapter heading or list marker that survived derivation
        # must stop the run instead of being read out.
        problem = narration_line_error(line)
        if problem:
            raise ValueError(f"{problem}\n    {line}")
        sentences = [
            item.strip()
            for item in re.split(r"(?<=[。！？!?；;])", line)
            if item.strip()
        ]
        for sentence in sentences or [line]:
            pieces.extend(split_oversized(sentence, max_chars))

    chunks: list[str] = []
    current: list[str] = []
    current_chars = 0
    for piece in pieces:
        size = spoken_count(piece)
        if current and current_chars + size > max_chars:
            chunks.append("\n".join(current))
            current, current_chars = [], 0
        current.append(piece)
        current_chars += size
    if current:
        chunks.append("\n".join(current))
    # Greedy packing can leave a tiny tail, which is exactly where an
    # independent TTS request becomes unstable. Move complete sentences from
    # the preceding chunk until the tail is reasonably sized, without crossing
    # the request budget.
    minimum_tail = max(12, round(max_chars * 0.4))
    if len(chunks) > 1 and spoken_count(chunks[-1]) < minimum_tail:
        previous = chunks[-2].splitlines()
        tail = chunks[-1].splitlines()
        while len(previous) > 1 and spoken_count("\n".join(tail)) < minimum_tail:
            candidate = previous[-1]
            if spoken_count("\n".join(previous[:-1])) < minimum_tail:
                break
            if spoken_count(candidate + "\n" + "\n".join(tail)) > max_chars:
                break
            previous.pop()
            tail.insert(0, candidate)
        chunks[-2] = "\n".join(previous)
        chunks[-1] = "\n".join(tail)
    if compact("".join(chunks)) != compact(text):
        raise ValueError("TTS chunking changed narration text")
    return chunks


def settings(project: Path) -> dict:
    config = load_json(project / "project-config.json")
    audio = config.setdefault("audio", {})
    voice = config.setdefault("voice", {})
    consistency = voice.setdefault("consistency", {})
    return {
        "max_seconds": float(audio.get("tts_request_max_seconds", 30)),
        "target_seconds": float(audio.get("tts_request_target_seconds", 25)),
        "planning_chars_per_second": float(
            audio.get("tts_planning_min_chars_per_second", 3.2)
        ),
        "segment_gap": float(audio.get("segment_pause_seconds", 0.8)),
        "scene_gap": float(audio.get("scene_gap_seconds", 0.8)),
        "chunk_gap": float(audio.get("tts_chunk_pause_seconds", 0.12)),
        "candidate_count": int(consistency.get("candidate_count", 2)),
        "max_attempts": int(consistency.get("max_attempts_per_chunk", 4)),
        "target_rate": float(consistency.get("target_chars_per_second", 4.6)),
        "rate_tolerance": float(consistency.get("pace_tolerance_ratio", 0.18)),
        "adjacent_tolerance": float(
            consistency.get("max_adjacent_pace_ratio", 0.15)
        ),
        "min_coverage": float(consistency.get("min_asr_coverage", 0.90)),
        "min_tail_coverage": float(consistency.get("min_tail_coverage", 0.5)),
        "tail_characters": int(consistency.get("tail_characters", 6)),
        "edge_threshold_db": float(
            consistency.get("speech_edge_threshold_db", -50.0)
        ),
        "edge_lead": float(consistency.get("speech_lead_seconds", 0.06)),
        "edge_release": float(consistency.get("speech_release_seconds", 0.08)),
        "edge_gap": float(consistency.get("speech_gap_seconds", 0.18)),
        "max_tail_extra": int(consistency.get("max_tail_extra_characters", 1)),
        "tail_trim_coverage": float(consistency.get("tail_trim_min_coverage", 0.8)),
        "max_tail_trim": float(consistency.get("max_tail_trim_seconds", 1.2)),
        "target_lufs": float(consistency.get("target_lufs", -16)),
        "lufs_tolerance": float(consistency.get("lufs_tolerance", 0.6)),
        "true_peak": float(consistency.get("true_peak_db", -1.5)),
        "target_lra": float(consistency.get("target_lra", 7)),
        "sample_rate": int(voice.get("sample_rate", 48000)),
        "channels": int(voice.get("channels", 1)),
        "instruction": voice.get(
            "instruction",
            "中文知识分享口播，声音自然、清晰，语速稍快、节奏紧凑，"
            "重点处有轻微强调，不夸张",
        ),
    }


def build_plan(project: Path, chapters: list[str], cfg: dict) -> dict:
    timing = load_json(project / "timing/chapters.json")["chapters"]
    rules = pronunciation_rules(project)
    max_chars = max(
        20,
        math.floor(cfg["target_seconds"] * cfg["planning_chars_per_second"]),
    )
    plan = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "request_limit_seconds": cfg["max_seconds"],
        "request_target_seconds": cfg["target_seconds"],
        "planning_max_spoken_characters": max_chars,
        "chapters": {},
    }
    for chapter in chapters:
        if chapter not in timing:
            raise ValueError(f"unknown chapter {chapter}")
        chunk_items = []
        order = 0
        for segment in timing[chapter]["segments"]:
            parts = bounded_chunks(segment["text"], max_chars)
            for index, text in enumerate(parts, 1):
                order += 1
                spoken = apply_pronunciation(text, rules)
                count = spoken_count(spoken)
                item = {
                    "id": f"{segment['id']}-C{index:02d}",
                    "chapter": chapter,
                    "segment": segment["id"],
                    "order": order,
                    "text": text,
                    # The hash covers what will actually be spoken, so editing
                    # pronunciation.json invalidates the cached take.
                    "text_sha256": text_sha256(spoken),
                    "spoken_characters": count,
                    "planning_seconds": round(
                        count / cfg["planning_chars_per_second"], 2
                    ),
                }
                if spoken != text:
                    item["tts_text"] = spoken
                chunk_items.append(item)
        plan["chapters"][chapter] = {"chunks": chunk_items}
    return plan


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as wav:
        return wav.getnframes() / wav.getframerate()


def loudness(path: Path, start: float = 0, end: float | None = None) -> dict:
    cmd = ["ffmpeg", "-hide_banner", "-nostats"]
    if start > 0:
        cmd += ["-ss", f"{start:.6f}"]
    if end is not None:
        cmd += ["-t", f"{max(end - start, 0.01):.6f}"]
    cmd += [
        "-i", str(path),
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=7:print_format=json",
        "-f", "null", "-",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    match = re.search(r'\{\s*"input_i".*?\}', result.stderr, re.DOTALL)
    if not match:
        raise RuntimeError(f"ffmpeg did not report loudness for {path}")
    return json.loads(match.group(0))


def flat_factor(path: Path) -> float:
    result = subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
            "-af", "astats", "-f", "null", "-",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    values = [
        float(value)
        for value in re.findall(r"Flat factor:\s*([-0-9.]+)", result.stderr)
    ]
    return max(values, default=0.0)


def scored_text(text: str) -> str:
    """Spoken text minus Latin runs, which a Chinese recogniser cannot score.

    Whisper renders `Markdown` as 麦克顿/麻烦/骂托 and `V1` as 为1/唯1 from one
    take to the next while the speech itself is correct, so counting those
    characters measures the recogniser, not the take. Pace still counts them —
    they take time to say.
    """
    return re.sub(r"[A-Za-z]+", "", spoken_text(text))


def coverage(script: str, heard: str) -> float:
    expected = scored_text(script)
    actual = scored_text(heard)
    matcher = difflib.SequenceMatcher(None, expected, actual, autojunk=False)
    matched = sum(block.size for block in matcher.get_matching_blocks())
    return matched / len(expected) if expected else 1.0


def tail_coverage(script: str, heard: str, characters: int) -> float:
    """How much of the final few script characters survived into the transcript."""
    expected = scored_text(script)
    actual = scored_text(heard)
    if not expected:
        return 1.0
    tail = expected[-characters:]
    window = actual[-(characters * 3):] or actual
    matcher = difflib.SequenceMatcher(None, tail, window, autojunk=False)
    matched = sum(block.size for block in matcher.get_matching_blocks())
    return min(matched / len(tail), 1.0)


def speech_clusters(
    pcm: Path,
    threshold_db: float,
    min_gap: float,
    frame_seconds: float = 0.01,
) -> list[tuple[float, float]]:
    """Audible stretches, split wherever silence runs longer than `min_gap`.

    A single first/last pair cannot tell a sentence apart from a sentence plus
    whatever the model exhaled after it; both end at the same audible frame.
    Clusters can, because the stray syllable arrives as its own island on the
    far side of a pause.

    Recogniser timestamps land on the last *token*, which is routinely earlier
    than the last audible sample, so they must never define a trim point on
    their own — they only pick which island to trim at.
    """
    with wave.open(str(pcm), "rb") as source:
        rate = source.getframerate()
        channels = source.getnchannels()
        samples = array.array("h")
        samples.frombytes(source.readframes(source.getnframes()))
    if channels > 1:
        samples = samples[::channels]
    step = max(1, int(frame_seconds * rate))
    threshold = 32768.0 * (10 ** (threshold_db / 20))
    gap_frames = max(1, round(min_gap / frame_seconds))
    clusters: list[list[float]] = []
    silent = gap_frames
    for index in range(0, len(samples) - step + 1, step):
        window = samples[index:index + step]
        energy = math.sqrt(sum(value * value for value in window) / len(window))
        if energy <= threshold:
            silent += 1
            continue
        if clusters and silent < gap_frames:
            clusters[-1][1] = (index + step) / rate
        else:
            clusters.append([index / rate, (index + step) / rate])
        silent = 0
    return [(start, end) for start, end in clusters]


def trailing_extra(script: str, heard: str, characters: int = 6) -> tuple[str, int]:
    """What the recogniser heard after the script ran out, and where it ended.

    `tail_coverage` asks whether the scripted ending survived into the take.
    This asks the opposite question — whether the take carried on once that
    ending was done. A model that voices a syllable past the final full stop
    passes the first test and fails this one.

    Returns the unscripted text and the `heard` index of the last scripted
    character, which is an index into the recogniser's spans as well.

    Latin endings are exempt: whisper renders `Skill` as 斯基尔, which at this
    level is indistinguishable from a syllable nobody asked for.
    """
    expected = spoken_text(script)
    actual = canon(heard)
    if not expected or not actual:
        return "", -1
    if re.search(r"[A-Za-z]", expected[-characters:]):
        return "", -1
    matcher = difflib.SequenceMatcher(None, expected, actual, autojunk=False)
    blocks = [block for block in matcher.get_matching_blocks() if block.size]
    if not blocks:
        return "", -1
    end = blocks[-1].b + blocks[-1].size
    return heard[end:], end - 1


def assess_candidate(
    path: Path,
    text: str,
    asr,
    cfg: dict,
) -> dict:
    duration = wav_duration(path)
    with tempfile.TemporaryDirectory() as tmp:
        pcm = to_pcm16k(path, Path(tmp) / "16k.wav")
        tokens = asr.transcribe(pcm, "zh")
        clusters = speech_clusters(
            pcm, cfg["edge_threshold_db"], cfg["edge_gap"]
        )
    heard, spans = explode(tokens)
    if not spans:
        return {
            "audio": str(path),
            "duration": round(duration, 3),
            "coverage": 0.0,
            "heard": "",
            "error": "recogniser found no speech",
        }
    if clusters:
        speech_start, speech_end = clusters[0][0], clusters[-1][1]
    else:
        speech_start, speech_end = spans[0][0], spans[-1][1]
    energy_end = clusters[-1][1] if clusters else None
    tail = tail_coverage(text, heard, cfg["tail_characters"])
    extra, last_scripted = trailing_extra(text, heard, cfg["tail_characters"])
    trimmed = 0.0
    if extra and clusters and tail >= cfg["tail_trim_coverage"]:
        kept = [
            item for item in clusters if item[0] <= spans[last_scripted][1]
        ]
        removed = speech_end - kept[-1][1] if kept else 0.0
        # Cut only across a pause the script had already finished before, and
        # only a short one: a stray breath is brief, so a long cut means the
        # recogniser lost the ending rather than the model adding to it.
        if kept and 0 < removed <= cfg["max_tail_trim"]:
            speech_end = kept[-1][1]
            trimmed = round(removed, 3)
    start = max(0.0, speech_start - cfg["edge_lead"])
    end = min(duration, speech_end + cfg["edge_release"])
    active = max(speech_end - speech_start, 0.001)
    stats = loudness(path, start, end)
    return {
        "audio": str(path),
        "duration": round(duration, 3),
        "coverage": round(coverage(text, heard), 4),
        "tail_coverage": round(tail, 4),
        "tail_extra": extra,
        "tail_trimmed": trimmed,
        "heard": heard,
        "speech_start": round(start, 3),
        "speech_end": round(end, 3),
        "asr_end": round(spans[-1][1], 3),
        "energy_end": round(energy_end, 3) if energy_end is not None else None,
        "active_duration": round(active, 3),
        "chars_per_second": round(spoken_count(text) / active, 3),
        "input_lufs": float(stats["input_i"]),
        "input_true_peak": float(stats["input_tp"]),
        "input_lra": float(stats["input_lra"]),
        "flat_factor": flat_factor(path),
    }


def basic_reasons(candidate: dict, cfg: dict) -> list[str]:
    reasons = []
    if candidate.get("error"):
        reasons.append(candidate["error"])
    if candidate["duration"] > cfg["max_seconds"] + 0.01:
        reasons.append(
            f"duration {candidate['duration']:.2f}s exceeds "
            f"{cfg['max_seconds']:.2f}s"
        )
    if candidate.get("coverage", 0) < cfg["min_coverage"]:
        reasons.append(
            f"ASR coverage {candidate.get('coverage', 0):.1%} below "
            f"{cfg['min_coverage']:.1%}"
        )
    tail = candidate.get("tail_coverage")
    if tail is not None and tail < cfg["min_tail_coverage"]:
        reasons.append(
            f"sentence tail only {tail:.0%} recognised, take is likely cut short"
        )
    extra = candidate.get("tail_extra") or ""
    if len(extra) > cfg["max_tail_extra"] and not candidate.get("tail_trimmed"):
        # Trimmed takes are already clean, so only the unfixable case is fatal:
        # the model ran on without leaving a pause to cut at.
        reasons.append(
            f"take says {extra} after the script ends, with no pause to trim at"
        )
    if candidate.get("flat_factor", 1) != 0:
        reasons.append(f"flat factor {candidate.get('flat_factor')} indicates clipping")
    rate = candidate.get("chars_per_second", 0)
    low = cfg["target_rate"] * (1 - cfg["rate_tolerance"])
    high = cfg["target_rate"] * (1 + cfg["rate_tolerance"])
    if not low <= rate <= high:
        reasons.append(f"pace {rate:.2f} chars/s outside {low:.2f}-{high:.2f}")
    return reasons


def adjacency_ok(candidate: dict, previous_rate: float | None, cfg: dict) -> bool:
    if previous_rate is None:
        return True
    rate = candidate["chars_per_second"]
    return abs(rate / previous_rate - 1) <= cfg["adjacent_tolerance"]


def candidate_score(candidate: dict, previous_rate: float | None, cfg: dict) -> float:
    rate = candidate["chars_per_second"]
    score = abs(math.log(rate / cfg["target_rate"]))
    if previous_rate is not None:
        score += 0.8 * abs(math.log(rate / previous_rate))
    score += max(0, cfg["min_coverage"] + 0.05 - candidate["coverage"])
    if candidate.get("tail_extra"):
        # Trimming removed the stray syllable, but a take that never produced
        # one needs no faith in the trim, so it is the better ship.
        score += 0.25
    return score


def reference_voice_sha256(engineering_root: Path) -> str:
    values = load_env(engineering_root / ".skill.env")
    value = values.get("MIMO_REFERENCE_VOICE", "")
    if not value:
        return ""
    path = Path(value)
    if not path.is_absolute():
        path = engineering_root / path
    if not path.exists():
        raise RuntimeError(f"configured reference voice does not exist: {path}")
    return sha256(path)


def synthesize(
    engineering_root: Path,
    project: Path,
    chunk: dict,
    attempt: int,
    instruction: str,
) -> Path:
    env_file = engineering_root / ".skill.env"
    values = load_env(env_file)
    proxy = values.get("SKILL_PROXY", "")
    if not proxy:
        raise RuntimeError(f"SKILL_PROXY is required in {env_file}")
    env = os.environ.copy()
    env.update({
        "SKILL_PROJECT_ROOT": str(engineering_root),
        "SKILL_PROXY_STRICT": "1",
        "HTTP_PROXY": proxy,
        "HTTPS_PROXY": proxy,
        "ALL_PROXY": proxy,
        "http_proxy": proxy,
        "https_proxy": proxy,
    })
    output_root = project / "audio/voice-candidates"
    command = [
        "python3",
        str(engineering_root / ".cursor/skills/mimo-tts/scripts/mimo_tts.py"),
        "--text", request_text(chunk),
        "--title", f"{chunk['id']}-take-{attempt}",
        "--instruction", instruction,
        "--pause", "0",
        "--env-file", str(env_file),
        "--output-root", str(output_root),
    ]
    result = subprocess.run(
        command,
        env=env,
        capture_output=True,
        text=True,
        timeout=240,
    )
    if result.returncode:
        detail = (result.stdout + result.stderr)[-1200:]
        raise RuntimeError(f"MiMo failed for {chunk['id']} take {attempt}:\n{detail}")
    paths = [
        Path(line.strip())
        for line in result.stdout.splitlines()
        if line.strip().endswith("narration.wav")
    ]
    if not paths or not paths[-1].exists():
        raise RuntimeError(f"MiMo returned no narration path for {chunk['id']}")
    return paths[-1]


def normalize_candidate(source: Path, output: Path, candidate: dict, cfg: dict) -> dict:
    first = loudness(source, candidate["speech_start"], candidate["speech_end"])
    # Aim quieter than the delivery true-peak so a final LUFS trim still has headroom.
    stage_peak = min(cfg["true_peak"] - 1.2, -2.5)
    filt = (
        f"loudnorm=I={cfg['target_lufs']}:TP={stage_peak}:"
        f"LRA={cfg['target_lra']}:"
        f"measured_I={first['input_i']}:measured_LRA={first['input_lra']}:"
        f"measured_TP={first['input_tp']}:measured_thresh={first['input_thresh']}:"
        f"offset={first['target_offset']}:linear=true:print_format=summary"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ffmpeg", "-v", "error", "-y",
            "-ss", f"{candidate['speech_start']:.6f}",
            "-t", f"{candidate['speech_end'] - candidate['speech_start']:.6f}",
            "-i", str(source),
            "-af", filt,
            "-ar", str(cfg["sample_rate"]),
            "-ac", str(cfg["channels"]),
            "-c:a", "pcm_s16le",
            str(output),
        ],
        check=True,
    )
    after = loudness(output)
    measured = float(after["input_i"])
    delta = cfg["target_lufs"] - measured
    if abs(delta) > 0.15:
        trimmed = output.with_suffix(".gain.wav")
        peak_room = cfg["true_peak"] - float(after["input_tp"]) - 0.05
        gain = min(delta, max(peak_room, 0.0)) if delta > 0 else delta
        chain = None
        if measured + gain < cfg["target_lufs"] - cfg["lufs_tolerance"] + 0.2:
            # Plain gain cannot lift this take into tolerance because a single
            # transient owns the headroom. Limiting that peak is correct;
            # shipping the whole chunk under-level is not. Keep this a last
            # resort — limiting material that would have passed on gain alone
            # risks flat-topping sustained speech.
            # alimiter caps sample peaks while inter-sample peaks land higher,
            # so sit well below the true-peak ceiling.
            ceiling = 10 ** ((cfg["true_peak"] - 1.0) / 20)
            chain = (
                f"volume={delta:.4f}dB,"
                f"alimiter=limit={ceiling:.6f}:attack=5:release=50:level=disabled"
            )
        elif abs(gain) > 0.01:
            chain = f"volume={gain:.4f}dB"
        if chain:
            subprocess.run(
                [
                    "ffmpeg", "-v", "error", "-y",
                    "-i", str(output),
                    "-af", chain,
                    "-ar", str(cfg["sample_rate"]),
                    "-ac", str(cfg["channels"]),
                    "-c:a", "pcm_s16le",
                    str(trimmed),
                ],
                check=True,
            )
            trimmed.replace(output)
            after = loudness(output)
    result = {
        "audio": str(output),
        "duration": round(wav_duration(output), 3),
        "lufs": float(after["input_i"]),
        "true_peak": float(after["input_tp"]),
        "flat_factor": flat_factor(output),
    }
    if abs(result["lufs"] - cfg["target_lufs"]) > cfg["lufs_tolerance"]:
        raise RuntimeError(
            f"{output.name}: normalized loudness {result['lufs']:.2f} LUFS "
            f"misses target {cfg['target_lufs']:.2f}"
        )
    if result["true_peak"] > cfg["true_peak"] + 0.1:
        raise RuntimeError(f"{output.name}: true peak exceeds target")
    if result["flat_factor"] != 0:
        raise RuntimeError(f"{output.name}: normalization produced clipping")
    return result


def merge_wavs(paths: list[Path], output: Path, gap_seconds: float) -> float:
    if not paths:
        raise ValueError("cannot merge an empty WAV list")
    output.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(paths[0]), "rb") as first:
        params = first.getparams()
    with wave.open(str(output), "wb") as target:
        target.setparams(params)
        for index, path in enumerate(paths):
            with wave.open(str(path), "rb") as source:
                current = source.getparams()
                if (
                    current.nchannels != params.nchannels
                    or current.sampwidth != params.sampwidth
                    or current.framerate != params.framerate
                    or current.comptype != params.comptype
                ):
                    raise RuntimeError(f"incompatible WAV format: {path}")
                target.writeframes(source.readframes(source.getnframes()))
            if index < len(paths) - 1 and gap_seconds > 0:
                frames = round(gap_seconds * params.framerate)
                target.writeframes(
                    b"\x00" * frames * params.nchannels * params.sampwidth
                )
    return round(wav_duration(output), 3)


def update_chapter_timing(project: Path, chapter: str, durations: dict[str, float]) -> None:
    path = project / "timing/chapters.json"
    data = load_json(path)
    item = data["chapters"][chapter]
    cursor = 0.0
    gap = float(item.get("pause", 0))
    for segment in item["segments"]:
        duration = durations[segment["id"]]
        segment["duration"] = duration
        segment["start"] = round(cursor, 3)
        segment["end"] = round(cursor + duration, 3)
        cursor = segment["end"] + gap
    item["duration"] = item["segments"][-1]["end"]
    write_json(path, data)


def run_checked(command: list[str], cwd: Path) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def only_adjacency_failures(candidates: list[dict], previous_rate: float | None, cfg: dict) -> bool:
    if previous_rate is None or not candidates:
        return False
    basic_ok = [item for item in candidates if not item["rejection_reasons"]]
    if not basic_ok:
        return False
    return all(not adjacency_ok(item, previous_rate, cfg) for item in basic_ok)


def rank_valid(candidates: list[dict], previous_rate: float | None, cfg: dict) -> list[dict]:
    valid = [
        item for item in candidates
        if not item["rejection_reasons"] and adjacency_ok(item, previous_rate, cfg)
    ]
    return sorted(valid, key=lambda item: candidate_score(item, previous_rate, cfg))


def commit_selection(
    chapter: str,
    chunk: dict,
    selected: dict,
    candidates: list[dict],
    alternatives: list[dict],
    work: Path,
    cfg: dict,
) -> dict:
    for item in candidates:
        item.pop("selected", None)
        item.pop("normalized", None)
    normalized_path = work / chapter / "chunks" / f"{chunk['id']}.wav"
    try:
        normalized = normalize_candidate(
            Path(selected["audio"]), normalized_path, selected, cfg
        )
    except RuntimeError as exc:
        selected.setdefault("rejection_reasons", []).append(str(exc))
        raise
    selected["selected"] = True
    selected["normalized"] = normalized
    return {
        **chunk,
        "candidates": candidates,
        "selected_attempt": selected["attempt"],
        "selected_metrics": {
            "coverage": selected["coverage"],
            "chars_per_second": selected["chars_per_second"],
            "normalized_lufs": normalized["lufs"],
            "normalized_true_peak": normalized["true_peak"],
            "normalized_audio": str(normalized_path),
        },
        "_selected": selected,
        "_alternatives": alternatives,
        "_normalized_path": normalized_path,
    }


def deepen_candidates(
    engineering_root: Path,
    project: Path,
    chunk: dict,
    cfg: dict,
    asr,
    candidates: list[dict],
    extra: int,
) -> list[dict]:
    """Add takes to an already-settled chunk so backtracking has somewhere to go."""
    attempt = max((item.get("attempt", 0) for item in candidates), default=0)
    limit = min(cfg["max_attempts"], attempt + extra)
    while attempt < limit:
        attempt += 1
        try:
            audio = synthesize(
                engineering_root, project, chunk, attempt, cfg["instruction"]
            )
            assessed = assess_candidate(audio, request_text(chunk), asr, cfg)
        except (RuntimeError, subprocess.SubprocessError) as exc:
            assessed = {
                "audio": "",
                "duration": 0.0,
                "coverage": 0.0,
                "heard": "",
                "chars_per_second": 0.0,
                "flat_factor": 1.0,
                "error": str(exc),
            }
        assessed["attempt"] = attempt
        assessed["rejection_reasons"] = basic_reasons(assessed, cfg)
        candidates.append(assessed)
    return candidates


def reachable_rate(candidates: list[dict], cfg: dict) -> float | None:
    """Median pace the stranded chunk can actually hit, ignoring adjacency."""
    rates = sorted(
        item["chars_per_second"]
        for item in candidates
        if not item.get("rejection_reasons") and item.get("chars_per_second")
    )
    if not rates:
        return None
    return rates[len(rates) // 2]


def synthesize_until_choice(
    engineering_root: Path,
    project: Path,
    chunk: dict,
    previous_rate: float | None,
    cfg: dict,
    asr,
    seed_candidates: list[dict] | None = None,
) -> tuple[dict | None, list[dict], list[dict]]:
    candidates = list(seed_candidates or [])
    attempt = max((item.get("attempt", 0) for item in candidates), default=0)
    while True:
        ranked = rank_valid(candidates, previous_rate, cfg)
        if ranked and attempt >= cfg["candidate_count"]:
            selected = ranked[0]
            return selected, ranked[1:], candidates
        if attempt >= cfg["max_attempts"]:
            if ranked:
                selected = ranked[0]
                return selected, ranked[1:], candidates
            return None, [], candidates
        attempt += 1
        try:
            audio = synthesize(
                engineering_root,
                project,
                chunk,
                attempt,
                cfg["instruction"],
            )
            assessed = assess_candidate(audio, request_text(chunk), asr, cfg)
        except (RuntimeError, subprocess.SubprocessError) as exc:
            assessed = {
                "audio": "",
                "duration": 0.0,
                "coverage": 0.0,
                "heard": "",
                "chars_per_second": 0.0,
                "flat_factor": 1.0,
                "error": str(exc),
            }
        assessed["attempt"] = attempt
        assessed["rejection_reasons"] = basic_reasons(assessed, cfg)
        candidates.append(assessed)


def load_resumable_production(
    project: Path,
    plan: dict,
    cfg: dict,
    engineering_root: Path,
) -> dict | None:
    path = project / "audio/voice-production.json"
    if not path.exists():
        return None
    existing = load_json(path)
    if existing.get("plan_sha256") != plan_digest(plan):
        return None
    if existing.get("settings_sha256") != text_sha256(
        json.dumps(cfg, ensure_ascii=False, sort_keys=True)
    ):
        return None
    if existing.get("reference_voice_sha256") != reference_voice_sha256(engineering_root):
        return None
    return existing


def generate(
    project: Path,
    plan: dict,
    cfg: dict,
    chapters: list[str],
    model: str,
) -> dict:
    engineering_root = Path(__file__).resolve().parents[4]
    asr = resolve_recognizer(model)
    print(f"recogniser: groq ({asr.model})", flush=True)

    existing = load_resumable_production(project, plan, cfg, engineering_root)
    production = existing or {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "plan_sha256": plan_digest(plan),
        "settings_sha256": text_sha256(
            json.dumps(cfg, ensure_ascii=False, sort_keys=True)
        ),
        "reference_voice_sha256": reference_voice_sha256(engineering_root),
        "settings": cfg,
        "chapters": {},
    }
    production["resumed_at"] = datetime.now(timezone.utc).isoformat()
    work = project / "audio/voice-work"

    for chapter in chapters:
        prior = production.get("chapters", {}).get(chapter) or {}
        if prior.get("status") == "selected" and prior.get("audio"):
            print(f"{chapter}: resume skip (already selected)")
            continue

        production["chapters"][chapter] = {
            "status": "in_progress",
            "chunks": [],
        }
        selected_stack: list[dict] = []
        selected_paths: dict[str, list[Path]] = {}
        segment_order: list[str] = []
        plan_chunks = plan["chapters"][chapter]["chunks"]
        prior_by_id = {
            item["id"]: item
            for item in prior.get("chunks", [])
            if item.get("selected_attempt") is not None
        }

        # Restore completed prefix so a blocked chapter can continue.
        for chunk in plan_chunks:
            prior_chunk = prior_by_id.get(chunk["id"])
            if not prior_chunk:
                break
            selected = next(
                (
                    item for item in prior_chunk.get("candidates", [])
                    if item.get("attempt") == prior_chunk.get("selected_attempt")
                ),
                None,
            )
            if not selected or not selected.get("audio"):
                break
            alternatives = [
                item for item in prior_chunk.get("candidates", [])
                if not item.get("rejection_reasons")
                and item.get("attempt") != selected.get("attempt")
                and Path(item.get("audio", "")).exists()
            ]
            alternatives = sorted(
                alternatives,
                key=lambda item: candidate_score(
                    item,
                    selected_stack[-1]["_selected"]["chars_per_second"]
                    if selected_stack else None,
                    cfg,
                ),
            )
            try:
                record = commit_selection(
                    chapter, chunk, selected, prior_chunk["candidates"], alternatives, work, cfg
                )
            except RuntimeError as exc:
                # Normalization rules may have changed since the take was
                # chosen. Hand the chunk back to the generation loop, which
                # knows how to reject it and look for another take.
                print(f"{chapter}: resume re-normalize failed for {chunk['id']}: {exc}")
                selected.setdefault("rejection_reasons", []).append(str(exc))
                prior_chunk["selected_attempt"] = None
                break
            selected_stack.append(record)
            if chunk["segment"] not in selected_paths:
                selected_paths[chunk["segment"]] = []
                segment_order.append(chunk["segment"])
            selected_paths[chunk["segment"]].append(record["_normalized_path"])
            production["chapters"][chapter]["chunks"] = [
                {k: v for k, v in item.items() if not k.startswith("_")}
                for item in selected_stack
            ]
            write_json(project / "audio/voice-production.json", production)
            print(
                f"{chapter}: resume keep {chunk['id']} "
                f"(take {selected['attempt']}, {selected['chars_per_second']:.2f} chars/s)"
            )

        index = len(selected_stack)
        while index < len(plan_chunks):
            chunk = plan_chunks[index]
            if chunk["segment"] not in selected_paths:
                selected_paths[chunk["segment"]] = []
                segment_order.append(chunk["segment"])
            previous_rate = (
                selected_stack[-1]["_selected"]["chars_per_second"]
                if selected_stack else None
            )
            seed = None
            prior_chunk = next(
                (
                    item for item in prior.get("chunks", [])
                    if item.get("id") == chunk["id"]
                ),
                None,
            )
            if prior_chunk and prior_chunk.get("candidates"):
                seed = [
                    item for item in prior_chunk["candidates"]
                    if item.get("audio") and Path(item["audio"]).exists()
                ]
                for item in seed:
                    # Scoring rules may have changed since the take was stored;
                    # re-score from the transcript before judging it again.
                    if item.get("heard"):
                        item["coverage"] = round(
                            coverage(request_text(chunk), item["heard"]), 4
                        )
                        item["tail_coverage"] = round(
                            tail_coverage(
                                request_text(chunk), item["heard"],
                                cfg["tail_characters"],
                            ), 4
                        )
                        item["tail_extra"] = trailing_extra(
                            request_text(chunk), item["heard"],
                            cfg["tail_characters"],
                        )[0]
                    item["rejection_reasons"] = basic_reasons(item, cfg)
            selected, alternatives, candidates = synthesize_until_choice(
                engineering_root,
                project,
                chunk,
                previous_rate,
                cfg,
                asr,
                seed_candidates=seed,
            )
            if selected is None and only_adjacency_failures(candidates, previous_rate, cfg):
                # Greedy earlier choice can strand later chunks. Prefer an
                # alternate previous take before spending more provider calls.
                target = reachable_rate(candidates, cfg)
                while selected_stack:
                    previous = selected_stack.pop()
                    prior_rate = (
                        selected_stack[-1]["_selected"]["chars_per_second"]
                        if selected_stack else None
                    )
                    alt = previous.get("_alternatives") or []
                    if not alt:
                        # No stored alternative means the earlier chunk settled
                        # on its only viable take. Buy more takes for it rather
                        # than declaring the run blocked.
                        pool = deepen_candidates(
                            engineering_root,
                            project,
                            previous,
                            cfg,
                            asr,
                            previous["candidates"],
                            2,
                        )
                        previous["candidates"] = pool
                        alt = [
                            item for item in pool
                            if not item.get("rejection_reasons")
                            and adjacency_ok(item, prior_rate, cfg)
                            and item.get("attempt") != previous["selected_attempt"]
                        ]
                        if alt:
                            print(
                                f"{chapter}: deepened {previous['id']} pool to "
                                f"{len(pool)} takes to unblock {chunk['id']}"
                            )
                    if not alt:
                        selected_stack.append(previous)
                        break
                    if target is not None:
                        # Prefer the earlier take whose pace the stranded chunk
                        # can actually match, not merely the next best one.
                        alt.sort(key=lambda item: abs(
                            math.log(item["chars_per_second"] / target)
                        ))
                    replacement = alt.pop(0)
                    print(
                        f"{chapter}: backtrack {previous['id']} "
                        f"take {previous['selected_attempt']} -> {replacement['attempt']}"
                    )
                    try:
                        rebuilt = commit_selection(
                            chapter,
                            {k: previous[k] for k in (
                                "id", "chapter", "segment", "order", "text",
                                "tts_text", "text_sha256", "spoken_characters",
                                "planning_seconds",
                            ) if k in previous},
                            replacement,
                            previous["candidates"],
                            alt,
                            work,
                            cfg,
                        )
                    except RuntimeError as exc:
                        print(f"{chapter}: backtrack normalize failed: {exc}")
                        previous["_alternatives"] = alt
                        selected_stack.append(previous)
                        continue
                    selected_stack.append(rebuilt)
                    # Rebuild path lists from the stack.
                    selected_paths = {}
                    segment_order = []
                    for item in selected_stack:
                        segment = item["segment"]
                        if segment not in selected_paths:
                            selected_paths[segment] = []
                            segment_order.append(segment)
                        selected_paths[segment].append(item["_normalized_path"])
                    # The stack holds committed chunks only; keep the bucket the
                    # chunk being placed will write into.
                    if chunk["segment"] not in selected_paths:
                        selected_paths[chunk["segment"]] = []
                        segment_order.append(chunk["segment"])
                    previous_rate = rebuilt["_selected"]["chars_per_second"]
                    selected, alternatives, candidates = synthesize_until_choice(
                        engineering_root,
                        project,
                        chunk,
                        previous_rate,
                        cfg,
                        asr,
                        seed_candidates=candidates,
                    )
                    if selected is not None:
                        break
                    if not only_adjacency_failures(candidates, previous_rate, cfg):
                        break

            if selected is None:
                summary = "; ".join(
                    f"take {item['attempt']}: "
                    f"{', '.join(item['rejection_reasons']) or 'adjacent pace mismatch'}"
                    for item in candidates
                )
                blocked = {
                    **chunk,
                    "candidates": candidates,
                    "selected_attempt": None,
                    "status": "blocked",
                }
                production["chapters"][chapter]["chunks"] = [
                    {k: v for k, v in item.items() if not k.startswith("_")}
                    for item in selected_stack
                ] + [blocked]
                production["chapters"][chapter]["status"] = "blocked"
                write_json(project / "audio/voice-production.json", production)
                raise RuntimeError(
                    f"{chunk['id']}: no acceptable take after "
                    f"{max((c.get('attempt', 0) for c in candidates), default=0)}: {summary}"
                )

            record = None
            while record is None:
                choice = selected
                remaining = list(alternatives)
                while choice is not None:
                    try:
                        record = commit_selection(
                            chapter, chunk, choice, candidates, remaining, work, cfg
                        )
                        selected = choice
                        alternatives = remaining
                        break
                    except RuntimeError as exc:
                        print(
                            f"{chapter}: normalize failed for {chunk['id']} "
                            f"take {choice['attempt']}: {exc}"
                        )
                        # A take that will not normalize is not a usable take.
                        # Record why so the generator looks for a different one
                        # instead of aborting the whole run.
                        choice.setdefault("rejection_reasons", []).append(str(exc))
                        choice = remaining.pop(0) if remaining else None
                if record is not None:
                    break
                spent = max((c.get("attempt", 0) for c in candidates), default=0)
                if spent >= cfg["max_attempts"]:
                    break
                selected, alternatives, candidates = synthesize_until_choice(
                    engineering_root,
                    project,
                    chunk,
                    previous_rate,
                    cfg,
                    asr,
                    seed_candidates=candidates,
                )
                if selected is None:
                    break
            if record is None:
                blocked = {
                    **chunk,
                    "candidates": candidates,
                    "selected_attempt": None,
                    "status": "blocked",
                }
                production["chapters"][chapter]["chunks"] = [
                    {k: v for k, v in item.items() if not k.startswith("_")}
                    for item in selected_stack
                ] + [blocked]
                production["chapters"][chapter]["status"] = "blocked"
                write_json(project / "audio/voice-production.json", production)
                raise RuntimeError(f"{chunk['id']}: all acceptable takes failed normalization")

            selected_stack.append(record)
            selected_paths[chunk["segment"]].append(record["_normalized_path"])
            production["chapters"][chapter]["chunks"] = [
                {k: v for k, v in item.items() if not k.startswith("_")}
                for item in selected_stack
            ]
            write_json(project / "audio/voice-production.json", production)
            print(
                f"{chapter}: selected {chunk['id']} "
                f"take {selected['attempt']} ({selected['chars_per_second']:.2f} chars/s)"
            )
            index += 1

        segment_paths = []
        segment_durations = {}
        for segment in segment_order:
            output = work / chapter / "segments" / f"{segment}.wav"
            duration = merge_wavs(
                selected_paths[segment], output, cfg["chunk_gap"]
            )
            segment_paths.append(output)
            segment_durations[segment] = duration

        chapter_output = project / f"audio/segments/{chapter}.wav"
        chapter_duration = merge_wavs(
            segment_paths, chapter_output, cfg["segment_gap"]
        )
        update_chapter_timing(project, chapter, segment_durations)
        production["chapters"][chapter] = {
            "status": "selected",
            "chunks": [
                {k: v for k, v in item.items() if not k.startswith("_")}
                for item in selected_stack
            ],
            "segments": [
                {
                    "id": segment,
                    "audio": str(path),
                    "duration": segment_durations[segment],
                }
                for segment, path in zip(segment_order, segment_paths)
            ],
            "audio": str(chapter_output),
            "audio_sha256": sha256(chapter_output),
            "duration": chapter_duration,
        }
        write_json(project / "audio/voice-production.json", production)

    scripts = engineering_root / ".cursor/skills/knowledge-video-builder/scripts"
    align = scripts / "align_audio.py"
    align_command = [
        "python3", str(align), "--project", str(project),
        "--chapters", *chapters,
        "--model", asr.model,
    ]
    run_checked(align_command, engineering_root)

    voice_plan_path = project / "script/voice-plan.json"
    voice_plan = load_json(voice_plan_path) if voice_plan_path.exists() else {"pauses": []}
    for chapter in chapters:
        if chapter_pauses(voice_plan, chapter):
            run_checked(
                [
                    "python3", str(scripts / "apply_voice_plan.py"),
                    "--project", str(project),
                    "--chapter", chapter,
                ],
                engineering_root,
            )

    run_checked(align_command, engineering_root)
    for chapter in chapters:
        output = project / f"audio/segments/{chapter}.wav"
        production["chapters"][chapter]["status"] = "aligned"
        production["chapters"][chapter]["final_audio_sha256"] = sha256(output)
        production["chapters"][chapter]["final_duration"] = round(
            wav_duration(output), 3
        )
    all_chapters = sorted(
        load_json(project / "timing/chapters.json")["chapters"]
    )
    chapter_paths = [
        project / f"audio/segments/{chapter}.wav" for chapter in all_chapters
    ]
    if all(path.exists() for path in chapter_paths):
        master = project / "audio/narration.wav"
        production["master_duration"] = merge_wavs(
            chapter_paths, master, cfg["scene_gap"]
        )
        production["master_audio"] = str(master)
        production["master_audio_sha256"] = sha256(master)
    write_json(project / "audio/voice-production.json", production)

    run_checked(
        ["python3", str(scripts / "build_timing.py"), "--project", str(project)],
        engineering_root,
    )
    run_checked(
        ["python3", str(scripts / "apply_timing.py"), "--project", str(project)],
        engineering_root,
    )
    run_checked(
        ["python3", str(scripts / "check_sync.py"), "--project", str(project)],
        engineering_root,
    )

    production["completed_at"] = datetime.now(timezone.utc).isoformat()
    write_json(project / "audio/voice-production.json", production)
    write_json(
        project / "audio/tts-manifest.json",
        {
            "schema_version": "1.0",
            "provider": "mimo-tts",
            "status": "generated_and_validated",
            "tts_plan": "audio/tts-plan.json",
            "voice_production": "audio/voice-production.json",
            "format": {
                "codec": "pcm_s16le",
                "sample_rate": cfg["sample_rate"],
                "channels": cfg["channels"],
            },
            "instruction": cfg["instruction"],
            "request_limit_seconds": cfg["max_seconds"],
            "chapters": [
                {
                    "id": chapter,
                    "audio": production["chapters"][chapter]["audio"],
                    "duration": production["chapters"][chapter]["final_duration"],
                    "sha256": production["chapters"][chapter]["final_audio_sha256"],
                }
                for chapter in chapters
            ],
            "master_audio": production.get("master_audio"),
            "master_duration": production.get("master_duration"),
            "created_at": production["completed_at"],
        },
    )
    return production


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", required=True, type=Path)
    ap.add_argument("--chapters", nargs="*")
    ap.add_argument("--generate", action="store_true")
    ap.add_argument("--model", default=GROQ_MODEL,
                    help="groq speech-to-text model used to score takes")
    args = ap.parse_args()

    project = args.project.resolve()
    timing = load_json(project / "timing/chapters.json")["chapters"]
    chapters = args.chapters or sorted(timing)
    cfg = settings(project)
    plan = build_plan(project, chapters, cfg)
    plan_path = project / "audio/tts-plan.json"
    write_json(plan_path, plan)
    chunks = sum(len(item["chunks"]) for item in plan["chapters"].values())
    print(
        f"TTS plan: {len(chapters)} chapter(s), {chunks} bounded chunk(s), "
        f"target {cfg['target_seconds']:.0f}s, hard limit {cfg['max_seconds']:.0f}s"
    )
    print(plan_path)
    if args.generate:
        generate(project, plan, cfg, chapters, args.model)


if __name__ == "__main__":
    main()
