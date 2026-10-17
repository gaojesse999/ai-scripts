#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""读取台账 + 口播脚本 + 帧目录，套用模板生成复盘报告骨架。

数据、脚本原文、关键帧路径由脚本自动填入；三层归因（数据/脚本/视觉）与
问题诊断、迭代建议保留结构化占位，交由 Agent 结合基准逐节完成。
这样 Agent 不必重复排版或搬运数据，专注做判断。

用法：
  python build_report.py --start 2026-10-09 --end 2026-10-15
  python build_report.py --period-dir "..." --force   # 强制重新生成骨架
"""

from __future__ import annotations

import argparse
import statistics
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    load_ledger, materials_root, parse_date, period_dir_name, daterange,
)

SKILL_DIR = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL_DIR / "templates" / "复盘报告模板.md"


def pct(x, d=2):
    return "-" if x is None else f"{x * 100:.{d}f}%"


def num(x, d=2):
    return "-" if x is None else f"{x:.{d}f}"


def stats_line(values, pct_vals=False):
    vals = [v for v in values if v is not None]
    if not vals:
        return "-", "-", "-"
    if pct_vals:
        return pct(min(vals)), pct(max(vals)), pct(statistics.median(vals))
    lo, hi, med = min(vals), max(vals), statistics.median(vals)
    return f"{lo:.0f}", f"{hi:.0f}", f"{med:.0f}"


def render_work(period_dir: Path, i: int, w: dict) -> str:
    f = w.get("files", {})
    L = [f"### {i}. {w['name'].split('#')[0]}",
         f"\n**文件**：`{w.get('file_base','')}`　**发布**：{w['publish_time']}　**体裁**：{w.get('genre','-')}\n"]
    L.append("**数据表现**\n")
    L.append(
        f"- 播放 {w.get('plays')}　|　完播率 {pct(w.get('completion_rate'))}　|　"
        f"5s完播 {pct(w.get('complete_5s'))}　|　2s跳出 {pct(w.get('bounce_2s'))}　|　"
        f"封面点击 {pct(w.get('cover_ctr'))}")
    L.append(
        f"- 平均播放 {num(w.get('avg_play_sec'))}s / 视频时长 {num(w.get('video_duration'))}s"
        f"（播放时长占比 {pct(w.get('play_duration_ratio'))}）")
    L.append(
        f"- 赞 {w.get('likes')}　藏 {w.get('collects')}　评 {w.get('comments')}　"
        f"转 {w.get('shares')}　互动率 {pct(w.get('engagement'))}　"
        f"主页访问 {w.get('homepage_visits')}　涨粉 {w.get('new_fans')}\n")

    # 脚本原文
    L.append("**口播脚本原文**\n")
    txt_name = f.get("txt")
    if txt_name:
        txt_path = period_dir / txt_name
        script = txt_path.read_text(encoding="utf-8").strip() if txt_path.exists() else ""
        quoted = "\n".join("> " + line for line in script.splitlines()) if script else "> （脚本为空）"
        L.append(quoted)
    else:
        L.append("> （脚本缺失：检查 MP3 是否已转写）")
    L.append("")

    # 关键帧
    stem = (txt_name or f.get("mp4") or w.get("file_base", ""))
    if stem.endswith(".txt"):
        stem = stem[:-4]
    elif stem.endswith(".mp4"):
        stem = stem[:-4]
    frame_dir = period_dir / "frames" / stem
    frames = sorted(frame_dir.glob("*.jpg")) if frame_dir.exists() else []
    if frames:
        L.append("**关键帧**（视觉分析依据，逐张查看）：")
        L.append("`" + "`、`".join(
            f"frames/{stem}/{p.name}" for p in frames) + "`")
    else:
        L.append("**关键帧**：未抽取（运行 extract_frames.py）")
    L.append("")

    L.append("**三层归因（待分析）**\n")
    L.append("- 数据层：漏斗哪一环异常（对照基准与同周期其他条）：")
    L.append("- 脚本层：")
    L.append("  - 0-2s 钩子（12 字痛点/反问）：")
    L.append("  - 2-5s 承接（反常识/高手偷跑/超预期）：")
    L.append("  - 中段（单点是否讲透、有无废话）：")
    L.append("  - 结尾 CTA（利他型关注钩子）：")
    L.append("- 视觉层（表情/花字/动作/着装道具）：")
    L.append("- 一句话结论（选题/钩子/结构/动作/视觉/时长）：")
    L.append("\n---\n")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="生成复盘报告骨架")
    ap.add_argument("--start", default=None)
    ap.add_argument("--end", default=None)
    ap.add_argument("--period-dir", default=None)
    ap.add_argument("--force", action="store_true", help="报告已存在时强制重新生成")
    args = ap.parse_args()

    if args.period_dir:
        period_dir = Path(args.period_dir).resolve()
        start = end = None
    else:
        if not args.start or not args.end:
            sys.exit("需提供 --start/--end 或 --period-dir")
        start, end = parse_date(args.start), parse_date(args.end)
        period_dir = (materials_root() / period_dir_name(start, end)).resolve()

    ledger = load_ledger(period_dir)
    if not ledger:
        sys.exit(f"未找到台账，请先运行 parse_data.py：{period_dir / '_采集清单.json'}")
    if not TEMPLATE.exists():
        sys.exit(f"模板不存在：{TEMPLATE}")

    works = ledger.get("works", [])
    daily = ledger.get("daily", [])
    fans = ledger.get("fans", [])
    p = ledger.get("period", {})
    start = parse_date(p.get("start", args.start)) if start is None else start
    end = parse_date(p.get("end", args.end)) if end is None else end
    date_range = f"{start.strftime('%m月%d日')}-{end.strftime('%m月%d日')}"
    days = (end - start).days + 1

    # 汇总
    def s(key):
        return sum(w.get(key) for w in works if w.get(key) is not None)
    overview = (
        f"| 作品数 | 总播放 | 总点赞 | 总收藏 | 总评论 | 总转发 | 总涨粉 |\n"
        f"|---|---|---|---|---|---|---|\n"
        f"| {len(works)} | {s('plays')} | {s('likes')} | {s('collects')} | "
        f"{s('comments')} | {s('shares')} | {s('new_fans')} |\n")

    play_lo, play_hi, play_med = stats_line([w.get("plays") for w in works])
    c5_lo, c5_hi, c5_med = stats_line([w.get("complete_5s") for w in works], True)
    b2_lo, b2_hi, b2_med = stats_line([w.get("bounce_2s") for w in works], True)

    # 每日表
    daily_rows = ["| 日期 | 投稿 | 播放 | 赞 | 藏 | 评 | 转 | 5s完播 | 2s跳出 | 平均播放 |",
                  "|---|---|---|---|---|---|---|---|---|---|"]
    dmap = {d["date"]: d for d in daily}
    for d in daterange(start, end):
        r = dmap.get(d.isoformat())
        if r:
            daily_rows.append(
                f"| {d.strftime('%m-%d')} | {r.get('posts','-')} | {r.get('plays')} | "
                f"{r.get('likes')} | - | {r.get('comments')} | {r.get('shares')} | "
                f"{pct(r.get('complete_5s'))} | {pct(r.get('bounce_2s'))} | "
                f"{num(r.get('avg_play_sec'))}s |")
        else:
            daily_rows.append(f"| {d.strftime('%m-%d')} | - | - | - | - | - | - | - | - | - |")
    daily_table = "\n".join(daily_rows)

    # 粉丝表
    if fans:
        frows = ["\n**粉丝趋势**\n", "| 日期 | 总粉丝 | 净增 | 吸粉 | 脱粉 | 回访 |",
                 "|---|---|---|---|---|---|"]
        fmap = {f["date"]: f for f in fans}
        for d in daterange(start, end):
            r = fmap.get(d.isoformat())
            if r:
                frows.append(
                    f"| {d.strftime('%m-%d')} | {r.get('total_fans')} | {r.get('net_fans')} | "
                    f"{r.get('gained')} | {r.get('lost')} | {r.get('returning')} |")
        fans_table = "\n".join(frows)
    else:
        fans_table = "\n（本周期无粉丝数据表，粉丝画像未开放，跳过。）"

    works_sections = "\n".join(render_work(period_dir, i + 1, w) for i, w in enumerate(works))

    repl = {
        "{{DATE_RANGE}}": date_range,
        "{{DAYS}}": str(days),
        "{{WORK_COUNT}}": str(len(works)),
        "{{DATA_OVERVIEW}}": overview,
        "{{PLAY_MIN}}": play_lo, "{{PLAY_MAX}}": play_hi, "{{PLAY_MEDIAN}}": play_med,
        "{{C5_MIN}}": c5_lo, "{{C5_MAX}}": c5_hi,
        "{{B2_MIN}}": b2_lo, "{{B2_MAX}}": b2_hi,
        "{{DAILY_TABLE}}": daily_table,
        "{{FANS_TABLE}}": fans_table,
        "{{WORKS_SECTIONS}}": works_sections,
    }
    text = TEMPLATE.read_text(encoding="utf-8")
    for k, v in repl.items():
        text = text.replace(k, v)

    out = period_dir / f"{date_range.replace('月','').replace('日','')}抖音作品深度复盘与迭代分析报告.md"
    # 文件名规整为 周期名（去中文月日）
    out = period_dir / f"{period_dir_name(start, end)}抖音作品深度复盘与迭代分析报告.md"
    if out.exists() and not args.force:
        print(f"报告已存在（保留人工分析，不覆盖）：{out.name}")
        print("如需重新生成骨架请加 --force。")
        return 0
    out.write_text(text, encoding="utf-8")
    print(f"已生成报告骨架：{out}")
    print(f"含 {len(works)} 条作品的数据与脚本；请逐节完成三层归因与迭代建议。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
