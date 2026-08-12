# knowledge-video-builder

A staged Agent Skill for producing evidence-grounded knowledge videos about Skills, software, repositories, and workflows.

## Phases

1. Source analysis
2. Content brief
3. Narration and storyboard
4. TTS and timing
5. HyperFrames visual build
6. QA and render

Voice generation defaults to the bundled `mimo-tts` Skill. Other TTS providers are considered only when MiMo is unavailable, and the fallback must be recorded.

User-facing approvals occur at the complete narration gate and after each
completed chapter; internal analysis, brief, voice, and visual artifacts do not
create extra approval requests unless a blocking ambiguity requires one.

## Initialize a project

```bash
python scripts/project.py init ./my-project --title "My Explainer" --source ./input.skill
```

## Engineering-root network proxy and keys

Keep one `.skill.env` in the fixed engineering root—the directory containing `.cursor/skills/knowledge-video-builder`—rather than copying it into each video artifact directory. Set `SKILL_PROXY` before external source inspection, TTS, transcription, HyperFrames, or dependency downloads:

```text
SKILL_PROXY=http://xxx.xxx.xxx.xxx:xxxx
GROQ_API_KEY=your-groq-api-key
```

`GROQ_API_KEY` is required: forced alignment and candidate scoring both recognise speech through Groq's hosted `whisper-large-v3`. There is no local recogniser to install.

When this Skill is active, the proxy is required and direct fallback is disabled. Export `HTTP_PROXY`, `HTTPS_PROXY`, and `ALL_PROXY` for subprocesses such as `npx` and Playwright; those tools do not read `.skill.env` automatically. Keep the real `.skill.env` local-only and never copy it into generated video artifacts.

## Check status

```bash
python scripts/project.py status ./my-project
```

## Generate review and HyperFrames scaffold

```bash
python scripts/build_review.py ./my-project
python scripts/build_hyperframes.py ./my-project
```
