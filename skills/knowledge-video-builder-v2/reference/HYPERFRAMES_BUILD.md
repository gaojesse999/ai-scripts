# HyperFrames Build

The renderer consumes `scene-plan.json`, actual timing, `motion-plan.yaml`, and `style-tokens.json`.

Rules:

- compositions and nested scenes;
- stable human-readable IDs for timeline-visible elements;
- `class="clip"`, `data-start`, `data-duration`, `data-track-index`;
- paused GSAP timelines registered on `window.__timelines`;
- absolute deterministic positions;
- scene duration must match final audio timing;
- no manual media seeking/playback control;
- centralized tokens and reusable components;
- renderer must not invent claims or timing.

Recommended checks:

```bash
npx hyperframes doctor
npx hyperframes lint
npx hyperframes inspect
npx hyperframes snapshot --frames 8
npx hyperframes preview
```
