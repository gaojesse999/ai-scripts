---
name: batch-image-generation
description: Batch generate images from a user-specified prompt file, including prompt parsing, platform-neutral prompt optimization, variant chaining, image quality selection, output organization, and summary writing; skill-authored prose defaults to Chinese unless the user requests English. Use when the user asks to generate images, create images, make pictures, batch image generation, image generation, picture generation, 生图, 批量生图, 生成图片, 生成图像, 图片生成, 出图, 以图生图, or variants of those phrases.
---

# Batch Image Generation

## Purpose

Batch generate all images described in a user-specified prompt file, fully automatically. Do not ask for confirmation once the prompt file and task are clear.

## Defaults

```text
DEFAULT_IMAGE_MODEL = gpt-5.5-none
DEFAULT_IMAGE_QUALITY = 4k
DEFAULT_GROUP_COUNT = 1
```

Use `DEFAULT_IMAGE_MODEL` as the default image generation model whenever the image tool or API exposes a model option. If the available tool has no model selector, proceed with the available image generation tool and record that assumption in `image-outputs-<RUN_TS>/summary.md`.

Resolve image quality for each run as: user-specified quality or resolution first, otherwise `DEFAULT_IMAGE_QUALITY`. To change the default quality later, edit only `DEFAULT_IMAGE_QUALITY` in this section.

Resolve **group count** `N` for each run as: the number explicitly requested by the user (e.g. "生成4组", "出三组", "generate 4 sets/groups/variations per image"), otherwise `DEFAULT_GROUP_COUNT` (= 1). `N` must be a positive integer; if the user gives an ambiguous or non-numeric request like "多生几组", default to `N = 4` and record the assumption in `image-outputs-<RUN_TS>/summary.md`.

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

## Style Prefix

The prompt file may contain an optional **style prefix block** that defines a unified visual style to apply to **every** image in the run. Detection and parsing rules:

1. Locate the first line that contains `风格前缀` (case-insensitive on any accompanying English like `STYLE PREFIX`), regardless of surrounding markdown emphasis (`**…**`), parentheses, or colons. This line is the **style prefix heading**.
2. The style prefix content **starts on the next non-empty line** after the heading and continues until the first section heading (a line matching `<chapter-id> <image-object-name>` where `<chapter-id>` is `x.x` or `x.x.x`), or until end of file.
3. Preserve the style prefix text verbatim except for trimming leading/trailing blank lines. Bullet markers like `*` or `-` and bilingual labels such as `风格 (Style)` are part of the style and should be kept.
4. If no `风格前缀` heading exists, treat the run as having an empty style prefix and proceed normally; record this in `image-outputs-<RUN_TS>/summary.md`.
5. The style prefix is **global** for the run. Do not treat it as a section, do not generate an image for it, and do not chain it as a variant.

For a concrete style prefix example, see [references/example.md](references/example.md).

## Prompt Selection

For each image or variant:

1. Prefer `英文提示词` over `中文提示词`.
2. If English is missing, use Chinese.
3. A label containing `-变体` means the prompt is a variant prompt, often only an incremental change.
4. Collect prompt text after the selected label until the next prompt label, next variant heading, next section heading, or end of file.
5. Preserve prompt text verbatim except for trimming leading and trailing blank lines.

## Prompt Optimization

Before generating each image, optimize the selected prompt into a platform-neutral prompt that can work across image generation platforms and models.

Before prompt optimization, resolve the image quality for the current run: use the user's requested quality/resolution if provided, otherwise use `DEFAULT_IMAGE_QUALITY`.

When optimizing:

