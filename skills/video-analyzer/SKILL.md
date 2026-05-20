---
name: video-analyzer
description: >-
  **本地**视频文件 / 本地视频目录（mp4/mkv/mov/webm/m4v 等）转结构化专题文档、实操教程或知识整理。
  不处理任何在线 URL。
  Applicable when: 用户在请求中**直接给出本地文件系统路径**（绝对路径或相对路径）指向一个视频文件，或指向一个包含视频的本地目录，要求生成 Markdown 形式的视频内容分析、教程或专题文档
  Not applicable when: 用户提供的是任何在线视频链接（bilibili、YouTube、抖音、b23.tv 短链等），或仅描述视频内容而未提供本地路径
  Example prompts: "分析本地视频 /path/to/xxx.mp4", "分析本机这个视频文件",
    "分析下载好的视频", "本地视频转 Markdown", "本地mp4转文档",
    "把这个本地视频文件转成笔记", "video-analyzer", "local video analysis",
    "分析本地视频目录", "批量分析本地视频目录", "分析这个文件夹里的所有本地视频"
---

# Video Analyzer

## Description

本地视频内容分析工具。用户提供一个**本地视频文件路径**或**包含视频的本地目录路径**，本 skill 自动抽取关键帧，优先提取字幕（视频内嵌轨 → 同名外挂字幕 → image_only fallback），再结合关键帧重组为高质量的专题文档或实操教程。

支持两种模式：

- **单文件模式**：用户输入一个视频文件 → 生成 `<视频名>/视频分析.md`
- **批量目录模式**：用户输入一个目录 → 对目录第一层每个视频独立生成 `<视频名>/视频分析.md`；当视频数 ≥ 2 时，再在原目录下生成 `<目录名>_summary/合集视频分析.md` 合并汇总

**核心特点**：
- 不依赖任何在线接口；纯本地视频处理
- 字幕优先级：**视频内嵌字幕轨 → 同名外挂字幕（.srt/.vtt/.ass/.ssa）→ image_only**；每一步失败/异常自动降级
- 抽帧 + 相邻帧 pHash 去重，保留原始帧到 `images_raw/`、去重后帧到 `images/`
- 输出文档严格图文对应，使用 `![frame_xxxx: 描述](./images/frame_xxxx.jpg)` 格式
- **输出目录始终生成在视频文件同级**（统一规则）
- **目录冲突自动避让**：若目标输出目录已存在，自动追加 `_YYYYMMDD-HHMMSS` 后缀保留旧结果

## Source & Documentation

