# -*- coding: utf-8 -*-
"""Add two centered title lines to a blank cover without touching any other pixel.

The blank cover is composited with a type layer only. It never passes through an
image-generation model, so the scene, framing and resolution stay bit-identical
across runs.

Type metrics are calibrated from a reference cover produced by an image model:
CJK ink height ~145px on a 1024-tall canvas (14.2%), two-line block ~326px (31.8%).

Usage:
    python scripts/make_cover.py "自动习惯设计" "系统｜01"
    python scripts/make_cover.py "自动习惯设计" "系统｜01" --base cover/封面.png -o out/ep1.png
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

SKILL_DIR = Path(__file__).resolve().parent.parent
BUNDLED_FONT = SKILL_DIR / "assets" / "NotoSerifSC-VF.ttf"
COVER_DIR = SKILL_DIR / "cover"

FILL = (0xE0, 0xCB, 0xA8, 255)  # #E0CBA8, within #D8C29C–#E6D3B0
STROKE = (0x3A, 0x28, 0x1F, 255)  # #3A281F
WEIGHT = 700
INK_RATIO = 145 / 1024
BLOCK_RATIO = 326 / 1024
SHADOW_OPACITY = 0.32
SAFE_WIDTH_RATIO = 0.92
SSAA = 2

OUTPUT_STEM_FORMAT = "image-outputs-%y%m%d-%H%M%S"

# Used when --base is omitted. Bundled with the skill, so the default works from
# any working directory.
BASE_BY_RATIO = {
    "16:9": COVER_DIR / "封面16x9.png",
    "21:9": COVER_DIR / "封面21x9.png",
}
DEFAULT_RATIO = "16:9"
ASPECT_TOLERANCE = 0.02


def load_font(font_path: Path, size: float) -> ImageFont.FreeTypeFont:
    font = ImageFont.truetype(str(font_path), size=size)
    try:
        font.set_variation_by_axes([WEIGHT])
    except OSError:
        pass  # static font, no weight axis to set
    return font


def ink_height(font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    """Ink height and top bearing of a full-width CJK box glyph."""
    top, bottom = font.getbbox("国", anchor="lt")[1::2]
    return bottom - top, top


def pick_font_size(font_path: Path, target_ink_h: float) -> tuple[ImageFont.FreeTypeFont, float]:
    lo, hi = 8.0, target_ink_h * 2.2
    for _ in range(28):
        mid = (lo + hi) / 2
        if ink_height(load_font(font_path, mid))[0] < target_ink_h:
            lo = mid
        else:
            hi = mid
    return load_font(font_path, lo), lo


def tracking_to_width(advances: list[float], target: float) -> float:
    if len(advances) <= 1:
        return 0.0
    return (target - sum(advances)) / (len(advances) - 1)


def draw_tracked(
    draw: ImageDraw.ImageDraw,
    text: str,
    origin: tuple[float, float],
    font: ImageFont.FreeTypeFont,
    advances: list[float],
    tracking: float,
    fill: tuple[int, int, int, int],
    stroke_fill: tuple[int, int, int, int] | None = None,
    stroke_width: int = 0,
) -> None:
    x, y = origin
    for char, advance in zip(text, advances):
        kwargs: dict = {"font": font, "anchor": "lt", "fill": fill}
        if stroke_width and stroke_fill is not None:
            kwargs["stroke_width"] = stroke_width
            kwargs["stroke_fill"] = stroke_fill
        draw.text((x, y), char, **kwargs)
        x += advance + tracking


def check_width(rect_w: float, canvas_w: int) -> None:
    """Type size is fixed by design, so a long title must be shortened, not scaled down."""
    if rect_w > canvas_w:
        raise SystemExit(
            f"标题过宽，会画到画面外: 需要 {rect_w:.0f}px，底图只有 {canvas_w}px。\n"
            "字号是固定的，请改短标题，或换一张更宽的底图。"
        )
    if rect_w > canvas_w * SAFE_WIDTH_RATIO:
        print(
            f"提醒: 标题占了画面宽度的 {rect_w / canvas_w:.0%}，两侧留白很少，建议改短一点。",
            file=sys.stderr,
        )


def render(line1: str, line2: str, base_path: Path, font_path: Path, out_path: Path) -> dict:
    base = Image.open(base_path).convert("RGBA")
    width, height = base.size
    sw, sh = width * SSAA, height * SSAA

    font, font_size = pick_font_size(font_path, INK_RATIO * height * SSAA)
    ink_h, ink_top = ink_height(font)

    gap = BLOCK_RATIO * height * SSAA - 2 * ink_h
    if gap < 0.02 * height * SSAA:
        gap = 0.037 * height * SSAA
    block_top = (sh - (2 * ink_h + gap)) / 2

    adv1 = [font.getlength(c) for c in line1]
    adv2 = [font.getlength(c) for c in line2]
    # One fixed type size for both lines. The shorter line is tracked out so that
    # both lines share the same left and right edges.
    rect_w = max(sum(adv1), sum(adv2))
    lines = (
        (line1, adv1, tracking_to_width(adv1, rect_w), block_top - ink_top),
        (line2, adv2, tracking_to_width(adv2, rect_w), block_top + ink_h + gap - ink_top),
    )
    left = (sw - rect_w) / 2
    check_width(rect_w / SSAA, width)

    stroke_w = max(2, round(0.010 * font_size))
    shadow_dy = round(0.045 * font_size)
    shadow_blur = max(2, round(0.035 * font_size))

    shadow = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    for text, advances, tracking, y in lines:
        draw_tracked(shadow_draw, text, (left, y + shadow_dy), font, advances, tracking, STROKE)
    r, g, b, a = shadow.split()
    a = a.point(lambda p: int(p * SHADOW_OPACITY))
    shadow = Image.merge("RGBA", (r, g, b, a)).filter(ImageFilter.GaussianBlur(shadow_blur))

    type_layer = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    type_draw = ImageDraw.Draw(type_layer)
    for text, advances, tracking, y in lines:
        draw_tracked(type_draw, text, (left, y), font, advances, tracking, FILL, STROKE, stroke_w)

    overlay = Image.alpha_composite(shadow, type_layer).resize((width, height), Image.Resampling.LANCZOS)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    Image.alpha_composite(base, overlay).convert("RGB").save(out_path, format="PNG", optimize=True)

    report = verify(base_path, out_path)
    report["font"] = f"{font_path.name} @ {font_size / SSAA:.1f}px"
    report["ink_h_ratio"] = f"{ink_h / SSAA / height:.4f} (目标 {INK_RATIO:.4f})"
    return report


def change_mask(a: Image.Image, b: Image.Image) -> Image.Image:
    """Any-channel difference mask.

    Channels are combined with lighter() rather than convert("L"), whose weighted
    rounding would silently drop a 1-level difference in a single channel.
    """
    red, green, blue = ImageChops.difference(a, b).split()
    merged = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    return merged.point(lambda p: 255 if p else 0)


def verify(base_path: Path, out_path: Path) -> dict:
    """Prove the output differs from the base only inside one title block."""
    base = Image.open(base_path).convert("RGB")
    out = Image.open(out_path).convert("RGB")
    if base.size != out.size:
        raise SystemExit(f"分辨率不一致: 底图 {base.size}, 输出 {out.size}")

    mask = change_mask(base, out)
    box = mask.getbbox()
    if box is None:
        raise SystemExit("输出与底图完全相同，标题没有画上去")

    # Blank out the title block; anything left is an unintended background change.
    ImageDraw.Draw(mask).rectangle(box, fill=0)
    leaked = mask.getbbox()
    if leaked is not None:
        raise SystemExit(f"标题区域以外发生了改动: {leaked}")

    return {
        "output": str(out_path),
        "size": f"{out.width}x{out.height} (与底图一致)",
        "title_box": f"x{box[0]}-{box[2] - 1} y{box[1]}-{box[3] - 1}",
        "background": "标题区域以外 0 像素改动",
    }


def resolve_base(base_arg: Path | None, ratio: str) -> Path:
    if base_arg is not None:
        if not base_arg.is_file():
            raise SystemExit(f"底图不存在: {base_arg}")
        return base_arg
    bundled = BASE_BY_RATIO[ratio]
    if not bundled.is_file():
        raise SystemExit(
            f"skill 自带的 {ratio} 底图缺失: {bundled}\n"
            "请恢复该文件，或用 --base 指定底图路径。"
        )
    return bundled


def check_aspect(base_path: Path, ratio: str) -> None:
    """Rendering is height-based and works at any aspect, so a mismatch is only a warning."""
    with Image.open(base_path) as im:
        actual = im.width / im.height
    expected = eval_ratio(ratio)
    if abs(actual - expected) / expected > ASPECT_TOLERANCE:
        print(
            f"提醒: 底图实际比例 {actual:.3f}，与 --ratio {ratio} ({expected:.3f}) 不符。"
            f"排版按底图高度计算，出图不会失败，但请确认底图没放错。",
            file=sys.stderr,
        )


def eval_ratio(ratio: str) -> float:
    w, h = ratio.split(":")
    return int(w) / int(h)


def resolve_font(font_arg: Path | None) -> Path:
    if font_arg is not None:
        if not font_arg.is_file():
            raise SystemExit(f"字体文件不存在: {font_arg}")
        return font_arg
    if BUNDLED_FONT.is_file():
        return BUNDLED_FONT
    raise SystemExit(
        f"skill 自带字体缺失: {BUNDLED_FONT}\n"
        "请恢复该文件，或用 --font 指定一个宋体/明朝体字体文件。"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="在无文字封面上叠加两行标题，背景像素不变")
    parser.add_argument("line1", help="第一行标题")
    parser.add_argument("line2", help="第二行标题")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="输出 PNG 路径。省略时写到当前目录的 image-outputs-YYMMDD-HHMMSS.png",
    )
    parser.add_argument(
        "--ratio",
        choices=sorted(BASE_BY_RATIO),
        default=DEFAULT_RATIO,
        help=f"画面比例，决定省略 --base 时用哪张底图（默认 {DEFAULT_RATIO}）",
    )
    parser.add_argument(
        "--base",
        type=Path,
        default=None,
        help="无文字封面底图。省略时用 skill 自带的对应比例底图，给了则以此为准",
    )
    parser.add_argument("--font", type=Path, default=None, help="覆盖字体（默认用 skill 自带的 Noto Serif SC）")
    args = parser.parse_args()

    base_path = resolve_base(args.base, args.ratio)
    check_aspect(base_path, args.ratio)
    out_path = args.output or Path(f"{datetime.now():{OUTPUT_STEM_FORMAT}}.png")
    report = render(args.line1, args.line2, base_path, resolve_font(args.font), out_path)
    print(f"base: {base_path}")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
