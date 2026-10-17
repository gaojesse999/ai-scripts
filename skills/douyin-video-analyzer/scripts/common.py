#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""douyin-video-analyzer 公共工具库。

仅依赖 Python 3.9+ 标准库（数据解析另需 openpyxl，见 parse_data.py）。
负责：环境配置、ffmpeg 定位、路径约定、文件命名、ffprobe 校验。

设计要点（与 video-to-mp3 / audio-stt 保持一致）：
- .skill.env 从工程根目录向上查找；
- 所有结构化产物围绕“周期目录”组织，文件名能跨 mp4/mp3/txt 对齐；
- 一天多条视频时按发布时间加两位序号。
"""

from __future__ import annotations

import io
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, date, timedelta
from pathlib import Path

# Windows 控制台 UTF-8（与既有 skill 一致）
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)
if hasattr(sys.stderr, "buffer"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", line_buffering=True)


# ── 工程路径 ─────────────────────────────────────────────────────────────────

def engineering_root() -> Path:
    """工程根目录（.skill.env 所在处）。脚本位于 <root>/.agents/skills/<skill>/scripts/。"""
    cur = Path(__file__).resolve().parent
    for parent in [cur, *cur.parents]:
        if (parent / ".skill.env").exists():
            return parent
    # scripts -> skill -> skills -> .agents -> root
    return Path(__file__).resolve().parents[4]


def video_analysis_root() -> Path:
    """视频分析根目录：<工程根>/视频分析。"""
    return engineering_root() / "视频分析"


def materials_root() -> Path:
    """素材根目录：默认 <工程根>/视频分析/视频素材；可用 .skill.env 的 MATERIALS_ROOT 覆盖。"""
    custom = load_env().get("MATERIALS_ROOT", "").strip()
    if custom:
        p = Path(custom)
        if p.is_dir():
            return p
    return video_analysis_root() / "视频素材"


# ── 环境配置 ─────────────────────────────────────────────────────────────────

def load_env(env_path: Path | None = None) -> dict[str, str]:
    """读取工程根 .skill.env，返回键值对（不去依赖系统环境变量）。"""
    path = env_path or (engineering_root() / ".skill.env")
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def python_exe() -> str:
    """用于调用其它 skill 脚本的 Python 解释器。"""
    env = load_env()
    p = env.get("PYTHON_EXE") or shutil.which("python") or shutil.which("python3")
    if not p:
        sys.exit("未找到 Python，请在 .skill.env 配置 PYTHON_EXE。")
    return p


def find_ffmpeg(exe: str = "ffmpeg") -> str:
    """定位 ffmpeg / ffprobe：优先 .skill.env，其次 PATH，再次常见安装路径。"""
    env = load_env()
    if exe == "ffmpeg" and env.get("FFMPEG_PATH") and os.path.isfile(env["FFMPEG_PATH"]):
        return env["FFMPEG_PATH"]
    on_path = shutil.which(exe)
    if on_path:
        return on_path
    win_candidates = [
        rf"D:\Programs\ffmpeg\bin\{exe}.exe",
        rf"C:\ffmpeg\bin\{exe}.exe",
        rf"C:\Program Files\ffmpeg\bin\{exe}.exe",
        rf"C:\Program Files (x86)\ffmpeg\bin\{exe}.exe",
    ]
    for c in win_candidates:
        if os.path.isfile(c):
            return c
    sys.exit(f"未找到 {exe}，请安装 ffmpeg 并加入 PATH，或在 .skill.env 配置 FFMPEG_PATH。")


def get_downloads_dir() -> Path:
    """浏览器下载目录（bu.download / 导出按钮的落点）。"""
    home = Path.home()
    return home / "Downloads"


# ── 周期与命名 ────────────────────────────────────────────────────────────────

def parse_date(s: str) -> date:
    """宽松解析日期，支持 2026-10-09 / 20261009 / 2026/10/9 / 10-09。"""
    s = str(s).strip()
    m = re.search(r"(20\d{2})[-/.年]?\s*(\d{1,2})[-/.月]?\s*(\d{1,2})", s)
    if m:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m2 = re.match(r"^\s*(\d{1,2})[-/.月](\d{1,2})\s*$", s)
    if m2:
        return date(datetime.now().year, int(m2.group(1)), int(m2.group(2)))
    raise ValueError(f"无法解析日期：{s!r}")


def period_dir_name(start: date, end: date) -> str:
    """周期目录名：跨区间 20261009-20261015；单天 20261016。"""
    if start == end:
        return start.strftime("%Y%m%d")
    return f"{start.strftime('%Y%m%d')}-{end.strftime('%Y%m%d')}"


def daterange(start: date, end: date) -> list[date]:
    """包含起止两端的日历日列表（断更日也在其中）。"""
    days = []
    cur = start
    while cur <= end:
        days.append(cur)
        cur += timedelta(days=1)
    return days


# 文件名非法字符（Windows）+ emoji / 话题清理
_INVALID_CHARS = re.compile(r'[\\/:*?"<>|\r\n\t]')
_HASHTAG = re.compile(r"#\s*[^#\s]+")
_EMOJI = re.compile(
    "[" 
    "\U0001F000-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "✨⭐️️️️️️️️️️️️️️️️→✅🎉🏆🔻🔴🟢🎯📚⚡️💪🔥 ]",
    flags=re.UNICODE,
)


def clean_title(title: str, max_len: int = 14) -> str:
    """把抖音标题清洗成适合做文件名的短标题。

    去 emoji、去 #话题、去非法字符，取前 max_len 个有效字符。
    """
    t = str(title or "")
    t = _HASHTAG.sub("", t)
    t = _EMOJI.sub("", t)
    t = _INVALID_CHARS.sub("", t)
    t = re.sub(r"\s+", "", t)
    t = t.strip("-_. ·，,。.!！?？")
    return t[:max_len] if t else "未命名"


def build_file_base(pub_dt: datetime, index_in_day: int, title: str) -> str:
    """生成 mp4/mp3/txt 共用的文件主名。

    约定 index_in_day：
      - 当天只有 1 条时传 0  -> 20261011-单点突破法（不加序号）
      - 当天有 N 条时传 1..N -> 20261007-01-知识缝接 / 20261007-02-无效假打卡（全部加两位序号）
    调用方（parse_data）需先统计当天总条数，再决定传 0 还是序号。
    """
    day = pub_dt.strftime("%Y%m%d")
    short = clean_title(title)
    if index_in_day and index_in_day >= 1:
        return f"{day}-{index_in_day:02d}-{short}"
    return f"{day}-{short}"


# ── ffprobe 校验 ─────────────────────────────────────────────────────────────

def probe_media(path: Path) -> dict:
    """返回媒体信息：duration、宽高、是否含音频/视频流、编码。"""
    ffprobe = find_ffmpeg("ffprobe")
    cmd = [
        ffprobe, "-v", "error",
        "-show_entries", "format=duration:stream=codec_type,codec_name,width,height",
        "-of", "json", str(path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    info = {"duration": None, "width": None, "height": None,
            "has_video": False, "has_audio": False, "vcodec": None, "acodec": None, "ok": False}
    if proc.returncode != 0:
        return info
    try:
        data = json.loads(proc.stdout or "{}")
    except json.JSONDecodeError:
        return info
    fmt = data.get("format") or {}
    try:
        info["duration"] = float(fmt.get("duration")) if fmt.get("duration") else None
    except (TypeError, ValueError):
        info["duration"] = None
    for st in data.get("streams", []):
        ctype = st.get("codec_type")
        if ctype == "video":
            info["has_video"] = True
            info["vcodec"] = st.get("codec_name")
            info["width"] = st.get("width")
            info["height"] = st.get("height")
        elif ctype == "audio":
            info["has_audio"] = True
            info["acodec"] = st.get("codec_name")
    info["ok"] = info["has_video"] and info["duration"] is not None
    return info


def is_complete_video(path: Path, expect_duration: float | None = None,
                      tol: float = 2.5) -> bool:
    """判定下载的文件是否为“完整可播放”的 mp4。

    必须同时含视频流与音频流，且（若给定时长）时长与作品时长误差 ≤ tol。
    用于排除抖音 DASH 的 HEVC 纯视频流（无音频）和异常拼接长流。
    """
    if not path.exists() or path.stat().st_size < 50_000:
        return False
    info = probe_media(path)
    if not (info["has_video"] and info["has_audio"]):
        return False
    if expect_duration is not None and info["duration"] is not None:
        if abs(info["duration"] - expect_duration) > tol:
            return False
    return True


# ── 台账 ─────────────────────────────────────────────────────────────────────

LEDGER_NAME = "_采集清单.json"


def load_ledger(period_dir: Path) -> dict:
    p = period_dir / LEDGER_NAME
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {}


def save_ledger(period_dir: Path, ledger: dict) -> None:
    period_dir.mkdir(parents=True, exist_ok=True)
    (period_dir / LEDGER_NAME).write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )


if __name__ == "__main__":
    # 自检：打印关键路径
    print("工程根:", engineering_root())
    print("素材根:", materials_root())
    print("下载目录:", get_downloads_dir())
    print("ffmpeg:", find_ffmpeg("ffmpeg"))
    print("ffprobe:", find_ffmpeg("ffprobe"))
    print("Python:", python_exe())
    print("周期目录示例:", period_dir_name(date(2026, 10, 9), date(2026, 10, 15)))