| 工具 | 用途 | Repository | 文档 |
|------|------|------------|------|
| **Python** | 执行准备脚本 | - | [官网](https://www.python.org/) |
| **OpenCV** | 视频读取与抽帧 | [opencv/opencv](https://github.com/opencv/opencv) | [文档](https://docs.opencv.org/) |
| **Pillow + ImageHash** | 感知哈希去重 | [JohannesBuchner/imagehash](https://github.com/JohannesBuchner/imagehash) | [Pillow](https://pillow.readthedocs.io/) |
| **ffmpeg / ffprobe（可选）** | 内嵌字幕轨抽取 | [FFmpeg](https://ffmpeg.org/) | [文档](https://ffmpeg.org/documentation.html) |

## Installation

### 1. Python 3.10+

```bash
python --version
```

### 2. Python 依赖

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install opencv-python-headless pillow ImageHash
```

### 3. ffmpeg / ffprobe（可选，用于内嵌字幕）

如果未安装 `ffmpeg`，内嵌字幕轨步骤会被静默跳过，直接降级到外挂字幕扫描。

```bash
# Linux (Debian/Ubuntu)
sudo apt install ffmpeg
# macOS
brew install ffmpeg
# Windows
choco install ffmpeg
```

## Scope

- 输入是**本地视频文件**或**本地目录**
- 输出是**专题文档 / 实操教程 / 结构化知识整理**
- 字幕优先；缺失时退回到纯关键帧分析
- 不适用：纯字幕逐句转录、简短摘要、非视频文件

## Internal Workflow

- 判断输入是文件还是目录；目录则枚举第一层视频文件并向用户展示待分析列表
- `scripts/prepare.py` 按 `--fps` 抽帧到 `images_raw/`，相邻帧 pHash 去重后输出到 `images/`
- `scripts/text_prepare.py` 按"内嵌字幕 → 外挂字幕 → image_only"链路准备文本主线
- 结合 `text_segments.json`（如有）与 `images/` 分批做多模态分析
- 按主题（非时间线流水账）重组为 `视频分析.md`
- 目录模式额外把各视频文档合并为 `合集视频分析.md`

## Provided Scripts

### `scripts/prepare.py` — 本地视频抽帧 + 去重

```bash
python scripts/prepare.py <视频路径> [-o 输出目录] [--fps 1.0] [--similarity 0.80] [--no-dedup]
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `video` | 本地视频文件路径（必需，位置参数） | - |
| `-o, --output` | 输出目录 | `<视频所在目录>/<视频文件名去扩展名>/` |
| `--fps` | 抽帧帧率 | `1.0` |
| `--similarity` | 相邻帧 pHash 相似度去重阈值（0-1） | `0.80` |
| `--no-dedup` | 禁用去重 | `false` |

**支持的视频扩展名（默认稳定支持）**：`.mp4` `.mkv` `.mov` `.webm` `.m4v`

其它扩展名仍允许传入，但若 OpenCV/ffmpeg backend 无法解码会报错，建议先转码为 mp4。

**目录冲突避让**：若目标 `output` 目录已存在，自动追加 `_YYYYMMDD-HHMMSS` 后缀避免覆盖。例如 `My Demo Video/` 已存在则生成 `My Demo Video_20260520-143015/`。

**输出结构**：

```
<output>/
├── images_raw/       # 按 fps 抽取的全部原始帧
├── images/           # 去重后的关键帧（重新编号）
├── metadata.json     # source_path / duration / fps / 帧统计
└── frames.json       # 保留帧 → source_file + 时间戳 + 相邻相似度
```

**关键输出（stdout）**：脚本会在最后一行打印 `[OK] {"output_dir": ..., "raw_frame_count": ..., "final_frame_count": ...}`，**Workflow 必须解析此处的 `output_dir` 作为 text_prepare.py 的 `-o`**，因为可能由于冲突已加了时间戳后缀。

### `scripts/text_prepare.py` — 字幕优先 / 图片兜底的文本准备

```bash
python scripts/text_prepare.py <视频路径> -o <prepare.py 实际输出目录>
```

| 参数 | 说明 |
|------|------|
| `video` | 本地视频路径（必需，位置参数，用于定位外挂字幕） |
| `-o, --output` | 必须与 `prepare.py` 实际输出目录一致（解析自 prepare.py stdout） |

**字幕优先级链**（任一步骤失败/异常自动降级）：

1. **视频内嵌字幕轨**（需要 ffmpeg/ffprobe）
   - 选轨优先级：中文 (`zh`/`chi`/`zho`/...) → 英文 (`en`/`eng`) → 第一条
   - 跳过 bitmap 字幕（`dvd_subtitle` / `hdmv_pgs_subtitle` 等）
2. **外挂字幕**：扫描视频同目录下同名的 `.srt` / `.vtt` / `.ass` / `.ssa`
   - 多语言后缀（如 `name.zh.srt`、`name.en.srt`）优先中文
3. **image_only fallback**

**输出（stdout JSON）**：

- 字幕命中：`{"mode": "subtitle", "subtitle_count": N, "origin": {...}, "files": {...}}`，并写出 `subtitles.json` / `subtitles.txt` / `text_segments.json`
- 字幕缺失：`{"mode": "image_only", "reason": "subtitle_unavailable"}`

## Workflow (Prompt)

你是一个本地视频内容分析助手。当用户提供本地视频路径或目录路径时，按以下步骤执行。

### Step 0: 判断输入是文件还是目录

- **文件** → 单文件模式
- **目录** → 批量目录模式（仅枚举该目录第一层、按文件名排序、过滤为已知视频扩展名）
  - 把待分析列表（文件名 + 文件大小或时长）展示给用户并**等待确认**
  - 若目录下视频数 = 1 → 退化为单文件模式，无需 summary 目录
  - 若目录下视频数 ≥ 2 → 进入批量流程，最后合并

### 全局 Step 1: 抽帧 + 去重

```bash
python scripts/prepare.py "<视频路径>"
```

**fps 建议**：

| 视频时长 | `--fps` |
|----------|---------|
| < 10 分钟 | 1.0（默认） |
| 10–30 分钟 | 0.5 |
| > 30 分钟 | 0.2 |

**必须**从 stdout 末尾 `[OK] {...}` 行解析 `output_dir`，传给后续 `text_prepare.py`。

### 全局 Step 2: 准备文本主线

```bash
python scripts/text_prepare.py "<视频路径>" -o "<Step 1 解析得到的 output_dir>"
```

- 返回 `mode=subtitle` → 后续优先读取 `text_segments.json` 建立章节脉络
- 返回 `mode=image_only` → 直接进入纯图片分析，**不要伪造口播内容**

### 全局 Step 3: 联合分析文本与关键帧

**分批策略**（与 bilibili-analyzer 一致）：

| 总图片数 | 分批数量 |
|---------|---------|
| 1–30 | 1 批 |
| 31–60 | 2 批 |
| 61–120 | 3 批 |
| 121–200 | 4 批 |
| 200+ | 5 批 |

**任务模式**：默认在当前会话中顺序执行；用户说 "使用subagent" / "并行分析" / "用task分析" 时改用 Task 工具并行。

**多模态分析 Prompt 模板**：

```
结合 <output_dir>/text_segments.json（如果存在）与 <output_dir>/images/ 下的 frame_xxxx.jpg 到 frame_yyyy.jpg 进行分析。

【目标】
1. 先用文本主线（若有）理解这一段在讲什么
2. 再核对每张图片真实出现了什么
3. 记录代码 / UI / 终端 / 报错 / 按钮位置 / 页面变化等视觉证据
4. 标注文本与画面是否一致；冲突显式写出，不要强行合并
5. 如果文本未覆盖某图，只根据图片描述
6. image_only 模式下不要伪造字幕

【输出格式】
## 本批摘要
- 文本主线：...
- 关键视觉主题：...

## frame_xxxx.jpg
- 文本关联：...
- 场景：[代码编辑器 / 终端 / 浏览器 / PPT / 对话 / 其他]
- 视觉内容：...
- 画面文字/代码：```...```
- 一致性判断：[一致 / 补充 / 冲突]
- 要点：...
```

### 全局 Step 4: 生成 `视频分析.md`

把每帧分析按**主题**重新组织（不是时间线流水账）。

**判断视频类型**：
- **实操类**（编程、操作演示、配置等）→ 操作教程模板
- **知识类**（概念、原理、经验等）→ 专题文档模板

**关键原则**：
1. **章节主线/叙事顺序**优先参考字幕；缺失则按主题归类
2. **代码 / UI / 报错 / 操作位置**优先参考图片
3. **文本与图片冲突**显式标注
4. **图文严格对应**：`![frame_xxxx: 图片实际内容](./images/frame_xxxx.jpg)`
5. **代码注明来源**：`<!-- 来自 frame_xxxx -->`
6. **独立可读**：不看视频也能理解

### 批量目录模式额外阶段（Phase C: 合并）

当目录下视频数 ≥ 2 时，把每个子视频的 `视频分析.md` 合并成 `<原目录>/<目录名>_summary/合集视频分析.md`。

合并规则：
1. summary 目录命名 `<原目录名>_summary`；若已存在则追加 `_YYYYMMDD-HHMMSS`
2. 文件开头写入合集概要（视频总数、生成时间、列表）
3. 按文件名顺序拼接，每个视频前加一级标题：`# 第N个: {视频文件名}`
4. 子文档内部标题统一**降一级**（`#` → `##`，`##` → `###`，依此类推）
5. 图片相对路径调整为 `../<视频名>/images/frame_xxxx.jpg`（summary 在子目录内，需 `../` 回到原目录访问兄弟视频结果目录）
6. 失败视频的位置写入 `❌ 该视频分析失败：{原因摘要}` 占位段

### 失败处理（统一规则）

- 目录模式下任一视频在 Step 1/2/3/4 抛错时：
  1. 捕获并记录到 `<原目录>/<目录名>_summary/errors.log`
  2. **继续处理后续视频**，不阻塞整体流程
  3. 在最终 `合集视频分析.md` 对应位置写入失败占位

## Output Format

### 实操教程类

```markdown
# {教程主题}

## 简介
{教程目标 / 前置条件}

## 环境准备
{软件 / 配置}

## 操作步骤

### 1. {步骤标题}
{说明}

![frame_xxxx: 准确描述](./images/frame_xxxx.jpg)

<!-- 来自 frame_xxxx -->
```代码```

### 2. {步骤标题}
...

## 完整代码
<!-- 汇总自 frame_xxxx, frame_yyyy -->
...

## 常见问题
## 总结
```

### 知识文档类

```markdown
# {主题}

## 概述
{背景 / 为什么重要}

## {章节1}
{内容}

![frame_xxxx: 描述](./images/frame_xxxx.jpg)

## {章节2}
...

## 核心要点
- ...

## 延伸阅读
```

### 合集合并文档（目录模式）

```markdown
# {目录名}

## 合集概要
- **视频总数**: N
- **生成时间**: YYYY-MM-DD HH:MM
- **来源目录**: /path/to/<目录>

## 视频列表
1. ...
2. ...

---

# 第1个: {视频1文件名}

## {视频1的章节1}
...
![frame_xxxx: 描述](../<视频1文件名>/images/frame_xxxx.jpg)

---

# 第2个: {视频2文件名}
...
```

### 图片插入规范

| 规则 | 说明 |
|------|------|
| **帧号必标注** | `![frame_0015: 描述](./images/frame_0015.jpg)` |
| **描述准确** | 反映图片实际内容，不是期望内容 |
| **图文匹配** | 上下文与图片内容直接相关 |
| **代码注源** | `<!-- 来自 frame_0025 -->` |
| **不乱插图** | 没有合适的图就不插 |
| **合集路径** | 合集文档使用 `../<视频名>/images/frame_xxxx.jpg` |

### 文本主线使用规范

| 规则 | 说明 |
|------|------|
| **字幕优先** | `text_segments.json` 存在时章节主线优先参考字幕 |
| **代码/UI 以图为准** | 优先以图片为准 |
| **冲突显式标注** | 不要强行合并 |
| **image_only 不伪造** | `mode=image_only` 时不要编造口播 |

## Examples

### 示例 1: 单视频

```bash
python scripts/prepare.py "/path/to/Demo.mp4" --fps 0.5
# stdout 末尾: [OK] {"output_dir": "/path/to/Demo", "raw_frame_count": 600, "final_frame_count": 42}
python scripts/text_prepare.py "/path/to/Demo.mp4" -o "/path/to/Demo"
# → 生成 /path/to/Demo/视频分析.md
```

### 示例 2: 目录批量

```bash
# 目录 /path/to/my_videos/ 含 a.mp4, b.mp4, c.mp4
python scripts/prepare.py "/path/to/my_videos/a.mp4"
python scripts/text_prepare.py "/path/to/my_videos/a.mp4" -o "/path/to/my_videos/a"
# → 生成 /path/to/my_videos/a/视频分析.md
# ... 对 b.mp4, c.mp4 同样
# → 最后合并到 /path/to/my_videos/my_videos_summary/合集视频分析.md
```

### 示例 3: 长视频降帧率

```bash
python scripts/prepare.py "/path/to/long.mp4" --fps 0.2
```

### 示例 4: 输出目录冲突自动加时间戳

```bash
python scripts/prepare.py "/path/to/Demo.mp4"
# 第二次运行：自动写到 /path/to/Demo_20260520-143015/
```

### 示例 5: 外挂字幕

```
/path/to/
├── lecture.mp4
└── lecture.zh.srt    # 自动被 text_prepare.py 识别（优先于 .en.srt）
```

### 示例 6: 禁用去重

```bash
python scripts/prepare.py "/path/to/Demo.mp4" --no-dedup
```

## Quality Checklist

### 内容质量
- [ ] 内容已按主题重组，非时间线流水账
- [ ] 章节清晰、独立可读
- [ ] 包含概述/前置条件与总结
- [ ] 字幕可用时主线与字幕一致；image_only 时未伪造口播

### 图文对应
- [ ] 每张图都标注帧号 `![frame_xxxx: 描述](./images/frame_xxxx.jpg)`
- [ ] 描述准确反映图片实际内容
- [ ] 没有乱插无关图
- [ ] 代码块标注 `<!-- 来自 frame_xxxx -->`

### 代码质量
- [ ] 代码来自图片实际内容，不是编造
- [ ] 完整代码章节汇总并标源

### 文本链路
- [ ] `text_prepare.py` 的 `mode` 已确认
- [ ] 字幕与图片冲突处显式标注

### 目录模式
- [ ] 待分析列表已向用户确认
- [ ] 所有视频已处理或失败已标注
- [ ] `合集视频分析.md` 包含概要、列表与失败说明
- [ ] 合集文档图片路径已调整为 `../<视频名>/images/...`
- [ ] 子文档标题级别已正确降级
- [ ] `errors.log`（若有）记录了所有失败原因

### 输出目录
- [ ] 单视频结果目录在视频同级
- [ ] 目录模式 summary 目录在原目录内
- [ ] 目录冲突时已自动加 `_YYYYMMDD-HHMMSS` 后缀

## Tags

`local-video`, `video-analysis`, `frame-extraction`, `subtitle`, `multimodal`, `markdown`, `tutorial`, `python`, `opencv`, `imagehash`, `ffmpeg`, `batch`

## Compatibility

- Codex: Yes
- Claude Code: Yes
