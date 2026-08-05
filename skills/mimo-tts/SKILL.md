---
name: mimo-tts
description: Generate Chinese or multilingual speech with Xiaomi MiMo V2.5 TTS, including preset voices, voice design, voice cloning, emotion, pacing, and style control. Use when the user asks to turn text into speech with MiMo, create male/female narration, choose an emotional voice, or synthesize audio from a script.
disable-model-invocation: true
---

# MiMo TTS

Use the bundled script to synthesize WAV audio through the official MiMo API:

`https://mimo.mi.com/docs/zh-CN/quick-start/usage-guide/audio/speech-synthesis-v2.5`

## Credential policy

- Never ask the user to paste an API key into chat.
- Read `MIMO_API_KEY` from the environment or the project-root `.mimo.env`.
- `.mimo.env` is local-only and must remain ignored by Git.
- Never print, expose, or include the key in manifests, logs, generated files, or responses.

Expected local configuration:

```text
MIMO_API_KEY=replace-with-your-key
# Optional. Leave empty or omit for direct connection.
MIMO_PROXY=http://xxx.xxx.xxx.xxx:xxxx
```

Proxy behavior:

- If `MIMO_PROXY` is absent or empty, use a direct connection.
- If `MIMO_PROXY` contains a real proxy URL, use it for HTTP and HTTPS requests.
- `http://xxx.xxx.xxx.xxx:xxxx` is only a template placeholder and must be replaced or removed.
- If direct connection fails, tell the user that network restrictions may require setting `MIMO_PROXY`.
- Never expose the proxy credential, API key, or hidden environment values in output.

## Workflow

1. Confirm the text source (`--text`, `--input`, or supplied content).
2. Choose a model:
   - `mimo-v2.5-tts`: preset voices; default to `mimo_default` if unspecified.
   - `mimo-v2.5-tts-voicedesign`: describe a new voice in `--instruction`.
   - `mimo-v2.5-tts-voiceclone`: provide an authorized `.mp3` or `.wav` sample with `--voice-sample`.
3. Ask for or infer voice, gender, emotion, pacing, and other style requirements. Do not silently invent a strong emotional direction.
4. Run `scripts/mimo_tts.py`.
5. Verify the returned WAV exists and report its exact path.

The script creates:

```text
audio-outputs/<semantic-title>-YYYYMMDD-HHMMSS/
├── narration.wav
└── tts-manifest.json
```

The semantic title is extracted from the first line/sentence unless `--title` is supplied.

## Commands

Preset male voice:

```bash
python .cursor/skills/mimo-tts/scripts/mimo_tts.py \
  --input script.txt \
  --voice 苏打 \
  --instruction "男声，沉稳、清晰，语速适中，适合知识讲解"
```

Preset female voice:

```bash
python .cursor/skills/mimo-tts/scripts/mimo_tts.py \
  --text "待合成文字" \
  --voice 冰糖 \
  --instruction "女声，温柔自然，带有轻微的亲切感"
```

Voice design:

```bash
python .cursor/skills/mimo-tts/scripts/mimo_tts.py \
  --model mimo-v2.5-tts-voicedesign \
  --input script.txt \
  --instruction "年轻女性，声音清亮温暖，语速适中，像专业播客主持人"
```

Voice cloning:

```bash
python .cursor/skills/mimo-tts/scripts/mimo_tts.py \
  --model mimo-v2.5-tts-voiceclone \
  --input script.txt \
  --voice-sample voice.wav \
  --instruction "自然、沉稳、清晰，适合知识讲解"
```

## API-specific rules

- Target narration belongs in an `assistant` message, not a `user` message.
- Natural-language style instructions belong in a `user` message.
- `mimo-v2.5-tts-voicedesign` requires the voice description in the `user` message.
- The script uses non-streaming WAV output for a simple, complete first workflow.
- Do not claim audio quality or pronunciation has been reviewed unless the file was actually inspected or played.
