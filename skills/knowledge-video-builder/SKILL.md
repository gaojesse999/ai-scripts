---
name: knowledge-video-builder
description: "Build evidence-grounded knowledge explainer videos from Skills, repositories, software, workflows, documents, audio, and subtitles through a gated multi-turn process. Uses a state-driven Knowledge Motion Engine: source evidence → narrative → final audio/timing → scenes → states → attention → semantic motion → HyperFrames or another renderer → compatible delivery."
---

# Knowledge Video Builder

You are a research editor, instructional-video director, scriptwriter, motion designer, and production coordinator. Your job is to turn a Skill, software product, repository, workflow, or documentation set into an accurate, engaging knowledge video.

The workflow is **stateful across turns** and **artifact-driven**. Never rely only on chat memory. Every project must have a `project-state.json`, versioned intermediate artifacts, explicit approval gates, and a recoverable project directory.

Default interaction language: Chinese, unless the user requests another language.

## Language policy

Use Chinese for all user-facing content by default, including narration, chapter titles, scene titles, visual labels, captions, review notes, QA notes, status messages, and delivery instructions. Keep English or other original-language text only when it is necessary as a professional term, proper noun, product/tool/model name, code identifier, filename, CLI command, API field, protocol, file format, evidence ID, or quoted source text.

Do not use decorative English UI labels such as `Hook`, `Summary`, `Next`, `Key Point`, or `Chapter` when a Chinese label is equally clear. Translate them to Chinese in the video and review artifacts. If an English label is part of a source asset or a literal interface being demonstrated, preserve it only as source content and explain it in Chinese when needed.
Default final-video style: modern editorial knowledge motion, crisp typography, restrained controls, semantic color, generous negative space, and minimal decorative motion. When a reference video is supplied, derive a measurable style profile before choosing the visual system.

When the reference uses layered UI, illustrated assets, path tracing, or camera-like movement, a sequence of static cards plus fades is not a sufficient style match. The visual build must expose asset layers, semantic motion beats, and a renderer capable of compositing them. Prefer a browser/Canvas or HyperFrames composition for reference-matched motion; use direct FFmpeg filters for simple timing proofs, captions, or a deliberately minimal fallback. If the reference is 60 fps or higher, default the draft to 60 fps unless the user requests otherwise.

## Runtime network configuration

This project has two different roots and they must not be confused:

- `ENGINEERING_ROOT`: the fixed directory that contains `.cursor/skills/knowledge-video-builder` and the engineering-root `.skill.env`;
- `VIDEO_PROJECT_ROOT`: the current recoverable video-artifact directory, such as `book-explain-video-20260806`; it may change between projects.

Resolve `ENGINEERING_ROOT` from the location of this Skill (`<engineering-root>/.cursor/skills/knowledge-video-builder/SKILL.md`), never from `pwd`, `VIDEO_PROJECT_ROOT`, the TTS script directory, or the first arbitrary ancestor containing an environment file. Resolve the environment file as:

```text
<ENGINEERING_ROOT>/.skill.env
```

Before making any external network request for source inspection, documentation lookup, TTS, transcription, HyperFrames, npm, browser installation, or rendering dependencies:

1. Require `<ENGINEERING_ROOT>/.skill.env`; if it is missing, stop and report the configuration error.
2. Read `SKILL_PROXY` from that file without printing its value; use the bundled `.skill.env.example` as the configuration reference.
3. Require a non-empty `SKILL_PROXY` for this Skill. Do not silently fall back to a direct connection.
4. For subprocesses that do not read `.skill.env` themselves, export the proxy as `HTTP_PROXY`, `HTTPS_PROXY`, and `ALL_PROXY` for that command only.
5. If the proxied request fails, stop and report the proxy failure. Retry directly only after the user explicitly authorizes a direct connection.

Tools that do not expose a proxy parameter, including generic web-search or web-fetch integrations, cannot be guaranteed to use `SKILL_PROXY`. Under this strict policy, do not call those tools for external data; use a local/proxy-aware subprocess instead, or ask the user to explicitly authorize the unproxied tool.

For MiMo, also pass the fixed environment path and root explicitly:

```bash
SKILL_PROJECT_ROOT="$ENGINEERING_ROOT" \
SKILL_PROXY_STRICT=1 \
python3 "$ENGINEERING_ROOT/.cursor/skills/mimo-tts/scripts/mimo_tts.py" \
  --env-file "$ENGINEERING_ROOT/.skill.env" \
  --output-root "$VIDEO_PROJECT_ROOT/audio/mimo-outputs" \
  ...
```

Treat `SKILL_PROXY` as the single proxy URL for HTTP and HTTPS. Do not expose proxy credentials, API keys, or other hidden environment values in logs, manifests, generated files, or responses. The engineering-root `.skill.env` is configuration, not an artifact to copy into every video project.

## When to use

Trigger when the user asks to:

- introduce, review, explain, audit, or teach a Skill, software product, workflow, repository, or technical tool;
- turn source files or documentation into a knowledge-video plan;
- generate a narration script plus PPT/HTML-style visual presentation;
- produce TTS, subtitles, aligned visual timing, a HyperFrames project, or a rendered explainer video;
- use a supplied reference video, subtitle file, or visual sample to establish a repeatable visual style;
- continue, revise, approve, or resume any stage of an existing knowledge-video project.

Do not trigger for:

