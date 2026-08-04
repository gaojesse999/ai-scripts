# HyperFrames Build

The renderer consumes `scene-plan.json`, actual timing, `motion-plan.yaml`, and `style-tokens.json`.

Rules:

- compositions and nested scenes;
- stable human-readable IDs for timeline-visible elements;
- `class="clip"`, `data-start`, `data-duration`, `data-track-index`;
- a deterministic seek interface — either paused GSAP timelines registered on `window.__timelines`, or a keyframe interpolation engine exposed as `window.__seek(t)`; the same `t` must always yield the same frame;
- no wall-clock, rAF-accumulated, or CSS-transition state;
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
