---
name: bilibili-analyzer
description: >-
  B站/bilibili视频、合集/系列及多P视频转专题文档、实操教程或结构化知识整理
  Applicable when: 用户提供bilibili/B站视频、合集/系列链接或多P视频链接，要求转文档、生成教程、课程笔记或步骤化学习材料
  Example prompts: "分析B站视频", "bilibili转文档", "视频转教程",
    "合集", "视频合集", "UGC合集", "系列视频", "全集", "分P全部",
    "B站合集分析", "合集转文档", "分析整个合集", "批量分析视频", "分析合集视频"
---

# Bilibili Analyzer

## Description

B站视频、合集/系列与多P视频内容分析工具。提供视频、合集/系列 URL 或多P视频链接后，自动下载视频、拆解成帧图片，并优先获取平台字幕；若字幕不可用，则直接分析视频提取的关键帧，生成**高质量的专题文档或实操教程**。

支持两种模式：
- **单视频模式**：只分析当前一个视频；如果当前链接属于多P视频，则只分析当前这一P，生成 `视频分析.md`
- **合集模式**：统一表示“多视频 / 多P 范围分析”。可用于分析 UGC 合集、系列视频，或当前多P视频的全部P；最终生成 `合集视频分析.md` 或 `分P视频分析.md`

这个 skill 的内部实现基于 Python：先通过 Bilibili 公共接口下载视频，再抽取原始帧到 `images_raw/`，按相邻帧相似度做去重并输出关键帧到 `images/`；随后优先获取平台字幕，字幕不可用时直接进入关键帧图片分析；最后将可用文本主线与关键帧分析结果重组为可直接阅读或执行的 Markdown 文档。

**核心特点**:
- 不是简单的时间线记录，而是**重新组织整理**成一篇完整的文档
- 实操类视频 → 生成**可直接使用的操作教程**
- 知识类视频 → 生成**结构化的专题文档**
- 字幕优先，字幕不可用时直接进入图片分析，由关键帧提供视觉证据
- 基础流程使用 Python 直接调用 Bilibili 公共接口下载视频，不依赖 `.NET`
- 保留 `images_raw/` 原始帧，并将去重后的关键帧输出到 `images/`
- 报告中插入关键截图，使用 `![描述](./images/frame_xxxx.jpg)` 格式
- 自动判断当前请求是“单视频范围”还是“多视频 / 多P 范围”，并处理合集、系列与多P嵌套场景

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
- `collection.py` 与 `text_prepare.py` 仅使用 Python 标准库访问 Bilibili 接口与字幕数据
- 本 skill 不要求安装 `.NET`

## Scope

- 输入是 B站/bilibili 视频或合集链接，输出目标是专题文档、实操教程、课程笔记或结构化知识整理
- 支持单个视频、UGC 合集 / 系列视频，以及多P视频全部分P的批量分析
- 支持“字幕优先 -> 图片兜底”的内容理解链路
- 适合把视频内容重组成可阅读、可复用的文档，而不是保留时间线流水账
- 不适用于纯字幕提取、逐句转录，或只做简短摘要的场景

## Internal Workflow

- 先根据用户措辞判断当前请求是“单视频模式”还是“合集模式”
- 使用 `scripts/resolve_scope.py` 把原始 URL 解析成**最终要处理的明确单元**（单视频、当前P、当前 BV 的全部P、整个合集 / 系列）
- `scripts/prepare.py` 只处理 resolver 产出的明确视频 URL 或明确 `?p=` page URL，并按设定 `fps` 抽取原始帧到 `images_raw/`
- `scripts/text_prepare.py` 只处理 resolver 产出的明确视频 URL 或明确 `?p=` page URL，优先获取平台字幕；字幕不可用时直接进入仅图片模式
- 对相邻帧执行基于 `ImageHash` 的相似度去重，将保留帧输出到 `images/`
- 结合 `text_segments.json` 与关键帧分析结果，按主题重组内容并生成 `视频分析.md`
- 合集模式下，将各视频或各P的 `视频分析.md` 先按底层单元合并，再根据目标范围生成 `合集视频分析.md` 或 `分P视频分析.md`
- 需要时保留 `metadata.json`、`frames.json`、`subtitles.json`、`text_segments.json` 等中间产物，便于后续核对时间轴与图片来源

