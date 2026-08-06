# HyperFrames Build

This reference reflects the official HyperFrames CLI and composition model available when this Skill was built. Verify current official documentation before relying on version-sensitive flags.

## Recommended project creation

```bash
npx hyperframes init <project-name> --example blank --resolution landscape
```

Use `portrait` for vertical video and `landscape-4k` only after a 1080p draft passes QA.

## Development loop

```bash
npx hyperframes doctor
npx hyperframes compositions
npx hyperframes lint
npx hyperframes inspect
npx hyperframes snapshot --frames 8
npx hyperframes preview
npx hyperframes render --docker --output output.mp4
```

## Composition rules

- Composition HTML is the render source.
- Timed layers use `class="clip"` plus `data-start`, `data-duration`, and `data-track-index`.
- Nested scenes use `data-composition-src`.
- The framework owns audio/video playback and seeking.
- Do not call `play()`, `pause()`, or assign `currentTime` manually.

## GSAP rules

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
<script>
  const tl = gsap.timeline({paused: true});
  tl.from("#title", {opacity: 0, y: 48, duration: 0.6}, 0);
  tl.set({}, {}, 8.0);
  window.__timelines = window.__timelines || {};
  window.__timelines["S01"] = tl;
</script>
```

- Timeline key must match `data-composition-id`.
- Use absolute timeline positions.
- Extend the timeline to the full scene duration.
- Do not use real-time randomness or unseeded procedural variation.

## Variables

Declare reusable variables with `data-composition-variables`, pass instance values with `data-variable-values`, and read them through `window.__hyperframes.getVariables()`.

Use variables for:

- titles and labels;
- theme variants;
- repeated cards;
- screenshots and media paths;
- data values;
- per-scene accent choices.

## Knowledge-video visual rules

- One primary explanatory idea per scene.
- Use large blocks and clear hierarchy.
- Keep motion semantic: reveal, group, compare, transform, trace, or emphasize.
- Avoid constant floating, wobbling, particle noise, and decorative micro-motion.
- Maintain consistent margins, title positions, type scale, and transitions.
- Use screen recordings or screenshots only when they prove a concrete operation.
- Use a reusable caption layer rather than custom caption markup in every scene.

## Reference-style build rules

When `project.style_profile` is `editorial-technical-dark` or a reference profile requests a similar system:

- use a flat charcoal canvas, crisp borders, large white type, and a restrained accent palette;
- render a persistent chapter label and progress rail at the top;
- render captions through one shared bottom-safe-area layer rather than custom caption markup in every scene;
- route scenes through reusable `hero`, `metric-grid`, `compare`, `flow`, `code`, `architecture`, and `summary` components;
- read structured `visual_data` for diagrams and comparisons, with plain screen text as a fallback;
- keep motion semantic: reveal, draw, trace, fill, compare, focus, or resolve;
- use hard cuts or brief fades between distinct arguments and avoid perpetual decorative loops.

## Browser/Canvas fallback

When HyperFrames is unavailable but a browser runtime exists, use a deterministic browser/Canvas composition as the visual fallback:

- author at the target canvas, normally 1920x1080;
- expose `window.renderAt(seconds)` so keyframes can be inspected without wall-clock playback;
- use `canvas.captureStream(60)` or deterministic frame capture for a 60 fps reference;
- keep the same chapter rail, caption safe area, palette, and scene-plan motion beats;
- encode the browser output once to the delivery codec and report the fallback renderer in QA.

This fallback is appropriate for layered cards, document panels, diagrams, masks, path tracing, controlled glow, and camera-like movement. It should remain driven by the canonical scene plan, not by a separate ad hoc storyboard.

The scaffold must be useful on first render: it should produce the reference-style canvas and visible layout primitives even before a scene receives bespoke art direction.

## Timing

Use actual values from `timing/scenes.json`. Visual beats should align to sentence/word anchors rather than arbitrary guessed delays.
