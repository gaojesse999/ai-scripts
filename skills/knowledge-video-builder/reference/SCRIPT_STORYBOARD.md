# Script and Storyboard

## Two passes, one gate

Narration and storyboard are written in separate passes. Phase 3A produces
`script/SCRIPT.md` alone and stops for the narration gate; Phase 3B derives the
machine-readable artifacts and adds the visual direction. Writing both at once
means every wording change drags a full visualisation pass behind it, and
narration is the part that gets rewritten most.

A paragraph boundary in `SCRIPT.md` is a scene boundary — scene ids come from
segment ids, and both renderers match scenes to timing by id. So re-splitting
paragraphs is free before audio exists and costs a re-record afterwards. Review
the split as the first step of Phase 3B, not later. Do not invent sub-scene ids
such as `S31a` to work around it; that forks scene ids from timing ids and
breaks the matching both renderers rely on.

## Narration rules

- 口语, not written prose — short sentences, clear causal transitions, and grammar that still parses when heard once. See [Voice And Sentence Rhythm](POPULAR_KNOWLEDGE_SCRIPT_STYLE.md#voice-and-sentence-rhythm).
- Lead with the concrete result.
- Define technical terms at first meaningful use.
- State boundaries early.
- Do not read long field lists aloud; summarize and let the visual carry structure.
- Keep examples specific enough to demonstrate decisions.
- Mark optional personal remarks separately from factual explanation.

## Storyboard rules

Every narration paragraph needs a visible purpose. Choose one:

- prove;
- compare;
- transform;
- locate;
- demonstrate;
- summarize;
- transition.

Avoid generic instructions such as “show some icons” or “add animation”. Specify what changes, where, when, and why.

Bad:

```text
Show the workflow with a cool animation.
```

Good:

```text
A single source archive enters from the left. It splits into six evidence cards. Only verified cards continue into the content brief; one unsupported claim falls into a red “excluded” lane.
```

## Scene plan minimum fields

`id`, `chapter`, and `narration` are written by
`scripts/derive_script_artifacts.py`. Everything else is hand-authored art
direction, and the script never touches it. Change wording in `SCRIPT.md` and
re-derive; editing `narration` here makes the scene plan disagree with what is
actually spoken.

```json
{
  "id": "S01",
  "chapter": "开场",
  "purpose": "展示转变",
  "narration": "...",
  "evidence_ids": ["C001"],
  "screen_text": ["来源", "证据", "视频"],
  "visual_type": "transformation",
  "visual_description": "...",
  "visual_beats": [
    {"anchor": "sentence:1", "action": "show-source"}
  ],
  "assets": [],
  "estimated_duration": 8.0,
  "transition": "hard-cut"
}
```

## Screen text

- Use labels, conclusions, and contrasts.
- Prefer 2–8 words per item.
- Avoid duplicating the narration verbatim.
- Keep key text inside a 10% safe margin.
- Chinese body text should generally remain large enough for mobile viewing.

## Reference-style scene composition

When a reference style profile exists, the storyboard must name a reusable `layout` for every scene and keep the explanation inside a stable design system.

- `hero` carries one claim, result, or metric.
- `metric-grid` carries two to four proof points.
- `compare` places opposing states side by side and ends with a visible verdict.
- `flow` shows a sequence from left to right; the active step is traced from the narration.
- `code` pairs a short excerpt with the behavior or risk it explains.
- `architecture` shows nodes and relationships with one highlighted path.
- `summary` closes with before/after, problem/solution, or tool-selection logic.

Use `visual_data` for the structure. Do not hide columns, nodes, or steps inside a long `visual_description` string. Use a shared bottom caption layer for narration subtitles and keep explanatory screen text shorter than the caption.

Default semantic motion vocabulary: `reveal`, `rise`, `draw`, `trace`, `fill`, `compare`, `focus`, `collapse`, and `resolve`. Each motion must have a sentence or word anchor and a reason tied to the idea being taught.
