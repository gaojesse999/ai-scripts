#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""导出已抓取文章到 CSV / JSON / Markdown。

支持三种模式：
- 单篇导出：--article-id <id>；如果不传文章 ID，则默认导出第一篇（当前按发布时间倒序排序的最新一篇）
- 多篇导出：--article-id <id1> --article-id <id2> ... 或 --article-ids id1,id2
- 全量导出：--all

编码通过 --encoding 控制：
- utf-8: 适合程序处理
- utf-8-sig: Excel 更友好，中文不容易乱码

如果不指定 --json / --csv / --md，脚本默认同时导出 CSV、JSON 和 Markdown。
如果不指定 --include-empty-content，脚本默认只导出有正文内容的文章。
Markdown 默认会清理正文尾部的微信预览/扫码噪音。
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import List


ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = Path(__file__).resolve().parent
DEFAULT_DB = ROOT / "data" / "db.db"
DEFAULT_OUT_DIR = ROOT / "data" / "exports"


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: List[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        attr_map = dict(attrs)
        if tag == "img":
            src = (attr_map.get("src") or "").strip()
            if not src:
                return
            alt = (attr_map.get("alt") or attr_map.get("title") or "图片").strip()
            self.parts.append(f"\n\n![{alt}]({src})\n\n")
            return

        if tag in {"br", "p", "div", "section", "article", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"p", "div", "section", "article", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if data:
            self.parts.append(data)


def _html_to_plain_markdown(html_content: str) -> str:
    extractor = _HTMLTextExtractor()
    extractor.feed(html_content or "")
    text = html.unescape("\n".join(extractor.parts))
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    text = "\n\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="导出已抓取文章为 CSV / JSON / Markdown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    1) 导出全部文章，默认同时导出 CSV、JSON 和 Markdown：
     python3 tools/export_articles.py --all

  2) 导出多篇文章：
     python3 tools/export_articles.py --article-id ID1 --article-id ID2
     python3 tools/export_articles.py --article-ids ID1,ID2,ID3

  3) 单篇测试，不传文章 ID 时默认导出第一篇：
     python3 tools/export_articles.py
     python3 tools/export_articles.py --encoding utf-8-sig

  4) 指定单篇文章并只导出一种格式：
     python3 tools/export_articles.py --article-id ID1 --no-json
     python3 tools/export_articles.py --article-id ID1 --no-csv
      python3 tools/export_articles.py --article-id ID1 --no-md

  5) 导出全部文章并使用 Excel 友好编码：
     python3 tools/export_articles.py --all --encoding utf-8-sig

  6) 按公众号名称关键词导出（支持重复传入）：
      python3 tools/export_articles.py --all --mp-name-keyword 刘润
      python3 tools/export_articles.py --all --mp-name-keyword 洞见 --mp-name-keyword 粥左罗

  7) 包含无正文文章（默认会过滤无正文）：
      python3 tools/export_articles.py --all --include-empty-content

  8) 保留 Markdown 原始正文尾部，不做清理：
      python3 tools/export_articles.py --all --no-clean-md

