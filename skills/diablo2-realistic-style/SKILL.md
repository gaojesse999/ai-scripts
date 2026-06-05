---
name: diablo2-realistic-style
description: Generate near-photorealistic dark fantasy character portraits and scenes in the visual style of Diablo II live-action key art — gritty leather/metal textures, cinematic low-key rim lighting, ash-and-ruin atmosphere, bronze tanned skin with sweat sheen, full-body or three-quarter cinematic composition. Use when the user asks for images in the style of `image-outputs-00` ~ `image-outputs-03`, "暗黑II 风格", "diablo2 风格", "暗黑奇幻写实风格", "亚马逊女战士同款风格", "暗黑写实人像", "Diablo realistic portrait", or otherwise references the dark-fantasy-realistic look established in this project's reference images. Skill-authored prose defaults to Chinese unless the user requests English.
---

# Diablo II Realistic Style — 暗黑II 写实暗黑奇幻风格生图

## 用途与触发

本 skill 让 agent 以本项目 `image-outputs-00` ~ `image-outputs-03` 中已确立的视觉风格（**暗黑II live-action 写实暗黑奇幻**）生成新的人物/场景图。

允许变化的部分：**主体（人物、生物、场景）和姿态构图**。
固定不变的部分：**视觉风格 DNA**（见下文「风格 DNA」与「标准风格前缀」）。

何时触发：

- 用户提到 `image-outputs-00` ~ `image-outputs-03` 的风格、"那 4 个文件夹的风格"、"亚马逊女战士同款风格"
- 用户说 "暗黑II 风格 / diablo2 风格 / 暗黑奇幻写实 / 暗黑写实人像 / 接近真人的暗黑奇幻"
- 用户说 "Diablo realistic portrait / dark fantasy realism / live-action diablo style"

不要触发：

- 用户明确要求动漫、卡通、Q 版、像素、写实非奇幻题材时
- 用户使用 `batch-image-generation` 的批量提示词文件流程时（除非明确说要叠加本风格）

## 默认参数

```text
DEFAULT_GROUP_COUNT  = 1            # 用户没明说几组时
DEFAULT_IMAGE_QUALITY = 4k          # 仅当用户没在输入里提到分辨率/质量时使用
DEFAULT_ASPECT       = 16:9 cinematic widescreen
                                    # 仅当用户没在输入里提到画幅/比例时使用
DEFAULT_OUTPUT_LANG  = English      # 提示词语言；本 skill 散文默认中文
```

如用户明确要求 N 组（"生成 4 组"、"出 2 张"），按用户值。"多生几组" 这类模糊要求 → `N = 4` 并在 summary 记录假设。

### 比例与质量的探测规则

在拼提示词之前，先扫一遍用户输入（聊天文本 + 提示词文件，原文中英文都看），按以下关键词判定：

- **认为"用户已指定比例"** —— 出现下列任一即认为已指定，**跳过默认 16:9**：
  - 数字比 `2:3` / `3:2` / `4:3` / `3:4` / `16:9` / `9:16` / `1:1` 等
  - 关键词：`portrait`、`landscape`、`square`、`vertical`、`horizontal`、`wide`、`widescreen`、`竖图`、`横图`、`方图`、`正方形`、`竖构图`、`横构图`、`全身竖`、`头像方图`
  - 像素尺寸：`1024x1024` / `1920×1080` 等
- **认为"用户已指定质量/分辨率"** —— 出现下列任一即认为已指定，**跳过默认 4k**：
  - 关键词：`4k`、`8k`、`2k`、`1080p`、`720p`、`HD`、`high-res`、`high resolution`、`高清`、`超清`、`高分辨率`、`分辨率`、`画质`
  - 像素尺寸（同上）

判定结果记入 summary（"用户提供 / 默认 / 用户提供 + 默认补一个"）。两者独立判定。

## 风格 DNA（来自 4 个参考输出文件夹的提炼）

把以下要素全部具象化进每条优化提示词，**禁止省略**：

