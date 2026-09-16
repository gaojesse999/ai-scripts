# Voice Pipeline

## MiMo-first workflow

The default TTS provider is the local `mimo-tts` Skill. `knowledge-video-builder` uses a fixed `ENGINEERING_ROOT`: the directory containing `$SKILLS_ROOT/knowledge-video-builder` and the engineering-root `.skill.env`. Do not derive this path from the current video artifact directory.

Run the bundled script with the fixed Skill path and explicit environment file:

```bash
# SKILL_PROXY_STRICT=1 only when .skill.env defines a non-empty SKILL_PROXY.
SKILL_PROJECT_ROOT="$ENGINEERING_ROOT" \
SKILL_PROXY_STRICT="${SKILL_PROXY:+1}" \
HTTP_PROXY="$SKILL_PROXY" HTTPS_PROXY="$SKILL_PROXY" ALL_PROXY="$SKILL_PROXY" \
"$PYTHON_EXE" "$ENGINEERING_ROOT/$SKILLS_ROOT/mimo-tts/scripts/mimo_tts.py" \
  --env-file "$ENGINEERING_ROOT/.skill.env" \
  --input <scene-or-segment-text-file> \
  --output-root "$VIDEO_PROJECT_ROOT/audio/mimo-outputs"
```

When `SKILL_PROXY` is set it is mandatory, and a proxy failure is reported rather than retried directly. When it is empty, the run connects directly.

Only consider another TTS provider when `mimo-tts` is unavailable because its Skill, script, Python runtime, credentials, or API/network path cannot be used. Record the fallback reason in `audio/tts-manifest.json` and `qa/report.md`; do not silently switch providers.

`audio/tts-manifest.json` should contain:

```json
{
  "provider": "mimo-tts",
  "model": "auto",
  "voice": "auto",
  "language": "zh-CN",
    "env_file": "<engineering-root>/.skill.env",
  "format": {"codec": "pcm_s16le", "sample_rate": 48000, "channels": 1},
  "segments": [
    {
      "scene_id": "S01",
      "text": "...",
      "spoken_text": "...",
      "output": "audio/segments/S01.wav",
      "status": "pending"
    }
  ]
}
```

Relative `MIMO_REFERENCE_VOICE` paths are resolved from `ENGINEERING_ROOT`; output files are resolved from `VIDEO_PROJECT_ROOT`.

## Segmenting

- One scene per segment by default.
- Split very long scenes at semantic pauses.
- Preserve a stable segment ID across revisions.
- Regenerate only affected segments.
- Respect the provider's per-request audio-duration limit. When MiMo is operated with a 30-second cap, target 20–25-second chunks and reject any plan whose estimated upper bound reaches 30 seconds. Do not replace this with a whole-chapter request.
- A continuity group may contain several bounded TTS chunks. Measure each take, select candidates whose active speech rate is consistent, normalize loudness, and only then merge the group. “Same reference voice” does not make independent requests share pace, gain, or prosody.

Character count is only a conservative request-size guard, never final timing. Chinese speech rate varies with punctuation and emphasis; verify the returned duration and split/regenerate when a take reaches the provider limit.

### Measured consistency workflow

Build the request plan before spending API calls:

```bash
"$PYTHON_EXE" scripts/produce_voice.py --project <project-dir>
```

The command writes `audio/tts-plan.json`. It never puts a scene or chapter into
one oversized request: each original segment is divided at sentence/clause
boundaries using `audio.tts_request_target_seconds` and a conservative planning
rate. The returned audio duration remains the hard authority.

Generate only after reviewing the plan:

```bash
"$PYTHON_EXE" scripts/produce_voice.py --project <project-dir> --generate
```

For each chunk, the orchestrator:

1. calls the unchanged `mimo-tts` provider at least
   `voice.consistency.candidate_count` times;
2. transcribes each take, only to measure coverage and active speech span;
3. rejects takes beyond the duration cap, below ASR coverage, outside the pace
   band, discontinuous with the preceding selected take, clipped, or holding a
   silence longer than `max_internal_gap_seconds` between sentences;
4. selects the lowest-drift valid take;
5. trims to the energy edges of the take, never to a recogniser timestamp;
6. applies two-pass loudness normalization;
7. merges chunks with the configured intra-chunk pause and segments with the
   project segment pause;
8. applies `voice-plan.json`, then reruns final alignment, timing generation,
   timing injection, and the sync gate.

The objective record is `audio/voice-production.json`; it keeps all candidate
metrics and the selected take. Failed candidates remain auditable and are not
silently substituted.

