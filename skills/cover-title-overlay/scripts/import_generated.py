# -*- coding: utf-8 -*-
"""Copy generated cover variants from Cursor's temp assets folder into this skill.

GenerateImage writes to the Cursor assets directory. If the agent turn is
interrupted (timeout after ~7 minutes when generating several images at once),
the files are often already there — only the copy/resize step was skipped.

Usage:
    python scripts/import_generated.py
    python scripts/import_generated.py --src "C:/Users/.../assets"
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image

SKILL_DIR = Path(__file__).resolve().parent.parent
COVER_DIR = SKILL_DIR / "cover"
SIZE_REF = COVER_DIR / "封面16x9.png"
NAME_PREFIX = "封面16x9-生成-"


def fit_to(im: Image.Image, target_w: int, target_h: int) -> Image.Image:
    target_ratio = target_w / target_h
    w, h = im.size
    cur = w / h
    if abs(cur - target_ratio) > 0.01:
        if cur > target_ratio:
            new_w = round(h * target_ratio)
            left = (w - new_w) // 2
            im = im.crop((left, 0, left + new_w, h))
        else:
            new_h = round(w / target_ratio)
            top = (h - new_h) // 2
            im = im.crop((0, top, w, top + new_h))
    return im.resize((target_w, target_h), Image.Resampling.LANCZOS)


def default_asset_dirs() -> list[Path]:
    root = Path.home() / ".cursor" / "projects"
    if not root.is_dir():
        return []
    return sorted(
        (p for p in root.glob("*/assets") if p.is_dir()),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )


def collect_sources(explicit: Path | None) -> list[Path]:
    dirs = [explicit] if explicit else default_asset_dirs()
    found: dict[str, Path] = {}
    for folder in dirs:
        if folder is None or not folder.is_dir():
            continue
        for path in folder.glob(f"{NAME_PREFIX}*.png"):
            found.setdefault(path.name, path)
    return sorted(found.values(), key=lambda p: p.name)


def main() -> None:
    parser = argparse.ArgumentParser(description="把 Cursor 临时目录里已生成的封面图导入 skill/cover")
    parser.add_argument("--src", type=Path, default=None, help="Cursor assets 目录；省略则自动扫描")
    args = parser.parse_args()

    if not SIZE_REF.is_file():
        raise SystemExit(f"找不到尺寸参照: {SIZE_REF}")
    target_w, target_h = Image.open(SIZE_REF).size

    sources = collect_sources(args.src)
    if not sources:
        raise SystemExit(
            "没有找到已生成的封面图。\n"
            f"文件名应以 {NAME_PREFIX} 开头。可用 --src 指定 Cursor 的 assets 目录。"
        )

    COVER_DIR.mkdir(parents=True, exist_ok=True)
    for src in sources:
        dst = COVER_DIR / src.name
        im = Image.open(src).convert("RGB")
        fit_to(im, target_w, target_h).save(dst, format="PNG", optimize=True)
        print(f"{src.name}: {im.size[0]}x{im.size[1]} -> {target_w}x{target_h}  {dst}")


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