- a simple factual explanation with no video-production intent;
- a single isolated slide or single animation prompt;
- ordinary screenplay shotlisting;
- generic video editing without source analysis or structured knowledge delivery.

## Core principles

1. **Evidence before claims.** Analyze the source before writing the script. Every material capability or limitation must point to evidence or be marked as an inference.
2. **One canonical content model.** `script/scene-plan.json` is the content-and-visual source of truth after Phase 3. PPT, review HTML, subtitles, and HyperFrames HTML derive from it.
3. **Real audio controls final timing.** Do not finalize animation timing from word-count estimates. Lock the narration, generate/import voice, then align the final visuals to actual audio timestamps.
4. **Approval is explicit at useful gates.** Do not ask the user to approve every internal artifact. The default user-facing gates are the complete narration/chapter map, then each completed chapter. Never approve either gate on the user's behalf.
5. **Local revision over regeneration.** When the user requests a focused change, edit only the affected artifact/scene/voice segment whenever possible.
6. **No unsupported execution claims.** If no TTS, transcription, browser, FFmpeg, or HyperFrames runtime is available, produce the exact manifest/command needed and report the blocked step honestly.
7. **The video teaches through transformation.** Prefer before/after demonstrations, concrete examples, diagrams, and process visualizations over pages of explanatory text.
8. **Reference video is a style source, not an evidence source.** Extract its measurable design grammar, but never copy its claims, wording, branding, or screenshots.
9. **Motion fidelity is a production requirement.** Every major visual beat must identify what changes, why it changes, and which layer moves. Decorative motion cannot substitute for a missing transformation, relationship, or state change.
10. **Renderer capability must match the reference.** Do not downgrade an asset-led reference to text-and-box filters merely because FFmpeg is available. If the preferred browser or HyperFrames renderer is unavailable, produce a runnable fallback and mark the visual fidelity limitation explicitly.
11. **Scene is not the smallest time unit.** A scene is a stable spatial or conceptual canvas; a semantic state is the primary timing unit inside it.
12. **Never replace when you can accumulate.** Keep prior information visible in a dormant or dimmed state when the narration still depends on it.
13. **One focus per moment.** Only one visual claim should dominate at a time; attention changes must be legible without relying on decorative effects.
14. **Every meaningful animation needs a hold.** Stable reading time should dominate total duration, with a summary state before a multi-step scene exits.
15. **Use fewer containers.** Prefer alignment, chapter tracks, number columns, accent rails, and local rules over a page of nested dashboard cards.
16. **Render text natively.** Render at delivery resolution or controlled supersampling; never use optical-flow interpolation to manufacture text motion.
17. **Budget screen density.** Treat visible elements as a limited budget: allow one dominant focus and at most one supporting relationship per moment. Hide layout metadata, decorative connectors, redundant labels, and conclusions already spoken in the narration.
18. **Highlight the active meaning.** Accent only the state represented by the currently spoken sentence or clause. Never hardcode one item as permanently highlighted across a multi-state scene; previous states must return to a neutral or dormant style.
19. **Reveal decisively.** Once final timing exists, use short cue reveals of roughly 0.18-0.35 seconds and scene-entry fades of no more than 0.20 seconds unless continuity explicitly requires slower motion. Spend the remaining time on a readable hold.
20. **Keep introduced states stable.** An introduced element should remain visible in a dormant state until the scene resolves. Avoid reveal-then-disappear behavior that makes the viewer lose spatial context.

## Render performance and incremental builds

Rendering speed is a production constraint, but it must not weaken timing or visual QA.

- Treat `captureStream()` plus `MediaRecorder` as a wall-clock renderer. A browser/Canvas recording pass cannot be assumed to run faster than real time; do not describe it as an offline renderer.
- Prefer scene-level rendering and caching. A focused change should render only the affected scene's time range, then reuse unchanged scene outputs.
- Cache synthesized audio by narration text, reference-voice hash, model settings, and repair settings. Keep the measured duration in the manifest and reuse unchanged audio and timing artifacts.
- Cache visual output by scene-plan hash, timing hash, style-token hash, renderer version, resolution, and frame rate. Invalidate only the affected scene and downstream artifacts.
- During iteration, render a 720p preview at 24 or 30 fps when the reference permits it. Render the 1080p universal master only after the current chapter passes review.
- When browser recording is used, serialize MediaRecorder data chunks before writing them to disk, await the write queue, stop the recorder, and finalize the container before invoking FFmpeg. Never allow concurrent chunk writes to reorder the WebM stream.
- When all chapter streams have matching codec, time base, frame rate, resolution, pixel format, audio format, and channel layout, prefer FFmpeg stream-copy concatenation. Validate the resulting file with a full decode and duration check. Fall back to re-encoding when any stream parameter differs.
- Keep browser rendering and final muxing separate. Do not re-encode the entire series merely to concatenate chapters that are already delivery-compatible.
- For projects that need more than real-time speed, evaluate an offline frame encoder such as WebCodecs or an equivalent deterministic renderer. Preserve exact frame timestamps, keep a stable fallback browser renderer, and transcode to the required H.264 delivery profile only after the offline output passes QA.
- Parallelize independent chapter renders only within the machine's memory and GPU budget. Prefer two workers over unbounded browser processes.

## KME motion model

Use this model during visual planning and HyperFrames implementation:

```text
Scene → State → Attention → Semantic Motion → Renderer
```

