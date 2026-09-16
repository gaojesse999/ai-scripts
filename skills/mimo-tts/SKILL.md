---
name: mimo-tts
description: Generate Chinese or multilingual speech with Xiaomi MiMo V2.5 TTS, including preset voices, voice design, voice cloning, emotion, pacing, and style control. Use when the user asks to turn text into speech with MiMo, create male/female narration, choose an emotional voice, or synthesize audio from a script.
disable-model-invocation: true
---

<!--
════════════════════════════════════════════════════════════════════════
 内部配置 · INTERNAL CONFIG · 请勿对外暴露 / DO NOT EXPOSE
════════════════════════════════════════════════════════════════════════
 本 Skill 的全部配置项集中在工程根（ENGINEERING_ROOT）的 `.skill.env` 里，
 模板见本 Skill 目录下的 `.skill.env.example`。迁移 / 换机器时**只改那个文件**。
 All settings for this Skill live in `<ENGINEERING_ROOT>/.skill.env`; the template
 is this Skill's sibling `.skill.env.example`. Port or re-host by editing that file only.

     SKILLS_ROOT = 工程级 Skill 目录（相对 ENGINEERING_ROOT 的路径）。
                   默认 .workbuddy/skills —— 即 WorkBuddy 的工程级 Skill 目录
                   （agent 侧等价路径 .codebuddy/skills，两者指向同一份文件）。
     PYTHON_EXE  = 执行本 Skill 脚本的 Python 解释器（绝对路径）。mimo_tts.py
                   只用标准库，但调用方（knowledge-video-builder）的脚本需要
                   numpy，为保持一致请指向同一个解释器。留空则依次回退到
                   启动脚本的解释器（sys.executable）与 PATH 上的 python3。

 本 Skill 位于：
     <ENGINEERING_ROOT>/<SKILLS_ROOT>/mimo-tts

 下文出现的 $SKILLS_ROOT / $PYTHON_EXE 均指上述两项。它们的值从 `.skill.env`
 读取；随附脚本会自行读取该文件，通常无需手工设置。读 `.skill.env` 时不要
 打印其中的 API key 或代理凭据。

 迁移示例 / migration（改 `.skill.env` 的 SKILLS_ROOT 一行即可）:
     Cursor        →  SKILLS_ROOT=.cursor/skills
     Claude Code   →  SKILLS_ROOT=.claude/skills
     Codex         →  SKILLS_ROOT=.codex/skills
 PYTHON_EXE 与 agent 无关，只跟机器有关：换机器时改成该机器上装了 numpy 的
 解释器绝对路径即可（conda env、venv 或系统 Python 都行）。
════════════════════════════════════════════════════════════════════════
-->

# MiMo TTS

Use the bundled script to synthesize WAV audio through the official MiMo API:

`https://mimo.mi.com/docs/zh-CN/quick-start/usage-guide/audio/speech-synthesis-v2.5`

## Credential policy

- Never ask the user to paste an API key into chat.
- Read `MIMO_API_KEY` from the environment or the `.skill.env` path supplied by the caller.
- `.skill.env` is local-only and must remain ignored by Git.
- Never print, expose, or include the key in manifests, logs, generated files, or responses.

Expected local configuration:

```text
# When called by knowledge-video-builder, this file is the fixed engineering-root
# .skill.env passed through --env-file, never the video artifact directory.
MIMO_API_KEY=replace-with-your-key
# Optional. Leave empty or omit for direct connection.
# Example: SKILL_PROXY=http://10.0.0.1:8080
SKILL_PROXY=
# Optional. Leave empty for standard MiMo synthesis.
# Relative paths are resolved from the project root.
# Example: MIMO_REFERENCE_VOICE=reference-voice/my-teacher-voice.wav
# Example: MIMO_REFERENCE_VOICE=reference-voice/female-narrator.mp3
MIMO_REFERENCE_VOICE=
```

Proxy behavior:

- Read `SKILL_PROXY` from the `.skill.env` supplied by the caller. The legacy `MIMO_PROXY` environment variable is accepted only as a compatibility fallback.
- If `SKILL_PROXY` contains a real proxy URL, try HTTP and HTTPS requests through it first.
- If `SKILL_PROXY_STRICT=1`, do not retry directly when the proxied request fails; report the proxy failure.
- Without `SKILL_PROXY_STRICT=1`, retain the standalone fallback behavior and retry directly after a proxy failure.
- If `SKILL_PROXY` is absent or empty, use a direct connection.
- `http://xxx.xxx.xxx.xxx:xxxx` is only a template placeholder and must be replaced or removed.
- If the direct connection also fails, tell the user that network restrictions may require setting `SKILL_PROXY` in the project-root `.skill.env`.
- Never expose the proxy credential, API key, or hidden environment values in output.