## Provided Scripts

本 skill 提供了四个脚本：

### scripts/resolve_scope.py — 统一解析最终处理范围

用于把用户提供的原始 URL 和当前模式（`single` / `collection`）解析成**最终应该处理的明确单元列表**。

它负责：

- 解析 `b23.tv` 短链接
- 判断当前输入是合集 / 系列总链接、普通视频链接、当前P链接还是多P总链接
- 在单视频模式下，把总链接下沉到第一个可分析单元
- 在合集模式下，决定是处理整个合集 / 系列，还是处理当前 BV 的全部P
- 展开合集 / 系列中嵌套的多P子视频，给出完整目标结构

**运行方式**: 使用 Python 直接执行

#### 使用方法

```bash
# 单视频模式
python scripts/resolve_scope.py "<URL>" --mode single

# 合集模式
python scripts/resolve_scope.py "<URL>" --mode collection
```

#### 关键输出字段

| 字段 | 说明 |
|------|------|
| `input_link_type` | 当前链接类型，例如 `collection_root`、`video`、`current_p`、`multi_p_root` |
| `resolved_scope` | 最终处理范围，例如 `single_video`、`single_page`、`all_pages_of_current_bv`、`full_collection` |
| `display_logic` | 应向用户展示的处理逻辑说明 |
| `targets` | 最终待处理单元列表；其内 URL 已经是可直接传给 `prepare.py` / `text_prepare.py` 的明确目标 |

**重要说明**：

- 后续执行 `prepare.py` / `text_prepare.py` 时，优先使用 `resolve_scope.py` 输出的 `targets[*].url`
- 不要直接把多P总链接传给 `prepare.py` / `text_prepare.py`

### scripts/prepare.py — 视频下载与拆帧

用于下载单个**明确视频单元**、提取原始帧并输出去重后的关键帧。

**运行方式**: 使用 Python 直接执行

#### 使用方法

```bash
# 基本用法
python scripts/prepare.py "<视频URL>" -o <输出目录>

# 示例
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output

# 明确处理某个分P
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=2" -o ./output-p2

# 长视频（降低帧率）
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --fps 0.5
```

**多P注意**：如果目标视频是多P视频，必须先通过 `resolve_scope.py` 得到明确的 `?p=` URL，再传给 `prepare.py`。`prepare.py` 不再接受模糊的多P总链接。

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

用于检测 URL 是单视频还是合集 / 系列，并输出结果 JSON。这个脚本现在更适合作为 **resolver 的父级列表获取器** 使用。

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
  "also_in_series": true,
  "series_info": {"collection_title": "系列标题", "total": 5},
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

#### 多P说明

`collection.py` 只负责**合集 / 系列**检测，不负责多P总列表枚举。多P视频请通过 `view` API 的 `pages` 字段判断与展开：

- `pages <= 1`：普通单P视频
- `pages > 1` 且 URL 含 `?p=`：当前P链接
- `pages > 1` 且 URL 不含 `?p=`：多P总链接

### scripts/text_prepare.py — 字幕优先 / 图片兜底的文本准备

用于为后续内容理解准备文本主线。它遵循以下优先级：

1. **优先使用平台字幕**
2. **字幕不可用时，返回仅图片模式**

**运行方式**: 使用 Python 直接执行

#### 使用方法

```bash
# 基本用法
python scripts/text_prepare.py "<视频URL>" -o <输出目录>

# 明确处理某个分P
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=2" -o ./output-p2
```

#### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `url` | B站视频 URL（必需） | - |
| `-o, --output` | 输出目录 | 当前目录 |

**多P注意**：如果目标视频是多P视频，必须先通过 `resolve_scope.py` 得到明确的 `?p=` URL，再传给 `text_prepare.py`。`text_prepare.py` 不再接受模糊的多P总链接。

#### 输出模式

**字幕模式**：如果平台字幕可用，输出：