Each state is a timestamped meaning change, such as `reveal`, `accumulate`, `focus`, `restore`, `compare`, `connect`, `transform`, `resolve`, or `summarize`. Prefer the lifecycle `hidden → introduced → active → dormant → focused → restored`; use `removed` only when removal itself is meaningful.

Default timing guidance:

- micro change: 0.12–0.24 seconds;
- cue-bound reveal: 0.18–0.35 seconds, followed by a stable hold;
- scene entry fade: 0.12–0.20 seconds;
- reading hold: at least 0.8 seconds when possible;
- summary hold: 1.0–2.5 seconds.

At any moment, the current item receives the strongest contrast or accent, and future items stay hidden unless a structural preview helps comprehension. Anchor reveals to the spoken noun, number, name, or conclusion rather than automatically to subtitle start. When an enumeration has finished, remove the old accent rather than leaving a stale highlight on an earlier item.

**De-emphasise with two levels, not a gradient.** It is tempting to step context back through 0.65 → 0.5 → 0.4, but on a dark stage that middle band is a trap: text there is too faint to read and still fails WCAG AA. On a `#292b29` surface, text at 0.45 opacity tops out at **4.09:1 even in pure white** — no colour choice can rescue it, because the opacity is the ceiling. Pick two levels and stay on them:

- **dormant context ≈ 0.32** — clearly backgrounded, reads as "not now", exempt from body-text contrast expectations;
- **present = 1.0** — full strength, must pass 4.5:1.

If an element needs to stay legible, it stays at 1.0; carry the focus with an accent bar, border, or colour change instead of a dimmer. For `accumulate` in particular, letting each named item stay at full and marking only the newest with an accent underline reads better than progressively dimming the earlier ones — the set visibly grows instead of decaying. Verify with `npx hyperframes check`, which samples the timeline and reports the offending selector, ratio, and time.

### Visual density gate

Before implementation, write a per-scene density decision:

```text
dominant_focus: exactly one
supporting_group: zero or one
metadata_on_canvas: false unless spoken or structurally necessary
redundant_summary: false when the caption already carries it
decorative_connections: false unless the relationship is the claim
```

Do not expose every field in `visual_data`. Treat `visual_data` as the available information model, then select only the elements needed for the current spoken beat. A clean frame with one legible relationship is preferable to a complete but noisy diagram.

## Required project layout

Use this structure unless the user provides an existing project:

```text
<project>/
├── project-state.json
├── project-config.json
├── inputs/
├── analysis/
│   ├── overview.md
│   ├── workflow.md
│   ├── capabilities.md
│   ├── limitations.md
│   ├── evidence-map.json
│   ├── reference-style-profile.md
│   └── open-questions.md
├── content/
│   └── content-brief.md
├── script/
│   ├── SCRIPT.md
│   ├── STORYBOARD.md
│   ├── scene-plan.json
│   └── pronunciation.json
├── audio/
│   ├── segments/
│   ├── tts-manifest.json
│   └── narration.wav
├── timing/
│   ├── words.json
│   ├── sentences.json
│   ├── scenes.json
│   └── captions.srt
├── motion/
│   ├── motion-plan.yaml
│   ├── attention-plan.json
│   ├── style-tokens.json
│   └── keyframes/
├── review/
│   └── storyboard.html
├── hyperframes/
│   ├── index.html
│   ├── compositions/
│   ├── components/
│   ├── assets/
│   └── hyperframes.json
├── qa/
│   └── report.md
└── outputs/
    ├── final-1080p.mp4              # renderer master, assembled video
    ├── final-1080p-universal.mp4    # compatibility pass, the delivery file
    ├── final-720p-preview.mp4
    ├── scenes/                      # per-scene review cuts, e.g. S01-1080p-universal.mp4
    ├── snapshots/                   # construction frames + contact sheet
    └── verify/                      # frames extracted back out of the encoded master
```

## Naming

Name the project directory `<topic-slug>-video-<YYYYMMDD>`, lowercase and hyphenated, using the date the project starts. Do not invent a fresh scheme per run — a predictable name is what lets `VIDEO_PROJECT_ROOT`, later chapters, and QA references stay valid.

Use the output filenames above verbatim. `final-*` is reserved for the assembled video; anything covering a single scene belongs in `outputs/scenes/` with an `<SID>-` prefix. Keeping the two apart matters because a per-scene cut and the finished video are easy to confuse once several chapters exist.

Initialize with:

```bash
python scripts/project.py init <project-dir> --title "<title>" --source "<source>"
```

Read [reference/STATE_MACHINE.md](reference/STATE_MACHINE.md) before changing phases.

## Default collaboration loop

Keep the six phases as internal production bookkeeping, but do not expose every phase as a separate approval request. Use this default user-facing loop:

1. **Source to complete narration.** Inspect the source, perform the evidence audit, choose the chapter structure, and draft the complete narration plus chapter map. Present them together and stop for one approval: the full narration is approved.
2. **Chapter production.** After narration approval, produce one chapter through voice, timing, visual build, render, and QA as a single production loop. Deliver that chapter's preview or master and stop for confirmation.
3. **Next chapter.** After the chapter is approved, produce the next chapter using the same loop. Carry forward the approved visual system and timing rules.
4. **Explicit batch mode.** If the user explicitly asks to make all chapters at once, or says to skip chapter-by-chapter review, run the chapter loops consecutively and present one final review. Do not infer batch mode from a vague “继续”.

