# audio-stt

语音转文字（Speech-to-Text）Agent Skill，基于 **Groq 托管的 Whisper-large-v3** 大模型，实现快速、精准、低成本的音频转文字。

支持单文件与目录批量转写，输出与音频同名的 `.txt` 文件，每行对应一个自然语音段落。

---

## 核心特性

- **完全自包含（Zero Extra Pip Dependencies）**：仅需 Python 3.9+ 标准库与 `ffmpeg`，**无需安装 numpy、torch 等任何臃肿的第三方 Python 包**，轻量便携；
- **极速识别**：Groq LPU 硬件加速，100 秒音频通常只需 2~4 秒即可转录完毕；
- **智能防幻觉**：内置 `no_speech_prob` 过滤机制，自动剔除静音段可能产生的重复幻觉文本；
- **大音频安全切片**：单个音频超过 24MB 时，自动在静音停顿处精准切片上传并无缝拼接；
- **网络阻断自停**：遇到网络限制或 403 阻断时立即停止，详细输出进程和目标 URL，杜绝盲目重试。

---

## 快速配置与环境要求

如果将本 Skill 独立移植到其他工程或全新环境，请确保完成以下配置：

### 1. 注册并获取 GROQ API Key（免费）

Groq 提供了非常慷慨的免费调用额度，无需绑定外币信用卡即可直接使用 Whisper-large-v3。

1. **访问官网**：打开 [Groq Cloud 控制台](https://console.groq.com/)；
2. **注册/登录**：支持使用 Google 账号、GitHub 账号或邮箱直接注册；
3. **创建 API Key**：
   - 直接访问密钥管理页面：[https://console.groq.com/keys](https://console.groq.com/keys)
   - 点击 **"Create API Key"**；
   - 输入名称（如 `audio-stt`），点击创建并**立即复制保存**（格式通常为 `gsk_...`，离开页面后将无法再次查看完整密钥）；
4. **填入配置**：将密钥填入工程根目录的 `.skill.env` 中。

---

### 2. 系统环境依赖（ffmpeg）

脚本依赖 `ffmpeg` 与 `ffprobe` 完成音频下采样（转为 16kHz mono FLAC）与静音检测。

#### 安装方式：
- **Windows**：
  ```powershell
  # 推荐使用 Windows 包管理器一键安装
  winget install Gyan.FFmpeg
  # 或使用 Chocolatey
  choco install ffmpeg
  ```
  *安装后请确保在系统环境变量 `PATH` 中能直接执行 `ffmpeg`。*
- **macOS**：
  ```bash
  brew install ffmpeg
  ```
- **Linux (Ubuntu/Debian)**：
  ```bash
  sudo apt update && sudo apt install -y ffmpeg
  ```

#### 验证安装：
```bash
ffmpeg -version
ffprobe -version
```

---

### 3. 创建 `.skill.env` 配置文件

在你的**工程根目录**（通常为包含 `.agents` 或代码根目录的层级）下创建 `.skill.env`：

```bash
# 复制模板文件
cp .agents/skills/audio-stt/.skill.env.example .skill.env
```

编辑 `.skill.env` 填入配置：

```env
# [必填] 你的 Groq API Key
GROQ_API_KEY=gsk_your_actual_key_here

# [选填] 如果国内直连 api.groq.com 被阻断或报 403，配置代理地址
SKILL_PROXY=http://127.0.0.1:7890

# [选填] 指定 Python 解释器路径（留空则默认使用系统当前 python）
PYTHON_EXE=
```

---

## CLI 命令速查

你可以直接在终端中调用脚本，也可以由 Agent 自动调度：

### 单文件转录
```bash
python .agents/skills/audio-stt/scripts/transcribe.py --input "path/to/meeting.mp3"
```
> 输出文件为同目录下的 `path/to/meeting.txt`。

### 目录批量转录
```bash
python .agents/skills/audio-stt/scripts/transcribe.py --input-dir "path/to/audio-folder"
```
> 支持自动扫描：`.mp3`、`.wav`、`.flac`、`.m4a`、`.ogg`、`.opus`、`.aac`、`.webm`、`.mp4`。

### 增量转录（跳过已生成的 .txt）
```bash
python .agents/skills/audio-stt/scripts/transcribe.py --input-dir "path/to/folder" --skip-existing
```

### 指定识别语言（默认 `zh` 普通话）
```bash
python .agents/skills/audio-stt/scripts/transcribe.py --input "english.mp3" --language en
```

### 指定自定义环境文件或输出目录
```bash
python .agents/skills/audio-stt/scripts/transcribe.py \
  --input-dir "audios/" \
  --output-dir "transcripts/" \
  --env-file "/path/to/custom/.skill.env"
```

---

## 文件目录结构

```text
audio-stt/
├── SKILL.md              # Agent 识别入口与指引
├── README.md             # 独立使用说明与环境配置文档（本文档）
├── .skill.env.example    # 环境配置文件模板
└── scripts/
    └── transcribe.py     # 独立自包含转录脚本（支持单文件/批量/切片/代理）
```
