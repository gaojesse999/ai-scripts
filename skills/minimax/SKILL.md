---
name: minimax
preamble-tier: 2
version: 1.0.0
description: |
  MiniMax AI 完整功能 CLI - chat、tts、image、vision、music 等。
  支持配置默认模型、角色、声音等参数。
  当用户说 "minimax"、"tts"、"生成语音"、"聊天" 等时使用。
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
---

# MiniMax CLI

MiniMax AI 完整功能命令行工具，支持：

## 功能模块

| 命令 | 功能 | 默认模型 |
|------|------|---------|
| `chat` | AI 对话 | MiniMax-M2.7-highspeed |
| `tts` | 文字转语音 | speech-2.8-turbo |
| `image` | 图片生成 | image-01 |
| `vision` | 图片理解 | image-01 |
| `music` | 音乐生成 | music-2.6 |
| `search` | 网络搜索 | - |

## 配置管理

```bash
minimax config show          # 显示当前配置
minimax config set <key> <value>  # 设置配置项
minimax config voice list   # 列出可用声音
minimax config model list    # 列出可用模型
```

## TTS 配置项

- `tts.model` - TTS 模型 (默认: speech-2.8-turbo)
- `tts.voice` - 默认声音 (如: female-tianmei、male-yunyang)
- `tts.speed` - 语速 (0.5-2.0, 默认: 1.0)
- `tts.pitch` - 音调 (0.5-2.0, 默认: 1.0)

## TTS 注意事项

### 文本限制
- **长度限制**：文本需小于 10000 字符
- **推荐流式**：文本大于 3000 字符时推荐使用流式输出（默认已是流式）

### 文本格式

**段落切换**：用换行符 `\n` 标记段落

**停顿控制**：使用 `<#x#>` 标记，x 为停顿时长（秒），范围 [0.01, 99.99]，最多两位小数
```
示例：今天天气真好<#1.5#>我们去吃饭吧
```

**语气词标签**：仅支持 `speech-2.8-hd` 和 `speech-2.8-turbo` 模型

| 标签 | 含义 |
|------|------|
| `(laughs)` | 笑声 |
| `(chuckle)` | 轻笑 |
| `(coughs)` | 咳嗽 |
| `(clear-throat)` | 清嗓子 |
| `(groans)` | 呻吟 |
| `(breath)` | 正常换气 |
| `(pant)` | 喘气 |
| `(inhale)` | 吸气 |
| `(exhale)` | 呼气 |
| `(gasps)` | 倒吸气 |
| `(sniffs)` | 吸鼻子 |
| `(sighs)` | 叹气 |
| `(snorts)` | 喷鼻息 |
| `(burps)` | 打嗝 |
| `(lip-smack)` | 咂嘴 |
| `(humming)` | 哼唱 |
| `(hissing)` | 嘶嘶声 |
| `(emm)` | 嗯 |
| `(sneezes)` | 喷嚏 |

**示例**：
```
你好<#0.5#>今天天气真好(laughs)我们去公园散步吧<#1.0#>下一站去哪？
```

## 使用示例

```bash
# 配置
minimax config set api.url https://mimimax.cn
minimax config set api.key <your-key>
minimax config set tts.voice Chinese\\\\ (Mandarin)_Gentleman

# TTS（默认流式，无缓存问题，自动处理语气词和停顿）
minimax tts "你好世界"
minimax tts "你好(chuckles)<#1.0#>我们去散步吧"
minimax tts "播报内容" --speed 1.5

# Chat
minimax chat "写一首诗"

# Image
minimax image "一只猫" -o cat.png
minimax image "风景画" --style 漫画 --ratio 16:9 -o landscape.png
minimax image "插画" --style 水彩 -n 4

# Vision
minimax vision photo.jpg "描述这张图片"

# Music
minimax music "独立民谣" -o song.mp3
minimax music "轻音乐" -i  # instrumental 纯音乐模式
```

## 可用声音列表 (TTS)

完整音色列表保存在 [voices.json](voices.json) 文件中。

常用音色：

| 声音ID | 描述 |
|--------|------|
| female-tianmei | 甜美女性音色 |
| female-yujie | 御姐音色 |
| female-chengshu | 成熟女性音色 |
| female-shaonv | 少女音色 |
| male-qn-qingse | 青涩青年音色 |
| male-qn-jingying | 精英青年音色 |
| male-qn-badao | 霸道青年音色 |
| male-qn-daxuesheng | 青年大学生音色 |

查看所有音色：
```bash
minimax config voice list
```

## 配置文件位置

- Linux/WSL: `~/.minimax-cli.conf`
- Windows: `%USERPROFILE%\.minimax-cli.conf`
