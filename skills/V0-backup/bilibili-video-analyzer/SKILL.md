---
name: bilibili-video-analyzer
description: >-
  B站/bilibili视频转专题文档、实操教程或结构化知识整理（Python 版）。
  Use when: 用户提供bilibili/B站视频链接，要求转文档、生成教程、课程笔记或步骤化学习材料。
  Voice triggers: "分析B站视频", "bilibili转文档", "视频转教程"。
---

# Bilibili Video Analyzer (Python)

## 核心特点

- 不是时间线流水账，而是**重新组织整理**成完整文档
- 实操类视频 → 生成**可直接使用的操作教程**
- 知识类视频 → 生成**结构化的专题文档**
- 文档中插入关键截图，格式: `![frame_xxxx: 描述](./images/frame_xxxx.jpg)`

## Installation

### 1. 安装 Python 3.8+

脚本使用纯 Python 实现，需要安装 Python 3.8 或更新版本。

下载地址: https://www.python.org/downloads/

验证安装:
```bash
python --version
# 或
python3 --version
```

### 2. 安装 Python 依赖

仅依赖 `requests`（用于访问 Bilibili API 与下载视频文件）：

```bash
pip install requests
```

如果你使用工作区内置虚拟环境（如本仓库的 `.venv`），请先激活：

```bash
# Linux / macOS
source .venv/bin/activate
pip install requests
```

### 3. 安装 FFmpeg

**Windows:**
```powershell
# Chocolatey
choco install ffmpeg

# 或 Scoop
scoop install ffmpeg

# 或手动下载: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install ffmpeg
```

验证安装:
```bash
ffmpeg -version
```

## Provided Script

本 skill 提供了 `scripts/prepare.py` 脚本用于下载视频和提取帧图片。

**脚本位置**: `scripts/prepare.py`（相对当前 skill 根目录）

**运行方式**: 使用 Python 3 直接执行

### 使用方法

下面命令默认在**当前 skill 根目录**执行，也就是 `SKILL.md` 所在目录。

如果你是在其他目录里运行命令，请把 `scripts/prepare.py` 替换成这个 skill 中脚本文件的实际相对路径或绝对路径。

```bash
# 基本用法
python scripts/prepare.py "<视频URL>" -o <输出目录>

# 示例
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output

# 长视频（降低帧率）
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --fps 0.5
```

> 与 .NET 版本不同，Python 版本无需 `--` 分隔符；所有参数都直接传给脚本本身。

### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `url` | B站视频URL（必需），支持合集分P（如 `?p=4`） | - |
| `-o, --output` | 输出目录 | 当前目录 |
| `--fps` | 每秒提取帧数 | 自动（<10分钟:1.0, 10-30分钟:0.5, >30分钟:0.2） |
| `--similarity` | 相似度阈值（0-1），超过此值的帧会被去重 | 0.65 |
| `--no-dedup` | 禁用相似帧去重 | false |
| `--video-only` | 只下载视频，不提取帧 | false |
| `--frames-only` | 只提取帧（需已有video.mp4；此模式下请显式传 `--fps`） | false |

### 相似帧去重

脚本会自动对帧进行相似度检测，去除相似度超过阈值（默认65%）的重复帧：

- 原始帧提取到 `images_raw/` 目录（保留全部原始帧）
- 去重后的帧复制到 `images/` 目录（重新编号：frame_0001.jpg, frame_0002.jpg, ...）
- 同时生成 `dedup_manifest.json`，记录 raw → output 的帧号映射关系
- 使用 ffmpeg 的 SSIM/PSNR 算法计算相似度
- **与最后保留帧比较**：每帧都与最近一个被保留的帧比较，确保连续相似帧只保留第一帧
- 可通过 `--similarity` 调整阈值
- 可通过 `--no-dedup` 禁用去重（仍会从 `images_raw/` 复制全部帧到 `images/`）

**阈值选择建议**：

| 视频类型 | 推荐阈值 | 说明 |
|---------|---------|------|
| **代码/编程教程** | `--similarity 0.65`（默认） | 光标闪烁、字幕变化等微小差异较多，需要较低阈值有效去重 |
| **PPT/演讲** | `--similarity 0.70` | 翻页间长时间不变，默认阈值即可；如需更激进可用 0.60 |
| **动态演示** | `--similarity 0.80` | 页面切换频繁，较高阈值避免误删有差异的帧 |
| **字幕密集型视频** | `--similarity 0.60` | 画面相同仅字幕不同，需要更低阈值 |
| **快速浏览/混剪** | `--similarity 0.85` | 内容变化快，高阈值只去除几乎完全相同的帧 |

