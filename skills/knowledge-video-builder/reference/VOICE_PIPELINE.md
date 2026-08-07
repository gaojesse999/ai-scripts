# Voice Pipeline

## MiMo-first workflow

The default TTS provider is the local `mimo-tts` Skill. `knowledge-video-builder` uses a fixed `ENGINEERING_ROOT`: the directory containing `.cursor/skills/knowledge-video-builder` and the engineering-root `.skill.env`. Do not derive this path from the current video artifact directory.

Run the bundled script with the fixed Skill path and explicit environment file:

```bash
SKILL_PROJECT_ROOT="$ENGINEERING_ROOT" \
SKILL_PROXY_STRICT=1 \
HTTP_PROXY="$SKILL_PROXY" HTTPS_PROXY="$SKILL_PROXY" ALL_PROXY="$SKILL_PROXY" \
python3 "$ENGINEERING_ROOT/.cursor/skills/mimo-tts/scripts/mimo_tts.py" \
  --env-file "$ENGINEERING_ROOT/.skill.env" \
  --input <scene-or-segment-text-file> \
  --output-root "$VIDEO_PROJECT_ROOT/audio/mimo-outputs"
```

The proxy is mandatory for this Skill. Do not retry directly after a proxy failure.

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

## Merge target

Normalize all segments before merge:

- WAV PCM 16-bit
- 48 kHz
- mono or consistent stereo
- consistent loudness
- controlled gaps between segments

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

Timing must be generated from the final merged audio or from final approved segments with exact offsets.

Required timing artifacts:

- `words.json`
- `sentences.json`
- `scenes.json`
- `captions.srt`

If automatic alignment is unavailable, create a timing manifest with `status: needs_alignment` and do not claim Phase 4 is complete.
