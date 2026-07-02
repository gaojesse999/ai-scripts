# Asset Sheet Template

The asset sheet is a **single Markdown file** delivered at end of Phase 2. It is the user's working document for image generation.

Save to the project's `plans/` folder (or equivalent) as:
```
Assets_<scope>.md      # e.g., Assets_Scene1.md, Assets_Act1.md, Assets_Sc21-23.md
```

Reference prefixes: [`reference/ASSET_PROMPT_PREFIX.md`](../reference/ASSET_PROMPT_PREFIX.md).

**Key change from the old template:** there is no longer one giant universal prefix pasted onto every asset. Prefixes are now **subject-scoped** (人物 / 场景 / 道具) and **tier-scoped** (写实 / 动画). Each section carries its own short, camera-first prefix. This makes prompts photo-real (not AI-looking) and much shorter. Lock the **tier** once per project from the aesthetic.

---

## Skeleton

```markdown
# <Project> — <Scope> 资产清单

**Scene/Scope:** `<INT./EXT. LOCATION — TIME>` (or scope range)
**Source:** `<path/to/script.md>` (lines X–Y)
**Purpose:** 用于 Nano Banana / Soul / 即梦 / Midjourney / Flux 等图像工具生成基础资产，回传后用于 Seedance 2.0 提示词分镜。
**质感档 (Tier):** `写实` 或 `动画（画风：<画风>）` — 全项目锁定。
**项目美学一句话:** `<aesthetic line>` — 全项目锁定。

> 用法：每个分区（人物 / 场景 / 道具）顶部有各自的**风格前缀**。把该分区前缀 + 某条**资产描述** + 末尾 `输出：单张图，<比例>，<背景>。` 拼接，即得一条可直接粘贴的提示词。
> ⚠️ **负面行只给有负面框的工具（Midjourney / SD / 即梦）放进负面框。用 GPT / DALL·E / 文生图（无负面框）→ 整行负面都不要粘**——否则负面词会被当正向照着画（皮肤 / 长相类外观词尤其危险，只在正文正向写）。
> 质感是硬指标：写实档要与真人 / 真实照片无法区分；动画档保留画风但要顶级动画长片的最高保真度。二者都不接受廉价 / 扁平 / 塑料 / AI 感。见 `ASSET_PROMPT_PREFIX.md`。

---

## Characters 人物

<粘贴 ASSET_PROMPT_PREFIX.md §2A（写实）或 §2B（动画）的「风格前缀 · 人物」块，把 <项目美学一句话> 填入。>

**负面（仅 Midjourney/SD/即梦 放负面框；⚠️GPT/文生图整行不要粘）：** <粘贴 §2 对应档位的 character negative line。>

> ⚠️ **主参考先出肖像**：写实档角色**先出一张竖幅胸上 / 头肩中近景、四分之三侧身、抓拍视线**的主参考（`4:5`）——脸够大才有真实肤质（半身对年轻脸会被磨平）。**全身 / 三视图**作为可选第二张只锁服装（放 Style References），脸小、偏摆拍，不作面部依据。**别用全身正面立正当唯一角色图**（全身立绘看着假的根因）。
> ⚠️ **去美化 + 水润配平**：年轻 / 漂亮角色写 `普通真实素人长相 / 非网红脸 / 素颜或极淡妆`（压模型的美颜默认脸）；同时皮肤要 `水润健康、有油脂光泽`，别写成干哑砂纸感。
> **自然情境背景**（符合角色世界、简洁不喧宾夺主，非纯色影棚）；**面部完整不遮挡**（除非角色设定要求）。
> ⚠️ **性别 / 属性标识**：每个角色开头标 `【女性】` / `【男性】` / `【非人类：<物种>】`（决定长睫默认仅女性、胡须默认仅男性）。

- **<NAME 姓名> <ROMANIZATION (optional)>** `【女性 / 男性 / 非人类：<物种>】` `[已存在: <path>]` *(if applicable)*
  <一段视觉描述：体型、发型、肤色、服装、特征、配饰、磨损 / 伤痕。只写镜头能看到的；戏剧动机不写。写清一个自然的抓拍瞬间（走动 / 回头 / 侧望等），而非「立正面向镜头」。⚠️手放松下垂 / 扶包带 / 部分出画，别抬到脸前或做复杂手势（易出 AI 手）；手部戏留给视频。>
  建议文件名：`<name>.png`
  输出：单张图，4:5，胸上 / 头肩中近景、四分之三侧身抓拍，自然情境背景，简洁不喧宾夺主。

- **<NAME>**
  <description>
  建议文件名：`<name>.png`
  输出：单张图，4:5，胸上 / 头肩中近景、四分之三侧身抓拍，自然情境背景，简洁不喧宾夺主。

- **<群演组 GROUP — N 人>**
  <统一描述 + 配置差异（哪些昏迷 / 哪些清醒 / 装备差异等）>

---

## Locations 场景

<粘贴 ASSET_PROMPT_PREFIX.md §3A（写实）或 §3B（动画）的「风格前缀 · 场景」块。注意：场景前缀不含皮肤 / 毛发 / 眼睛条目。>

**负面（仅 Midjourney/SD/即梦 放负面框；⚠️GPT/文生图整行不要粘）：** <粘贴 §3 对应档位的 location negative line。>

> establishing `21:9` / 室内 `16:9`，写入世界环境。

- **<LOCATION 名称>**
  <视觉描述：天空 / 地面 / 远景物 / 光线方向 / 大气 / 颜色基调。只写一帧能看到的。>
  建议文件名：`<location>.png`
  输出：单张图，21:9，世界内环境。

- **<LOCATION>**
  <description>

---

## Props 道具

<粘贴 ASSET_PROMPT_PREFIX.md §4A（写实）或 §4B（动画）的「风格前缀 · 道具」块。>

**负面（仅 Midjourney/SD/即梦 放负面框；⚠️GPT/文生图整行不要粘）：** <粘贴 §4 对应档位的 prop negative line。>

> `1:1`，默认置于世界内真实表面 / 情境（in-world surface）；不强制纯白影棚。

### <子分类，例如「武器」「载具」「个人物品」>

- **<PROP 名称 PROP NAME>**
  <视觉描述：尺寸、材料、磨损、颜色、可活动部分、铭文 / 图案。只写**外观**，不写戏剧时机。>
  建议文件名：`<prop>.png`
  输出：单张图，1:1，世界内真实表面 / 情境。

- **<PROP>**
  <description>

---

## Style References 风格参考（可选生成）

> 可选生成的辅助资产，用于跨场景复用。优先级低于必备资产。

- **<NAME — 三视图 / Detail / Establishing>**：<用途说明>。
- **<NAME>**：<purpose>。

---

## 上传与命名约定

请生成后回传，文件名建议（小写下划线，无空格，扩展名 `.png`）：

```
<asset_name_1>.png
<asset_name_2>.png
<asset_name_3>.png
...
```

已存在的资产复用即可，不必重做：

```
<existing_path>           ✅ 已存在
```

---

## 下一步

请先生成上述资产并回传，命名按上方约定。然后告诉我：

1. **要为 <scope> 哪一段构建分镜？** 例如：
   - `<sub-scope-1>`：<一句话描述，约 N 个 15 秒提示词>
   - `<sub-scope-2>`：<…>
2. **是否启用自定义风格 block？**（默认采用 `reference/STYLE_BLOCK.md` Lubezki × Deakins 逆光 / 60:30:10 / 仅实用光源）

确认后我会先输出**多人场地的俯视空间调度图（top-down schema）**，待确认后再生成 HTML 分镜。
```