### 输出结构

```
<输出目录>/
├── video.mp4              # 下载的视频文件
├── dedup_manifest.json    # 去重映射清单（raw帧号 → output帧号）
├── images_raw/            # 原始提取的全部帧图片
│   ├── frame_0001.jpg
│   ├── frame_0002.jpg
│   └── ...
└── images/                # 去重后的帧图片（文档生成从此目录读取）
    ├── frame_0001.jpg
    ├── frame_0002.jpg
    └── ...
```

## Workflow (Prompt)

你是一个视频内容分析助手。当用户提供B站视频链接时，按以下步骤执行：

### Step 1: 下载视频并拆帧

使用提供的脚本下载视频并拆解成帧图片：

```bash
python scripts/prepare.py "<视频URL>" -o <输出目录>
```

脚本会自动：
1. 下载视频到 `video.mp4`
2. 根据视频时长自动选择 fps（合集视频使用所选分P的时长，而非总时长）
3. 提取全部帧到 `images_raw/` 目录
4. 去重后复制到 `images/` 目录，并生成 `dedup_manifest.json`

**注意事项**:
- fps 默认自动选择，也可通过 `--fps` 手动指定覆盖
- 合集/分P视频：URL 中包含 `?p=N` 时自动下载对应分P
- `prepare.py` 会自动使用 HTTP/1.1、断点续传、重试和 `backup_url` 兜底，以提高 B 站 CDN 中断时的成功率
- 如果使用 `--frames-only`，请显式传入 `--fps`，因为此模式不会重新获取视频元信息来自动判定帧率

### Step 2: 分析帧图片

优先使用当前 agent 直接分析 `images/` 目录中的图片；如果环境提供 **Task 工具**，可以只把它当作当前 agent 的分批整理手段，而不是委托新的代理。

如果当前模型/环境不支持图片 vision，先使用 OCR 为图片建立文字索引，再基于 OCR 结果整理文档。推荐优先使用工作区里已有的 OCR 能力，例如已配置 Python 环境中的 `rapidocr-onnxruntime`。

**执行限制**:
- **禁止使用 subagent / 子代理 / runSubagent / 委托代理工具**。
- 即使需要分批处理，也必须由当前 agent 直接完成图片分析，不要把任何批次再次分发给其他 agent。
- 这里的分批仅用于控制分析顺序、工作量和结果整理方式，不代表可以启动新的代理。
- 如果没有 Task 工具，就按同样的分批策略由当前 agent 顺序完成，不要因为工具缺失而中断流程。

**分批策略**（根据总图片数动态计算）:

| 总图片数 | 分批数量 | 每批图片数 |
|---------|---------|-----------|
| 1-30 | 1 批 | 全部 |
| 31-60 | 2 批 | 约 15-30 张/批 |
| 61-120 | 3 批 | 约 20-40 张/批 |
| 121-200 | 4 批 | 约 30-50 张/批 |
| 200+ | 5 批 | 平均分配 |

**计算公式**:
```
总图片数 <= 30: 1 批
总图片数 <= 60: 2 批
总图片数 <= 120: 3 批
总图片数 <= 200: 4 批
总图片数 > 200: 5 批

每批图片数 = 总图片数 / 分批数量（向上取整）
```

**示例**：假设有 85 张图片 → 分 3 批

```
Task 1: 分析 frame_0001.jpg ~ frame_0029.jpg（29张）
Task 2: 分析 frame_0030.jpg ~ frame_0058.jpg（29张）
Task 3: 分析 frame_0059.jpg ~ frame_0085.jpg（27张）
```

**Task Prompt 模板**:

