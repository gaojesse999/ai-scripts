#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把浏览器下载到系统下载目录的文件，归档到分析周期目录。

浏览器（bu.download / 导出按钮）的落点固定是系统下载目录，且文件名不统一：
  - 官方三表：作品列表导出.xlsx / 数据表现_短视频全量指标.xlsx / 数据表现_粉丝全量指标.xlsx
              （可能带 (1)(2) 重复后缀）
  - 视频：在 BROWSER_RUNBOOK 中要求用 bu.download(url, filename=标准名.mp4) 下载，
          标准名形如 20261011-标题.mp4 或 20261007-01-标题.mp4

本脚本把上述文件移入周期目录；周期目录已存在同名文件时跳过，保证幂等。
只移动符合命名规范的本周期视频，避免误动下载目录里的无关文件。

用法：
  python normalize_names.py --start 2026-10-09 --end 2026-10-15
  python normalize_names.py --period-dir "..." --copy
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import daterange, get_downloads_dir, materials_root, parse_date, period_dir_name  # noqa: E402

XLSX_KEYWORDS = ["作品列表", "短视频", "粉丝"]
VIDEO_NAME_RE = re.compile(r"^(20\d{6})(?:-\d{2})?-.+\.mp4$", re.IGNORECASE)


def _transfer(src: Path, dst_dir: Path, copy: bool, moved: list) -> None:
    dst = dst_dir / src.name
    if dst.exists():
        print(f"  · 目标已存在，跳过：{src.name}")
        return
    dst_dir.mkdir(parents=True, exist_ok=True)
    if copy:
        shutil.copy2(src, dst)
    else:
        shutil.move(str(src), str(dst))
    moved.append(src.name)
    print(f"  {'复制' if copy else '移动'}：{src.name}")


def collect_xlsx(downloads: Path, period_dir: Path, copy: bool, moved: list) -> None:
    print("[1/2] 归档官方三表")
    for kw in XLSX_KEYWORDS:
        # 下载目录内匹配的文件，按修改时间取最新（规避 (1)(2) 重复件）
        hits = sorted(
            (f for f in downloads.glob("*.xlsx")
             if kw in f.name and not f.name.startswith("~$")),
            key=lambda f: f.stat().st_mtime, reverse=True,
        )
        if not hits:
            print(f"  · 未找到含『{kw}』的表（粉丝表可缺失）")
            continue
        _transfer(hits[0], period_dir, copy, moved)


def collect_videos(downloads: Path, period_dir: Path, days: set, copy: bool, moved: list) -> None:
    print("[2/2] 归回本周期视频")
    found = 0
    for f in sorted(downloads.glob("*.mp4")):
        m = VIDEO_NAME_RE.match(f.name)
        if not m:
            continue
        try:
            d = datetime.strptime(m.group(1), "%Y%m%d").date()
        except ValueError:
            continue
        if d not in days:
            continue
        found += 1
        _transfer(f, period_dir, copy, moved)
    if not found:
        print("  · 下载目录没有符合标准命名的本周期视频。")
        print("    （请确认在浏览器里用 bu.download(url, filename=标准名.mp4) 下载）")


def main() -> int:
    ap = argparse.ArgumentParser(description="归档下载目录中的三表与视频到周期目录")
    ap.add_argument("--start", default=None)
    ap.add_argument("--end", default=None)
    ap.add_argument("--period-dir", default=None)
    ap.add_argument("--copy", action="store_true", help="复制而非移动（默认移动）")
    args = ap.parse_args()

    if args.period_dir:
        period_dir = Path(args.period_dir).resolve()
        start = end = None
    else:
        if not args.start or not args.end:
            sys.exit("需提供 --start/--end 或 --period-dir")
        start, end = parse_date(args.start), parse_date(args.end)
        period_dir = (materials_root() / period_dir_name(start, end)).resolve()
    period_dir.mkdir(parents=True, exist_ok=True)

    downloads = get_downloads_dir()
    if not downloads.is_dir():
        sys.exit(f"下载目录不存在：{downloads}")
    days = set(daterange(start, end)) if start else None

    print(f"下载目录：{downloads}")
    print(f"周期目录：{period_dir}\n")
    moved: list = []
    collect_xlsx(downloads, period_dir, args.copy, moved)
    if days is not None:
        collect_videos(downloads, period_dir, days, args.copy, moved)

    print("\n" + "=" * 60)
    print(f"归档完成，处理文件 {len(moved)} 个。")
    print("下一步：运行 parse_data.py 重新对齐并校验音视频完整性。")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