1. **写实程度**：near-photorealistic / live-action human proportions / close-to-real-person。**禁止**卡通、动漫、Q 版、塞璐璐、像素、油画风、平涂。
2. **打光**：cinematic low-key dramatic lighting，强 rim light / 边缘光勾勒身形，volumetric haze，moody shadows，high contrast。
3. **皮肤与质感**：tanned bronze skin with subtle sweat / oil sheen，realistic skin texture pores，battle-grime；皮肤、皮甲、金属各自有独立的写实材质响应。
4. **服装/装备质感**：battle-worn leather + reinforced metal trim，gritty medieval fantasy armor，详细的接缝、磨损、划痕、灰尘、血污可选。
5. **氛围 / 背景**：smoky ancient ruins、storm clouds、ash-filled battlefield、ruined temple、dead trees、broken stone columns。色调偏 **earthy 暗棕 + 冷灰 + 烟雾**。
6. **构图**：cinematic key art composition，主体居中或略偏，留出环境呼吸感。具体画幅（竖/横/方/比例）由用户输入或本次默认决定，不在风格 DNA 里写死。
7. **解剖**：realistic anatomy，肌肉线条 visible but not exaggerated；脸部 grounded、不萌、不卡通比例。
8. **整体调性**：grim、mature、grounded、Diablo II key art 美术方向；**不**走鲜艳、明亮、糖果色、二次元、可爱风。

负面（写进 negative 段或显式声明）：
`no cartoon, no anime, no chibi, no cel-shading, no flat illustration, no pixel art, no neon, no candy colors, no oversaturation, no airbrushed plastic skin, no celebrity likeness`.

## 标准风格前缀（英文，平台中立，必须挂在每张图前）

`[Global Style Prefix]` **不写死画幅与质量**，画幅和质量在末尾的 `[Output]` 行里按本次解析结果动态补：

```text
[Global Style Prefix]
Dark fantasy realism in the style of Diablo II live-action key art. Near-photorealistic, grounded live-action human look, realistic anatomy and material response. Cinematic low-key dramatic lighting with strong rim light, volumetric haze, moody atmospheric shadows, high contrast. Tanned bronze skin with subtle sweat sheen and realistic pores, battle-worn leather and reinforced metal armor with visible scuffs and grime, gritty medieval fantasy texture. Earthy palette of dark browns, charcoal grays, and smoke. Smoky ancient ruins or ash-filled battlefield ambience. Cinematic character key art composition, subject framed with breathing room. No cartoon, no anime, no chibi, no cel-shading, no flat illustration, no pixel art, no neon or candy colors, no airbrushed plastic skin, no celebrity likeness.
```

## 提示词构造模板（极简：风格前缀 + 用户原意 + 动态尾行）

每张图的最终 prompt 只做一件事：**把固定风格前缀和"从用户输入里提取出来的人物/场景描述"直接拼起来**，再在末尾按需补一行 `[Output]`。不再切槽位、不再补背景、不再二次创作。

```text
[Global Style Prefix]
<上一节那段固定英文，逐字照搬，不增不删>

[Subject & Scene]
<从用户输入里提取的人物/场景描述，英文一段流水文>

[Output]
<按下方"动态尾行规则"生成；如果两项都被用户写过，可整行省略>
```

### 动态尾行（`[Output]`）规则

依据上文「比例与质量的探测规则」的判定结果，按下表填写：

| 用户已指定比例? | 用户已指定质量? | `[Output]` 行内容 |
|---|---|---|
| 否 | 否 | `Aspect ratio: 16:9 cinematic widescreen. Output quality/resolution: 4k.` |
| 否 | 是 | `Aspect ratio: 16:9 cinematic widescreen.` |
| 是 | 否 | `Output quality/resolution: 4k.` |
| 是 | 是 | （整行省略，连 `[Output]` 标签也不要写） |

注意：**用户明确给的比例/质量值要保留在 `[Subject & Scene]` 段里**（按"提取规则 1：只抽取、不发明"原样翻译过来即可），不要改写、不要合并到 `[Output]`，也不要和默认值打架。

提取规则（处理用户输入 → `[Subject & Scene]`）：