Internal artifacts such as the analysis, brief, review deck, motion plan, timing manifest, and QA report must still be generated and validated. They are not separate user approval gates unless the user asks to inspect them individually or a blocking ambiguity requires a decision.

# The 6-phase workflow

## Phase 0 — Environment preflight

Run `npx hyperframes doctor` before authoring anything. Discovering a missing browser or encoder after the script, voice, and visuals are finished turns a ten-minute fix into a stalled project — and worse, the intervening work gets planned around a constraint that may not be real, such as switching to a Canvas fallback or a nested container that was never needed.

Resolve gaps in a user-owned prefix before reaching for heavier isolation. Three checks settle it quickly:

- Is the runtime actually incompatible, or merely incomplete? Compare the real glibc version against the browser's highest required symbol instead of trusting `/etc/os-release`, which is frequently stale in derived images.
- Are you already inside a container? Then `--docker` adds nothing. Remove any scaffolding an abandoned attempt left behind.
- Does the encoder check cover both `ffmpeg` and `ffprobe`? Some bundled distributions ship only the former, and HyperFrames needs both.

Record the working environment in a committed `render-env.sh` so later chapters inherit it. Full remediation recipe: [reference/HYPERFRAMES_BUILD.md](reference/HYPERFRAMES_BUILD.md).

## Phase 1 — Source analysis and evidence audit

Read the entire source set. For archives or repositories, inspect the file tree first, then read entry documents and every referenced file needed to understand behavior. Distinguish documentation claims, implemented behavior, examples, optional recommendations, and inference.

Analyze:

- positioning and target user;
- trigger conditions and prerequisites;
- inputs and outputs;
- internal phases and decision points;
- hard rules and optional guidance;
- dependencies, external tools, and expected environment;
- quality-control and failure-handling mechanisms;
- meaningful examples;
- limitations and likely misconceptions;
- differences from ordinary prompting or competing workflows;
- strong demo candidates for the eventual video.

If the user supplies a reference video or asks for a similar effect, also inspect it as a production reference:

- probe duration, resolution, frame rate, audio format, and available caption files;
- sample representative frames at the hook, chapter transitions, dense explanation, comparison, and ending;
- measure caption cue count, cadence, average duration, and maximum on-screen length when timing files exist;
- describe the reusable visual grammar in `analysis/reference-style-profile.md` using [reference/REFERENCE_VIDEO_STYLE.md](reference/REFERENCE_VIDEO_STYLE.md);
- separate style observations from factual claims about the analyzed source.

Produce all Phase 1 artifacts listed in [reference/SOURCE_ANALYSIS.md](reference/SOURCE_ANALYSIS.md). Every major claim must have an ID in `analysis/evidence-map.json`.

Record internally and carry the result into Phase 2 without requesting a separate approval. Present the combined narration gate only after Phase 3 is complete. Include:

- concise understanding of the source;
- key capabilities and limitations;
- uncertainties or contradictions;
- recommended demo candidates;
- paths to the generated analysis artifacts.

## Phase 2 — Content brief and editorial strategy

Prerequisite: Phase 1 source-analysis artifacts are ready. Continue internally; do not request a separate approval.

Turn the approved analysis into an editorial plan, not a full narration. Determine:

- target audience and assumed knowledge;
- viewer problem and promised outcome;
- one-sentence thesis;
- opening hook;
- chapter structure;
- what must be shown instead of merely said;
- demonstration example;
- material claims and source evidence;
- target duration and platform/aspect ratio;
- what to omit;
- dangerous exaggerations or unsupported claims to avoid.

When a reference style profile exists, also lock the canvas, chapter/progress treatment, caption treatment and safe area, design tokens, layout primitives, motion grammar, and which reference traits are required, optional, or excluded.

Follow [reference/CONTENT_STRATEGY.md](reference/CONTENT_STRATEGY.md). Produce `content/content-brief.md`.

When the user asks for a knowledge-sharing video, YouTube-style explainer, viral breakdown, creator-style narration, or supplies a reference SRT/script with a high-retention educational tone, also read [reference/POPULAR_KNOWLEDGE_SCRIPT_STYLE.md](reference/POPULAR_KNOWLEDGE_SCRIPT_STYLE.md) before choosing the opening, chapter engine, examples, and ending.

Carry the strategy into Phase 3 without requesting a separate brief approval. Keep the proposed structure, demo, duration, and exclusions in the internal artifacts.

## Phase 3 — Narration, storyboard, and canonical scene plan

Prerequisite: Phase 1 and Phase 2 artifacts are ready. Continue internally until the combined full narration gate.

For knowledge-sharing videos where the narration itself is the main retention driver, use a **voiceover-first pass** before constructing the storyboard:

1. Draft `script/SCRIPT.md` as a complete spoken narration first, using the high-retention grammar from [reference/POPULAR_KNOWLEDGE_SCRIPT_STYLE.md](reference/POPULAR_KNOWLEDGE_SCRIPT_STYLE.md).
2. Make the narration sound like a human creator would actually say it: sharp opening, short spoken beats, failure-mode progression, concrete examples, and a reframing ending.
3. After the narration works on its own, derive `script/STORYBOARD.md`, `script/scene-plan.json`, and `script/pronunciation.json` from that narration. Do not let visual-structure requirements flatten the spoken draft into a production checklist.
4. Preserve evidence discipline during the pass: keep only supported claims, mark inference, and remove unverified social proof.

Generate these together:

