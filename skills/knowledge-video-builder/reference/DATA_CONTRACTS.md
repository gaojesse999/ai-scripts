# Data Contracts

## `project-state.json`

Required fields:

```json
{
  "schema_version": "1.0",
  "project_id": "slug",
  "title": "Title",
  "current_phase": "analysis",
  "status": "active",
  "source": {"path": "", "sha256": ""},
  "phases": {
    "analysis": {"status": "in_progress", "version": 1},
    "brief": {"status": "not_started", "version": 0},
    "script": {"status": "not_started", "version": 0},
    "voice": {"status": "not_started", "version": 0},
    "visual": {"status": "not_started", "version": 0},
    "render": {"status": "not_started", "version": 0}
  },
  "history": []
}
```

## `script/scene-plan.json`

```json
{
  "schema_version": "1.0",
  "project": {
    "title": "",
    "language": "zh-CN",
    "aspect_ratio": "16:9",
    "width": 1920,
    "height": 1080,
    "fps": 60,
    "target_duration": 240,
    "style_profile": "editorial-technical-dark",
    "renderer": "hyperframes",
    "visual_system": {
      "canvas": "#171917",
      "accent": "#ff9f0a",
      "caption_mode": "bottom-pill",
      "chapter_count": 6
    }
  },
  "scenes": []
}
```

Each scene requires:

- `id`
- `chapter`
- `purpose`
- `narration`
- `evidence_ids`
- `screen_text`
- `visual_type`
- `visual_description`
- `visual_beats` (short strings or objects with `anchor`, `action`, `layer`, and optional `duration`)
- `assets`
- `estimated_duration`
- `transition`

Reference-style scenes may also include:

- `layout`: `hero`, `metric-grid`, `compare`, `flow`, `code`, `architecture`, or `summary`;
- `visual_data`: structured content for columns, steps, nodes, metrics, or code excerpts;
- `motion`: semantic actions with sentence/word anchors;
- `motion`: semantic actions with sentence/word anchors; prefer explicit layers for asset-led motion;
- `caption`: shared caption-layer settings;
- `style_tokens`: a local override of the project visual system.

## `audio/tts-plan.json`

Written by `scripts/produce_voice.py` before API calls:

```json
{
  "schema_version": "1.0",
  "request_limit_seconds": 30,
  "request_target_seconds": 25,
  "planning_max_spoken_characters": 80,
  "chapters": {
    "S02": {
      "chunks": [
        {
          "id": "S22-C01",
          "chapter": "S02",
          "segment": "S22",
          "order": 2,
          "text": "第一条……",
          "text_sha256": "...",
          "spoken_characters": 72,
          "planning_seconds": 22.5
        }
      ]
    }
  }
}
```

`planning_seconds` is only a conservative request-size estimate. Returned WAV
duration is measured and rejected when it exceeds `request_limit_seconds`.

## `audio/voice-production.json`

Written incrementally by `scripts/produce_voice.py`:

```json
{
  "schema_version": "1.0",
  "plan_sha256": "...",
  "settings": {
    "max_seconds": 30,
    "target_rate": 4.8,
    "target_lufs": -16
  },
  "chapters": {
    "S02": {
      "chunks": [
        {
          "id": "S22-C01",
          "candidates": [
            {
              "attempt": 1,
              "duration": 24.3,
              "coverage": 0.96,
              "chars_per_second": 4.72,
              "flat_factor": 0,
              "rejection_reasons": []
            }
          ],
          "selected_attempt": 1,
          "selected_metrics": {
            "normalized_lufs": -16,
            "normalized_true_peak": -1.5
          }
        }
      ],
      "final_audio_sha256": "...",
      "final_duration": 125.4
    }
  }
}
```

Every rejected candidate keeps explicit reasons. Selection is invalid when the
plan hash, chunk text hash, reference voice, or consistency settings change.

## `script/voice-plan.json`

Exact delivery pauses live outside spoken narration:

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

`after_unit` is the stable unit used by alignment and motion. `after_text` is a freshness assertion: applying the plan fails when the narration at that unit changed. `source` is `user` or `automatic`; a user pause wins when two entries target the same anchor.

Do not encode pauses in `SCRIPT.md` or TTS input with pseudo tags.

## `audio/voice-plan-application.json`

Written by `scripts/apply_voice_plan.py`. It binds the current per-chapter pause plan to the exact WAV produced by applying it:

```json
{
  "schema_version": "1.0",
  "voice_plan": "script/voice-plan.json",
  "chapters": {
    "S01": {
      "chapter_plan_sha256": "...",
      "input_sha256": "...",
      "output_sha256": "...",
      "duration_before": 18.24,
      "duration_after": 19.24,
      "pauses": [
        {"id": "P01", "after_unit": "S01.2", "at": 7.42, "seconds": 1.0}
      ]
    }
  }
}
```

The sync gate requires `output_sha256` to match `audio/segments/<chapter>.wav` and `chapter_plan_sha256` to match the current enabled pauses.

## `timing/align/<chapter>.json`

Written by `scripts/align_audio.py`. Times are chapter-relative.

```json
{
  "chapter": "S01",
  "duration": 30.08,
  "granularity": "line",
  "source": "groq forced alignment",
  "model": "whisper-large-v3",
  "match_rate": 0.99,
  "snapped_units": 4,
  "units": [
    {
      "id": "S01.3",
      "segment": "S01",
      "text": "你是不是经常做计划，最后却完不成？",
      "start": 10.92,
      "end": 14.84,
      "anchors": 14,
      "chars": [{"i": 0, "c": "你", "start": 10.92, "end": 11.05, "a": true}]
    }
  ],
  "asr_text": "..."
}
```

`anchors` counts characters the recogniser matched directly; the rest were interpolated. `chars[].i` is the index in the unit's own text, which lets a caption be split anywhere in the line without falling back to an estimate. `asr_text` is kept so the sync gate can show what was heard. `source` and `model` record which recogniser produced the timing, so a match rate can be read against the model that earned it.

## `timing/beats.json`

Written by `scripts/build_timing.py`; consumed by `scripts/apply_timing.py`. The single source of truth for motion anchors.

```json
{
  "source": "groq forced alignment",
  "gap_seconds": 0.8,
  "duration": 451.84,
  "beats": {
    "S01.3": {
      "chapter": "S01",
      "segment": "S01",
      "text": "你是不是经常做计划，最后却完不成？",
      "start": 10.92,
      "end": 14.84,
      "global_start": 10.92,
      "anchors": 14
    }
  }
}
```

`start`/`end` are chapter-relative, matching what a composition needs; `global_start` is on the assembled timeline.

## `timing/scenes.json`

```json
{
  "audio_file": "audio/narration.wav",
  "duration": 12.5,
  "scenes": [
    {"id": "S01", "start": 0.0, "end": 7.2, "duration": 7.2}
  ]
}
```

Scene IDs must match `scene-plan.json` exactly.
