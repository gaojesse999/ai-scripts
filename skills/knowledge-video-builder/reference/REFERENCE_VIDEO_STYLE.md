# Reference Video Style

Use this reference when the user supplies a video, subtitle file, storyboard, or frame samples and asks for a similar visual effect. The reference is a style source, never an evidence source.

## Inspection contract

1. Inventory the reference files and identify picture, audio, and caption tracks.
2. Probe duration, resolution, aspect ratio, frame rate, codec, audio format, and caption format.
3. Sample the hook, at least two chapter transitions, a dense explanation, a comparison or workflow scene, and the ending.
4. When timing files exist, measure cue count, average cue duration, cadence, maximum cue length, and whether cues represent sentences or words.
5. Write `analysis/reference-style-profile.md` before choosing the final visual system.

The profile must distinguish measurable observations, editorial interpretation, and style choices to carry forward.

## Editorial technical dark preset

Use this preset when the reference resembles a clean technical explainer with dark canvas, bright accent color, and diagram-led teaching. Override it when the reference clearly establishes another system.

### Tokens

```text
canvas:   #171917
surface:  #292b29
surface-2:#343735
ink:      #f5f5f0
muted:    #8b9089
accent:   #ff9f0a
danger:   #ff5362
success:  #39d98a
blue:     #5f8fff
purple:   #a875ff
teal:     #26c4aa
```

Use a flat canvas, crisp 1-2px borders, restrained shadows, and generous negative space. Do not add gradients, grain, particle fields, bokeh, or decorative blobs.

### Persistent frame

- 16:9 landscape; author at 1920x1080 and render a 1280x720 preview when appropriate.
- Reserve the top 8-12% for a small chapter label and a thin progress rail.
- Reserve the bottom 12-16% for one shared caption layer.
- Keep explanatory content inside a 8-10% safe margin.
- Use 4-8 chapters. The active chapter and progress segment use `accent`; inactive segments are muted.

### Caption layer

- Captions are separate from explanatory screen text.
- Use a near-black pill or bar with white text, centered near the bottom safe area.
- Show one semantic cue at a time, normally no more than two lines.
- Split long cues before they collide with diagrams or exceed mobile readability.
- Keep captions stable while the diagram changes; do not animate every word unless the reference clearly does so.

### Layout primitives

Choose one named primitive per scene:

- `hero`: one claim, title, metric, or transformation.
- `metric-grid`: two to four values or proof points.
- `compare`: two opposing panels with a visible verdict.
- `flow`: a left-to-right sequence with active step tracing.
- `code`: a short source excerpt paired with the behavior it causes.
- `architecture`: nodes and relationships, with one highlighted path.
- `summary`: before/after, problem/solution, or tool-selection matrix.

Each scene has one primary idea, 2-4 visible modules, and a semantic reason for every motion. Use `visual_data` for columns, steps, nodes, metrics, and code excerpts instead of encoding structure in prose.

### Motion grammar

Allowed default actions are `reveal`, `rise`, `draw`, `trace`, `fill`, `compare`, `focus`, `collapse`, and `resolve`. Tie them to sentence or word anchors from real timing. Use short entrances, 80-140ms stagger for related items, and hard cuts or brief fades between distinct arguments. Never use ambient floating, random motion, or perpetual loops to fill silence.

### Density and pacing

- Aim for 1.2-3.5 second semantic beats and 4-12 second scene units.
- Change the visual when the argument changes, not on every subtitle cue.
- Keep on-screen copy shorter than narration; prefer labels, conclusions, and contrasts.
- Use a concrete example early, then reuse the same visual vocabulary for the rest of the explanation.

### Fidelity ladder

Use this ladder when comparing a draft to the reference:

1. **Structural match:** persistent chapter chrome, caption safe area, palette, title hierarchy, and reusable layout primitives.
2. **Semantic motion match:** each narration beat changes a visible state through reveal, trace, focus, compare, fill, or resolve.
3. **Asset match:** scenes use concrete modules such as documents, interface panels, diagrams, illustrations, metrics, or shotlist rows instead of placeholder rectangles.
4. **Cinematic match:** layered entrances, masked transitions, path drawing, controlled glow/shadow, and 60 fps motion are coordinated as one composition.

A draft is not reference-matched when it only satisfies the first rung. For the third and fourth rungs, prefer a browser/Canvas or HyperFrames renderer. Treat a direct FFmpeg filter graph as a timing fallback and label the fidelity gap in QA.

## QA checks

The final review must verify chapter continuity, caption safe area, caption legibility, token consistency, layout reuse, diagram readability, and semantic motion. A style match is not successful if the video only has the right colors while the information hierarchy, pacing, and caption behavior are wrong.