```json
{
   "mode": "subtitle",
   "subtitle_count": 120,
   "files": {
      "subtitles_json": "/abs/output/subtitles.json",
      "subtitles_txt": "/abs/output/subtitles.txt",
      "text_segments_json": "/abs/output/text_segments.json"
   }
}
```

**仅图片模式**：如果字幕不可用，输出：

```json
{
   "mode": "image_only",
   "reason": "subtitle_unavailable"
}
```

#### 中间产物说明

| 文件 | 说明 |
|------|------|
| `subtitles.json` | 字幕模式下的结构化字幕结果 |
| `subtitles.txt` | 字幕纯文本 |
| `text_segments.json` | 字幕模式下统一后的时间轴文本片段，供后续分析使用 |

## Workflow (Prompt)

你是一个视频内容分析助手。当用户提供B站视频、合集/系列链接或多P视频链接时，按以下步骤执行：

### Step 0: 判断单视频模式 / 合集模式

先把用户请求映射成两种范围之一：

- **单视频模式**：只分析当前一个视频；如果当前链接属于多P视频，则只分析当前这一P
- **合集模式**：统一表示“多视频 / 多P 范围分析”，包括合集、系列、批量视频、全集、分P全部等语义

#### 0A. 先判断用户意图属于哪一类

**合集模式关键词**："合集"、"视频合集"、"UGC合集"、"系列视频"、"全集"、"分P全部"、"B站合集分析"、"合集转文档"、"分析整个合集"、"批量分析视频"、"分析合集视频" 等。

规则：

- 只要用户请求语义明确落在上面这些“多视频 / 多P 范围”关键词中，就进入**合集模式**
- 其余情况默认进入**单视频模式**

#### 0B. 再判断链接本身属于哪一类

需要区分 4 种链接：

1. **合集 / 系列总链接**
  - 例如 `space.bilibili.com/{mid}/channel/collectiondetail?sid=...`
  - 例如 `space.bilibili.com/{mid}/channel/seriesdetail?sid=...`
2. **普通视频链接**
  - 例如 `https://www.bilibili.com/video/BVxxx`
  - 可能是普通单P视频，也可能是合集/系列中的某一个视频
3. **当前P链接**
  - 例如 `https://www.bilibili.com/video/BVxxx?p=2`
4. **多P总链接**
  - `view` API 中 `pages > 1`
  - 用户提供的是 `BV` 链接本身，但 URL 不带 `?p=`

判断方法：

1. 如有 `b23.tv` 短链接，先解析到最终 URL
2. 如果是 `space.bilibili.com` 的合集 / 系列页面，直接视为“合集 / 系列总链接”
3. 如果是 `BV` 链接，先调用 `view` API 读取 `pages`
4. 若 `pages > 1` 且 URL 含 `?p=` → 视为“当前P链接”
5. 若 `pages > 1` 且 URL 不含 `?p=` → 视为“多P总链接”
6. 如需判断当前 BV 是否属于合集 / 系列，再调用 `collection.py`

#### 0C. 单视频模式的路由规则

| 链接类型 | 处理方式 |
|----------|----------|
| 合集 / 系列总链接 | 正常分析**第一个可分析单元**：先取合集 / 系列中的第一个视频；如果这个第一个视频本身还是多P视频，则继续下沉到它的第一P |
| 多P总链接 | 正常分析**第一P** |
| 当前P链接 | 按**当前这一P**执行单视频分析 |
| 普通 BV 链接（即便它属于合集/系列中的某一个视频） | 按**当前这一个视频**执行单视频分析 |

对应场景：

- 用户在单视频模式下提供了合集 / 系列中的某一个视频链接 → 正常分析当前这一个视频
- 用户在单视频模式下提供了多P视频中的某一个 `?p=` 链接 → 正常分析当前这一P
- 用户在单视频模式下提供了合集 / 系列 / 多P 的**总链接** → 正常下沉到第一个可分析单元（第一个视频或第一P）

A.2 补充要求：

