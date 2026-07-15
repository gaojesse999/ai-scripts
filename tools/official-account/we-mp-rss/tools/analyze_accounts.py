#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公众号批量分析脚本
================

从一个「公众号名称列表」文件出发，自动完成：
  1. 搜索公众号并加入订阅（feeds 表），已存在则跳过
  2. 抓取每个公众号最近若干页文章（写入 articles 表）
  3. 基于已入库文章做统计分析（发文量 / 时间分布 / 原创比例 / 标题高频词等）
  4. 输出分析报告到 data/analysis/ 下的 Markdown 与 JSON 文件

前提：
  - 已在后台完成「扫码授权」（否则 search_Biz / 抓取会失败）
  - 已设置代理环境变量以访问微信（由用户自行配置，本脚本不硬编码），例如：
        export HTTPS_PROXY=http://<代理IP>:<端口>
        export HTTP_PROXY=http://<代理IP>:<端口>

输入文件格式：每行一个公众号名称（支持制表符分隔，取第一列；# 开头为注释）
    刘润
    洞见
    粥左罗

用法：
    .venv/bin/python tools/analyze_accounts.py data/accounts.txt
    .venv/bin/python tools/analyze_accounts.py data/accounts.txt --max-page 5 --no-gather
选项：
    --max-page N     每个公众号抓取的页数（每页约 5 篇），默认取 config 的 max_page
    --no-gather      只做分析，不联网抓取新文章（用于已抓过的场景）
    --top-keywords N 标题高频词 Top N，默认 20
    --out DIR        报告输出目录，默认 data/analysis
"""
import argparse
import json
import os
import random
import re
import sys
import time
from collections import Counter
from datetime import datetime

# 将项目根目录加入 import 路径
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def read_account_names(file_path: str) -> list:
    """读取公众号名称列表：每行一个，支持制表符（取第一列），# 为注释。"""
    names = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            name = line.split("\t")[0].strip()
            if name:
                names.append(name)
    # 去重保序
    seen = set()
    result = []
    for n in names:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result


def ensure_subscribed(name: str, session, Feed):
    """确保公众号已订阅：存在则返回，否则搜索并创建 Feed。返回 (feed, created)。"""
    import base64
    from core.wx import search_Biz

    existing = session.query(Feed).filter(Feed.mp_name == name).first()
    if existing:
        return existing, False

    search_result = search_Biz(name, limit=5, offset=0)
    mp_info = None
    candidates = []
    if search_result and "list" in search_result:
        for item in search_result["list"]:
            candidates.append(item.get("nickname"))
            if item.get("nickname") == name:
                mp_info = item
                break
        # 未精确命中时退回第一个结果
        if mp_info is None and search_result["list"]:
            mp_info = search_result["list"][0]

    if mp_info is None:
        raise ValueError(f"未搜索到公众号 '{name}'，候选: {candidates}")

    mp_id = mp_info.get("fakeid", "")
    mpx_id = base64.b64decode(mp_id).decode("utf-8")
    now = datetime.now()
    feed = Feed(
        id=f"MP_WXS_{mpx_id}",
        mp_name=mp_info.get("nickname", name),
        mp_cover=mp_info.get("round_head_img", ""),
        mp_intro=mp_info.get("signature", ""),
        status=1,
        created_at=now,
        updated_at=now,
        faker_id=mp_id,
        update_time=0,
        sync_time=0,
    )
    session.add(feed)
    session.commit()
    return feed, True


def gather_articles(feed, max_page: int):
    """抓取指定公众号的文章并写入 DB（复用 WxGather + UpdateArticle）。"""
    from core.wx import WxGather
    from jobs.article import UpdateArticle

    wx = WxGather().Model()
    wx.get_Articles(
        faker_id=feed.faker_id,
        Mps_id=feed.id,
        Mps_title=feed.mp_name,
        CallBack=UpdateArticle,
        start_page=0,
        MaxPage=max_page,
    )


# 标题分词用的简单停用词（避免噪音）
_STOPWORDS = set(
    "的 了 和 与 及 或 在 是 我 你 他 她 它 我们 你们 他们 这 那 有 无 就 都 也 "
    "而 但 如果 因为 所以 一个 一种 这个 那个 什么 怎么 为什么 如何 让 把 被 从 "
    "对 对于 关于 一 二 三 不 没 很 更 最 会 能 要 说 看 想 做 吗 呢 啊 吧".split()
)


def extract_keywords(titles: list, top_n: int) -> list:
    """标题高频词。优先用 jieba，未安装则退回中文二字词切分。"""
    counter = Counter()
    try:
        import jieba  # 可选依赖

        for t in titles:
            for w in jieba.cut(t or ""):
                w = w.strip()
                if len(w) >= 2 and w not in _STOPWORDS and not w.isdigit():
                    counter[w] += 1
    except Exception:
        # 退回：抽取连续中文串，做 2-gram 统计
        han = re.compile(r"[\u4e00-\u9fa5]+")
        for t in titles:
            for seg in han.findall(t or ""):
                for i in range(len(seg) - 1):
                    gram = seg[i : i + 2]
                    if gram not in _STOPWORDS:
                        counter[gram] += 1
    return counter.most_common(top_n)


