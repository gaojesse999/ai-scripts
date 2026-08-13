# HyperFrames Build

This reference reflects the official HyperFrames CLI and composition model available when this Skill was built. Verify current official documentation before relying on version-sensitive flags.

## Recommended project creation

```bash
npx hyperframes init <project-name> --example blank --resolution landscape
```

Use `portrait` for vertical video and `landscape-4k` only after a 1080p draft passes QA.

## Development loop

```bash
npx hyperframes doctor          # run FIRST, before authoring anything
npx hyperframes compositions
npx hyperframes check           # lint + runtime + layout + motion + contrast
npx hyperframes snapshot --at 4,12,20,28,36,44
npx hyperframes render --fps 30 --quality high -o output.mp4
```

`check` supersedes the older `lint` / `validate` pair. Always snapshot before rendering: it costs seconds and is the only cheap way to catch a frozen timeline, which `lint` cannot see.

Render locally by default; `--docker` is opt-in and `project-config.json` ships
`hyperframes.docker_render: false`. The flag exists for a host that genuinely
cannot install the browser and FFmpeg dependencies, and it is never useful when
the runtime is already inside a container, where it only builds a nested image
and duplicates those same dependencies. Docker itself is not a prerequisite: a
machine without it renders locally once the browser and both `ffmpeg` and
`ffprobe` are on PATH, including from a user-owned prefix.

## Composition rules

- Composition HTML is the render source.
- Timed layers use `class="clip"` plus `data-start`, `data-duration`, and `data-track-index`.
- Nested scenes use `data-composition-src`.
- The framework owns audio/video playback and seeking.
- Do not call `play()`, `pause()`, or assign `currentTime` manually.

## GSAP rules

Vendor GSAP into the project; do not load it from a CDN. The render browser is frequently offline or proxy-isolated, and a failed CDN script means `gsap is undefined`, the timeline never registers, and the render silently freezes on frame one.

```bash
curl -o hyperframes/assets/vendor/gsap.min.js https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js
```

```html
<script src="assets/vendor/gsap.min.js"></script>
<script>
  const tl = gsap.timeline({paused: true});
  tl.to("#title", {opacity: 1, y: 0, duration: 0.6}, 0);
  tl.set({}, {}, 8.0);
  window.__timelines = window.__timelines || {};
  window.__timelines["S01"] = tl;
</script>
```

- Timeline key must match `data-composition-id`.
- Asset URLs must be root-relative (`assets/…`), never `../assets/…`; compositions are served with the project root as base URL, so `../` resolves above the root and 404s in Studio preview.
- Fonts must also be local `@font-face` files. Verify the weights actually exist — a family shipping only Regular will synthesize fake bold for every `font-weight: 800` and look muddy. Prefer a variable font.
- Prefer setting initial state in CSS and animating with `.to()`. Where you need GSAP to own the whole transform, use `.fromTo()`; never set a CSS `transform` on a property GSAP also tweens, or GSAP discards the rest of the transform.
- Use absolute timeline positions.
- Extend the timeline to the full scene duration.
- Do not use real-time randomness or unseeded procedural variation.
- Prove the timeline is actually driven: render or snapshot two frames from different beats and confirm they differ. A static video is the expected symptom of a timeline the host never seeks.

## Never ship the scaffold

`scripts/build_hyperframes.py` produces a *starting point*, not a deliverable.

The generator now emits a clean frame — chapter rail, headline, and one layout block — with a timeline that accumulates items and then walks focus across them in order. That is a sane default, not art direction. Every scene still needs the beats from `motion/motion-plan.yaml` at their measured anchor times, and a layout chosen for that scene's actual claim rather than the generic `screen_text` grid.

Compositions generated before this was fixed carry placeholder content that violates the visual density gate. Grep for and delete:

- `eyebrow` — filled with the layout name (`hero`, `compare`, `flow`);
- `lede` — filled with `visual_description`, which is director's notes, not viewer-facing copy;
- `footer` — prints `visual_type · duration` onto the canvas;
- `stage-nav` — defaults to `Script / Assets / Space / Prompt / Shot / Deliver`, from an unrelated template;
- a scene-level `caption` div, which double-renders against the root caption layer.

Their timelines also animate everything inside the first ~1.5 s and then pad with `tl.set({}, {}, duration)`, leaving the scene static for the remainder. Replace them.

## Persistent elements belong to the root composition

