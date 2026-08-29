# KME Motion Engine

This file expands the KME motion model summarized in `SKILL.md`. The two must agree; the timing and opacity constants below are the same ones enforced by the hard rules and by `templates/style-tokens.json`.

## Architecture

`Scene → State → Attention → Semantic Motion → Renderer`

## Scene

A stable spatial/narrative canvas. Keep it alive long enough for information to accumulate.

## State

A timestamped semantic change. State is the primary timeline unit.

## Lifecycle

`hidden → introduced → active → dormant → focused → restored → removed`

Use `dormant`, not removal, when context remains relevant.

## Grammar

- reveal
- accumulate
- focus
- restore
- compare
- connect
- transform
- resolve
- summarize
- replace (rare)

## Attention

Only one dominant focus per moment. Carry that focus with an accent bar, border, or colour change rather than with a dimmer.

De-emphasise with exactly two levels, never a gradient:

- dormant context: opacity `0.32`;
- present: opacity `1.0`.

The middle band is unusable on a dark stage. On `#292b29`, text at 0.45 opacity tops out at 4.09:1 even in pure white, so no colour choice can bring it back to WCAG AA. Anything that must stay legible stays at `1.0`. For `accumulate`, keep earlier named items at full strength and mark only the newest with an accent — the set then visibly grows instead of decaying.

## Timing

- micro change: 0.12–0.24 s
- cue-bound reveal: 0.18–0.35 s, followed by a stable hold
- scene entry fade: 0.12–0.20 s
- reading hold: at least 0.8 s when possible
- summary hold: 1.0–2.5 s

Stable reading time should dominate total duration. Anchor a reveal to the spoken noun, number, name, or conclusion rather than automatically to subtitle start, and clear a stale accent once an enumeration has moved on.

## Enumeration example

```yaml
states:
  - at: 10.00
    action: reveal
    target: point_1
  - at: 11.60
    action: accumulate
    target: point_2
    keep: [point_1]
  - at: 13.20
    action: accumulate
    target: point_3
    keep: [point_1, point_2]
  - at: 15.00
    action: focus
    target: point_1
    dim: [point_2, point_3]
  - at: 17.00
    action: restore
  - at: 18.00
    action: summarize
    hold: 1.5
```
