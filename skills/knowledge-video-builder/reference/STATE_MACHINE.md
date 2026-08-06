# State Machine

## Phase order

```text
analysis → brief → script → voice → visual → render
```

Each phase has one of these states:

- `not_started`
- `in_progress`
- `pending_review`
- `approved`
- `needs_revision`
- `blocked`
- `invalidated`

The phase states remain useful for artifact bookkeeping, but they are not all user-facing approval gates.

## User-facing gates

Use two default gates:

1. **Full narration gate:** analysis, brief, and script are prepared internally and presented together as the complete narration plus chapter map. User approval unlocks production.
2. **Chapter gate:** voice, visual, render, and QA are executed as one loop for the current chapter. User approval of that chapter unlocks the next chapter.

If the user explicitly selects batch mode, run all chapter loops after the full narration gate and request one final review.

## Normal transition

```text
not_started → in_progress → pending_review → approved
```

A user revision changes `pending_review` or `approved` to `needs_revision`. When editing begins, set it back to `in_progress`, then `pending_review`.

## Approval behavior

Approval must:

1. verify required artifacts exist;
2. store approval time and note;
3. store artifact hashes when possible;
4. mark the next phase `not_started` if it was previously blocked;
5. never automatically execute the next user-facing gate.

## Rollback and invalidation

Rolling back to phase X:

- preserves source files;
- marks X `needs_revision`;
- marks all downstream phases `invalidated`;
- keeps old outputs for traceability, but they must not be used as current artifacts.

## Dependency table

| Internal phase | Requires | Primary output | User gate |
|---|---|---|---|
| analysis | source files | `analysis/evidence-map.json` | — |
| brief | source analysis | `content/content-brief.md` | — |
| script | analysis + brief | `script/scene-plan.json` | full narration gate |
| voice | approved narration, current chapter | `audio/narration.wav`, `timing/scenes.json` | — |
| visual | current chapter voice/timing | `review/storyboard.html`, `hyperframes/index.html` | — |
| render | current chapter visual | `qa/report.md`, chapter video | chapter gate |

## Resume behavior

When the user says “continue”, “resume”, or references a prior project:

1. read `project-state.json`;
2. report current phase and outstanding review;
3. continue only the active phase;
4. if status is `pending_review`, determine whether it is the full narration gate or a chapter gate; request approval/revision only for those gates, otherwise continue the current internal loop.