When invoked by `knowledge-video-builder`, the caller should set:

```text
SKILL_PROJECT_ROOT=<fixed engineering root>
# 1 only when the engineering-root .skill.env defines a non-empty SKILL_PROXY;
# 0 (or unset) makes an empty SKILL_PROXY mean a direct connection.
SKILL_PROXY_STRICT=${SKILL_PROXY:+1}
```

and pass `--env-file <engineering-root>/.skill.env`. This keeps relative
`MIMO_REFERENCE_VOICE` paths and proxy policy tied to the engineering root even
when the video artifact directory changes.

## Workflow

1. Confirm the text source (`--text`, `--input`, or supplied content).
2. Use automatic model selection unless the user explicitly chooses a model:
   - empty `MIMO_REFERENCE_VOICE` → `mimo-v2.5-tts`;
   - configured `MIMO_REFERENCE_VOICE` → `mimo-v2.5-tts-voiceclone`.
   A command-line `--voice-sample` overrides the environment setting. An explicit
   `--model` overrides automatic selection.
3. Choose or confirm the style:
   - `mimo-v2.5-tts`: preset voices; default to `mimo_default` if unspecified.
   - `mimo-v2.5-tts-voicedesign`: describe a new voice in `--instruction`.
   - `mimo-v2.5-tts-voiceclone`: provide an authorized `.mp3` or `.wav` sample with `--voice-sample`.
4. Ask for or infer voice, gender, emotion, pacing, and other style requirements. Do not silently invent a strong emotional direction.
5. Run `scripts/mimo_tts.py`.
6. Verify the returned WAV exists and report its exact path.

The script creates:

```text
audio-outputs/<semantic-title>-YYYYMMDD-HHMMSS/
├── narration.wav
├── segments/
└── tts-manifest.json
```

The semantic title is extracted from the first line/sentence unless `--title` is supplied.
When the input contains `## S01 · ...`-style headings, the script removes those
headings, synthesizes each slide body separately, and inserts 1 second of silence
between segments by default. Set `--pause` to change it; use `--pause 0` to disable
the pauses. Long slide bodies are further split at sentence boundaries to prevent
single requests from being truncated. The manifest records each segment and duration.

## Commands

Preset male voice:

```bash
"$PYTHON_EXE" "$SKILLS_ROOT/mimo-tts/scripts/mimo_tts.py" \
  --input script.txt \
  --voice 苏打 \
  --pause 1.0 \
  --instruction "男声，沉稳、清晰，语速适中，适合知识讲解"
```

Preset female voice:

```bash
"$PYTHON_EXE" "$SKILLS_ROOT/mimo-tts/scripts/mimo_tts.py" \
  --text "待合成文字" \
  --voice 冰糖 \
  --instruction "女声，温柔自然，带有轻微的亲切感"
```

Voice design:

```bash
"$PYTHON_EXE" "$SKILLS_ROOT/mimo-tts/scripts/mimo_tts.py" \
  --model mimo-v2.5-tts-voicedesign \
  --input script.txt \
  --instruction "年轻女性，声音清亮温暖，语速适中，像专业播客主持人"
```

Voice cloning:

```bash
"$PYTHON_EXE" "$SKILLS_ROOT/mimo-tts/scripts/mimo_tts.py" \
  --model mimo-v2.5-tts-voiceclone \
  --input script.txt \
  --voice-sample voice.wav \
  --instruction "自然、沉稳、清晰，适合知识讲解"
```

Automatic clone from `.skill.env`:

```text
MIMO_REFERENCE_VOICE=reference-voice/voice.wav
```

Then run without `--model` or `--voice-sample`:

```bash
"$PYTHON_EXE" "$SKILLS_ROOT/mimo-tts/scripts/mimo_tts.py" \
  --input script.md \
  --instruction "沉稳、清晰，适合教程讲解"
```

## API-specific rules

- Target narration belongs in an `assistant` message, not a `user` message.
- Natural-language style instructions belong in a `user` message.
- `mimo-v2.5-tts-voicedesign` requires the voice description in the `user` message.
- The script uses non-streaming WAV output for a simple, complete first workflow.
- Do not claim audio quality or pronunciation has been reviewed unless the file was actually inspected or played.
