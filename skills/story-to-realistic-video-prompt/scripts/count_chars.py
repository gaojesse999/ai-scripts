#!/usr/bin/env python3
"""统计 story-to-realistic-video-prompt 生成的提示词正文字数。

口径：只统计「# 提示词」标题之后、首个 `---` 分隔符之前的正文，
去掉以 `#` 开头的标题行，再用正则 \\S 计非空白字符数
（中文、标点、英文、数字各算 1 个，忽略空格 / 换行 / 制表符）。

用法：
    python3 count_chars.py <文件1.md> [文件2.md ...]

退出码：
    0  全部文件正文字数落在目标区间 [2300, 2700]
    1  存在超出区间的文件
    2  参数缺失或文件读取失败
"""

import re
import sys

# skill 规定的目标区间：2500 字左右（2300-2700）
MIN_CHARS = 2300
MAX_CHARS = 2700


def count_body_chars(path: str) -> int:
    """返回提示词正文（首个 --- 之前、排除 # 标题行）的非空白字符数。"""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    body = text.split("---")[0]
    body = "\n".join(line for line in body.splitlines() if not line.startswith("#"))
    return len(re.findall(r"\S", body))


def main(argv: list[str]) -> int:
    files = argv[1:]
    if not files:
        print(f"用法: python3 {argv[0]} <文件1.md> [文件2.md ...]", file=sys.stderr)
        return 2

    all_ok = True
    for path in files:
        try:
            n = count_body_chars(path)
        except OSError as exc:
            print(f"[读取失败] {path}: {exc}", file=sys.stderr)
            all_ok = False
            continue

        if n < MIN_CHARS:
            status = f"偏少（< {MIN_CHARS}）"
            all_ok = False
        elif n > MAX_CHARS:
            status = f"偏多（> {MAX_CHARS}）"
            all_ok = False
        else:
            status = "达标"
        print(f"{path}: 正文非空白字符数 {n} —— {status}")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