Anything that spans the whole video — chapter rail, chapter label, captions, watermark — goes in the root composition, never inside each scene.

A progress rail authored inside a scene can only measure that scene, so in an assembled video it **resets at every scene boundary**. Nine chapters means nine resets, which reads as a bug. Duplicating the element per scene also invites drift in position and styling.

Put the rail at the root instead and it becomes exact by construction:

```js
tl.fromTo('#rail-fill', { scaleX: 0 }, { scaleX: 1, duration: TOTAL, ease: 'none' }, 0);
```

`TOTAL` is the root duration, so the fill stays continuous across boundaries and automatically re-spans as chapters are added — no cross-scene coordination, and no re-render of earlier scenes.

The chapter label swaps per scene, so express it the same way captions are expressed: one `clip` div per scene carrying `data-start` / `data-duration` from `timing/scenes.json`. Give the label slot a **fixed width**; otherwise the rail track shifts sideways whenever a longer chapter name appears.

Two consequences worth planning for:

- A scene composition that previously drew its own chrome must reclaim that space, normally by folding the removed element's height into the stage's top padding, so content does not shift upward. Verify with a pixel diff against the previous render, not by eye.
- Snapshotting a scene composition alone will no longer show the rail or label. Review persistent elements from the root composition.

## Visual coverage must be contiguous even where audio is not

TTS pipelines insert deliberate pauses between segments **and** between scenes — breathing room, and reaction time before the slide or next scene changes. That silence is design intent, not dead air to be trimmed.

Default length is **0.8 s** for both (`project-config.json` → `audio.segment_pause_seconds` and `audio.scene_gap_seconds`). Keep them equal unless the user overrides. Slideshow / module beats inside a scene use the segment pause; do not invent a separate “slide gap”.

The trap: those pauses are in the *audio* timeline, and it is natural to size scene hosts from each scene's own audio duration. Do that and every inter-scene pause becomes a window with **no scene mounted at all** — a black flash. If the incoming scene also fades up from `opacity: 0`, the two compound into roughly half a second of nothing.

Note what this costs: a black flash gives the viewer no reaction time, so the defect silently defeats the exact purpose the pause was added for.

Size every "where we are" layer from the **next scene's start**, not from its own duration:

```python
covered = next_start - start if next_scene else duration
```

Apply it to the scene host *and* the chapter label. Fixing only the host leaves the label blinking off for the length of the pause. The scene composition's own timeline stays at its audio length — GSAP clamps a seek past the end, so the outgoing scene simply holds its last frame through the pause, which is what the reaction beat should look like.

Captions are the deliberate exception: they track what is being said, so they should be absent during silence. The distinction is the useful one to reason from — layers that answer *"where are we"* tile without holes; layers that answer *"what is being said"* follow the audio exactly.

A hard cut must also land on content that is already there. Give the incoming scene's title a visible initial state rather than a fade from zero, and let the secondary elements animate in.

**Per-scene review cannot catch this.** The defect exists only in the assembly, and both scenes look perfect in isolation. Verify at the seam by measuring, not by eye: sample frames just inside and across the boundary and check that non-background pixel coverage never drops to zero.

```bash
ffmpeg -v error -i frame.png -vf "crop=1920:700:0:150,format=gray" -f rawvideo - | \
  python3 -c "import sys;d=sys.stdin.buffer.read();print(sum(b>45 for b in d)/len(d)*100)"
```

**Pick the brightness threshold per region, or the measurement lies.** A threshold of 45 separates content from the stage background, but a progress rail sits on its own track colour that is itself brighter than that. Measuring a `#3a3d3a` track (grey ≈ 60) at threshold 45 counts the empty track as filled and reports a flawless 100% at every timestamp — a reading that looks like a pass and proves nothing. Set the threshold between the track and the fill: for `#ff9f0a` fill (grey ≈ 171) on a `#3a3d3a` track, 120 works. Sanity-check any coverage number against what it should be before trusting it; a rail reading should equal `t / total` within a fraction of a percent.

## Root composition contract

The root element needs `data-start="0"` and `data-duration`, not just `data-composition-id`. Without `data-start` the runtime refuses to begin playback and prints `[StaticGuard] Invalid HyperFrame contract`. Read StaticGuard output on every run; it catches contract violations that `check` does not.

Nested scene hosts carry their own `data-start`/`data-duration` from `timing/scenes.json`, and the root `data-duration` must cover the last scene's end.

## Fonts