- 当单视频模式命中合集 / 系列 / 多P的总链接并触发自动下沉时，必须先向用户**展示当前处理逻辑**，明确说明：
  - 原始链接被识别成了哪一种总链接（合集 / 系列总链接，或多P总链接）
  - 当前将按什么规则下沉（第一个视频，或第一P）
  - 最终将处理的具体单元是什么（例如“将分析合集中的第一个视频 XXX”或“将分析当前多P视频的第1P：XXX”）
  - 用户若希望处理范围不同，应使用什么措辞（例如“分P全部”“分析整个合集”）

#### 0D. 合集模式的路由规则

合集模式下，先看用户提供的链接**落在嵌套结构的哪一层**，并始终优先处理“用户当前指到的最底一层完整单元”。

| 链接 / 检测结果 | 处理方式 |
|----------------|----------|
| 合集 / 系列总链接 | 分析整个合集 / 系列 |
| 当前 BV 属于合集 / 系列，且当前 BV 不是多P视频 | 分析整个合集 / 系列 |
| 当前 BV 是多P视频（无论它是否还属于合集 / 系列） | 分析**当前 BV 的全部P** |
| 当前P链接 | 分析**当前 BV 的全部P** |

嵌套处理规则：

- 如果用户提供的链接**本身就落在多P视频这一层**，即使这个多P视频还属于更外层合集 / 系列，也只处理**当前 BV 的全部P**
- 如果用户提供的是合集 / 系列中的其他视频链接，且这个合集 / 系列里**另外某些视频**是多P视频，则仍按**整个合集 / 系列**处理，但要提前提醒用户：后续会把这些多P子视频展开成全部P一起分析

#### 0E. 执行步骤

1. 先根据用户措辞判断是单视频模式还是合集模式
2. 调用 `resolve_scope.py` 得到最终处理范围：

```bash
# 单视频模式
python scripts/resolve_scope.py "<URL>" --mode single

# 合集模式
python scripts/resolve_scope.py "<URL>" --mode collection
```

3. 读取 resolver 输出中的 `input_link_type`、`resolved_scope`、`display_logic`、`targets`
4. 如果 resolver 在单视频模式下触发了“总链接自动下沉”，先把 `display_logic` 明确展示给用户，再继续分析
5. 如果 resolver 输出的是合集 / 系列或“当前 BV 的全部P”，则基于 `targets` 生成目录结构并在开始处理前展示给用户
6. 后续调用 `prepare.py` / `text_prepare.py` 时，只使用 resolver 输出的明确 `targets[*].url`

### 全局 Step 1: 下载视频并拆帧

使用提供的脚本下载视频并拆解成帧图片：

```bash
python scripts/prepare.py "<视频URL>" -o <输出目录>
```

**注意事项**:
- 短视频（<10分钟）: 使用默认 `--fps 1`
- 中等视频（10-30分钟）: 使用 `--fps 0.5`
- 长视频（>30分钟）: 使用 `--fps 0.2`

### 全局 Step 2: 准备文本主线（字幕优先，缺失时直接图片分析）

在抽帧完成后，立即为视频准备文本上下文：

```bash
python scripts/text_prepare.py "<视频URL>" -o <输出目录>
```

**优先级规则**:
1. 如果平台字幕可用 → 使用字幕作为主文本来源
2. 如果字幕不可用 → 进入仅图片模式

**执行要求**:
- 无需额外文本回退参数，默认按“字幕 -> 图片”执行
- 如果返回 `mode=subtitle`，后续分析时必须先读取 `text_segments.json`
- 如果返回 `mode=image_only`，后续退回纯图片分析流程

**文本链路原则**:
- 字幕负责提供“讲了什么”“步骤顺序是什么”“口播解释是什么”
- 图片负责提供“画面上具体出现了什么”“代码/UI/报错是否真实出现”
- 没有字幕时，不要伪造口播内容，直接以图片和界面证据组织文档

### 全局 Step 3: 联合分析文本与关键帧

根据 `text_prepare.py` 的输出模式执行内容分析。

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

#### 全局 Step 3.1: 先读文本主线

如果 `text_prepare.py` 返回 `mode=subtitle`：

1. 先读取 `<输出目录>/text_segments.json`
2. 总结视频的主叙事、章节脉络、口播重点
3. 识别每个阶段需要哪些关键帧来支撑文本内容

