---
name: bilibili-analyzer
description: >-
  B站/bilibili视频及合集转专题文档、实操教程或结构化知识整理
  Applicable when: 用户提供bilibili/B站视频或合集链接，要求转文档、生成教程、课程笔记或步骤化学习材料
  Example prompts: "分析B站视频", "bilibili转文档", "视频转教程",
    "合集", "视频合集", "UGC合集", "系列视频", "全集", "分P全部",
    "B站合集分析", "合集转文档", "分析整个合集", "批量分析视频", "分析合集视频"
---

# Bilibili Analyzer

## Description

B站视频及合集内容分析工具。提供视频或合集URL后，自动下载视频、拆解成帧图片，然后使用AI分析内容，最终生成**高质量的专题文档或实操教程**。

支持两种模式：
- **单视频模式**：分析单个B站视频，生成 `视频分析.md`
- **合集模式**：分析 UGC 合集 / 系列视频中的所有视频，逐个分析后合并生成 `合集视频分析.md`

这个 skill 的内部实现基于 Python：先通过 Bilibili 公共接口下载视频，再抽取原始帧到 `images_raw/`，按相邻帧相似度做去重并输出关键帧到 `images/`，最后将分析结果重组为可直接阅读或执行的 Markdown 文档。

**核心特点**:
- 不是简单的时间线记录，而是**重新组织整理**成一篇完整的文档
- 实操类视频 → 生成**可直接使用的操作教程**
- 知识类视频 → 生成**结构化的专题文档**
- 使用 Python 直接调用 Bilibili 公共接口下载视频，不依赖 `.NET` 或 `ffmpeg`
- 保留 `images_raw/` 原始帧，并将去重后的关键帧输出到 `images/`
- 报告中插入关键截图，使用 `![描述](./images/frame_xxxx.jpg)` 格式
- 自动检测链接是单视频还是合集，合集时自动列出并逐个分析

## Source & Documentation

