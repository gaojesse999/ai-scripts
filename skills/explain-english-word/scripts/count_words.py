#!/usr/bin/env python3
"""Count words in an input file for the explain-english-word skill.

Usage:
    python count_words.py <file_path> [--json]

Output (human-readable by default):
    - total English word tokens
    - unique English words (lowercased, de-duplicated, order preserved)
    - whether the file contains non-English content
    - a small sample of the non-English content found

With --json, prints a JSON object:
    {
      "file": "...",
      "total_words": 0,
      "unique_count": 0,
      "unique_words": [...],
      "has_non_english": false,
      "non_english_sample": [...]
    }
"""

import json
import re
import sys

# An "English word" is a run of ASCII letters, optionally containing
# internal apostrophes or hyphens (e.g. "don't", "well-known").
WORD_RE = re.compile(r"[A-Za-z]+(?:['\-][A-Za-z]+)*")

# Characters we consider "normal" alongside English words: ASCII letters,
# digits, whitespace, and common punctuation. Anything else (CJK, accented
# letters, emoji, etc.) is treated as non-English content.
ALLOWED_NON_WORD_RE = re.compile(r"[A-Za-z0-9\s\.,;:!\?\-'\"()\[\]{}/\\@#$%^&*+=_<>|~`’“”…—–]")


def analyze(text: str):
    tokens = WORD_RE.findall(text)
    seen = set()
    unique = []
    for tok in tokens:
        low = tok.lower()
        if low not in seen:
            seen.add(low)
            unique.append(low)

    # Find non-English characters (anything not allowed and not a word char).
    non_english_chars = []
    for ch in text:
        if WORD_RE.match(ch):
            continue
        if ALLOWED_NON_WORD_RE.match(ch):
            continue
        if ch.strip() == "":
            continue
        non_english_chars.append(ch)

    # Build a short, de-duplicated sample of the non-English content.
    sample = []
    sample_seen = set()
    for ch in non_english_chars:
        if ch not in sample_seen:
            sample_seen.add(ch)
            sample.append(ch)
        if len(sample) >= 30:
            break

    return {
        "total_words": len(tokens),
        "unique_count": len(unique),
        "unique_words": unique,
        "has_non_english": len(non_english_chars) > 0,
        "non_english_sample": sample,
    }


def main():
    args = [a for a in sys.argv[1:]]
    as_json = "--json" in args
    paths = [a for a in args if a != "--json"]

    if not paths:
        print("Usage: python count_words.py <file_path> [--json]", file=sys.stderr)
        sys.exit(2)

    path = paths[0]
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except OSError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    result = analyze(text)
    result["file"] = path

    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"File: {path}")
    print(f"Total English word tokens: {result['total_words']}")
    print(f"Unique English words: {result['unique_count']}")
    if result["has_non_english"]:
        print("Contains non-English content: YES")
        print("Non-English sample: " + " ".join(result["non_english_sample"]))
    else:
        print("Contains non-English content: NO")
    print()
    print("Unique word list:")
    print(", ".join(result["unique_words"]))


if __name__ == "__main__":
    main()