Recommended defaults:

- request target / hard cap: 25 / 30 seconds;
- two candidates, up to four attempts;
- project-selected active speech rate ±18%;
- adjacent selected pace delta ≤15%; if the next chunk is stranded by adjacency alone, backtrack to an alternate earlier take before more provider calls;
- longest silence *inside* a take ≤1.0 s (`max_internal_gap_seconds`);
- interrupted runs resume from `audio/voice-production.json` when plan, settings, and reference-voice hashes still match;
- ASR coverage ≥90% (review proper-noun noise separately);
- final `tail_characters` of the chunk recognised at `min_tail_coverage` or better, so a take the provider cut short is rejected instead of merged;
- selected output `-16 LUFS`, `-1.5 dBTP`, flat factor `0.000`.

### Silence inside a chunk is measured, not hoped for

Every other pause in the narration is deliberate: chunk joins use
`tts_chunk_pause_seconds` (0.12 s), segment and scene joins use 0.8 s. The
pauses *inside* a chunk were the exception — the provider chose them and
nothing measured them. On one 150-second video that produced 1.27 s and 1.36 s
between consecutive short sentences, ten times the designed join, in the one
chunk a viewer was most likely to notice.

The pace gate cannot catch this, because `chars_per_second` divides by the
whole first-to-last-sample span and therefore counts silence as speech. A take
that articulates normally and stops for a second between sentences measures as
*merely slow*, and merely slow is inside an ±18% band: the offending chunk
scored 3.90 against a 4.6 target and was accepted. The same blindness disables
the adjacent-pace rule, which compares two numbers that do not mean what their
name says.

`assess_candidate()` therefore reads the gaps between the energy clusters it
already computes for edge trimming — the data was there and was being thrown
away — and records four fields per take: `max_internal_gap`,
`internal_silence`, `long_gaps`, and `voiced_chars_per_second` (characters
divided by the span *minus* the gaps). A take whose longest inner gap exceeds
`max_internal_gap_seconds` is rejected like any other failure, and among takes
that pass, `candidate_score()` adds the silence ratio so the tighter take wins.

The 1.0 s default is calibrated, not guessed. Replaying the measurement over
the eleven selected takes of that project gave worst-gap values of 0.28, 0.41,
0.49, 0.74, 0.79, 0.86, 0.90, 0.92, 1.12, 1.37 and 1.82 seconds. A 0.6 s gate
would have rejected eight of eleven and spent the attempt budget on takes
nobody had complained about; 1.0 s rejects the three real outliers, including
the 1.37 s chunk that prompted the gate, and leaves sub-second breathing to the
soft preference in the scorer. Raise the limit for a deliberately slow, spacious
register; lower it for dense explanatory narration.

Two consequences worth knowing. `voiced_chars_per_second` is recorded but not
gated, and the gap between the two rates is wide: on those same takes the gated
rate ran 3.77–5.31 while the voiced rate ran 5.89–7.40. Moving the pace gate
onto the voiced rate therefore needs `target_chars_per_second` re-standardised
from 4.6 to roughly 6.5, not a small adjustment — do it as its own change, with
an old project re-measured for reference. And silence is measured from the
waveform rather than the transcript, so a candidate stored before this existed
cannot be re-judged on resume the way `coverage` can; those records are dropped
from the seed instead of being ranked above measured takes.

### The style instruction shapes rate, never pauses

`voice.instruction` may carry one global rate descriptor, and it should agree
with `target_chars_per_second` — dropping the descriptor entirely is not an
improvement, because the provider's unguided pace can sit far enough from the
target that every take is rejected and the run burns its attempt budget.

What the instruction must never contain is pause-shaping wording: `不要赶`,
`停顿明显`, `慢慢说`, `每句之间留白`. Those lengthen silence rather than slow
articulation, which is the one thing no downstream stage can repair and, until
the gate above existed, the one thing nothing measured. The project that
produced the 1.3-second gaps had overridden the default to `语速偏慢，不要赶`:
`语速偏慢` was legitimate and gated, `不要赶` was neither, and it applied to
all 28 chunks at once.

Slow a specific line by planning it — an exact pause in
`script/voice-plan.json`. Slow the whole project by lowering
`target_chars_per_second`. Both are inspectable and both are gated.

### Do not score a Chinese recogniser on Latin words

A chunk containing `Markdown` and `V1` failed the coverage gate eight takes in
a row at 77–80%. The speech was correct every time; the recogniser rendered the
same word as 麦克顿, 麻烦, 骂托, 马档 and 先出唯1 from take to take. Scoring those
characters measures the recogniser, not the take.

