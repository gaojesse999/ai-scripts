# KME Motion Engine

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

Current focus is strongest. Previous context remains at roughly 40–65% visual strength. Only one dominant focus per moment.

## Timing

- micro: 0.18–0.40 s
- reveal: 0.35–0.65 s
- hold: at least 0.8 s when possible
- summary: 1.0–2.5 s

Stable reading time should dominate total duration.

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
