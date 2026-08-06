# Voice Pipeline

## Provider-neutral workflow

The Skill may use any available TTS provider, local model, or imported recording. Do not hard-code a provider into the content model.

`audio/tts-manifest.json` should contain:

```json
{
  "provider": "configured-or-manual",
  "voice": "default",
  "language": "zh-CN",
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

## Alignment

Timing must be generated from the final merged audio or from final approved segments with exact offsets.

Required timing artifacts:

- `words.json`
- `sentences.json`
- `scenes.json`
- `captions.srt`

If automatic alignment is unavailable, create a timing manifest with `status: needs_alignment` and do not claim Phase 4 is complete.
