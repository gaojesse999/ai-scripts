---
name: audio-stt
description: >-
  使用 Groq Whisper (whisper-large-v3) 将音频文件批量转写为文本文件。
  支持处理单个文件或整个目录中的所有音频文件（MP3、WAV、FLAC、M4A、OGG 等格式均可）。
  结果以同名 .txt 文件保存在与音频文件相同的目录中，每个语音段落为一行。
  当用户要求「语音转文字」「转录音频」「音频转文本」「STT」「把 MP3/WAV 转成文字/文本」，
  或者提到某个音频目录需要批量识别时使用。
  具备完全独立的自包含实现，配置说明见 README.md，环境模板见 .skill.env.example。
---

# Audio STT（语音转文字）

将本地音频文件（MP3 / WAV / FLAC / M4A / MP4 等）通过 Groq Whisper-large-v3 转录为中文文本，
输出到同名 `.txt` 文件，每条语音段落占一行。

本 Skill **完全自包含**，仅依赖 Python 3.9+ 标准库与 `ffmpeg`，不依赖任何第三方 Python 包或外部 Skill。

详细独立部署与 GROQ API Key 申请说明见 [README.md](./README.md)，环境模板见 [.skill.env.example](./.skill.env.example)。

## 依赖与前置条件

1. **Groq API Key**：在工程根目录的 `.skill.env` 中配置 `GROQ_API_KEY`（免费申请地址：[https://console.groq.com/keys](https://console.groq.com/keys)）；
2. **ffmpeg / ffprobe**：系统 PATH 中可用；
3. **Python**：>= 3.9（标准库即可）。
4. **网络代理（可选）**：若访问 `api.groq.com` 受限，在 `.skill.env` 中配置 `SKILL_PROXY=http://127.0.0.1:7890`。

> 若网络请求受阻（403、URLError、超时等），**立即暂停并向用户报告进程路径、目标 URL 和具体错误**，等待用户授权。

---

## 使用方法

### 一、 单文件转录

```bash
"$PYTHON_EXE" .agents/skills/audio-stt/scripts/transcribe.py \
  --input "path/to/audio.mp3"
```

输出：`path/to/audio.txt`（与源文件同目录同名，仅扩展名替换为 `.txt`）。

### 二、 批量转录（整个目录）

```bash
"$PYTHON_EXE" .agents/skills/audio-stt/scripts/transcribe.py \
  --input-dir "path/to/mp3-folder"
```

会处理目录中所有 `.mp3 .wav .flac .m4a .ogg .opus .aac .webm .mp4` 文件，逐一生成同名 `.txt`。

### 三、 增量跳过已生成的文件

```bash
"$PYTHON_EXE" .agents/skills/audio-stt/scripts/transcribe.py \
  --input-dir "path/to/mp3-folder" --skip-existing
```

### 四、 指定语言（默认 `zh` 普通话）

```bash
"$PYTHON_EXE" .agents/skills/audio-stt/scripts/transcribe.py \
  --input "audio.mp3" --language en
```

---

## Agent 执行流程

1. **读取配置**：优先从工程根目录读取 `.skill.env`；
2. **确认目标**：单文件时检查存在性，目录模式时扫描符合支持格式的文件；
3. **调用脚本**：执行 [scripts/transcribe.py](./scripts/transcribe.py)；
4. **验证反馈**：确认 `.txt` 已输出，向用户展示转写状态、字数和行数；
5. **网络阻断处理**：如遇到网络异常，脚本会自动输出标准阻断诊断并退出，Agent 暂停任务并通知用户。
