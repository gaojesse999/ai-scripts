---
name: local-video-content-analyzer
description: Analyzes local short-form video files together with user-provided engagement data (views, likes, followers) to attribute why a video went viral and produce a replicable blueprint. The skill itself never calls an external model and has no API-key / model configuration — a small Python helper prepares the data and prompt, and the agent (current Cursor session) performs the actual multimodal video analysis. Use when the user asks to analyze a local video file, diagnose a viral hit or flop, or extract replicable viral formulas from saved videos.
disable-model-invocation: true
---

# Local Video Content Analyzer

Analyze LOCAL short-form video files and explain **why they went viral**,
using both the video content and the engagement data the user provides.

The skill has **no model, no adapter, no API key** anywhere. The Python
helper only does data preparation (file discovery, metadata normalization,
metric computation, prompt assembly). The agent that runs this skill
performs the actual video understanding and writes the final report.

## Inputs

### 1. Video files (required, one of)

- `--video / -v PATH` - single local video file
- `--video-dir / -V DIR` - folder; supported extensions: `mp4 mov mkv webm m4v`

### 2. Engagement metadata (required - no data = no attribution)

Provide either a **sidecar JSON** next to each video (`aweme_001.mp4` →
`aweme_001.json`), or a **unified `--metadata FILE`** (CSV or JSON).

Canonical fields per video:

- **Required**: `views`, `likes`, `author_followers`
- **Recommended**: `comments`, `saves`, `shares`
- **Optional**: `title`, `platform`, `publish_time`, `video_duration_sec`,
  `completion_rate`, `ctr`, `author`, `notes`

**Chinese / platform-native field names are accepted as aliases** and
normalized to the canonical names above. Common aliases:

| Canonical | Accepted aliases |
|---|---|
| `views` | `播放` / `播放量` / `播放数` / `plays` / `playCount` |
| `likes` | `点赞` / `点赞数` / `赞` / `diggCount` |
| `comments` | `评论` / `评论数` / `commentCount` |
| `shares` | `分享` / `分享数` / `转发` / `转发数` / `shareCount` |
| `saves` | `收藏` / `收藏数` / `收藏量` / `bookmarks` / `collectCount` |
| `author_followers` | `粉丝` / `粉丝数` / `followers` / `fans` |
| `title` / `platform` / `author` / `publish_time` / `video_duration_sec` / `notes` | `标题` / `平台` / `账号` / `作者` / `发布时间` / `时长` / `备注` |

> Use canonical English keys in metadata (e.g. `saves` for bookmarks). Chinese
> aliases such as `收藏` are still accepted and normalized automatically.
> If a required metric is not visible on the platform, set it to `null` (JSON)
> or leave it blank (CSV). For example, Douyin may not expose `views`; use
> `"views": null`.

Behavior on missing fields:

- Any **required** field missing or `null` → that video is **skipped** with a reason
- Recommended/optional missing → marked `unavailable` in `field_availability`,
  the agent is instructed not to use it as evidence

> Note: `downloads` (save-to-album) is NOT exposed by any consumer platform
> (Douyin, Xiaohongshu, Shipinhao, BiliBili). Do not put it in metadata.
> See [REFERENCE.md](REFERENCE.md) for a full per-platform availability table.

### 3. Control flags (optional)

| Flag | Default | Meaning |
|---|---|---|
| `--viral-threshold` | `5.0` | `views/followers` above this is tagged `breakout` |
| `--output / -o` | `viral-analysis-tasks.json` | Output task-list JSON path |
| `--language / -l` | `zh` | `zh` or `en` for natural-language fields |
| `--max-videos / -n` | `10` | Cap videos per run |

## Usage

```bash
python3 .cursor/skills/local-video-content-analyzer/scripts/analyze_local_videos.py \
  --video-dir ./videos/ \
  --language zh
```

## Output

The helper writes **one** file: `viral-analysis-tasks.json` (path from
`--output`). It is a list, one entry per video, with:

- `file`, `video_path` (absolute path) — so the agent can open / watch the video
- `metadata` (normalized) and `field_availability`
- `metrics` (engagement rates, viral_score, viral_tier)
- `language`
- `prompt` — the full analysis prompt to apply to the video
- `suggested_report_path` — `<video_dir>/<video_basename>-YYYYMMDDHHMMSS.md`,
  using a single timestamp generated **once per script run** and shared
  across all videos in that run

Result: **one run = exactly one `.md` per video**, and the next independent
ask gets a NEW timestamp → a new file, no overwrite of the previous one.
Skipped videos (missing required metadata) get a task entry with a
`skipped` reason and **no** `suggested_report_path` — they never produce
a `.md`.

## Agent workflow (REQUIRED)

This skill is a 2-step pipeline: helper prepares, agent analyzes & writes.

1. Run the helper above. Read `viral-analysis-tasks.json`.
2. For each task **without** a `skipped` field:
   a. Open / watch the video at `video_path` using your own multimodal
      capability. Do not call any external model SDK; do not require any
      API key.
   b. Treat the embedded `prompt` as the analysis spec, but produce a
      full natural-language report (in the requested `language`), not a
      bare JSON dump. Cover: data overview, hook, content structure,
      delivery style, CTA, primary/secondary viral drivers, replicable
      blueprint, anti-patterns, summary, and unavailable fields.
   c. Present that full report to the user in the chat reply.
   d. Write the **EXACT SAME** content to `suggested_report_path`. The
      file content and the chat reply must be identical — no
      summarize-down, no schema-flattening, no "abridged" file version.
3. For each task **with** a `skipped` field: tell the user the reason,
   do not write any `.md`.

## Limitations (read before trusting results)

1. **No video parsing inside the helper**: no frame extraction, no ASR, no
   OCR. Video understanding is entirely the agent's job.
2. **Subtitles are only implicit**: not extracted as a separate transcript;
   short flashes may be missed.
3. **No data → no attribution**: required engagement fields are mandatory.
4. **Unavailable fields are forbidden as evidence** (downloads,
   completion_rate when missing, etc.).
5. **Post-hoc attribution**, not causal proof.

For platform-by-platform field availability, design rationale, and
comparison with the remote-URL `video-content-analyzer` skill, see
[REFERENCE.md](REFERENCE.md).