`scored_text()` therefore strips Latin runs from both sides before computing
coverage and tail coverage. The gate keeps its teeth — on that chunk the
cleanly-read take rose from 0.865 to 0.985 while a genuinely garbled take stayed
at 0.600 and was still rejected. Pace still counts Latin characters, because
they take time to say.

Stored candidates must be re-scored on resume. A take judged under older rules
carries a stale `coverage` value, and reusing it silently reapplies the rule you
just changed.

### Backtracking must be able to buy more takes

The adjacent-pace rule creates deadlocks: an earlier chunk settles on a fast
take, and the next chunk's natural pace sits outside the window no matter how
many times it is regenerated. Backtracking exists for this, but it is useless
if it can only reshuffle takes that already exist — an earlier chunk that
settled on its *only* viable take offers nothing to swap in, and the run blocks.

So when backtracking reaches a chunk with no stored alternative, it generates
additional takes for that chunk (`deepen_candidates`, bounded by
`max_attempts`) instead of giving up. And it does not simply take the next-best
alternative: it sorts by proximity to `reachable_rate()`, the median pace the
stranded chunk actually achieved, so the swap targets the deadlock rather than
merely changing the number.

### A take that will not normalize is a rejected take

Provider output level varies widely. A take can pass every content gate and
still be unusable: one measured at `-39.5 LUFS` with a `-11.0 dBTP` transient —
a 28 dB peak-to-loudness ratio against the 10–15 dB normal for speech — cannot
reach `-16 LUFS` by gain alone without breaching the true-peak ceiling.

Two rules follow. The gain-correction stage limits that peak (`alimiter`, with
about 1 dB of headroom below the ceiling because it caps sample peaks while
inter-sample peaks land higher) rather than shipping the chunk under-level. And
when normalization still fails, the failure is appended to the take's
`rejection_reasons` and the producer generates another take, up to
`max_attempts`. It must never abort the run and wait for someone to clear the
rejection by hand.

### Trim to energy, never to the recogniser

The recogniser reports the end of the last *token*, which routinely lands earlier
than the last audible sample — measured spread on one 28-chunk project was −0.34 s to
+0.49 s against the true edge. Trimming there clips the natural decay of the
final syllable on some chunks and leaves half a second of dead air on others,
and the ASR-coverage gate cannot see it because the recogniser did hear the
word; only the trim point was wrong.

