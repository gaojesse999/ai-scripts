# knowledge-video-builder

A staged Agent Skill for producing evidence-grounded knowledge videos about Skills, software, repositories, and workflows.

## Phases

1. Source analysis
2. Content brief
3. Narration article (3A), then visual derivation (3B)
4. TTS and timing
5. HyperFrames visual build
6. QA and render

Voice generation defaults to the bundled `mimo-tts` Skill. Other TTS providers are considered only when MiMo is unavailable, and the fallback must be recorded.

User-facing approvals occur at the narration gate and after each completed
chapter; internal analysis, brief, voice, and visual artifacts do not create
extra approval requests unless a blocking ambiguity requires one.

`script/SCRIPT.md` is the only authority for spoken text. Everything downstream
is derived from it, so a wording change is one file edit plus one command
instead of three hand-synced copies.

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

## Derive artifacts from the approved narration

Once `script/SCRIPT.md` is approved, derive `timing/chapters.json` and the
narration side of `script/scene-plan.json`. The first command is a dry run that
reports the segment ids, any unit ids whose words changed, and the pauses and
motion anchors that point at them:

```bash
python3 scripts/derive_script_artifacts.py --project ./my-project
python3 scripts/derive_script_artifacts.py --project ./my-project --write
```

Re-run it after every later narration edit. Chapters whose text did not change
keep their measured timing; a chapter that is already recorded and no longer
matches needs `--force` to confirm the re-record.

## Produce voice and measured timing

`timing/chapters.json` must exist first. Then plan the requests, review the
plan, and generate:

```bash
python3 scripts/produce_voice.py --project ./my-project
python3 scripts/produce_voice.py --project ./my-project --generate
```

`--generate` runs candidate selection, normalization, merge, structured pauses,
final alignment, timing rebuild, and the sync gate. The same steps are available
individually for debugging a single chapter:

```bash
python3 scripts/align_audio.py  --project ./my-project
python3 scripts/build_timing.py --project ./my-project
python3 scripts/apply_timing.py --project ./my-project
python3 scripts/check_sync.py   --project ./my-project
```

## Generate review and HyperFrames scaffold

```bash
python scripts/build_review.py ./my-project
python scripts/build_hyperframes.py ./my-project
```

The scaffold is a starting point, not a deliverable: every scene still needs its
own art direction and the beats from `motion/motion-plan.yaml`.

## Validate and render

```bash
python scripts/validate_project.py ./my-project --phase render
python3 scripts/plan_workers.py --project ./my-project
```

Pass the recommended `--workers` value to `npx hyperframes render`; HyperFrames
sizes workers from total RAM and will happily start more Chrome processes than
the machine has free memory for.