如果返回 `mode=image_only`：

1. 直接跳到图片分析
2. 不要伪造字幕、不要编造口播内容

#### 全局 Step 3.2: 分批分析关键帧

**多模态分析 Prompt 模板**:

```
结合 <输出目录>/text_segments.json（如果存在）与 <输出目录>/images/ 目录下的 frame_0001.jpg 到 frame_0020.jpg（共20张图片）进行分析。

【你的目标】
1. 先用文本主线理解这一段主要在讲什么
2. 再核对每张图片里真实出现了什么
3. 记录代码、UI、终端输出、错误信息、按钮位置、页面变化等视觉证据
4. 标注“文本说了什么”与“画面展示了什么”是否一致
5. 如果文本没有覆盖某张图，就只根据图片描述该图
6. 如果文本与图片冲突，要明确写出冲突，不要强行合并

【输出格式】

## 本批摘要
- 文本主线: [如果存在文本，就总结该批次讲解重点；否则写“无文本主线，仅图片分析”]
- 关键视觉主题: [这一批图片主要展示什么]

## frame_0001.jpg
- 文本关联: [对应的字幕内容；若无则写“无”]
- 场景: [代码编辑器/终端/浏览器/PPT/对话/其他]
- 视觉内容: [详细描述界面、布局、正在展示的内容]
- 画面文字/代码:
  ```
  [图片中实际可见的文字、代码、命令、输出]
  ```
- 一致性判断: [一致/补充/冲突]
- 要点: [这张图对最终文档最重要的信息]

## frame_0002.jpg
...

【注意】
- 不要伪造字幕或口播内容
- 代码和 UI 名称优先以画面为准
- 概念解释和步骤顺序优先参考字幕
- 任何冲突都要显式标注
```

**分析要点**:
1. 如果存在字幕，先建立语义主线，再让图片补强
2. 如果不存在字幕，只依据图片进行分析
3. 记录每张图片的关键信息，并标注重要帧号
4. 对代码、命令、UI 名称、报错文案必须以图片中真实出现的内容为准

### 全局 Step 4: 生成文档

根据视频类型，将分析结果**重新组织整理**成 `视频分析.md`。

**判断视频类型**:
- 实操类: 编程教程、软件操作、配置演示等
- 知识类: 概念讲解、原理分析、经验分享等

**生成文档时的优先级**:
1. **章节主线 / 叙事顺序**：优先参考字幕
2. **代码 / UI / 页面 / 报错 / 操作位置**：优先参考图片
3. **文本与图片冲突时**：显式写出冲突，不要强行统一

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

1. **先整理文本主线与图片分析结果**
   - 如果有 `text_segments.json`，先用它建立章节脉络
   - 汇总所有帧的分析内容
   - 建立「时间轴文本 -> 关键帧 -> 内容」的对应关系

2. **按主题重新组织内容**（不是按时间顺序流水账）
   - 将相关内容归类到同一章节
  - 用字幕提供的解释串起章节
   - 用关键帧补充截图、界面、代码和操作细节

3. **插入图片时必须核对**
   - 只插入与当前内容**直接相关**的图片
   - 图片描述要准确反映图片实际内容
   - 使用格式: `![frame_xxxx: 图片实际内容描述](./images/frame_xxxx.jpg)`

4. **代码必须来自图片中的实际代码**
   - 不要自己编造代码
   - 代码块标注来源: `<!-- 来自 frame_0025 -->`

**重要原则**:
1. **文本主线 + 图片校验** - 文本负责讲解主线，图片负责真实性校验与细节补充
2. **图文对应** - 每张图片必须与其上下文内容匹配
3. **不要时间线流水账** - 重新组织内容，像写文章一样
4. **代码真实** - 只使用图片中出现的代码，不要编造
5. **独立可读** - 不看视频也能完全理解

### 合集模式分析流程

当 Step 0 进入合集模式时，目标范围可能是以下三种之一：

- 整个合集 / 系列
- 当前多P视频的全部P
- 整个合集 / 系列，但其中某些子视频需要展开成全部P

#### 合集模式 Phase A: 确认待分析列表与目录结构