详情请看 README-detailed.md。
        """,
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="导出数据库中 status!=6 的全部文章",
    )
    parser.add_argument(
        "--article-id",
        action="append",
        dest="article_ids",
        default=[],
        help="指定单篇或多篇文章 ID，可重复传入；不传时默认导出第一篇（当前按发布时间倒序排序的最新一篇）",
    )
    parser.add_argument(
        "--article-ids",
        dest="article_ids_text",
        default="",
        help="多个文章 ID，逗号或空格分隔",
    )
    parser.add_argument(
        "--mp-name-keyword",
        action="append",
        dest="mp_name_keywords",
        default=[],
        help="按公众号名称关键词过滤，可重复传入",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUT_DIR),
        help="输出目录，默认 data/exports",
    )
    parser.add_argument(
        "--output-name",
        default="",
        help="输出文件名前缀；不传时按模式自动命名并附带时间戳",
    )
    parser.add_argument(
        "--encoding",
        choices=["utf-8", "utf-8-sig"],
        default="utf-8",
        help="输出编码，utf-8-sig 更适合 Excel 打开中文",
    )
    parser.add_argument(
        "--json",
        dest="export_json",
        action="store_true",
        default=True,
        help="导出 JSON（默认开启；不指定时与 CSV、Markdown 一起导出）",
    )
    parser.add_argument(
        "--no-json",
        dest="export_json",
        action="store_false",
        help="不导出 JSON",
    )
    parser.add_argument(
        "--csv",
        dest="export_csv",
        action="store_true",
        default=True,
        help="导出 CSV（默认开启；不指定时与 JSON、Markdown 一起导出）",
    )
    parser.add_argument(
        "--no-csv",
        dest="export_csv",
        action="store_false",
        help="不导出 CSV",
    )
    parser.add_argument(
        "--md",
        dest="export_md",
        action="store_true",
        default=True,
        help="导出 Markdown（默认开启；不指定时与 CSV、JSON 一起导出）",
    )
    parser.add_argument(
        "--no-md",
        dest="export_md",
        action="store_false",
        help="不导出 Markdown",
    )
    parser.add_argument(
        "--with-content-only",
        dest="with_content_only",
        action="store_true",
        default=True,
        help="仅导出有正文内容的文章（默认开启）",
    )
    parser.add_argument(
        "--include-empty-content",
        dest="with_content_only",
        action="store_false",
        help="包含无正文内容的文章",
    )
    parser.add_argument(
        "--clean-md",
        dest="clean_md",
        action="store_true",
        default=True,
        help="清理 Markdown 正文尾部的微信预览/扫码噪音（默认开启）",
    )
    parser.add_argument(
        "--no-clean-md",
        dest="clean_md",
        action="store_false",
        help="不清理 Markdown 正文尾部，保留原始转换内容",
    )
    return parser.parse_args()


def collect_article_ids(args: argparse.Namespace) -> List[str]:
    ids: List[str] = []
    if getattr(args, "article_ids", None):
        for article_id in args.article_ids:
            if article_id:
                ids.append(article_id)
    if getattr(args, "article_ids_text", ""):
        for raw in str(args.article_ids_text).replace(",", " ").split():
            article_id = raw.strip()
            if article_id:
                ids.append(article_id)

    # 去重保序
    seen = set()
    result: List[str] = []
    for article_id in ids:
        if article_id not in seen:
            seen.add(article_id)
            result.append(article_id)
    return result


def collect_mp_name_keywords(args: argparse.Namespace) -> List[str]:
    keywords: List[str] = []
    for item in getattr(args, "mp_name_keywords", []) or []:
        if item and item.strip():
            keywords.append(item.strip())

    seen = set()
    result: List[str] = []
    for keyword in keywords:
        if keyword not in seen:
            seen.add(keyword)
            result.append(keyword)
    return result


def build_filters(with_content_only: bool, mp_name_keywords: List[str]) -> tuple[str, List[str]]:
    clauses: List[str] = ["a.status != 6"]
    params: List[str] = []

    if with_content_only:
        clauses.append("(coalesce(trim(a.content), '') != '' or coalesce(trim(a.content_html), '') != '')")

    if mp_name_keywords:
        name_conditions = " or ".join(["mp_name like ?"] * len(mp_name_keywords))
        clauses.append(f"a.mp_id in (select id from feeds where {name_conditions})")
        params.extend([f"%{keyword}%" for keyword in mp_name_keywords])

    return " and ".join(clauses), params


def clean_markdown_tail(markdown_body: str) -> str:
    for marker in ["预览时标签不可点", "微信扫一扫可打开此内容"]:
        index = markdown_body.find(marker)
        if index >= 0:
            return markdown_body[:index].strip()
    return markdown_body.strip()


def fetch_articles(
    conn: sqlite3.Connection,
    article_ids: List[str],
    export_all: bool,
    with_content_only: bool,
    mp_name_keywords: List[str],
) -> List[sqlite3.Row]:
    conn.row_factory = sqlite3.Row
    where_sql, where_params = build_filters(with_content_only, mp_name_keywords)

    if export_all:
        query = """
        select
          a.id,
          a.mp_id,
          a.title,
          a.url,
          a.description,
          a.publish_time,
          a.copyright_stat,
          a.has_content,
          a.content,
          a.content_html
        from articles a
        where {where_sql}
        order by a.publish_time desc
        """
        return conn.execute(query.format(where_sql=where_sql), where_params).fetchall()

    if not article_ids:
        latest_query = """
        select
          a.id,
          a.mp_id,
          a.title,
          a.url,
          a.description,
          a.publish_time,
          a.copyright_stat,
          a.has_content,
          a.content,
          a.content_html
        from articles a
        where {where_sql}
        order by a.publish_time desc
        limit 1
        """
        rows = conn.execute(latest_query.format(where_sql=where_sql), where_params).fetchall()
        if rows:
            print("未指定文章 ID，默认导出第一篇文章（当前按发布时间倒序排序的最新一篇）")
        return rows

    placeholders = ",".join(["?"] * len(article_ids))
    query = f"""
    select
      a.id,
      a.mp_id,
      a.title,
      a.url,
            a.description,
            a.publish_time,
            a.copyright_stat,
            a.has_content,
            a.content,
            a.content_html
        from articles a
        where {where_sql} and a.id in ({placeholders})
    """
    rows = conn.execute(query, where_params + article_ids).fetchall()

    # 按传入顺序排序，便于单篇/多篇测试时结果更可预测
    row_map = {row["id"]: row for row in rows}
    ordered_rows = [row_map[article_id] for article_id in article_ids if article_id in row_map]
    missing = [article_id for article_id in article_ids if article_id not in row_map]
    if missing:
        print(f"警告: 未找到文章 ID: {', '.join(missing)}")
    return ordered_rows


def write_csv(rows: List[sqlite3.Row], path: Path, encoding: str) -> None:
    fields = [
        "id",
        "mp_id",
        "title",
        "url",
        "description",
        "publish_time",
        "publish_time_local",
        "copyright_stat",
        "has_content",
        "content",
        "content_html",
    ]
    with path.open("w", encoding=encoding, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            article = dict(row)
            publish_time = article.get("publish_time")
            if publish_time:
                article["publish_time_local"] = datetime.fromtimestamp(
                    int(publish_time), tz=timezone.utc
                ).strftime("%Y-%m-%d %H:%M:%S")
            else:
                article["publish_time_local"] = ""
            writer.writerow({field: article.get(field, "") for field in fields})


def write_json(rows: List[sqlite3.Row], path: Path, encoding: str) -> None:
    articles = []
    for row in rows:
        article = dict(row)
        publish_time = article.get("publish_time")
        if publish_time:
            article["publish_time_local"] = datetime.fromtimestamp(
                int(publish_time), tz=timezone.utc
            ).strftime("%Y-%m-%d %H:%M:%S")
        else:
            article["publish_time_local"] = ""
        articles.append(article)

    payload = articles[0] if len(articles) == 1 else articles
    with path.open("w", encoding=encoding) as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def write_markdown(rows: List[sqlite3.Row], path: Path, encoding: str, clean_md: bool) -> None:
    if str(TOOLS_DIR) not in sys.path:
        sys.path.insert(0, str(TOOLS_DIR))

    try:
        from mdtools.html2doc import html_to_markdown as convert_html_to_markdown
    except ImportError:
        def convert_html_to_markdown(html_content: str) -> str:
            return _html_to_plain_markdown(html_content)

    sections: List[str] = []
    for row in rows:
        article = dict(row)
        publish_time = article.get("publish_time")
        if publish_time:
            publish_time_local = datetime.fromtimestamp(
                int(publish_time), tz=timezone.utc
            ).strftime("%Y-%m-%d %H:%M:%S")
        else:
            publish_time_local = ""

        source_html = article.get("content_html") or article.get("content") or ""
        markdown_body = convert_html_to_markdown(source_html) if source_html else ""
        if clean_md:
            markdown_body = clean_markdown_tail(markdown_body)
        markdown_body = markdown_body.strip() or "(无正文内容)"

        section = [
            f"# {article.get('title', '')}",
            "",
            f"- 文章 ID: {article.get('id', '')}",
            f"- 公众号 ID: {article.get('mp_id', '')}",
            f"- 发布时间: {publish_time_local}",
            f"- 原文链接: {article.get('url', '')}",
            f"- 摘要: {article.get('description', '')}",
            "",
            markdown_body,
        ]
        sections.append("\n".join(section).strip())

    with path.open("w", encoding=encoding) as f:
        f.write("\n\n---\n\n".join(sections) + "\n")


def main() -> None:
    args = parse_args()
    article_ids = collect_article_ids(args)
    mp_name_keywords = collect_mp_name_keywords(args)

    export_all = bool(args.all)
    if export_all and article_ids:
        raise SystemExit("--all 不能和 --article-id / --article-ids 同时使用")

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    stem = args.output_name.strip()
    if not stem:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if export_all:
            stem = f"all_articles_{timestamp}"
        elif len(article_ids) == 0:
            stem = f"single_article_test_{timestamp}"
        elif len(article_ids) == 1:
            stem = f"single_article_{timestamp}"
        else:
            stem = f"selected_articles_{timestamp}"

    db_path = DEFAULT_DB
    if not db_path.exists():
        raise SystemExit(f"数据库不存在: {db_path}")

    conn = sqlite3.connect(str(db_path))
    try:
        rows = fetch_articles(
            conn,
            article_ids,
            export_all,
            bool(args.with_content_only),
            mp_name_keywords,
        )
        if not rows:
            raise SystemExit("没有可导出的文章")

        print(f"导出文章数: {len(rows)}")
        print(f"输出目录: {out_dir}")
        print(f"编码: {args.encoding}")
        print(f"仅导出有正文: {bool(args.with_content_only)}")
        print(f"清理 Markdown 尾部: {bool(args.clean_md)}")
        if mp_name_keywords:
            print(f"公众号名称关键词: {', '.join(mp_name_keywords)}")

        if args.export_csv:
            csv_path = out_dir / f"{stem}.csv"
            write_csv(rows, csv_path, args.encoding)
            print(f"CSV: {csv_path}")

        if args.export_json:
            json_path = out_dir / f"{stem}.json"
            write_json(rows, json_path, args.encoding)
            print(f"JSON: {json_path}")

        if args.export_md:
            md_path = out_dir / f"{stem}.md"
            write_markdown(rows, md_path, args.encoding, bool(args.clean_md))
            print(f"Markdown: {md_path}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()