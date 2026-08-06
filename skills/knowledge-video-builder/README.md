# knowledge-video-builder

A staged Agent Skill for producing evidence-grounded knowledge videos about Skills, software, repositories, and workflows.

## Phases

1. Source analysis
2. Content brief
3. Narration and storyboard
4. TTS and timing
5. HyperFrames visual build
6. QA and render

Every phase stops for explicit user approval.

## Initialize a project

```bash
python scripts/project.py init ./my-project --title "My Explainer" --source ./input.skill
```

## Check status

```bash
python scripts/project.py status ./my-project
```

## Generate review and HyperFrames scaffold

```bash
python scripts/build_review.py ./my-project
python scripts/build_hyperframes.py ./my-project
```