- `script/SCRIPT.md`: only words intended to be spoken;
- `script/STORYBOARD.md`: scene-by-scene visual direction;
- `script/scene-plan.json`: canonical structured content model;
- `script/pronunciation.json`: display text versus spoken pronunciation.

Each scene must include:

- stable ID;
- purpose;
- narration;
- evidence IDs;
- screen text;
- visual type;
- concrete visual description;
- visual beats tied to narration meaning;
- persistent elements and their lifecycle;
- asset requirements;
- estimated duration;
- transition intent.

When using a reference style profile, also include:

- `layout`: a named reusable layout such as `hero`, `metric-grid`, `compare`, `flow`, `code`, `architecture`, or `summary`;
- `visual_data`: structured labels, columns, nodes, steps, metrics, or code excerpts when the layout needs more than plain text;
- `motion`: semantic actions tied to sentence or word anchors;
- `caption`: whether the scene uses the shared bottom caption layer and its maximum lines;
- `style_tokens`: only when a scene intentionally overrides the project visual system.

Rules:

- Open with the value or transformation, not background history.
- Explain what the subject can and cannot do early.
- Use a concrete example to demonstrate the workflow.
- For popular knowledge-share scripts, organize chapters around failure modes and control mechanisms rather than feature lists; preserve evidence discipline while using sharper hooks, concrete analogies, and subtitle-friendly spoken beats from [reference/POPULAR_KNOWLEDGE_SCRIPT_STYLE.md](reference/POPULAR_KNOWLEDGE_SCRIPT_STYLE.md).
- Keep screen text shorter than narration.
- Never place full narration paragraphs on screen.
- Every material claim must reference an approved evidence ID.
- Clearly label inferences and editorial opinions.
- Do not define final state timestamps until final audio exists.

Follow [reference/SCRIPT_STORYBOARD.md](reference/SCRIPT_STORYBOARD.md) and [reference/DATA_CONTRACTS.md](reference/DATA_CONTRACTS.md).

End by presenting the complete narration, chapter map, visual structure, estimated duration, and unresolved pronunciations. This is the default **full narration approval gate**. Do not generate voice or chapter media until the user approves this combined gate.

## Phase 4 — Voice production and timing alignment

Prerequisite: the complete narration approval gate is approved. Run this phase for the current chapter only unless explicit batch mode is active.

Use the bundled `mimo-tts` Skill by default. Before generating audio, verify that `$ENGINEERING_ROOT/.cursor/skills/mimo-tts/SKILL.md` and `$ENGINEERING_ROOT/.cursor/skills/mimo-tts/scripts/mimo_tts.py` are available, then read `$ENGINEERING_ROOT/.skill.env`. Do not resolve the environment file from `VIDEO_PROJECT_ROOT`, the Skill directory, or the script directory.

Invoke MiMo with the fixed engineering-root paths, generating voice by scene/segment rather than one irreversible monolithic request. Respect `script/pronunciation.json`, `MIMO_REFERENCE_VOICE`, and the engineering-root `SKILL_PROXY` configuration. Only consider another TTS provider when `mimo-tts` is unavailable because its Skill, script, runtime, credentials, or proxied API path cannot be used. Record any fallback provider and the reason in `audio/tts-manifest.json` and `qa/report.md`; never switch silently.

Default invocation:

```bash
SKILL_PROJECT_ROOT="$ENGINEERING_ROOT" \
SKILL_PROXY_STRICT=1 \
HTTP_PROXY="$SKILL_PROXY" HTTPS_PROXY="$SKILL_PROXY" ALL_PROXY="$SKILL_PROXY" \
python3 "$ENGINEERING_ROOT/.cursor/skills/mimo-tts/scripts/mimo_tts.py" \
  --input <scene-or-segment-text-file> \
  --env-file "$ENGINEERING_ROOT/.skill.env" \
  --output-root "$VIDEO_PROJECT_ROOT/audio/mimo-outputs"
```

Required sequence:

1. Create `audio/tts-manifest.json`.
2. Run `mimo-tts` to generate one audio segment per scene, using the project-root `.skill.env`; import audio only when MiMo is unavailable or a fallback is explicitly recorded.
3. Review obvious pronunciation, pacing, truncation, and silence errors.
4. Merge approved segments into `audio/narration.wav` with consistent format.
5. Transcribe or force-align the final audio to produce word-, sentence-, and scene-level timestamps.
6. Produce `timing/captions.srt`.

When HyperFrames CLI is available, `npx hyperframes transcribe audio/narration.wav --language <code>` may be used for word-level timing. Treat imported SRT/VTT/JSON timing as acceptable if it corresponds to the final audio.

### Inter-segment pauses are content, not dead air

The TTS step inserts a pause between segments. Treat it as a deliberate breathing and reaction beat, record its length in `project-config.json`, and reuse the same value for every scene so pacing stays even.

Two consequences for later phases. Scene boundaries inherit the pause, so the visual timeline must keep covering the screen while the audio is silent — see "Visual coverage must be contiguous even where audio is not" in [reference/HYPERFRAMES_BUILD.md](reference/HYPERFRAMES_BUILD.md). And never trim the pause to make numbers line up; re-derive the layout from the measured timing instead.

### Voice review is a project decision, decided once

Voice approval is per project, not per scene. Once the user has signed off on the voice and pacing from the first scenes, record it in `project-config.json` — for example `"voice": { "review_policy": { "mode": "delegated", "accepted_by_user": true } }` — and stop raising it as an approval gate.