| 工具 | 用途 | Repository | 文档 |
|------|------|------------|------|
| **Python** | 执行准备脚本 | - | [官网](https://www.python.org/) / [文档](https://docs.python.org/3/) |
| **OpenCV** | 视频读取与抽帧 | [opencv/opencv](https://github.com/opencv/opencv) | [官网](https://opencv.org/) / [文档](https://docs.opencv.org/) |
| **Pillow + ImageHash** | 感知哈希去重 | [JohannesBuchner/imagehash](https://github.com/JohannesBuchner/imagehash) | [Pillow](https://pillow.readthedocs.io/) / [ImageHash](https://pypi.org/project/ImageHash/) |
| **Bilibili API** | 视频下载与合集检测 | [SocialSisterYi/bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect) | [API文档](https://github.com/SocialSisterYi/bilibili-API-collect) |

## Installation

### 1. 安装 Python

建议使用 Python 3.10 或更高版本。

验证安装:
```bash
python --version
```

### 2. 安装 Python 依赖

推荐在虚拟环境中安装：

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install opencv-python-headless pillow ImageHash
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install opencv-python-headless pillow ImageHash
```

说明：

- `opencv-python-headless` 负责读取视频并按目标 `fps` 抽帧
- `pillow` 与 `ImageHash` 用于计算相邻帧 `pHash`
- `collection.py` 仅使用 Python 标准库，无额外依赖
- 本 skill 不要求安装 `.NET` 或 `ffmpeg`

## Scope

- 输入是 B站/bilibili 视频或合集链接，输出目标是专题文档、实操教程、课程笔记或结构化知识整理
- 支持单个视频分析和 UGC 合集 / 系列视频的批量分析
- 适合把视频内容重组成可阅读、可复用的文档，而不是保留时间线流水账
- 不适用于纯字幕提取、逐句转录，或只做简短摘要的场景

## Internal Workflow

- 使用 `scripts/collection.py` 检测链接是单视频还是合集，合集时提取所有视频 URL 列表
- 使用 `scripts/prepare.py` 下载视频，并按设定 `fps` 抽取原始帧到 `images_raw/`
- 对相邻帧执行基于 `ImageHash` 的相似度去重，将保留帧输出到 `images/`
- 结合关键帧分析结果，按主题重组内容并生成 `视频分析.md`
- 合集模式下，将各视频的 `视频分析.md` 按顺序合并为 `合集视频分析.md`
- 需要时保留 `metadata.json`、`frames.json` 等中间产物，便于后续核对帧号、时间戳和图片来源

## Provided Scripts

本 skill 提供了两个脚本：

### scripts/prepare.py — 视频下载与拆帧

用于下载单个视频、提取原始帧并输出去重后的关键帧。

**运行方式**: 使用 Python 直接执行

#### 使用方法

```bash
# 基本用法
python scripts/prepare.py "<视频URL>" -o <输出目录>

# 示例
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output

# 长视频（降低帧率）
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --fps 0.5
```

#### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `url` | B站视频URL（必需） | - |
| `-o, --output` | 输出目录 | 当前目录 |
| `--fps` | 每秒提取帧数 | 1.0 |
| `--similarity` | 相似度阈值（0-1），超过此值的相邻帧会被去重 | 0.80 |
| `--no-dedup` | 禁用相似帧去重 | false |

#### 相似帧去重

脚本会自动对**相邻帧**进行相似度检测，去除相似度超过阈值（默认80%）的重复帧：

- 使用 `ImageHash` 的 `pHash` 计算感知相似度
- **只比较相邻帧**，不会跨帧比较
- 原始抽帧保留在 `images_raw/` 中
- 去重后将保留帧复制到 `images/`，并自动重新编号（`frame_0001.jpg`, `frame_0002.jpg`, ...）
- `frames.json` 会记录最终帧对应的 `source_file`、时间戳和相邻相似度
- 可通过 `--similarity 0.85` 调整阈值
- 可通过 `--no-dedup` 禁用去重

#### 输出结构

```
<输出目录>/
├── video.mp4           # 下载的视频文件
├── images_raw/         # 按 fps 抽取的全部原始帧
│   ├── frame_0001.jpg
│   ├── frame_0002.jpg
│   └── ...
├── images/             # 去重后的关键帧
│   ├── frame_0001.jpg
│   ├── frame_0002.jpg
│   └── ...
├── metadata.json       # 视频元数据与帧统计
└── frames.json         # 保留帧索引与 source_file 映射
```

### scripts/collection.py — 合集检测与视频列表提取

用于检测 URL 是单视频还是合集，并输出结果 JSON。

**运行方式**: 使用 Python 直接执行

#### 使用方法

```bash
python scripts/collection.py "<URL>"
```

#### 支持的 URL 格式

| URL 模式 | 说明 |
|----------|------|
| `https://www.bilibili.com/video/BVxxx` | 单视频或合集中的视频（自动检测） |
| `https://space.bilibili.com/{mid}/channel/collectiondetail?sid={season_id}` | UGC 合集主页 |
| `https://space.bilibili.com/{mid}/channel/seriesdetail?sid={series_id}` | 系列主页 |
| `https://b23.tv/xxxxx` | 短链接（自动解析） |

#### 输出格式

**单视频**:
```json
{
  "type": "single",
  "bvid": "BV1xx411c7mD",
  "title": "视频标题",
  "url": "https://www.bilibili.com/video/BV1xx411c7mD"
}
```

**合集（通过 BV 链接检测到 UGC 合集）**:
```json
{
  "type": "collection",
  "source": "ugc_season",
  "collection_title": "合集标题",
  "total": 5,
  "also_in_series": false,
  "videos": [
    {"bvid": "BV1aaa", "title": "第1集", "url": "https://www.bilibili.com/video/BV1aaa", "duration": 600},
    {"bvid": "BV1bbb", "title": "第2集", "url": "https://www.bilibili.com/video/BV1bbb", "duration": 720}
  ]
}
```

**合集（通过合集页面 URL）**:
```json
{
  "type": "collection",
  "source": "collection_page",
  "collection_title": "合集标题",
  "total": 5,
  "videos": [...]
}
```

**合集（通过系列页面 URL）**:
```json
{
  "type": "collection",
  "source": "series_page",
  "collection_title": "系列标题",
  "total": 5,
  "videos": [...]
}
```

## Workflow (Prompt)

你是一个视频内容分析助手。当用户提供B站视频或合集链接时，按以下步骤执行：

### Step 0: 判断分析模式

根据用户请求的措辞和 URL 类型，按以下规则判断分析模式：

**判断规则**：

| 用户是否提及合集关键词 | URL / 检测结果 | 处理方式 |
|----------------------|---------------|----------|
| 是 | URL 是 space.bilibili.com 合集/系列页面 | 合集流程 |
| 是 | BV 链接，检测到属于 UGC 合集 | 合集流程（从合集第一个视频开始） |
| 是 | BV 链接，检测到属于系列 | 合集流程（从系列第一个视频开始） |
| 是 | BV 链接，**同时**属于 UGC 合集和系列 | **仅按 UGC 合集处理**，提示用户该视频同时属于系列但将按 UGC 合集分析 |
| 是 | BV 链接，不属于任何合集 | 提示用户"该视频不属于任何合集"，按**单视频**流程分析 |
| 否 | 任何 BV 链接（无论是否属于合集） | **单视频**流程 |
| 否 | space.bilibili.com 合集/系列页面 | 合集流程（URL 本身已表明意图） |

**合集关键词**: "合集"、"视频合集"、"UGC合集"、"系列视频"、"全集"、"分P全部"、"整个合集"、"批量分析" 等。

**执行步骤**：

1. 判断用户是否提及合集关键词
2. 如果用户**未提及**合集关键词且 URL 不是合集/系列页面 → 直接进入 Step 1（单视频流程），无需调用 `collection.py`
3. 如果用户**提及**合集关键词或 URL 是合集/系列页面 → 调用 `collection.py` 检测：

```bash
python scripts/collection.py "<URL>"
```

4. 根据 `collection.py` 输出和上表规则决定后续流程

**注意**：合集模式下无论用户提供的是合集中的第几个视频链接，都从合集的**第一个视频**开始分析全部视频。

### Step 1: 下载视频并拆帧

使用提供的脚本下载视频并拆解成帧图片：

```bash
python scripts/prepare.py "<视频URL>" -o <输出目录>
```

**注意事项**:
- 短视频（<10分钟）: 使用默认 `--fps 1`
- 中等视频（10-30分钟）: 使用 `--fps 0.5`
- 长视频（>30分钟）: 使用 `--fps 0.2`

### Step 2: 分析帧图片

分批分析 `images/` 目录中的图片。

**任务拆分方式**:
- **默认模式**：在当前会话中顺序执行分批分析，**不使用 SubAgent/Task 工具**
- **SubAgent 模式**：使用 Task 工具并行分批分析（仅当用户在请求时指定时启用）

> 用户可通过 "使用subagent"、"并行分析"、"用task分析" 等关键词启用 SubAgent 模式。

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
批次 1: 分析 frame_0001.jpg ~ frame_0029.jpg（29张）
批次 2: 分析 frame_0030.jpg ~ frame_0058.jpg（29张）
批次 3: 分析 frame_0059.jpg ~ frame_0085.jpg（27张）
```

**分析 Prompt 模板**:

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

1. **先整理所有分析结果**
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

### 合集分析流程

当 Step 0 检测到合集时，按以下流程执行：

#### 合集 Step 1: 确认视频列表

1. 将 `collection.py` 输出的视频列表打印给用户
2. 显示合集标题、视频总数、每个视频的标题和时长
3. 等待用户确认后开始分析

#### 合集 Step 2: 逐个分析视频

对合集中的每个视频，依次执行 Step 1 → Step 2 → Step 3：

```bash
# 视频1
python scripts/prepare.py "<视频1 URL>" -o <合集输出目录>/<视频1 BV号>/
# → 分析帧图片 → 生成 视频分析.md

# 视频2
python scripts/prepare.py "<视频2 URL>" -o <合集输出目录>/<视频2 BV号>/
# → 分析帧图片 → 生成 视频分析.md

# ... 依次处理所有视频
```

**注意**：
- 每个视频的输出目录使用 BV 号命名（如 `BV1aaa/`）
- 如果某个视频分析失败，记录错误并继续分析后续视频
- 两个视频之间适当间隔以避免 API 限流

#### 合集 Step 3: 合并生成合集文档

所有视频分析完成后，将各视频的 `视频分析.md` 按合集中的顺序合并为 `合集视频分析.md`：

1. 文件开头写入合集概要信息（合集标题、视频总数、UP 主等）
2. 按顺序拼接每个视频的分析内容
3. 每个视频前加一级标题分隔：`# 第X集: {视频标题}`
4. 各视频内部的标题级别降一级（`#` → `##`，`##` → `###`，依此类推）
5. 图片路径调整为相对于合集根目录：`./images/frame_xxxx.jpg` → `./<BV号>/images/frame_xxxx.jpg`
6. 分析失败的视频在对应位置标注失败信息

**合集输出目录结构**:

```
<合集输出目录>/
├── <视频1 BV号>/
│   ├── video.mp4
│   ├── images_raw/
│   ├── images/
│   ├── metadata.json
│   ├── frames.json
│   └── 视频分析.md
├── <视频2 BV号>/
│   ├── video.mp4
│   ├── images_raw/
│   ├── images/
│   ├── metadata.json
│   ├── frames.json
│   └── 视频分析.md
├── ...
└── 合集视频分析.md          ← 合并所有视频分析结果
```

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

### 合集文档

```markdown
# {合集标题}

## 合集概要

- **合集标题**: {合集标题}
- **视频总数**: {total} 个
- **UP 主**: {uploader}

---

# 第1集: {视频1标题}

## {视频1的章节1}

{内容}

![frame_xxxx: 描述](./<视频1 BV号>/images/frame_xxxx.jpg)

## {视频1的章节2}

{内容}

---

# 第2集: {视频2标题}

## {视频2的章节1}

{内容}

![frame_xxxx: 描述](./<视频2 BV号>/images/frame_xxxx.jpg)

...
```

### 图片插入规范

| 规则 | 说明 |
|------|------|
| **帧号必须标注** | `![frame_0015: 描述](./images/frame_0015.jpg)` |
| **描述必须准确** | 描述图片的实际内容，不是期望内容 |
| **内容必须匹配** | 图片上方/下方的文字必须与图片内容相关 |
| **代码标注来源** | `<!-- 代码来自 frame_0025 -->` |
| **不要乱插图** | 没有合适的图就不插，不要强行配图 |
| **合集路径** | 合集文档中使用 `./<BV号>/images/frame_xxxx.jpg` |

## API Reference

### Bilibili API

脚本使用 Bilibili 官方 API：

```
# 获取视频信息（含 ugc_season 合集检测）
GET https://api.bilibili.com/x/web-interface/view?bvid=BV1xx411c7mD

# 获取播放地址
GET https://api.bilibili.com/x/player/playurl?bvid=BV1xx411c7mD&cid={cid}&qn=80&fnval=1

# 获取 UGC 合集视频列表
GET https://api.bilibili.com/x/polymer/web-space/seasons_archives_list?mid={mid}&season_id={season_id}&page_num=1&page_size=100

# 获取系列视频列表
GET https://api.bilibili.com/x/series/archives?mid={mid}&series_id={series_id}&pn=1&ps=100
```

API 文档: https://github.com/SocialSisterYi/bilibili-API-collect

### Python 准备脚本说明

```bash
# 每秒 1 帧
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --fps 1

# 每秒 0.5 帧
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --fps 0.5

# 调整相似度阈值
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --similarity 0.85

# 保留全部原始帧，不执行去重
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --no-dedup
```

去重逻辑：脚本会先把全部抽帧写入 `images_raw/`，再按相邻帧 `pHash` 相似度筛出保留帧并复制到 `images/`。

### 合集检测脚本说明

```bash
# 检测单视频
python scripts/collection.py "https://www.bilibili.com/video/BV1xx411c7mD"

# 检测合集页面
python scripts/collection.py "https://space.bilibili.com/12345/channel/collectiondetail?sid=67890"

# 检测系列页面
python scripts/collection.py "https://space.bilibili.com/12345/channel/seriesdetail?sid=67890"

# 检测短链接
python scripts/collection.py "https://b23.tv/xxxxx"
```

## Examples

### 示例1: 分析单个视频

```bash
# 1. 检测链接类型
python scripts/collection.py "https://www.bilibili.com/video/BV1xx411c7mD"
# 输出: {"type": "single", ...}

# 2. 下载并拆帧
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./react-tutorial

# 3. 分析图片并生成 react-tutorial/视频分析.md
```

### 示例2: 分析合集

```bash
# 1. 检测链接类型
python scripts/collection.py "https://space.bilibili.com/12345/channel/collectiondetail?sid=67890"
# 输出: {"type": "collection", "total": 5, "videos": [...]}

# 2. 逐个下载并拆帧
python scripts/prepare.py "https://www.bilibili.com/video/BV1aaa" -o ./my-collection/BV1aaa/
python scripts/prepare.py "https://www.bilibili.com/video/BV1bbb" -o ./my-collection/BV1bbb/
# ...

# 3. 逐个分析图片并生成各视频的 视频分析.md
# 4. 合并生成 my-collection/合集视频分析.md
```

### 示例3: 分析长视频

```bash
# 降低帧率，减少图片数量
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./long-video --fps 0.2
```

### 示例4: 禁用去重

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --no-dedup
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
- [ ] 每张图片都标注了帧号，例如：

```text
![frame_xxxx: 描述](./images/frame_xxxx.jpg)
```

- [ ] 图片描述准确反映图片**实际内容**
- [ ] 图片上下文的文字与图片内容**直接相关**
- [ ] 没有随意插入不相关的图片
- [ ] 代码块标注了来源帧号: `<!-- 来自 frame_xxxx -->`

### 代码质量
- [ ] 代码来自图片中的实际代码，不是编造的
- [ ] 代码片段完整，可直接复制使用
- [ ] 完整代码章节汇总了所有代码并标注来源

### 合集相关（仅合集模式）
- [ ] 所有视频都已分析（失败的已标注）
- [ ] `合集视频分析.md` 包含合集概要信息
- [ ] 各视频按合集原始顺序排列
- [ ] 图片路径已调整为相对于合集根目录
- [ ] 各视频标题级别已正确降级

## Tags

`bilibili`, `video-analysis`, `ai`, `frame-extraction`, `markdown`, `tutorial`, `python`, `opencv`, `imagehash`, `collection`, `ugc-season`, `series`

## Compatibility

- Codex: Yes
- Claude Code: Yes