def analyze_feed(feed, session, Article, top_n: int) -> dict:
    """对单个公众号的已入库文章做统计分析。"""
    rows = (
        session.query(Article)
        .filter(Article.mp_id == feed.id, Article.status != 6)
        .order_by(Article.publish_time.desc())
        .all()
    )
    total = len(rows)
    result = {
        "mp_name": feed.mp_name,
        "mp_id": feed.id,
        "mp_intro": feed.mp_intro,
        "total_articles": total,
    }
    if total == 0:
        result["note"] = "暂无已入库文章（可能未授权/未抓取，或该号无历史文章）"
        return result

    times = [r.publish_time for r in rows if r.publish_time]
    titles = [r.title or "" for r in rows]
    originals = sum(1 for r in rows if (r.copyright_stat or 0) == 1)

    # 每月发文分布
    month_counter = Counter()
    for ts in times:
        month_counter[datetime.fromtimestamp(ts).strftime("%Y-%m")] += 1

    earliest = min(times) if times else None
    latest = max(times) if times else None
    span_days = ((latest - earliest) / 86400) if (earliest and latest) else 0
    weeks = max(span_days / 7, 1)

    result.update(
        {
            "time_range": {
                "earliest": datetime.fromtimestamp(earliest).strftime("%Y-%m-%d")
                if earliest
                else None,
                "latest": datetime.fromtimestamp(latest).strftime("%Y-%m-%d")
                if latest
                else None,
                "span_days": round(span_days, 1),
            },
            "avg_per_week": round(total / weeks, 2),
            "original_ratio": round(originals / total, 3),
            "avg_title_len": round(sum(len(t) for t in titles) / total, 1),
            "posts_per_month": dict(sorted(month_counter.items())),
            "top_keywords": extract_keywords(titles, top_n),
            "recent_titles": titles[:10],
        }
    )
    return result


def render_markdown(report: dict) -> str:
    lines = []
    lines.append("# 公众号分析报告")
    lines.append("")
    lines.append(f"- 生成时间：{report['generated_at']}")
    lines.append(f"- 分析账号数：{len(report['accounts'])}")
    lines.append("")
    for acc in report["accounts"]:
        lines.append(f"## {acc['mp_name']}")
        lines.append("")
        if acc.get("mp_intro"):
            lines.append(f"> {acc['mp_intro']}")
            lines.append("")
        lines.append(f"- 文章总数：**{acc['total_articles']}**")
        if acc.get("note"):
            lines.append(f"- 说明：{acc['note']}")
            lines.append("")
            continue
        tr = acc["time_range"]
        lines.append(
            f"- 时间跨度：{tr['earliest']} ~ {tr['latest']}（约 {tr['span_days']} 天）"
        )
        lines.append(f"- 平均每周发文：{acc['avg_per_week']} 篇")
        lines.append(f"- 原创占比：{acc['original_ratio'] * 100:.1f}%")
        lines.append(f"- 标题平均字数：{acc['avg_title_len']}")
        lines.append("")
        lines.append("**每月发文数：**")
        lines.append("")
        lines.append("| 月份 | 篇数 |")
        lines.append("| --- | --- |")
        for m, c in acc["posts_per_month"].items():
            lines.append(f"| {m} | {c} |")
        lines.append("")
        lines.append("**标题高频词 Top：**")
        lines.append("")
        kw = "、".join(f"{w}({c})" for w, c in acc["top_keywords"])
        lines.append(kw or "（无）")
        lines.append("")
        lines.append("**最近文章标题：**")
        lines.append("")
        for t in acc["recent_titles"]:
            lines.append(f"- {t}")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="从文件批量分析公众号")
    parser.add_argument("file", help="公众号名称列表文件（每行一个）")
    parser.add_argument("--max-page", type=int, default=None, help="每号抓取页数")
    parser.add_argument("--no-gather", action="store_true", help="只分析，不联网抓取")
    parser.add_argument("--top-keywords", type=int, default=20, help="标题高频词 Top N")
    parser.add_argument("--out", default=None, help="报告输出目录")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"错误: 文件不存在: {args.file}")
        sys.exit(1)

    from core.config import cfg
    from core.db import DB
    from core.models.feed import Feed
    from core.models.article import Article

    names = read_account_names(args.file)
    if not names:
        print("错误: 文件中没有有效的公众号名称")
        sys.exit(1)
    max_page = args.max_page if args.max_page is not None else int(cfg.get("max_page", 5))
    out_dir = args.out or os.path.join(ROOT, "data", "analysis")
    os.makedirs(out_dir, exist_ok=True)

    print(f"待分析公众号（{len(names)}）: {', '.join(names)}")
    print("=" * 60)

    session = DB.get_session()
    accounts = []
    for name in names:
        try:
            feed, created = ensure_subscribed(name, session, Feed)
            print(f"[{name}] {'新增订阅' if created else '已订阅'} -> {feed.id}")

            if not args.no_gather:
                print(f"  抓取文章中（最多 {max_page} 页）...")
                try:
                    gather_articles(feed, max_page)
                except Exception as e:
                    print(f"  抓取出错（继续分析已入库文章）: {e}")
                time.sleep(random.randint(1, 3))  # 防频控

            report = analyze_feed(feed, session, Article, args.top_keywords)
            accounts.append(report)
            print(
                f"  分析完成: 文章 {report['total_articles']} 篇"
                + (f"，{report.get('note', '')}" if report.get("note") else "")
            )
        except Exception as e:
            print(f"[{name}] 处理失败: {e}")
            accounts.append({"mp_name": name, "error": str(e), "total_articles": 0})
            session.rollback()

    report = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "accounts": accounts,
    }
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = os.path.join(out_dir, f"analysis_{ts}.json")
    md_path = os.path.join(out_dir, f"analysis_{ts}.md")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(render_markdown(report))

    print("=" * 60)
    print(f"报告已生成:\n  Markdown: {md_path}\n  JSON:     {json_path}")


if __name__ == "__main__":
    main()