`speech_edges()` therefore scans 10 ms RMS frames and returns the first and last
frame above `speech_edge_threshold_db` (default `-50`, roughly 30 dB above the
provider's noise floor). The chunk is cut at that edge plus
`speech_release_seconds` (default `0.08`) so every chunk ends the same distance
after its last audible sample. Recogniser spans are the fallback only when no
frame clears the threshold. Because the release replaces a variable pad, this
tightens total narration rather than padding it: on the same project it removed
3.73 s of dead air while recovering five clipped tails.

Do not use aggressive time stretching to rescue a slow take. Regenerate large
pace errors; reserve `atempo` for an explicitly approved correction below about
5%.

## Exact pauses

Keep narration provider-neutral. `SCRIPT.md` and every text file sent to TTS contain spoken words only; pseudo tags such as `<#1#>`, `[pause]`, or SSML-like fragments are invalid unless the selected provider explicitly supports them and the project has a provider-specific contract. The default MiMo path does not use inline pause markup.

Store deliberate exact pauses in `script/voice-plan.json`, anchored to a stable narration unit:

```json
{
  "schema_version": "1.0",
  "pauses": [
    {
      "id": "P01",
      "chapter": "S01",
      "after_unit": "S01.2",
      "after_text": "标题句全文。",
      "seconds": 1.0,
      "source": "user",
      "reason": "标题后的理解时间",
      "enabled": true
    }
  ]
}
```

Pause sources:

- `automatic`: proposed from the semantic structure and shown in review;
- `user`: requested in natural language, for example “在‘标题句全文。’后停 1 秒”;
- default scene/segment gaps: configured separately in `project-config.json`.

Application order:

1. synthesize clean text;
2. preliminarily align the unpaused take;
3. normalize/select the approved take;
4. run `scripts/apply_voice_plan.py` to insert exact PCM silence;
5. run the final alignment and rebuild timing.

`apply_voice_plan.py` validates `after_text` against the aligned unit, writes `audio/voice-plan-application.json`, and refuses double application. `check_sync.py` blocks a render if the plan is unapplied or stale.

## Pronunciation

`script/pronunciation.json` maps display text to spoken text:

```json
{
  "entries": [
    {
      "display": "shotlist-builder",
      "spoken": "shot list builder",
      "notes": "English pronunciation"
    }
  ]
}
```

`produce_voice.py` applies these substitutions when it builds the plan, and only to the provider request. The plan keeps the original narration in `text` and records the substituted form as `tts_text`; the chunk hash covers `tts_text`, so editing an entry invalidates exactly the takes it affects and leaves the rest cached.

Substituting the request rather than the script is what keeps a pronunciation fix from moving a caption. `timing/chapters.json` stays authoritative for alignment, beats, and captions, so `Skill` still occupies its original characters no matter how it is pronounced. The cost is confined to the recogniser: it hears the substituted form, so those characters arrive as unmatched insertions and the surrounding times are interpolated instead of anchored. That is the same tolerance the aligner already applies to a misrecognised Latin word.

Keep substitutions short and local for that reason. Rewriting a whole clause moves the interpolated span from a few characters to a sentence, which is where a real timing error starts. If a line needs heavy rewriting to read well, change the narration itself and re-approve it.

## Merge target

Normalize all segments before merge:

- WAV PCM 16-bit
- 48 kHz
- mono or consistent stereo
- consistent loudness
- controlled gaps between segments **and** between scenes — default **0.8 s** for both (`audio.segment_pause_seconds` / `audio.scene_gap_seconds` in `project-config.json`); keep them equal unless the user overrides

## Per-segment objective checks

Run these on every generated segment, including after voice review has been delegated. Subjective sign-off can be delegated; these cannot, because they catch defects that are inaudible on a first listen but bake into the master.

```bash
ffmpeg -hide_banner -i seg.wav -af astats=metadata=1 -f null - 2>&1 \
  | rg -o "Peak level dB: [-0-9.]+|Flat factor: [0-9.]+|Peak count: [0-9]+"
ffmpeg -hide_banner -i seg.wav -af volumedetect -f null - 2>&1 | rg -o '(mean|max)_volume: [-0-9.]+ dB'
```

**Flat factor is the check that matters, and `volumedetect` cannot substitute for it.** TTS engines occasionally emit a clipped take. A clipped segment reports a `max_volume` around −0.1 dB, which looks merely hot rather than broken, while `astats` exposes the real signature: a non-zero flat factor and a peak count in the dozens. A healthy segment reads flat factor `0.000` with a peak count of 2.

Clipping means the waveform is already flattened, so **attenuating afterwards cannot undo it — regenerate the segment.** Because TTS is non-deterministic, generate two retakes and pick on measurements: flat factor `0.000` and a duration in line with the rest of the project. A retake several seconds longer than the original has drifted in pace and will not cut against motion anchored to the original timing.

Also compare each segment's mean level against the project's existing spread rather than an absolute target; a segment is only an outlier if it falls outside the range you have already accepted.

Verify after every merge that the previously approved portion is untouched, by comparing raw PCM rather than the container — appending a segment rewrites the WAV header's RIFF and data length fields, so the files legitimately differ byte-for-byte while the audio is identical:

```bash
ffmpeg -v error -t <prev_duration> -i new.wav -f s16le - | cmp - <(ffmpeg -v error -i prev.wav -f s16le -)
```

## Alignment

Timing must be generated from the final merged audio or from final approved segments with exact offsets, and it must be **measured**. Never distribute a segment's duration across its characters in proportion to their count: Chinese TTS pauses at punctuation, stretches emphasis, and races through enumerations, so that estimate drifted up to 3 seconds on a 158-second chapter in this project — far enough to put a caption under the wrong sentence.

### Procedure

```bash
"$PYTHON_EXE" scripts/align_audio.py --project <project-dir>
"$PYTHON_EXE" scripts/build_timing.py --project <project-dir>
"$PYTHON_EXE" scripts/apply_timing.py --project <project-dir>
"$PYTHON_EXE" scripts/check_sync.py  --project <project-dir>
```

`align_audio.py` reads `timing/chapters.json` for the authoritative text and `audio/segments/<chapter>.<ext>` for the audio, and writes `timing/align/<chapter>.json`. Any container ffmpeg can decode is accepted — wav, flac, mp3, m4a, ogg, opus, aac, mp4, webm — because both recognition and the energy pass run on a 16 kHz mono copy made with ffmpeg rather than on the delivered file.

### Why this is alignment, not transcription

The script is already known. The recogniser only has to place it in time, so its mistakes are absorbed instead of propagated:

1. **Recognition** — word-level timestamps from Groq's hosted `whisper-large-v3`.
2. **Edit-distance alignment** — the recognised character stream is matched against the script with `difflib`. Correctly recognised characters become anchors; everything between them is interpolated. Both sides are case-folded and digit-folded, so `Skill`/`skill` and `八点`/`8点` still anchor. Every fold is 1:1 so character indices, which carry unit ownership, survive.
3. **Energy refinement** — recognition puts a boundary in the middle of a pause, up to half a second before the speaker actually opens up. Short-time energy pulls each boundary onto the real speech edge.

Layer 3 owns boundary precision, so the model choice does not set the sync floor. What a better model buys is match rate on proper nouns and homophones — and that is not cosmetic, because an unmatched run of characters is interpolated instead of measured. Expect ±0.2 s.

### Recognition runs on Groq

Recognition is hosted, not local. `align_audio.py` and `produce_voice.py` both call Groq's `whisper-large-v3` through `resolve_recognizer()`; `--model` overrides the model and nothing else needs configuring.

This pipeline used to run whisper.cpp locally, and the reason that is gone is worth keeping. Local recognition was the slowest step in the whole voice phase, and slow in a way that compounds, because `produce_voice.py` recognises *every* candidate take rather than only the selected one. On a 24-thread machine, whisper.cpp `small` took 33.8 s on a 20.7 s chapter; Groq takes 1.5 s. Across five chapters — 322 s of audio — that is roughly nine minutes against 12.1 s.

Accuracy moved the same direction, which is the part that actually changes the output. Match rates on those five chapters went from 88.3–96.2% to 92.5–100%. On one chapter the local model heard `计划里的事就被忘了` as `计划里的视觉被忘了` and `干货` as `钢火`; those unmatched characters cost anchors, and the line that should start at 7.27 s — where the measured onset of `你` actually is — landed at 8.20 s. A caption 0.9 s late is a sync complaint, and the energy pass cannot recover it because it only snaps to the *nearest* edge.

There is no local fallback, and that is deliberate rather than an oversight: the pipeline already needs network access for TTS, so a machine that cannot reach Groq cannot produce narration to align in the first place. A second recogniser would only add a code path that is never exercised and a second set of timings to reconcile.

Uploads are re-encoded to 16 kHz mono FLAC first. The service downsamples to that anyway, so it is a straight saving over the proxy: 2.1 MB instead of 20 MB on a 104 s take. Takes long enough to exceed the 25 MB limit are split at the middle of a detected silence and the timestamps offset back, so a seam never lands inside a word.

Two behaviours are worth knowing before debugging a failure. Word timestamps come back overlapping now and then — 16 of 451 words on one take started before the previous word ended — so each start is clamped to the running cursor before alignment sees it. And the endpoint sits behind an edge that refuses the default `Python-urllib` agent with a bare `error code: 1010`, which reads like an auth failure and is not; the request sends its own `User-Agent` for that reason.

### Reading the match rate

The per-unit anchor ratio is a drift detector, not just a quality score. A line the recogniser cannot find is either misrecognised or **not in the audio at all**:

- `简便易行` at 50% — the surrounding line matched, so this is recognition noise.
- `我的反馈只动了一处` at 67%, where the audio says `后来反馈只改了一处` — that is a stale recording, and no amount of re-rendering will fix it.

`check_sync.py` prints the script text beside what was heard so the two cases separate at a glance.

### Environment

`GROQ_API_KEY` in the engineering root's `.skill.env` (plus `SKILL_PROXY` when the machine reaches the internet only through a proxy), and ffmpeg. Nothing to install, no model to download.

A `1010` response is an edge rejection, not a bad key; a `429` is retried with backoff up to four times. If recognition stays unreachable, create a timing manifest with `status: needs_alignment` and do not claim Phase 4 is complete.

### Required timing artifacts

All are generated by `build_timing.py` from the alignment:

- `beats.json` — motion anchors keyed by unit id; the single source of truth for keyframes
- `cues/<chapter>.json` — caption cues, chapter-relative
- `words.json` — per-character spans
- `sentences.json` — measured sentence spans
- `scenes.json` — chapter spans on the global timeline
- `captions.srt` — subtitle deliverable

Captions are split at punctuation to a character limit and are **never truncated**. An ellipsis in a cue is a bug, not a style choice; `check_sync.py` treats it as blocking.