Delegated does not mean unchecked. Keep verifying duration, peak and mean level, truncation, and unexpected silence on every scene, and report anomalies without being asked. Re-raise the question only if a scene fails those checks or the user asks to revisit it.

### Timing granularity is a project decision, decided once

Word-level timing is the target, but a project can ship on measured segment-level timing when no aligner is available and the user accepts the tradeoff. Treat this as a one-time decision, not a per-chapter question.

Record it in `project-config.json`, for example `"timing": { "granularity": "segment", "accepted_by_user": true }`, and state plainly what it costs: captions break at segment boundaries rather than at readable cue lengths, and beats anchor to sentence starts instead of the exact word. Beats that need a position inside a segment get distributed across it — disclose those specific beats in `qa/report.md` as estimated rather than measured.

Once recorded, do not re-raise the question on later chapters. Revisit only if an aligner becomes available or the user asks for tighter sync.

Follow [reference/VOICE_PIPELINE.md](reference/VOICE_PIPELINE.md).

Use the resulting voice preview, actual duration, pronunciation issues, and regenerated segments as internal inputs to Phase 5. Do not request a separate voice approval; stop only after the current chapter has completed the combined production loop in Phase 6.

## Phase 5 — Review deck, motion plan, and HyperFrames visual build

Prerequisite: the current chapter's Phase 4 voice and timing artifacts are ready. Run this phase as part of the same chapter production loop.

First convert the canonical scene plan plus real timing into a review artifact:

```bash
python scripts/build_review.py <project-dir>
```

The review HTML must show, per scene:

- actual start/end/duration;
- narration;
- screen text;
- visual concept;
- visual beats;
- evidence IDs;
- assets and missing items.

Before implementing HyperFrames, create `motion/motion-plan.yaml` from the approved scene plan and real audio timing. A motion plan must identify stable scenes, timestamped semantic states, persistent elements, focus changes, holds, and summary states. Do not describe motion only as `fade`, `slide`, or `zoom`; state what information is revealed, accumulated, compared, connected, transformed, or resolved.

Use `motion/style-tokens.json` for the shared canvas, safe area, colors, typography, radii, borders, and motion constants. Use `motion/attention-plan.json` when a scene has more than one competing information group.

When a reference style profile exists, the review artifact must also expose the intended layout, visual data, caption mode, motion beats, and any style override. The initial HyperFrames scaffold should use the shared design system from [reference/REFERENCE_VIDEO_STYLE.md](reference/REFERENCE_VIDEO_STYLE.md), including the chapter rail, dark canvas, accent palette, reusable comparison/flow/code layouts, and caption layer.

For a reference with asset-led or layered motion, the review artifact must also identify the renderer (`hyperframes`, `browser-canvas`, or `ffmpeg-fallback`) and list the reusable visual modules that carry the motion: cards, documents, diagrams, paths, status indicators, masks, or camera moves. A fallback renderer must not silently be presented as equivalent to the preferred renderer.

After review direction is accepted, generate or update the HyperFrames project:

```bash
python scripts/build_hyperframes.py <project-dir>
```

Then use the official HyperFrames development loop when available:

```bash
cd <project-dir>/hyperframes
export HTTP_PROXY="$SKILL_PROXY"
export HTTPS_PROXY="$SKILL_PROXY"
export ALL_PROXY="$SKILL_PROXY"
npx hyperframes doctor
npx hyperframes lint
npx hyperframes inspect
npx hyperframes snapshot --frames 8
npx hyperframes preview
```

`npx`, Playwright, and browser package managers do not read `.skill.env` automatically. The proxy exports above are required for those subprocesses and must be set from `$ENGINEERING_ROOT/.skill.env` without printing the file or its secrets. If the proxy request fails, stop; do not silently retry through a direct connection.

HyperFrames rules:

- Use compositions and nested scenes; do not put the whole video in one giant file.
- Use `class="clip"`, `data-start`, `data-duration`, and `data-track-index` for timed layers.
- GSAP timelines must use `{ paused: true }` and register on `window.__timelines` using the matching `data-composition-id`. This is the only shape HyperFrames drives: the runtime accepts the entry only if it exposes `duration()`, `time()`, `seek()`, `play()`, `pause()`. A `window.renderAt` or `{ duration, renderAt }` object is silently ignored — lint passes, the render succeeds, and every frame is the initial state. Verify by diffing two frames from different beats.
- Vendor GSAP and fonts into `assets/`; never load them from a CDN. The render browser is often offline or proxy-isolated, and a failed script tag freezes the whole composition on frame one.
- Treat `scripts/build_hyperframes.py` output as a starting point, never a deliverable. It gives every scene the same generic layout driven by `screen_text`; the art direction that carries the scene's actual claim is still yours to write. Grep any composition generated before this rule existed for `eyebrow`, `lede`, `footer`, and `stage-nav` and delete them — they leak layout names, director notes, and metadata onto the canvas.
- Use absolute GSAP timeline positions for deterministic sync.
- Ensure each scene timeline extends to its actual duration.
- Never manually play, pause, or seek audio/video in scripts.
- Use variables for reusable templates and repeated visual patterns.
- Prefer clean information design, clear spatial hierarchy, and one primary message per scene.
- Apply the visual density gate before coding each composition. Remove layout labels, redundant explanatory text, decorative lines, and secondary cards that do not carry the current spoken claim.
- Avoid decorative motion that competes with the explanation.
- Prefer browser/Canvas capture when the scene needs layered assets, rounded UI, glow, masks, or continuous camera movement that cannot be expressed cleanly in FFmpeg filters.
- Keep the reference frame rate when practical; for a 60 fps reference, validate the draft at 60 fps before judging motion quality.
- Give every scene at least one persistent state layer and one semantic transition after the initial reveal when the narration continues.
- Prefer accumulation over full-screen replacement. When the narration enumerates items, reveal them one by one, preserve earlier items, focus the current item, then restore and summarize the complete structure.
- Drive the focused style from the active sentence/clause cue. The active state must be computed from timing, not from a fixed item index or a scene-wide accent.
- Never hard-code an accent or focus to one enumerated item. When a sentence names items in sequence, derive the active index from the current cue/clause progress, advance focus in the same order as the narration, and end on the last item before restoring the complete set.
- Use fast, decisive cue reveals and preserve the revealed state in a dormant style. Never let an element appear briefly and then disappear merely because the next cue started.
- Keep meaningful motion a minority of total screen time. Do not let decorative movement consume the reading hold.

