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