1. **只抽取、不发明**：用户写了什么主体、外貌、服装、武器、姿态、场景、情绪、画幅、质量，就保留什么；用户没写的，**不要**补"废墟/暴风/低调光"等环境元素，那些已经在风格前缀里了。
2. **语言归一化**：如果用户输入是中文或中英混合，把它直译/轻改写成英文一段流水文（不要再分小标题、不要再加 `[xxx]` 块）。
3. **真人/版权角色降级**：用户提到具体真人演员或受版权角色 → 改写成 archetype（如 `warrior princess archetype`、`grim swordsman archetype`），并在 summary 记录这次改写。
4. **去重**：如果用户输入里出现的形容词已经在风格前缀里覆盖了（如 `dark fantasy`、`cinematic lighting`），可以删掉避免冗余；但**画幅/比例/分辨率/质量这类用户显式给出的硬性参数，永远保留**。
5. **多组之间是否变化**：默认 N 组共用同一段合并后的 prompt，多样性靠采样随机性。仅当用户明确要求"每组不同视角/动作/场景"时，才在 `[Subject & Scene]` 末尾追加一句区分（例如 `; full body heroic stance` vs `; three-quarter close-up`），其余部分仍 100% 一致。

## 工作流

1. **解析输入**
   - 主体来源可以是：用户聊天内联设定、外部提示词文件、用户提到的某个角色名、"和参考图相同的亚马逊女战士"。
   - 解析 `N`（组数）；缺省走 `DEFAULT_GROUP_COUNT = 1`。
   - 按上文「比例与质量的探测规则」分别判定**用户是否给了比例**、**用户是否给了质量**；两者独立。
   - 如果用户只说"生成同样风格的图"但完全没给主体，问 1 个简短中文澄清问题（"想生成什么主体？"），其余一律自动补默认。

2. **生成 RUN_TS 与输出根目录**
   - `RUN_TS = YYYYMMDDHHMMSS`（本地时间）
   - 输出根目录：`/host/workdir/projects/project-0529/image-outputs-<RUN_TS>/`
   - 章节子目录命名：`<chapter-id>-<slug>`（slug 为主体英文 kebab-case；中文主体也要给个英文 slug，不然路径里别用空格）

3. **构造提示词（合并即可）**
   - 固定风格前缀（逐字照搬）+ 提取出的用户主体/场景一段英文流水文 + 按「动态尾行规则」生成的 `[Output]` 行 → 完事。
   - 用户已给比例/质量 → 不补默认；都给 → 整行 `[Output]` 省略；都没给 → 末尾补 `Aspect ratio: 16:9 cinematic widescreen. Output quality/resolution: 4k.`。
   - 默认 N 组共用同一段合并后的 prompt，靠采样随机性出多样性；仅当用户明确要求每组不同时，在 `[Subject & Scene]` 末尾加一句小区分（视角/动作/景别）。
   - 真人/版权角色 → archetype 降级，并在 summary 记录。

4. **调用图片生成工具（standalone 模式）**
   - 直接使用当前可用的图片生成工具（如 `GenerateImage`），不要跳到 `batch-image-generation` skill。
   - 不传参考图（默认纯文本风格）。仅当用户主动给参考图时再传。
   - 生成的文件名建议：`base-g01.png` ~ `base-gNN.png`（保持与 `image-outputs-00`~`03` 的命名一致）。
   - 工具输出后，把图片复制/移动到本次 `image-outputs-<RUN_TS>/<chapter>-<slug>/` 下。

5. **写 summary.md**
   - 每次 run 在输出根目录写一个 `summary.md`，模板见下一节。
   - 一定要记录：模型/工具假设、质量假设、参考图重写（如有）、各图状态、原始与优化后提示词。

6. **失败重试**
   - 单张图失败：原 prompt 重试 1 次；仍失败则记录 `失败` 并继续下一张。
   - 不要因为单张失败而中止整个 run。

## 输出目录命名约定

```text
image-outputs-<RUN_TS>/
├── summary.md
└── <chapter-id>-<slug>/
    ├── base-g01.png
    ├── base-g02.png
    └── ...
```

`<chapter-id>` 默认 `1.1`；多个主体依次 `1.1, 1.2, 1.3 ...`。
`<slug>` 必须是 kebab-case 英文，例如 `barbarian-warrior`、`necromancer-male`。

## summary.md 模板