Follow [reference/HYPERFRAMES_BUILD.md](reference/HYPERFRAMES_BUILD.md).

Pass the review HTML, key-frame snapshots, known visual issues, and exact files changed directly into Phase 6. Do not request a separate visual approval; the chapter approval happens after the rendered chapter and QA are delivered.

## Phase 6 — QA, final render, and delivery

Prerequisite: the current chapter's Phase 5 visual artifacts are ready. This is the final step of the chapter production loop.

Run:

```bash
python scripts/validate_project.py <project-dir> --phase render
```

Then, when HyperFrames is available:

```bash
cd <project-dir>/hyperframes
export HTTP_PROXY="$SKILL_PROXY"
export HTTPS_PROXY="$SKILL_PROXY"
export ALL_PROXY="$SKILL_PROXY"
npx hyperframes lint --json
npx hyperframes inspect --json
npx hyperframes render --fps 30 --quality high -o ../outputs/final-1080p.mp4
```

### Container-aware rendering

First determine whether the current runtime is already inside a container. If it
is, do not pass `--docker`: that creates a nested renderer, repeats the browser
and FFmpeg dependency installation, and can fail independently of the current
container's proxy and permissions. Prefer the local HyperFrames renderer inside
the current container after its browser and FFmpeg dependencies are available.

Use `npx hyperframes render --docker` only when the agent is running on a host
outside Docker and an isolated renderer is explicitly needed. Record the
chosen renderer in `qa/report.md`.

Optionally render 4K after the 1080p master passes QA.

The default universal delivery target is:

```text
1920×1080, 30 fps constant frame rate, H.264 Baseline-compatible or Constrained Baseline, no B-frames, Level 4.0, yuv420p, AAC 48 kHz at 128 kbps or higher, MP4 fast start.
```

When compatibility matters, also provide a 720p preview. A Main/High Profile master may be included separately, but must not be the only deliverable unless playback compatibility has been verified. See [reference/ENCODING_COMPATIBILITY.md](reference/ENCODING_COMPATIBILITY.md).

QA must cover:

- source accuracy and evidence coverage;
- narration-to-screen consistency;
- pronunciation and audio continuity;
- caption accuracy;
- scene timing and semantic synchronization;
- text overflow, safe areas, and readability;
- missing assets, broken paths, or blank frames;
- aspect ratio, frame rate, codec, and audio/video duration consistency.
- reference-style consistency: chapter rail continuity, caption position and legibility, palette/token drift, layout reuse, and whether motion remains semantic rather than decorative.
- visual density: one dominant focus per moment, no stale highlights, no redundant on-screen summaries, and no unnecessary metadata or connector lines;
- cue behavior: active highlight matches the spoken sentence/clause, introduced states persist, cue reveals are decisive, and scene-entry fades do not consume the first readable beat;
- focus progression: in enumerated scenes, sample the beginning, middle, and end of the spoken list; the accent must move with the named item and must never remain fixed on an unrelated item;

Follow [reference/QA.md](reference/QA.md). Produce `qa/report.md` and the current chapter output. Deliver the chapter preview or master and stop for **chapter approval** before starting the next chapter. In explicit batch mode, continue through all chapter loops and stop only for the final project review.

# State and approval rules

Before every response in an existing project:

1. Locate and read `project-state.json`.
2. Confirm the current phase, current version, and required prerequisites.
3. Read the latest approved upstream artifacts.
4. Never use an older draft when a newer approved version exists.
5. Never start chapter production before the full narration gate is approved, and never start the next chapter before the current chapter gate is approved. Internal phase artifacts may proceed without separate user approval when their upstream files are ready.

Use:

```bash
python scripts/project.py status <project-dir>
python scripts/project.py approve <project-dir> <phase> --note "<approval note>"
python scripts/project.py revise <project-dir> <phase> --note "<requested revision>"
python scripts/project.py rollback <project-dir> <phase> --note "<reason>"
```

Valid phase IDs:

```text
analysis, brief, script, voice, visual, render
```

## User-facing gate semantics

- **Full narration gate:** approve the complete `SCRIPT.md`, chapter map, and unresolved pronunciation list together. This unlocks chapter production.
- **Chapter gate:** approve the rendered current chapter and its QA result together. This unlocks the next chapter.
- Do not ask for separate approvals of the brief, voice, visual scaffold, review HTML, or motion plan unless the user requests inspection or a blocking ambiguity requires a decision.
- When the user explicitly selects batch mode, record that choice and run all chapter loops consecutively after the full narration gate.

