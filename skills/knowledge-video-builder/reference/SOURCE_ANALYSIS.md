# Source Analysis

## Inspection order

1. Inventory the full source tree.
2. Identify entry documents, manifests, package metadata, and referenced files.
3. Read the entry document completely.
4. Follow references needed to understand behavior.
5. Inspect examples and templates separately from normative instructions.
6. Record unresolved contradictions.

## Required artifacts

### `analysis/overview.md`

- What it is
- Who it is for
- What problem it solves
- High-level workflow
- One-paragraph verdict

### `analysis/workflow.md`

- Trigger and prerequisites
- Phase-by-phase behavior
- Approval or human-input gates
- External tool calls
- Output files
- Failure and recovery behavior

### `analysis/capabilities.md`

Use a table:

| Capability | Evidence ID | Confidence | Notes |
|---|---|---:|---|

### `analysis/limitations.md`

Separate:

- explicit limitations;
- implied limitations;
- environment dependencies;
- likely user misconceptions;
- unsupported marketing interpretations.

### `analysis/evidence-map.json`

Every material claim must have:

```json
{
  "id": "C001",
  "claim": "The workflow stops after the asset request.",
  "kind": "implemented_rule",
  "source": "SKILL.md",
  "location": "Phase 2",
  "quote_or_summary": "Stop and wait for uploaded images.",
  "confidence": "high"
}
```

Allowed `kind` values:

- `implemented_rule`
- `documented_capability`
- `example_only`
- `recommendation`
- `limitation`
- `inference`
- `contradiction`

Do not use an inference as a factual narration claim unless visibly qualified.

## Demo selection

A strong demo:

- exposes the subject's unique mechanism;
- creates a visible before/after transformation;
- is understandable without excessive domain background;
- can be completed within the target video duration;
- demonstrates both capability and boundary.