---

## Filling rules

1. **Prefixes are subject-scoped and tier-scoped.** Paste the 人物 prefix at the top of Characters, the 场景 prefix at the top of Locations, the 道具 prefix at the top of Props — each from `reference/ASSET_PROMPT_PREFIX.md`, at the project's locked tier (写实 / 动画). Do **not** paste the character skin/hair/eye block onto scenes or props. Two things vary per project inside each block: (a) the `<项目美学一句话>` clause, (b) the tier (locked once). Everything else is verbatim.
2. **Negatives live in a dedicated line per section**, meant for the tool's negative field — never as long inline `禁…禁…` chains inside the positive prompt.
3. **Visual descriptions only.** No "Want / Need / Hamartia" — that is the screenwriting tool's job. Write only what the camera will see.
   - **Label every character** with `【女性】` / `【男性】` / `【非人类：<物种>】` at the start of its entry (gates gender-linked texture: 浓密卷翘长睫默认仅女性、胡须默认仅男性；非人类默认都不套用).
4. **Mark `[已存在: path]`** for any asset that already has a reference image. Do not regenerate.
5. **Suggested filenames** must be `lowercase_with_underscores.png`. In Phase 3 they map to bracket aliases for video prompts (`[韩立]=韩立`). Never numbered image aliases.
6. **Group asset entries** under sub-headings only when 5+ items in a category. Otherwise flat list.
7. **Style References** — include only if there's obvious reuse value; else omit the section entirely.
8. **Length budget.** Each visual description ≈ 1–4 sentences. Cut purple prose. Because the prefix is now short and camera-first, the whole composed prompt should stay compact — that is what keeps images photo-real instead of "AI soup".

---

## Anti-patterns

- ❌ One giant universal prefix on every asset (old style). Use subject-scoped prefixes.
- ❌ `CG / 3D渲染 / 数字重建 / 8K / 超高清 / 微观细节` in a realistic prompt — these produce the AI-render look. Say `真实照片 / 剧照 / 实拍` instead.
- ❌ Video directives in an image prompt (`运动模糊 / 24fps / 180度快门 / 每帧运动 / 呼吸起伏`). They smear a still reference.
- ❌ Forced pure-color / white backdrop for characters. Use natural in-world background (pure backdrops read as CG turnaround sheets).
- ❌ Skin / hair / eye / eyelash / beard clauses on a location or prop.
- ❌ Long inline `禁X禁Y禁Z` negatives in the positive prompt. Use the negative line.
- ❌ Camera moves or scene-specific behavior in asset descriptions (those go into Phase 4 shotlist prompts).
- ❌ Mixing this image prefix with the video `STYLE_BLOCK.md` block. Two different pipelines.