开始处理前，必须先把 `resolve_scope.py` 输出的最终待分析结构列给用户。

1. 调用 `resolve_scope.py` 并读取 `resolved_scope` 与 `targets`
2. 如果目标是合集 / 系列：直接展示 resolver 输出的视频列表；其中多P子视频应已展开页级结构
3. 如果目标是多P视频：直接展示 resolver 输出的全部P列表
4. 显示标题、总数、每个视频或每个P的标题和时长
5. 显示预计输出目录结构
6. 等待用户确认后开始分析

#### 合集模式 Phase B: 逐个分析视频或分P

##### 情况 A：目标是合集 / 系列中的普通视频

对每个视频依次执行上文的**全局 Step 1（下载视频并拆帧）→ 全局 Step 2（准备文本主线）→ 全局 Step 3（联合分析文本与关键帧，含 3.1 / 3.2）→ 全局 Step 4（生成文档）**：

```bash
# 视频1（URL 来自 resolve_scope.py 的 targets）
python scripts/prepare.py "<视频1 URL>" -o <合集输出目录>/<视频1 BV号>/
python scripts/text_prepare.py "<视频1 URL>" -o <合集输出目录>/<视频1 BV号>/
# → 联合分析文本与关键帧 → 生成 视频分析.md
```

##### 情况 B：目标是当前多P视频的全部P

先通过 `view` API 读取全部 `pages`，再对每个P依次执行上文的**全局 Step 1（下载视频并拆帧）→ 全局 Step 2（准备文本主线）→ 全局 Step 3（联合分析文本与关键帧，含 3.1 / 3.2）→ 全局 Step 4（生成文档）**：

```bash
# P1（URL 来自 resolve_scope.py 的 targets）
python scripts/prepare.py "https://www.bilibili.com/video/<BV>?p=1" -o <多P输出目录>/P01/
python scripts/text_prepare.py "https://www.bilibili.com/video/<BV>?p=1" -o <多P输出目录>/P01/
# → 联合分析文本与关键帧 → 生成 视频分析.md

# P2（URL 来自 resolve_scope.py 的 targets）
python scripts/prepare.py "https://www.bilibili.com/video/<BV>?p=2" -o <多P输出目录>/P02/
python scripts/text_prepare.py "https://www.bilibili.com/video/<BV>?p=2" -o <多P输出目录>/P02/
# → 联合分析文本与关键帧 → 生成 视频分析.md
```

##### 情况 C：合集 / 系列中包含多P子视频

先按合集 / 系列顺序遍历每个子视频：

- 普通单P子视频 → 直接生成 `<BV号>/视频分析.md`
- 多P子视频 → 先展开全部P，生成 `<BV号>/P01/视频分析.md`、`<BV号>/P02/视频分析.md` ...，再在 `<BV号>/分P视频分析.md` 中合并

**注意**：

- 普通视频输出目录使用 BV 号命名（如 `BV1aaa/`）
- 多P视频建议使用 `P01/`、`P02/` ... 作为页级目录名
- 如果某个视频或某个P分析失败，记录错误并继续分析后续单元
- 两个视频之间适当间隔以避免 API 限流

#### 合集模式 Phase C: 合并生成最终文档

根据目标范围，合并策略分两种。

##### 合并为 `分P视频分析.md`

当目标是“当前 BV 的全部P”时：

1. 文件开头写入视频概要信息（视频标题、总P数、UP 主等）
2. 按P顺序拼接每个 `Pxx/视频分析.md`
3. 每个P前加一级标题分隔：`# 第X P: {分P标题}`
4. 各P内部标题级别降一级（`#` → `##`，`##` → `###`，依此类推）
5. 图片路径调整为相对于多P根目录：`./images/frame_xxxx.jpg` → `./P01/images/frame_xxxx.jpg`
6. 分析失败的P在对应位置标注失败信息

##### 合并为 `合集视频分析.md`

当目标是“整个合集 / 系列”时：