```
读取并分析 <输出目录>/images/ 目录下的 frame_0001.jpg 到 frame_0020.jpg（共20张图片）。

【重要要求】
你的响应必须是这些图片内容的【完整详细报告】，不要省略任何信息。

对每张图片，详细记录：

1. **帧号**: frame_xxxx.jpg
2. **场景类型**: 代码编辑器/终端/浏览器/PPT/对话/其他
3. **界面内容**:
   - 窗口标题、菜单、按钮等UI元素
   - 当前打开的文件/页面
4. **文字内容**:
   - 完整转录屏幕上的所有文字
   - 代码内容（完整复制，保留格式）
   - 终端命令和输出
   - 注释和说明文字
5. **操作动作**:
   - 鼠标位置、点击目标
   - 正在进行的操作
6. **关键信息**:
   - 重要的配置项
   - 关键步骤说明
   - 错误信息或警告

【输出格式】

## frame_0001.jpg
- 场景: [场景类型]
- 内容: [详细描述]
- 文字/代码:
  ```
  [完整的文字或代码内容]
  ```
- 操作: [正在进行的操作]
- 要点: [关键信息]

## frame_0002.jpg
...

【注意】
- 不要省略任何图片
- 代码和文字必须完整转录
- 信息越详细越好
```

**分析要点**:
1. 完整转录所有文字和代码内容
2. 详细描述界面元素和操作步骤
3. 记录每张图片的关键信息
4. 标注重要的截图帧号（如 frame_0042.jpg）

### Step 3: 生成文档

根据视频类型，将分析结果**重新组织整理**成 `视频分析.md`：

**判断视频类型**:
- 实操类: 编程教程、软件操作、配置演示等
- 知识类: 概念讲解、原理分析、经验分享等

**【关键】图片与内容必须严格对应**:

```
错误示例 ❌:
### 安装 Node.js
首先下载 Node.js...
![截图](./images/frame_0001.jpg)  ← 图片可能是其他内容

正确示例 ✅:
### 安装 Node.js
首先下载 Node.js...
![frame_0015: Node.js官网下载页面](./images/frame_0015.jpg)  ← 图片确实是下载页面
```

**生成文档的正确流程**:

1. **先整理所有 Task 返回的分析结果**
   - 汇总所有帧的分析内容
   - 建立「帧号 → 内容」的对应关系

2. **按主题重新组织内容**（不是按时间顺序）
   - 将相关内容归类到同一章节
   - 确定每个章节需要哪些帧的信息

3. **插入图片时必须核对**
   - 只插入与当前内容**直接相关**的图片
   - 图片描述要准确反映图片实际内容
   - 使用格式: `![frame_xxxx: 图片实际内容描述](./images/frame_xxxx.jpg)`

4. **代码必须来自图片中的实际代码**
   - 不要自己编造代码
   - 代码块标注来源: `<!-- 来自 frame_0025 -->`

**重要原则**:
1. **图文对应** - 每张图片必须与其上下文内容匹配
2. **不要时间线流水账** - 重新组织内容，像写文章一样
3. **结构清晰** - 有章节划分和逻辑顺序
4. **代码真实** - 只使用图片中出现的代码，不要编造
5. **独立可读** - 不看视频也能完全理解

## Output Format

### 实操教程类

```markdown
# {教程主题}

## 简介

{教程目标}
{前置条件和要求}

## 环境准备

{需要安装的软件}
{配置要求}

## 操作步骤

### 1. {步骤标题}

{详细说明，内容必须与下方图片对应}

![frame_xxxx: 图片实际内容的准确描述](./images/frame_xxxx.jpg)

<!-- 代码来自 frame_xxxx -->
```代码块```

### 2. {步骤标题}

{详细说明}

![frame_xxxx: 准确描述](./images/frame_xxxx.jpg)

...

## 完整代码

<!-- 汇总自 frame_xxxx, frame_xxxx, frame_xxxx -->
{汇总所有代码片段，标注来源帧号}

## 常见问题

{可能遇到的问题和解决方案}

## 总结

{核心要点回顾}
{延伸学习建议}
```

### 知识文档类

```markdown
# {主题}

## 概述

{主题背景介绍}
{为什么重要}

## {章节1标题}

{内容，必须与配图对应}

![frame_xxxx: 图片实际内容描述](./images/frame_xxxx.jpg)

## {章节2标题}

{内容}

![frame_xxxx: 图片实际内容描述](./images/frame_xxxx.jpg)

## 核心要点

- 要点1
- 要点2
- 要点3

## 延伸阅读

{相关资源和建议}
```

### 图片插入规范

| 规则 | 说明 |
|------|------|
| **帧号必须标注** | `![frame_0015: 描述](./images/frame_0015.jpg)` |
| **描述必须准确** | 描述图片的实际内容，不是期望内容 |
| **内容必须匹配** | 图片上方/下方的文字必须与图片内容相关 |
| **代码标注来源** | `<!-- 代码来自 frame_0025 -->` |
| **不要乱插图** | 没有合适的图就不插，不要强行配图 |

