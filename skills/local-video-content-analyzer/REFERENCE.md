# Reference — local-video-content-analyzer

Detailed reference for the skill. The main `SKILL.md` only contains the
minimum needed to invoke the helper; this file is loaded only when the
agent needs deeper context.

> The skill has **no model, no adapter, no API key**. The Python helper
> only prepares data; the agent (current Cursor session) performs the
> multimodal video analysis and writes the final per-video Markdown.

---

## 1. Field availability across platforms

Whether a metric is exposed to creators depends on the platform's creator
center. Fields not exposed by the platform must NOT be put into metadata.

> Field-name aliases (e.g. `收藏` → `saves`, `播放` → `views`, `粉丝数` →
> `author_followers`) are normalized by `normalize_metadata()` in
> `scripts/analyze_local_videos.py`. The full alias map is `FIELD_ALIASES`
> in that file — extend it there when you add support for a new platform's
> native field names.

| Field | Tier | Used For | 抖音 | 小红书 | 视频号 | B站 | TikTok |
|---|---|---|:-:|:-:|:-:|:-:|:-:|
| `views` | required | viral score + all rates | ✓ | ✓ | ✓ | ✓ | ✓ |
| `likes` | required | engagement rate | ✓ | ✓ | ✓ | ✓ | ✓ |
| `author_followers` | required | `views / followers` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `comments` | recommended | discussion depth | ✓ | ✓ | ✓ | ✓ | ✓ |
| `saves` (收藏) | recommended | long-tail value | ✓ | ✓ | ✓ | ✓ | ✓ |
| `shares` (转发/分享) | recommended | spread | ✓ | ✓ | ✓ | ✓ | ✓ |
| `completion_rate` | optional, strong | hook effectiveness | partial | partial | ✓ | ✓ | partial |
| `ctr` (封面点击率) | optional, strong | cover effectiveness | partial | partial | ✓ | ✓ | partial |
| `publish_time` | optional | timing attribution | ✓ | ✓ | ✓ | ✓ | ✓ |
| `video_duration_sec` | optional | pacing anchor | auto | auto | auto | auto | auto |
| `downloads` (保存到相册) | **NOT EXPOSED — do not use** | — | ✗ | ✗ | ✗ | ✗ | ✗ |

`partial` = available on some account tiers (e.g. only after enabling 创作者
中心 / 加入官方计划).

---

## 2. Computed metrics

The helper computes these from the metadata before the agent reads the
video. The agent receives them as read-only context and is forbidden from
recomputing.

| Metric | Formula |
|---|---|
| `engagement_rate_pct` | `(likes + comments + shares + saves) / views * 100` |
| `like_rate_pct` | `likes / views * 100` |
| `comment_rate_pct` | `comments / views * 100` |
| `share_rate_pct` | `shares / views * 100` |
| `save_rate_pct` | `saves / views * 100` |
| `viral_score` | `views / author_followers` |
| `viral_tier` | `breakout` (≥2×threshold) / `viral` (≥threshold) / `expected` (≥1) / `underperforming` |

Threshold is set via `--viral-threshold` (default `5.0`).

---

## 3. Task-list JSON schema (helper output)

The helper writes a single file (default `viral-analysis-tasks.json`). It
is a list, one entry per video:

```json
[
  {
    "file": "aweme_001.mp4",
    "video_path": "/abs/path/to/aweme_001.mp4",
    "metadata":           { "...": "what the user provided, normalized" },
    "metrics":            { "engagement_rate_pct": 9.51, "viral_score": 148.0, "viral_tier": "breakout", "...": "..." },
    "field_availability": { "views": "available", "completion_rate": "unavailable", "...": "..." },
    "language": "zh",
    "prompt": "...the full analysis prompt the agent should apply...",
    "suggested_report_path": "/abs/path/to/aweme_001-20260523151200.md"
  }
]
```

`suggested_report_path` uses a **single timestamp** generated once per
helper run and shared across all videos in that run, so:

- One helper run → exactly one `.md` per video (written by the agent).
- A later, independent ask → new timestamp → new file, no overwrite.

---

## 4. Skipped records

When required fields are missing, the entry looks like:

```json
{
  "file": "aweme_999.mp4",
  "video_path": "/abs/path/to/aweme_999.mp4",
  "metadata": { "...": "..." },
  "field_availability": { "views": "unavailable", "author_followers": "unavailable", "...": "..." },
  "skipped": "missing required field(s): views, author_followers"
}
```

No `suggested_report_path` is emitted for skipped entries, and the agent
MUST NOT write a `.md` for them — only surface the reason to the user.

---

## 5. Comparison with `video-content-analyzer`

| | `video-content-analyzer` | `local-video-content-analyzer` |
|---|---|---|
| Input medium | Remote URL | Local file |
| Model handling | Calls Gemini directly (key + SDK in skill) | No model in skill; agent does analysis |
| Engagement data | Optional | Required |
| Output focus | Generic content analysis | Viral attribution + replicable blueprint |
| Platforms | Instagram / TikTok / YouTube | Anything saved locally |

Use `video-content-analyzer` when the source video is reachable by URL and
you just want a content description via Gemini. Use this skill when you
have the video file locally, want a data-grounded "why it went viral"
explanation, and want the analysis done by the agent itself with no model
or key configuration.

---

## 6. Why the helper does NOT preprocess video / subtitles

By design. Adding ffmpeg / Whisper / OCR would force every user to install
a heavy toolchain just to use the skill. Instead, the skill delegates all
multimodal understanding to the agent, and is honest about the trade-off
in `SKILL.md`'s Limitations section.

If you need verbatim hook lines, on-screen text timestamps, or
shot-change detection, run a preprocessing pass externally and include
the extracted text in the `notes` field of the metadata.