1. 文件开头写入合集概要信息（合集标题、视频总数、UP 主等）
2. 按原始顺序拼接每个视频的分析内容
3. 每个视频前加一级标题分隔：`# 第X集: {视频标题}`
4. 普通单P视频直接引用 `<BV号>/视频分析.md`
5. 多P子视频先在 `<BV号>/分P视频分析.md` 中完成本地合并，再把该文件作为这个视频的分析结果纳入合集总文档
6. 图片路径按相对于合集根目录调整：
  - 单P视频：`./images/frame_xxxx.jpg` → `./<BV号>/images/frame_xxxx.jpg`
  - 多P视频：`./images/frame_xxxx.jpg` → `./<BV号>/P01/images/frame_xxxx.jpg`
7. 分析失败的视频或分P在对应位置标注失败信息

**输出目录结构示例 1：当前多P视频的全部P**

```
<多P输出目录>/
├── P01/
│   ├── video.mp4
│   ├── images_raw/
│   ├── images/
│   ├── metadata.json
│   ├── frames.json
│   ├── subtitles.json / text_segments.json
│   └── 视频分析.md
├── P02/
│   ├── video.mp4
│   ├── images_raw/
│   ├── images/
│   ├── metadata.json
│   ├── frames.json
│   ├── subtitles.json / text_segments.json
│   └── 视频分析.md
├── ...
└── 分P视频分析.md
```

**输出目录结构示例 2：合集 / 系列包含多P子视频**

```
<合集输出目录>/
├── <视频1 BV号>/
│   └── 视频分析.md
├── <视频2 BV号>/
│   ├── P01/
│   │   └── 视频分析.md
│   ├── P02/
│   │   └── 视频分析.md
│   └── 分P视频分析.md
├── <视频3 BV号>/
│   └── 视频分析.md
└── 合集视频分析.md
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

{详细说明。优先用字幕建立步骤解释，再用下方图片补充界面、代码和操作细节}

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

{内容。主叙事可来自字幕，视觉细节必须由配图支撑}

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

### 多P文档

```markdown
# {视频标题}

## 视频概要

- **视频标题**: {视频标题}
- **总P数**: {total_pages} 个
- **UP 主**: {uploader}

---

# 第1P: {P1标题}

## {P1章节1}

{内容}

![frame_xxxx: 描述](./P01/images/frame_xxxx.jpg)

---

# 第2P: {P2标题}

## {P2章节1}

{内容}

![frame_xxxx: 描述](./P02/images/frame_xxxx.jpg)

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
| **合集 / 多P路径** | 合集文档中使用 `./<BV号>/images/frame_xxxx.jpg`；多P文档中使用 `./P01/images/frame_xxxx.jpg`；合集中的多P子视频使用 `./<BV号>/P01/images/frame_xxxx.jpg` |

### 文本主线使用规范

| 规则 | 说明 |
|------|------|
| **字幕优先** | 如果 `text_segments.json` 来自字幕，章节主线优先参考字幕 |
| **代码/UI 以图为准** | 代码、按钮名、报错文案、页面结构优先以图片为准 |
| **冲突必须标注** | 文本与图片冲突时要明确说明，不要强行合并 |
| **无文本时退回图片模式** | `mode=image_only` 时，不能伪造口播内容 |

## API Reference

### Bilibili API

脚本使用 Bilibili 官方 API：

```
# 获取视频信息（含 ugc_season 合集检测）
GET https://api.bilibili.com/x/web-interface/view?bvid=BV1xx411c7mD

# 多P视频信息来自同一个 view 接口中的 pages 字段
# data.pages[].page       -> 第几P
# data.pages[].part       -> 分P标题
# data.pages[].duration   -> 分P时长
# URL 中是否包含 ?p=     -> 当前是否是具体某一P

# 获取播放地址
GET https://api.bilibili.com/x/player/playurl?bvid=BV1xx411c7mD&cid={cid}&qn=80&fnval=1

# 获取字幕元数据
GET https://api.bilibili.com/x/player/v2?bvid=BV1xx411c7mD&cid={cid}

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

### 文本准备脚本说明

```bash
# 字幕优先，无字幕时直接进入图片模式
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output
```

文本准备逻辑：脚本会优先检查 B 站平台字幕；若字幕存在，则输出 `subtitles.json` 与 `text_segments.json`。若字幕不存在，则直接返回 `image_only` 模式。

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

说明：如果要处理**多P总链接**或**当前P链接**，不要依赖 `collection.py` 返回P列表，而是使用 `view` API 的 `pages` 字段自行展开。

在当前实现里，更推荐直接调用 `resolve_scope.py`，因为它已经把 `view` API 与 `collection.py` 的结果统一成了最终待处理目标。

## Examples

### 示例1: 分析单个视频

```bash
# 1. 解析最终处理范围
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD" --mode single
# 输出: {"resolved_scope": "single_video", "targets": [{...}]}

