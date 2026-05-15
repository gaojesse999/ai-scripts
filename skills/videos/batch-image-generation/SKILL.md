---
name: batch-image-generation
description: Batch generate images from a user-specified prompt file, including prompt parsing, variant chaining, output organization, and summary writing; skill-authored prose defaults to Chinese unless the user requests English. Use when the user asks to generate images, create images, make pictures, batch image generation, image generation, picture generation, 生图, 批量生图, 生成图片, 生成图像, 图片生成, 出图, 以图生图, or variants of those phrases.
---

# Batch Image Generation

## Purpose

Batch generate all images described in a user-specified prompt file, fully automatically. Do not ask for confirmation once the prompt file and task are clear.

Use `gpt-5.5-low` as the default image generation model whenever the image tool or API exposes a model option. If the available tool has no model selector, proceed with the available image generation tool and record that assumption in `image-outputs/summary.md`.

## Input File

Use the prompt file specified by the user. Do not assume any particular filename is the input file unless the user explicitly names it or the active request clearly points to it.

If the user asks to generate images but does not specify a prompt file and it cannot be inferred from attached/open context, ask one concise clarification question for the file path before starting (in **Chinese** by default, or **English** if the user requested English output). After the prompt file is known, continue fully automatically.

## Prompt File Format

Prompt files may have different filenames or live in different directories, but should follow these structural conventions unless the user says otherwise. For a complete sample prompt file, see [references/example.md](references/example.md).

Sections start with a heading like:

```text
1.6 苗铁山 MIAO TIESHAN — 秃鹰帮大当家
1.8 执法机甲兵 × 4 — 战略司
1.2.3 Some Image Name
```

Recognize headings with:

```text
<chapter-id> <image-object-name>
```

where `<chapter-id>` is `x.x` or `x.x.x`.

Within a section, variants may start with lines like:

```text
变体 A — 机甲义肢展开（场景7进门）
变体 B — 机甲义肢锁死（场景9混战后）
```

Prompt labels may be:

```text
英文提示词...
中文提示词...
英文提示词-变体...
中文提示词-变体...
```

Accept labels with extra parenthetical notes and either Chinese or ASCII colon, for example `英文提示词（Midjourney）：`.

## Prompt Selection

For each image or variant:

1. Prefer `英文提示词` over `中文提示词`.
2. If English is missing, use Chinese.
3. A label containing `-变体` means the prompt is a variant prompt, often only an incremental change.
4. Collect prompt text after the selected label until the next prompt label, next variant heading, next section heading, or end of file.
5. Preserve prompt text verbatim except for trimming leading and trailing blank lines.

## Variant Chaining

Generate images section by section. Finish all images in one section before starting the next section.

For each section:

1. Generate the first full prompt image normally.
2. Treat the latest generated full prompt image in the same section as the current reference image.
3. For a variant whose selected prompt label contains `-变体`, generate it from the current reference image plus the variant prompt text.
4. After generating any variant, make that generated image the new current reference image for later incremental variants in the same section.
5. If a `-变体` prompt appears before any reference image exists in the section, generate it without a reference and record this assumption in the summary.

For a concrete variant chaining example, see [references/example.md](references/example.md).

## Output Layout

Save generated images under:

```text
<project-root>/image-outputs/<chapter-id>-<image-object-name>/
```

Use descriptive filenames for each generated image, for example:

```text
variant-A.png
variant-B.png
base.png
```

Sanitize directory and file names by replacing path separators, control characters, and characters invalid on common filesystems with hyphens. Keep chapter ids in the directory name.

If the image generation tool returns files outside `image-outputs`, move or copy them into the expected output directory after generation.

## Output language

Write all **skill-authored** human-readable text in **Chinese** by default. This includes but is not limited to `image-outputs/summary.md`, any other markdown or log text the skill writes under `image-outputs/`, and brief chat updates about batch progress or completion.

If the user **explicitly** requests **English** (or clearly states that summaries and related outputs should be in English), use **English** for all such prose for that run.

Do not translate **verbatim** excerpts from the prompt file when quoting them for traceability. Conventional filenames such as `variant-A.png` may stay as shown in this skill.

## Automation Rules

- Do not ask the user to confirm each image.
- Do not pause between sections unless a tool error requires recovery.
- If a single image generation fails, retry once with the same prompt and reference image.
- If it still fails, skip that image, record the failure in `summary.md`, and continue with the next image.
- Keep a per-image record while working: section, variant/base name, prompt language, full or variant prompt, reference image path if any, output path, status, and assumptions.

## Summary

After all image generation finishes, write:

```text
<project-root>/image-outputs/summary.md
```

The summary must include at least (headings and narrative in **Chinese** by default, or **English** if the user requested English output for this run):

- Task summary: prompt file, model requested, number of sections, number of images attempted, succeeded, skipped, or failed.
- Per-image results: section, image or variant name, output path, prompt language used, whether a reference image was used.
- Assumptions: missing model selector, missing English prompts, inferred references for incremental variants, skipped malformed sections, or any other judgment calls.
- Failures: image name, error summary, retry result, and whether generation continued.