```markdown
# 批量生图任务总结

- RUN_TS: `<RUN_TS>`
- 输出根目录: `/host/workdir/projects/project-0529/image-outputs-<RUN_TS>/`
- 风格: Diablo II 写实暗黑奇幻（diablo2-realistic-style skill）

## 任务概览

- 提示来源: <聊天内联 / 外部文件路径>
- 模型: 默认 `gpt-5.5-none`；当前图片工具未暴露模型选择，记录为假设
- 章节数: <N>
- 尝试图像数: <X>，成功: <Y>，失败: <Z>

## 分组、比例与质量

- N (组数): <N>，来源: <用户明确 / 默认 1>
- 比例: <用户提供 "xxx" / 默认 16:9 cinematic widescreen>
- 质量: <用户提供 "xxx" / 默认 4k>
- 比例与质量是否进入 `[Output]` 尾行: <两者都默认补 / 仅补质量 / 仅补比例 / 整行省略（用户两者都给了）>

## 风格前缀

直接复制本 skill 的 `[Global Style Prefix]` 段，并记录是否对前缀做过任何就地修改（理想情况是没有）。

## 逐图结果

| 分组 | 输出路径 | 状态 |
|---|---|---|
| g01 | ... | 成功 / 失败 |

## 提示词细节

### 原始用户输入

```
<原文>
```

### 优化后提示词（合并版，每组完整列出）

#### g01

\`\`\`text
[Global Style Prefix]
<风格前缀逐字照搬>

[Subject & Scene]
<从用户输入提取并英文化后的人物/场景一段流水文>

[Output]
<按动态尾行规则生成的 1 行；如果用户两者都给了，连同 [Output] 标签一起省略>
\`\`\`

## 假设与判断

- 工具/模型限制
- 真人/版权角色改写记录（如有）
- 章节号与 slug 的自定决策

## 失败记录

无 / 列出。
```

## 与 batch-image-generation 的关系

本 skill **完全独立**：
- 不依赖 `batch-image-generation` 的提示词文件解析。
- 也不去复用它的 summary 写法之外的内部状态。
- 但**输出目录约定（`image-outputs-<RUN_TS>/`、`base-gNN.png`、`summary.md`）刻意和它保持一致**，方便用户串看。

如果用户同时给了一个 batch-image-generation 风格的提示词文件 **并且** 要求"用 diablo2 风格批量出图"：本 skill 仍负责"风格前缀 + 提示词重写"，由 agent 把每张图按本 skill 的模板拼好后再走批量流程。

## 假设清单（在本次 run 适用时记入 summary）

- 当前图片工具不暴露 `model` 选择参数 → 默认 `gpt-5.5-none` 仅作记录。
- 当前图片工具不暴露原生 quality/resolution 与 aspect ratio 参数 → 都通过 prompt 文本传达。
- 默认比例 = `16:9 cinematic widescreen`，默认质量 = `4k`；用户在输入里显式给了任一项就**不要**再补默认值（避免和用户值打架）。
- 用户提到具体真人/版权角色时，自动降级为 archetype，且不复刻肖像。
- 用户没指定章节号时，agent 自行编排 `1.1, 1.2, ...`。

## 反例（禁止做的事）

- ❌ 把风格前缀里的 "near-photorealistic" 改成 "anime / cartoon / illustration"。
- ❌ 用户没说背景/光照，agent 自己又在 `[Subject & Scene]` 里再写一遍 "废墟、烟雾、低调光"——那些已经在风格前缀里了，重复只会稀释主体语义。
- ❌ 把整段中文人物设定原样塞给图片工具（必须先英文化成一段流水文）。
- ❌ 把简单合并改回多槽位（[Subject] / [Costume] / [Pose] / [Environment]）—— 已废弃。
- ❌ 用户已经在输入里写了"竖图 / 9:16 / 8k / 1080p"等，agent 还在 `[Output]` 行里又补一遍 `16:9` 或 `4k` —— 必须按"动态尾行规则"跳过默认值。
- ❌ 把用户给的比例/质量值（如 `9:16`、`8k`）擅自改写成默认的 `16:9` / `4k`。
- ❌ 把画幅（`vertical 2:3`、`16:9` 等）写回 `[Global Style Prefix]` —— 风格前缀必须保持画幅无关。
- ❌ 主动复刻特定演员/已有 IP 角色的肖像。
- ❌ 跨 run 复用同一个 `image-outputs-<RUN_TS>/` 目录。
