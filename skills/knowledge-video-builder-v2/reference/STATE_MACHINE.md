# State Machine

## Modes

- `review`: each phase needs user review before the next phase.
- `direct`: phases may be completed in one run when explicitly requested. Use `completed_unreviewed`, never fake `approved`.

## Phases

`analysis → brief → script → voice → motion → visual → render`

## Statuses

- pending
- in_progress
- completed_unreviewed
- approved
- revision_required
- invalidated
- blocked

## Invalidation matrix

| Change | Invalidate |
|---|---|
| source | all downstream |
| thesis/claims/audience | brief onward |
| narration | voice onward |
| pronunciation/voice delivery | affected timing, motion, visual, render |
| subtitle wording/time | subtitle-derived labels and QA; affected motion when semantic timing changes |
| motion plan | affected visual scenes and render |
| visual tokens/components | visual and render |
| codec/container | render only |

Direct mode does not remove the state machine. It removes mandatory stopping points.
