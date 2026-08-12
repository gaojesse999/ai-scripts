# Content Strategy

## Required brief sections

1. Video objective
2. Target audience
3. Viewer problem
4. One-sentence thesis
5. Opening hook
6. What it can do
7. What it cannot do
8. Narrative structure
9. Demonstration plan
10. Required evidence IDs
11. Material to omit
12. Target length and format
13. Visual language
14. Risky or prohibited claims

## Knowledge-video structure

The default structure for a Chinese knowledge explainer is five **stages**:

```text
解决什么问题 → 原理 → 怎么做 → 举例 → 总结
```

| Stage | Label | Job |
|---|---|---|
| 1 | 解决什么问题 | State the promise in one sentence, name the viewer's pain in two, then cut to the content. |
| 2 | 原理 | Explain the mechanism as failure modes plus the principle that fixes each one. |
| 3 | 怎么做 | Give the concrete procedure or tool: what you feed it, what it returns, how it iterates. |
| 4 | 举例 | Walk one real end-to-end case, ideally first draft → feedback → revised draft. |
| 5 | 总结 | Restate the loop, land one memorable line, then the call to action. |

Stage rules:

- Stage 1 opens with the promise, not with history, definitions, apologies, or how the tool was installed. Follow it immediately with the pain and a short "here's the substance" pivot.
- Stage 2 pairs each failure mode with exactly one principle. Do not list principles abstractly and explain them later.
- Stage 3 must be executable: named inputs, named outputs, and the revision loop. If the subject is a tool the author wrote, say so plainly in the first person.
- Stage 4 uses one case, carried all the way through. Do not sample three shallow cases.
- Stage 5 ends on reframing plus a single ask. Do not summarize every branch already spoken.
- Cite a book, paper, or brand only when the user asks for it. Teach the mechanism on its own terms.

**Stages are not slides.** Do not allocate one scene per stage by reflex. Split by content volume:

- A stage carrying one claim is one scene.
- A stage enumerating N parallel items is one scene with N accumulate states, or N scenes when each item needs its own layout.
- A stage longer than roughly 90 seconds of narration is split, because a single scene that long cannot hold one dominant focus.

Number chapters `S01…S0N` by stage, and scenes inside a stage `S11, S12…`. Keep the stage label visible in the chapter rail so the viewer always knows which of the five they are in.

Adapt or drop stages when the subject genuinely does not have them — a pure news explainer may have no 怎么做 — but state the deviation in `content/content-brief.md` rather than silently reshaping the video.

## Duration guidance

- 60–90 s: one insight and one demo
- 2–4 min: practical overview and compact example
- 5–10 min: deep tutorial with workflow and edge cases
- 10+ min: chaptered course; consider multiple videos

Do not inflate duration to fit every source detail. Place secondary detail in companion documentation.

## Visual planning

Assign each chapter a dominant visual grammar:

- transformation;
- comparison;
- flow diagram;
- interface walkthrough;
- code/document annotation;
- timeline;
- case study;
- summary matrix.

Use one dominant message per scene.