1. Remove or rewrite platform-specific syntax and parameters, such as Midjourney flags (`--ar`, `--style`, `--v`, etc.), Flux-only wording, or other model/vendor-specific controls.
2. Preserve the creative intent, subject identity, composition, style, lighting, camera language, constraints, and variant changes from the original prompt.
3. Convert useful platform parameters into generic natural-language instructions when possible. For example, turn an aspect ratio flag into "vertical 2:3 composition" or "wide 16:9 composition" instead of dropping it.
4. Do not invent new visual requirements that are not implied by the original prompt or the user's request.
5. Add the resolved image quality to the optimized prompt as a concise, platform-neutral output instruction, for example: `Output quality/resolution: <resolved-image-quality>.`
6. **Apply the parsed style prefix (see Style Prefix section) to every optimized prompt** so the entire run shares one unified visual style:
   - Prepend the style prefix as a clearly labeled block at the top of the optimized prompt, for example:
     ```text
     [Global Style Prefix]
     <verbatim style prefix content>

     [Scene Prompt]
     <optimized scene prompt>
     ```
   - If a per-image prompt directly conflicts with a style-prefix directive (for example, the scene needs neon while the prefix forbids neon, or the scene specifies artificial light while the prefix mandates natural light only), prefer the style prefix to keep the run consistent and record the conflict and resolution in the per-image record.
   - When the style prefix is empty, skip this step and record that no style prefix was applied.
   - Apply the style prefix to **base prompts and `-变体` (variant) prompts alike**, including when chaining from a reference image.
7. Use the optimized prompt (with style prefix applied) for image generation.
8. Keep both the original selected prompt and the optimized prompt in the per-image record. If no optimization was needed except adding the quality instruction and style prefix, record that clearly.

When calling the image generation tool, also set its native quality or resolution parameter to the resolved image quality if such a parameter exists. If the tool has no native quality/resolution selector, the quality instruction in the optimized prompt is the fallback; record this in `image-outputs-<RUN_TS>/summary.md`.

## Variant Chaining

Generation is organized into **waves** that span **all sections at once**, not section-by-section. A wave runs as one parallel batch, and the next wave only starts after the previous wave finishes (so per-group reference images are ready). This applies for both `N = 1` and `N > 1`; the only difference is how many group copies each item produces.

Definitions:

- For each section, list its prompts in document order. The first full prompt is the section's **base** (wave index `w = 0`). Each subsequent `-变体` prompt is the section's variant at wave index `w = 1, 2, 3, ...`.
- For a run with resolved group count `N`, every prompt expands into `N` independent generations indexed by group `g = 1..N`. When `N = 1`, each prompt is just one generation.
- Maintain a per-section, per-group reference pointer `ref[section][g]`.

Wave execution:

1. **Wave 0 — all bases in parallel.** Across **every section** in the prompt file, generate all base images in one parallel batch. For section `s` and group `g`, this produces `base[s][g]`. After the wave, set `ref[s][g] = base[s][g]` for every `(s, g)`.
2. **Wave w (w ≥ 1) — all w-th variants in parallel.** Across every section that has a variant at wave index `w`, generate the variant for each group `g` in parallel. Each generation for `(s, g, w)` uses `ref[s][g]` as its reference image plus the variant prompt text. After the wave, update `ref[s][g]` to the just-generated variant image for that `(s, g)`.
3. Continue until no section has a variant at the next wave index.
4. Sections with fewer variants simply contribute nothing to later waves; they do not block other sections.
5. Per-group isolation is strict: group `g`'s wave-`w` variant in section `s` must depend only on `ref[s][g]` (its own section, its own group). Never mix references across groups or across sections.
6. If a section's `-变体` prompt appears before any base exists in that section (malformed input), generate its wave-`w` images without a reference and record this assumption in the summary.
7. If `ref[s][g]` is missing because an earlier wave failed for that `(s, g)` (see Automation Rules), skip the rest of that `(s, g)` chain; other `(s, g)` chains continue normally in the same wave.

Worked example (two sections, `N = 2`, section 1 has one variant, section 2 has none):

- Wave 0 (parallel, 4 generations): `base[1][1]`, `base[1][2]`, `base[2][1]`, `base[2][2]` — i.e. `1.11`, `1.12`, `2.11`, `2.12`.
- Wave 1 (parallel, 2 generations): `var1[1][1]` from `base[1][1]`, `var1[1][2]` from `base[1][2]` — i.e. `1.21` depends on `1.11`, `1.22` depends on `1.12`. Section 2 has no wave-1 variant and contributes nothing.

For a concrete variant chaining example, see [references/example.md](references/example.md).

## Output Layout