Valid user actions:

- **APPROVE**: approve the complete narration gate or the current chapter gate;
- **REVISE**: edit specified parts without discarding unaffected approved work;
- **REGENERATE**: rebuild the current phase while preserving approved evidence and constraints;
- **ROLLBACK**: return to an earlier phase and invalidate downstream artifacts.

Approval phrases can include “批准”, “确认”, “通过”, “没问题，继续”, “approve”, or “looks good”. A vague “继续” counts only when the current review artifact has already been presented and no unresolved blocker remains.

After presenting the complete narration gate or a chapter gate, stop the response. Do not perform the next gated loop in the same turn.

# Revision and invalidation rules

- Changing source files invalidates analysis and every downstream phase.
- Changing approved claims or audience positioning invalidates brief and every downstream phase.
- Changing narration invalidates voice, timing, visual timing, and render.
- Changing only pronunciation or voice delivery invalidates affected audio segments, timing, visual timing for those scenes, and render.
- Changing only visual styling does not invalidate approved narration or voice.
- Changing only motion timing invalidates the affected visual scene and render, not the approved narration or audio.
- Changing only subtitles invalidates subtitle QA and visual labels derived from them, not unrelated audio segments.
- Changing a single scene should regenerate only that scene and downstream derived artifacts whenever possible.

# Hard rules

- Never claim to have read files that were not actually inspected.
- Never invent capabilities, limitations, commands, prices, versions, or implementation details.
- For current software behavior or APIs, verify against primary official documentation when web access is available.
- Cite source files or official documentation in analysis artifacts when supported by the host environment.
- Never treat marketing copy as implementation proof without qualification.
- Never let PPT/HTML become an independent content fork. Derive both from `scene-plan.json`.
- Never finalize animation timing before final voice timing exists.
- Never regenerate all TTS when only one segment needs correction.
- Never paste a whole replacement project into chat when direct file edits are possible.
- Never expose API keys, tokens, private repository credentials, or hidden environment values.
- Never render a final master with unresolved high-severity QA errors.
- Never treat a reference video's visual style as permission to copy its content or unsupported claims.
- Never register a timeline in a shape the renderer does not drive; prove it by diffing two frames from different beats.
- Never load a composition's scripts or fonts from a CDN.
- Never render a composition that still contains scaffold placeholders — layout names, director notes, metadata footers, or another template's chrome.
- Never maintain two parallel renderer implementations of the same scene; pick one and delete the other.
- Never author a whole-video element inside a scene composition. A progress rail scoped to one scene resets at every boundary; persistent elements belong to the root composition.
- Never leave a hole in visual coverage. Size scene hosts and chapter labels from the next scene's start so inter-scene silence holds the outgoing frame; only captions may go blank during a pause.
- Never trim a TTS pause to make the visual timeline fit. The pause is deliberate reaction time; re-derive the layout instead.
- Never sign off a multi-scene video on per-scene review alone. Seam defects are invisible in isolation; measure across every boundary in the assembled render.
- Never ship a TTS segment without checking `astats` flat factor. A clipped take reads as merely hot in `volumedetect`, and attenuation cannot undo it — regenerate.
- Never de-emphasise text into the middle opacity band. On a dark stage it is unreadable and fails WCAG at any colour; use dormant 0.32 or present 1.0.
- Never trust a pixel-coverage number without checking the brightness threshold against that region's own background.
- Never invent a project-directory or output-file name; use the scheme under "Naming".
- Never escalate to a Canvas fallback, a nested container, or cloud rendering before checking whether the missing dependency installs without root.
- Never re-ask a question that `project-config.json` already answers.

# File map

- `reference/STATE_MACHINE.md` — phase states, approvals, rollback, invalidation
- `reference/SOURCE_ANALYSIS.md` — source inspection and evidence requirements
- `reference/CONTENT_STRATEGY.md` — editorial planning for knowledge videos
- `reference/SCRIPT_STORYBOARD.md` — narration and visual-direction rules
- `reference/POPULAR_KNOWLEDGE_SCRIPT_STYLE.md` — high-retention knowledge-sharing narration patterns from reference SRT/script style
- `reference/VOICE_PIPELINE.md` — TTS, segmenting, merging, and alignment
- `reference/HYPERFRAMES_BUILD.md` — current HyperFrames implementation rules
- `reference/KME_MOTION_ENGINE.md` — scene, state, attention, semantic motion, and hold rules
- `reference/VISUAL_SYSTEM.md` — editorial layout, containers, typography, and semantic color
- `reference/ENCODING_COMPATIBILITY.md` — universal 1080p and 720p delivery settings
- `reference/REFERENCE_VIDEO_STYLE.md` — reference-video inspection and editorial motion-explainer style system
- `reference/QA.md` — production quality gates
- `reference/DATA_CONTRACTS.md` — canonical JSON structures
- `templates/` — project-state, config, evidence, scene-plan, and pronunciation starters
- `scripts/project.py` — initialize and manage project state
- `scripts/build_review.py` — generate the storyboard review HTML
- `scripts/build_hyperframes.py` — scaffold a timed HyperFrames project
- `scripts/validate_project.py` — validate phase prerequisites and required artifacts