# 2. 下载并拆帧（使用 targets[0].url）
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./react-tutorial

# 3. 准备文本主线（使用 targets[0].url）
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./react-tutorial

# 4. 联合分析文本与关键帧，生成 react-tutorial/视频分析.md
```

### 示例2: 分析合集

```bash
# 1. 解析最终处理范围
python scripts/resolve_scope.py "https://space.bilibili.com/12345/channel/collectiondetail?sid=67890" --mode collection
# 输出: {"resolved_scope": "full_collection", "targets": [...]} 

# 2. 按 resolver 返回的 targets 逐个下载并拆帧
python scripts/prepare.py "https://www.bilibili.com/video/BV1aaa" -o ./my-collection/BV1aaa/
python scripts/prepare.py "https://www.bilibili.com/video/BV1bbb" -o ./my-collection/BV1bbb/
# ...

# 3. 按 resolver 返回的 targets 逐个准备文本主线
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1aaa" -o ./my-collection/BV1aaa/
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1bbb" -o ./my-collection/BV1bbb/
# ...

# 4. 逐个联合分析文本与关键帧并生成各视频的 视频分析.md
# 5. 合并生成 my-collection/合集视频分析.md
```

### 示例3: 分析多P视频的全部分P

```bash
# 1. 解析最终处理范围
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD" --mode collection
# 输出: {"resolved_scope": "all_pages_of_current_bv", "targets": [{"url": "...?p=1"}, {"url": "...?p=2"}, ...]}

# 2. 列出全部分P并等待用户确认

# 3. 逐P下载并拆帧（使用 resolver 返回的明确 ?p= URL）
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=1" -o ./my-multi-p/P01/
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=2" -o ./my-multi-p/P02/

# 4. 逐P准备文本主线
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=1" -o ./my-multi-p/P01/
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=2" -o ./my-multi-p/P02/

# 5. 逐P生成 视频分析.md，再合并生成 my-multi-p/分P视频分析.md
```

### 示例4: 分析长视频

```bash
# 降低帧率，减少图片数量
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./long-video --fps 0.2
```

### 示例5: 禁用去重

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
- [ ] 如果字幕可用，章节主线与文本时间轴一致
- [ ] 如果字幕不可用，没有伪造口播内容

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

### 文本链路（字幕 / 图片）
- [ ] `text_segments.json` 的来源模式已确认（subtitle / image_only）
- [ ] 如果使用字幕，关键口播解释与章节结构一致
- [ ] 文本与图片冲突的地方已明确标注

### 合集模式相关（仅合集模式）
- [ ] 待分析范围已由 `resolve_scope.py` 确认：是整个合集 / 系列，还是当前 BV 的全部P
- [ ] 开始处理前，已向用户列出视频总数和目录结构
- [ ] 如果是整个合集 / 系列，所有视频都已分析（失败的已标注）
- [ ] 如果存在多P子视频，这些P已在目录结构和最终文档中正确展开
- [ ] `合集视频分析.md` 或 `分P视频分析.md` 已生成且概要信息完整
- [ ] 各视频或各P按原始顺序排列
- [ ] 图片路径已调整为相对于最终根目录
- [ ] 各视频或各P标题级别已正确降级

## Tags

`bilibili`, `video-analysis`, `ai`, `frame-extraction`, `subtitle`, `multimodal`, `markdown`, `tutorial`, `python`, `opencv`, `imagehash`, `collection`, `ugc-season`, `series`, `multi-p`

## Compatibility

- Codex: Yes
- Claude Code: Yes
