# Douyin Video Fetch（抖音视频下载）

OpenClaw 技能：支持通过 URL 或 `video_id` 下载抖音视频，支持批量任务与 JSON 结构化输出。

## 功能

- 按抖音视频 URL 下载
- 按 `video_id` 下载
- 支持批量输入（文件）
- 默认按 `video_id` 自动命名
- 支持 `--json` 输出，方便接入自动化流程

## OpenClaw 安装与使用（新增）

### 1) 安装 OpenClaw

请先按官方文档完成 OpenClaw 安装与初始化：

- Docs: `https://docs.openclaw.ai/start/getting-started`

### 2) 安装 ClawHub CLI（用于安装 Skill）

```bash
npm i -g clawhub
```

### 3) 登录 ClawHub 并安装本技能

```bash
clawhub login
clawhub install douyin-video-fetch
```

> 提示：如果你有多个工作目录，建议在 OpenClaw 的 workspace 目录里执行上面命令。

### 4) 让 OpenClaw 加载技能

安装后，建议新开一个 OpenClaw 会话（或重启当前会话），让技能稳定生效。

### 5) 在 OpenClaw 里这样使用

你可以直接对 OpenClaw 说：

- `帮我下载这个抖音视频：https://www.douyin.com/video/7599980362898427178`
- `帮我批量下载 input.txt 里的抖音链接，输出到 downloads/douyin`
- `下载后用 JSON 返回每条结果`

---

## 脚本直接使用（开发/调试）

### 依赖

- Python 3.10+
- `playwright`
- `aiohttp`
- Playwright Chromium

安装依赖：

```bash
pip install playwright aiohttp
playwright install chromium
```

### 用法

在当前技能目录下执行：

```bash
python scripts/fetch_video.py "https://www.douyin.com/video/7599980362898427178"
```

按 `video_id` 下载：

```bash
python scripts/fetch_video.py 7599980362898427178
```

批量下载（每行一个 URL 或 `video_id`）：

```bash
python scripts/fetch_video.py --file input.txt --output-dir ./downloads/douyin
```

输出 JSON 结果：

```bash
python scripts/fetch_video.py --file input.txt --output-dir ./downloads/douyin --json
```

### 输出约定

- 默认输出目录：`downloads`
- 文件名：`<video_id>.mp4`

## 说明

- 该仓库是 OpenClaw Skill 源码仓库。
- 技能元信息与调用说明见 `SKILL.md`。

---

# English (Short)

OpenClaw skill for downloading Douyin videos by URL or `video_id`, with batch mode and JSON output.

- Install skill: `clawhub install douyin-video-fetch`
- Script: `scripts/fetch_video.py`
- Skill metadata: `SKILL.md`
