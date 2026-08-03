# Data Contracts

## scene-plan.json

Each scene contains:

- id
- purpose
- narration
- evidence_ids
- screen_text
- visual_template
- persistent_elements
- semantic_beats
- assets
- transition_intent

## motion-plan.yaml

Top-level:

- version
- engine
- mode
- source
- delivery
- scenes
- principles

Each state contains:

- at
- action
- target
- keep
- dim
- restore
- hold
- narration_anchor
- subtitle_id

## attention-plan.json

Each timed range may define primary, supporting, dormant, hidden, and restore targets.
