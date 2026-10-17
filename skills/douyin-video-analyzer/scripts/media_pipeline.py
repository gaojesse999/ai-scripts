#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""媒体流水线：批量 MP4->MP3（video-to-mp3）-> 口播脚本（audio-stt）。

本脚本不重复实现转码与转写，而是按顺序调用既有的两个 Skill，保证全仓工具链一致：
  1) .agents/skills/video-to-mp3/scripts/convert.py   （--input-dir --skip-existing）
  2) .agents/skills/audio-stt/scripts/transcribe.py   （--input-dir --skip-existing --language zh）

两步都带 --skip-existing，天然支持断点续跑：中途失败重跑即可，已完成的会跳过。

用法：
  python media_pipeline.py --start 2026-10-09 --end 2026-10-15
  python media_pipeline.py --period-dir "..."           # 只转音频不转写
  python media_pipeline.py --period-dir "..." --skip-stt
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import engineering_root, materials_root, parse_date, period_dir_name, python_exe  # noqa: E402


def run(cmd: list[str], title: str) -> int:
    print("\n" + "=" * 64)
    print(f"▶ {title}")
    print("  命令：", " ".join(cmd))
    print("=" * 64)
    proc = subprocess.run(cmd, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        print(f"× {title} 失败（code={proc.returncode}）", file=sys.stderr)
    return proc.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description="批量 MP4->MP3->脚本（复用 video-to-mp3 / audio-stt）")
    ap.add_argument("--start", default=None)
    ap.add_argument("--end", default=None)
    ap.add_argument("--period-dir", default=None)
    ap.add_argument("--skip-stt", action="store_true", help="只转 MP3，不做语音转写")
    ap.add_argument("--language", default="zh", help="STT 语言，默认 zh")
    args = ap.parse_args()

    if args.period_dir:
        period_dir = Path(args.period_dir).resolve()
    else:
        if not args.start or not args.end:
            sys.exit("需提供 --start/--end 或 --period-dir")
        period_dir = (materials_root() / period_dir_name(
            parse_date(args.start), parse_date(args.end))).resolve()
    if not period_dir.is_dir():
        sys.exit(f"周期目录不存在：{period_dir}")

    root = engineering_root()
    py = python_exe()
    convert = root / ".agents" / "skills" / "video-to-mp3" / "scripts" / "convert.py"
    transcribe = root / ".agents" / "skills" / "audio-stt" / "scripts" / "transcribe.py"

    if not convert.exists():
        sys.exit(f"缺少 video-to-mp3 脚本：{convert}")
    mp4s = list(period_dir.glob("*.mp4"))
    if not mp4s:
        sys.exit(f"目录内无 mp4：{period_dir}")
    print(f"周期目录：{period_dir}\n视频数：{len(mp4s)}")

    rc = run([py, str(convert), "--input-dir", str(period_dir), "--skip-existing"],
             "Step 1/2 视频转 MP3")
    if rc != 0:
        return rc

    if args.skip_stt:
        print("已按 --skip-stt 跳过语音转写。")
        return 0
    if not transcribe.exists():
        sys.exit(f"缺少 audio-stt 脚本：{transcribe}")
    rc = run([py, str(transcribe), "--input-dir", str(period_dir),
              "--skip-existing", "--language", args.language],
             "Step 2/2 MP3 转口播脚本（Groq Whisper）")
    return rc


if __name__ == "__main__":
    sys.exit(main())
