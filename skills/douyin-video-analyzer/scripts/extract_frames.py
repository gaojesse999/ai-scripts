#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为周期目录内每个视频抽取关键帧，用于视觉层（钩子/表情/花字/动作）分析。

抽帧点位覆盖用户关心的留存节点与整体结构：
  0.5s / 1.5s / 2.5s / 3.5s / 5s —— 前 5 秒钩子（决定 2s 跳出、5s 完播）
  25% / 50% / 75%  —— 中段结构（铺垫/高潮/动作示范）
  90%               —— 结尾（CTA 关注钩子）
输出到周期目录 frames/<视频主名>/，jpg 质量较高、保留花字可辨。

用法：
  python extract_frames.py --start 2026-10-09 --end 2026-10-15
  python extract_frames.py --period-dir "..." --skip-existing
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    find_ffmpeg, load_ledger, materials_root, parse_date, period_dir_name,
    probe_media,
)


# 固定秒数点位（前 5 秒）+ 比例点位（中后段）
FIXED_SECONDS = [0.5, 1.5, 2.5, 3.5, 5.0]
RATIOS = [0.25, 0.5, 0.75, 0.9]


def extract_one(ffmpeg: str, mp4: Path, out_dir: Path, skip_existing: bool) -> int:
    duration = probe_media(mp4)["duration"]
    if not duration:
        print(f"  × 无法读取时长，跳过：{mp4.name}")
        return 0
    out_dir.mkdir(parents=True, exist_ok=True)

    # 点位：(标签, 秒)。标签用真实秒数避免舍入导致重名覆盖。
    points = [("t" + f"{s:g}".replace(".", "_") + "s", s)
              for s in FIXED_SECONDS if s < duration]
    for r in RATIOS:
        sec = duration * r
        points.append((f"p{int(r * 100):03d}", sec))

    n = 0
    for label, sec in points:
        out = out_dir / f"{label}.jpg"
        if skip_existing and out.exists():
            n += 1
            continue
        cmd = [
            ffmpeg, "-v", "error", "-y", "-ss", f"{sec:.2f}", "-i", str(mp4),
            "-frames:v", "1", "-q:v", "2", str(out),
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              encoding="utf-8", errors="replace")
        if proc.returncode == 0 and out.exists():
            n += 1
        else:
            print(f"    抽帧失败 {label}: {proc.stderr.strip()[-120:]}")
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description="为周期视频抽取关键帧")
    ap.add_argument("--start", default=None)
    ap.add_argument("--end", default=None)
    ap.add_argument("--period-dir", default=None)
    ap.add_argument("--skip-existing", action="store_true")
    args = ap.parse_args()

    if args.period_dir:
        period_dir = Path(args.period_dir)
    else:
        if not args.start or not args.end:
            sys.exit("需提供 --start/--end 或 --period-dir")
        period_dir = materials_root() / period_dir_name(
            parse_date(args.start), parse_date(args.end))
    if not period_dir.is_dir():
        sys.exit(f"周期目录不存在：{period_dir}")

    ffmpeg = find_ffmpeg("ffmpeg")
    mp4s = sorted(p for p in period_dir.glob("*.mp4") if p.stat().st_size > 50_000)
    if not mp4s:
        sys.exit(f"目录内未找到有效 mp4：{period_dir}")

    print(f"开始抽帧：{len(mp4s)} 个视频 -> {period_dir / 'frames'}")
    total = 0
    for mp4 in mp4s:
        out_dir = period_dir / "frames" / mp4.stem
        count = extract_one(ffmpeg, mp4, out_dir, args.skip_existing)
        total += count
        print(f"  √ {mp4.stem}：{count} 帧")
    print(f"完成，共 {total} 张关键帧。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