At the start of each run, compute a **run timestamp** `RUN_TS` in local time using the format `YYYYMMDDHHMMSS` (e.g. `20260518163102`). Use this same `RUN_TS` for every image and every artifact written by the run, so all files for one invocation land under the same root and parallel runs cannot overwrite each other.

The run's output root is:

```text
<project-root>/image-outputs-<RUN_TS>/
```

Save generated images under:

```text
<project-root>/image-outputs-<RUN_TS>/<chapter-id>-<image-object-name>/
```

Use descriptive filenames for each generated image. When `N = 1`, use the flat naming:

```text
base.png
variant-A.png
variant-B.png
```

When `N > 1`, suffix each file with its group index `g` (1-based, zero-padded to match the width of `N`, e.g. `g01..g04` for `N = 4`):

```text
base-g01.png
base-g02.png
base-g03.png
base-g04.png
variant-A-g01.png
variant-A-g02.png
...
```

Group indices must be consistent across the base and all variants in the same section, so `variant-A-g02.png` is always the variant chained from `base-g02.png` (or the previous `variant-*-g02.png`).

Sanitize directory and file names by replacing path separators, control characters, and characters invalid on common filesystems with hyphens. Keep chapter ids in the directory name.

If the image generation tool returns files outside the run's `image-outputs-<RUN_TS>/` root, move or copy them into the expected output directory after generation.

## Output language

Write all **skill-authored** human-readable text in **Chinese** by default. This includes but is not limited to `image-outputs-<RUN_TS>/summary.md`, any other markdown or log text the skill writes under `image-outputs-<RUN_TS>/`, and brief chat updates about batch progress or completion.

If the user **explicitly** requests **English** (or clearly states that summaries and related outputs should be in English), use **English** for all such prose for that run.

Do not translate **verbatim** excerpts from the prompt file when quoting them for traceability. Conventional filenames such as `variant-A.png` may stay as shown in this skill.

## Automation Rules

- Do not ask the user to confirm each image.
- Do not pause between waves unless a tool error requires recovery. Waves themselves are the only synchronization point: wave `w + 1` starts only after wave `w` completes (or its failures are recorded), because variants depend on the previous wave's per-group reference images.
- If a single image generation fails, retry once with the same prompt and reference image.
- If it still fails, skip that image, record the failure in `summary.md`, and continue with the next image.
- A failure in one `(section, group)` chain does not block any other `(section, group)` chain at the same or later waves. If `(s, g)` fails at some wave after retry, skip the rest of that chain (later variants for `(s, g)` have no valid reference) while every other `(s', g')` continues normally. Record the broken chain in `summary.md`.
- Keep a per-image record while working: section, variant/base name, **group index `g` and total `N`**, prompt language, original selected prompt, optimized prompt, full or variant prompt type, resolved image quality, how quality was applied (native tool setting, prompt instruction, or both), whether the style prefix was applied (and any style-vs-scene conflict resolution), reference image path if any, output path, status, and assumptions.

## Summary

After all image generation finishes, write:

```text
<project-root>/image-outputs-<RUN_TS>/summary.md
```

Include `RUN_TS` and the run's output root path at the top of the summary for traceability.

The summary must include at least (headings and narrative in **Chinese** by default, or **English** if the user requested English output for this run):

- Task summary: prompt file, model requested, number of sections, number of images attempted, succeeded, skipped, or failed.
- Group settings: resolved group count `N`, whether it came from the user request or from `DEFAULT_GROUP_COUNT`, and any per-group chain breaks caused by failures.
- Quality settings: requested/default quality, resolved quality used for the run, how quality was applied (native tool setting, prompt instruction, or both), and any tool limitation around quality or resolution.
- Style prefix: whether a `风格前缀` block was found, the verbatim style prefix content used (or note that it was empty), and any style-vs-scene conflicts and how they were resolved.
- Per-image results: section, image or variant name, output path, prompt language used, whether a reference image was used.
- Prompt details: include the original selected prompt and the optimized prompt for every image where optimization was performed. If many prompts are long, keep them under clear per-image subsections or collapsible-style markdown details.
- Assumptions: missing model selector, missing quality selector, missing English prompts, inferred references for incremental variants, skipped malformed sections, or any other judgment calls.
- Failures: image name, error summary, retry result, and whether generation continued.