The compiler maps common Latin families to deterministic substitutes and prints `No deterministic font mapping for: …` when it cannot. **`Microsoft YaHei` has no mapping**, so a CJK project that names it silently renders in a substituted face. Vendor the face instead:

```bash
curl -Lo hyperframes/assets/fonts/NotoSansSC-VF.ttf \
  https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/NotoSansSC-VF.ttf
```

```css
@font-face{font-family:"ProjectSans";src:url("assets/fonts/NotoSansSC-VF.ttf") format("truetype");font-weight:100 900;font-display:block}
```

Use a variable font so heavy weights are real rather than synthesized. Treat any `No deterministic font mapping` warning as a build failure.

## Environment: fix it without root before falling back

`npx hyperframes doctor` prints `sudo dnf install …` hints that are useless without root. Neither missing browser libraries nor a missing encoder justifies the Canvas fallback, a nested container, or cloud rendering — both are normally fixable in a user-owned prefix.

- Trust `ldd` over `/etc/os-release`; the release file is often stale in derived images. Compare `ldd --version` against the browser's highest required symbol (`objdump -T <chrome> | grep -oE 'GLIBC_[0-9.]+' | sort -uV | tail -1`). Only a genuinely older glibc justifies isolation.
- Extract missing libraries from distro packages into `$HOME`, then export `LD_LIBRARY_PATH`. Resolve transitively — fixing the first batch commonly reveals one more (`libgbm` pulls `libdrm`).
- HyperFrames needs both `ffmpeg` and `ffprobe`. A Python `imageio-ffmpeg` install provides only `ffmpeg`; fetch a static build that ships both.
- Record the working environment in a committed `render-env.sh` so later chapters inherit it instead of re-deriving it.

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
- Use a reusable caption layer rather than custom caption markup in every scene. The same applies to every whole-video element; see "Persistent elements belong to the root composition".

## Reference-style build rules

When `project.style_profile` is `editorial-technical-dark` or a reference profile requests a similar system:

- use a flat charcoal canvas, crisp borders, large white type, and a restrained accent palette;
- render a persistent chapter label and progress rail at the top, both from the root composition — see "Persistent elements belong to the root composition";
- render captions through one shared bottom-safe-area layer rather than custom caption markup in every scene;
- route scenes through reusable `hero`, `metric-grid`, `compare`, `flow`, `code`, `architecture`, and `summary` components;
- read structured `visual_data` for diagrams and comparisons, with plain screen text as a fallback;
- keep motion semantic: reveal, draw, trace, fill, compare, focus, or resolve;
- use hard cuts or brief fades between distinct arguments and avoid perpetual decorative loops.

## Browser/Canvas fallback

Use this **only** when HyperFrames genuinely cannot run, and only as a replacement for it — never alongside it.

**HyperFrames will not drive a `window.renderAt` composition.** Its runtime reads `window.__timelines[<data-composition-id>]` and accepts the entry only if it exposes `duration()`, `time()`, `seek()`, `play()`, and `pause()`. Verified against hyperframes 0.7.94: the string `__seek` does not appear in the runtime at all, and a `{ duration, renderAt }` object fails the interface check. The failure is silent — `lint` passes, the page looks right in a browser, the render completes, and every frame is the composition's initial state.

So before writing a fallback, exhaust the environment fixes below. A missing shared library is not "HyperFrames is unavailable".

If you do build the fallback:

- author at the target canvas, normally 1920x1080;
- expose `window.renderAt(seconds)` for deterministic frame capture by *your own* capture script, not by HyperFrames;
- use deterministic frame capture rather than wall-clock playback or `captureStream`;
- keep the same chapter rail, caption safe area, palette, and scene-plan motion beats;
- encode the browser output once to the delivery codec and report the fallback renderer in QA.

**Never maintain both.** Building a good-looking `renderAt` page next to a placeholder HyperFrames project is a recurring, expensive failure: all the design work lands in the file the renderer never executes, and the file that does get rendered still contains scaffold text. Pick one renderer per project and delete the other.

This fallback is appropriate for layered cards, document panels, diagrams, masks, path tracing, controlled glow, and camera-like movement. It should remain driven by the canonical scene plan, not by a separate ad hoc storyboard.

The scaffold must be useful on first render: it should produce the reference-style canvas and visible layout primitives even before a scene receives bespoke art direction.

## Timing

Use actual values from `timing/scenes.json`. Visual beats should align to sentence/word anchors rather than arbitrary guessed delays.