## API Reference

| 依赖 | 用途 | 文档 | License |
|------|------|------|------|
| **FFmpeg** | 视频下载、拆帧、相似度计算 | [ffmpeg.org](https://ffmpeg.org/documentation.html) / [GitHub](https://github.com/FFmpeg/FFmpeg) | LGPL/GPL |
| **requests** | HTTP 请求与文件下载 | [requests](https://requests.readthedocs.io/) | Apache-2.0 |
| **Bilibili API** | 视频信息与播放地址 | [API文档](https://github.com/SocialSisterYi/bilibili-API-collect) | - |

### Bilibili API

脚本使用 Bilibili 官方 API 下载视频：

```
# 获取视频信息（包含 duration、pages 等）
GET https://api.bilibili.com/x/web-interface/view?bvid=BV1xx411c7mD
# 返回: data.duration（秒）, data.pages[].cid（分P的cid）

# 获取播放地址（cid 根据分P选择）
GET https://api.bilibili.com/x/player/playurl?bvid=BV1xx411c7mD&cid={cid}&qn=80&fnval=1
```

API 文档: https://github.com/SocialSisterYi/bilibili-API-collect

### FFmpeg 拆帧命令

```bash
# 每秒1帧（提取到 images_raw/）
ffmpeg -i video.mp4 -vf "fps=1" -q:v 2 images_raw/frame_%04d.jpg

# 每秒0.5帧（每2秒1帧）
ffmpeg -i video.mp4 -vf "fps=0.5" -q:v 2 images_raw/frame_%04d.jpg

# 指定时间范围
ffmpeg -i video.mp4 -ss 00:01:00 -to 00:05:00 -vf "fps=1" -q:v 2 images_raw/frame_%04d.jpg

# 提取关键帧（场景变化）
ffmpeg -i video.mp4 -vf "select='gt(scene,0.3)'" -vsync vfr -q:v 2 images_raw/frame_%04d.jpg
```

更多选项: https://ffmpeg.org/ffmpeg.html

## Examples

### 示例1: 分析编程教程

```bash
# 1. 下载并拆帧（fps 自动选择）
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./react-tutorial

# 输出结构:
#   react-tutorial/video.mp4           ← 视频
#   react-tutorial/images_raw/         ← 原始帧
#   react-tutorial/images/             ← 去重后的帧（用于分析）
#   react-tutorial/dedup_manifest.json ← 映射清单

# 2. 分析图片（优先当前 agent；如无 vision 则先 OCR；禁止使用 subagent）
# 3. 生成 react-tutorial/视频分析.md
```

### 示例2: 分析长视频

```bash
# 手动指定低帧率（覆盖自动选择）
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./long-video --fps 0.2
```

### 示例3: 分析合集视频的第4集

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=4" -o ./episode-4
```

### 示例4: 只下载视频

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --video-only

# 如果视频已下载完成，再只做拆帧，请显式指定 --fps
python scripts/prepare.py dummy-url -o ./output --frames-only --fps 0.5
```

## Quality Checklist

生成文档前，**逐项检查**以下要求：

### 内容质量
- [ ] 内容重新组织，不是时间线流水账
- [ ] 章节结构清晰，有逻辑顺序
- [ ] 不看视频也能理解全部内容
- [ ] 包含环境准备/前置条件说明
- [ ] 包含总结和核心要点

### 图文对应（重要！）
- [ ] 每张图片都标注了帧号: `![frame_xxxx: 描述](...)`
- [ ] 图片描述准确反映图片**实际内容**
- [ ] 图片上下文的文字与图片内容**直接相关**
- [ ] 没有随意插入不相关的图片
- [ ] 代码块标注了来源帧号: `<!-- 来自 frame_xxxx -->`

### 代码质量
- [ ] 代码来自图片中的实际代码，不是编造的
- [ ] 代码片段完整，可直接复制使用
- [ ] 完整代码章节汇总了所有代码并标注来源

## Tags

`bilibili`, `video-analysis`, `ai`, `frame-extraction`, `markdown`, `tutorial`, `ffmpeg`, `python`

## Compatibility

- Codex: Yes
- Claude Code: Yes
