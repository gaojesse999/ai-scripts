# Asset Sheet Template

The asset sheet is a **single Markdown file** delivered at end of Phase 2. It is the user's working document for image generation.

Save to the project's `plans/` folder (or equivalent) as:
```
Assets_<scope>.md      # e.g., Assets_Scene1.md, Assets_Act1.md, Assets_Sc21-23.md
```

Reference image-prompt prefix: [`reference/ASSET_PROMPT_PREFIX.md`](../reference/ASSET_PROMPT_PREFIX.md).

---

## Skeleton

```markdown
# <Project> — <Scope> 资产清单

**Scene/Scope:** `<INT./EXT. LOCATION — TIME>` (or scope range)
**Source:** `<path/to/script.md>` (lines X–Y)
**Purpose:** 用于 Nano Banana / Soul / 即梦 / Midjourney / Flux 等图像工具生成基础资产，回传后用于 Seedance 2.0 提示词分镜。

---

**风格前缀 (STYLE PREFIX)**
*   风格 (Style)：8K IMAX。电影级写实CG —— 高精度3D渲染，写实皮肤与布料材质，写实配色，画面干净优雅，<项目美学一句话>。
*   光照 (Lighting)：仅限自然光 —— 逆光/背光 (contre-jour)，摄像机位于阴影侧，画面中始终带有氛围感薄雾。主光源仅来自天空和窗户。无人工照明。
*   色彩 (Color)：60:30:10 法则 —— 主色调 / 辅助色 / 点缀色。
*   镜头 (Camera)：物理电影镜头。180度快门运动模糊。
*   皮肤 (Skin)：毛孔级真实感 —— 面部绒毛，不对称的痣，毛细血管泛红，毛孔阴影与环境光照相匹配。
*   表演 (Acting)：好莱坞级别 —— 做出反应前的微小停顿，精准的视线，带有眼神光的灵动双眸，呼吸引起的胸部起伏。
*   物理 (Physics)：遵循重力和惯性 —— 物体有真实的重量感，正确的接触阴影。不要悬浮的道具。
*   构图 (Composition)：三分法 + 黄金比例。每个人从第一帧开始就处于运动状态。
*   连贯性 (Continuity)：角色、道具、环境在每个切换镜头中保持完全一致。无身份/特征偏移 (No identity drift)。
*   技术 (Technical)：24fps 平滑运动。8K 细节。画面无抖动。
*   音频 (Audio)：仅有环境音效 (SFX)。无音乐。无字幕。

> 把上面这段 STYLE PREFIX 与下面任意一条**资产描述**拼接，再在末尾加 `输出：单张图，<比例>，<背景>。`，就得到一条可直接粘贴到图像工具的提示词。

---

## Characters 人物

> 已有参考图请勿重做，标注 `[已存在: <path>]`。建议输出比例：单人立绘 `1:1` / 三视图 `16:9`，皆用中性无缝背景。

- **<NAME 姓名> <ROMANIZATION (optional)>** `[已存在: <path>]` *(if applicable)*
  <一段视觉描述：体型、发型、肤色、服装、特征、配饰、磨损/伤痕。只写镜头能看到的；戏剧动机不写。>

- **<NAME>**
  <description>

- **<群演组 GROUP — N 人>**
  <统一描述 + 配置差异（哪些昏迷 / 哪些清醒 / 装备差异等）>

---

## Locations 场景

> 建议输出比例：establishing `21:9` / 室内 `16:9`，写入世界环境。

- **<LOCATION 名称>**
  <视觉描述：天空 / 地面 / 远景物 / 光线方向 / 大气 / 颜色基调。只写一帧能看到的。>

- **<LOCATION>**
  <description>

---

## Props 道具

> 建议输出比例：`1:1` 白色无缝背景（用于贴入分镜）；如需在世界中展示则改为 `1:1` in-world surface。

### <子分类，例如「武器」「载具」「个人物品」>

- **<PROP 名称 PROP NAME>**
  <视觉描述：尺寸、材料、磨损、颜色、可活动部分、铭文/图案。如有触发逻辑（按下哪个键展开），只写**外观**层面，不写戏剧时机。>

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

1. **STYLE PREFIX is verbatim from `reference/ASSET_PROMPT_PREFIX.md`** — only the project-aesthetic clause inside the **风格 (Style)** bullet may be customized per project. Lock that line at the start of the project; reuse across scope.
2. **Visual descriptions only.** No "Want / Need / Hamartia" — that is the screenwriting tool's job. If the script tells you a character is "afraid of fire," do not write that here. Write only what the camera will see.
3. **Mark `[已存在: path]`** for any asset that already has a reference image in the project. Do not regenerate. Pass the path in chat to the user as a reminder.
4. **Suggested filenames** must be `lowercase_with_underscores.png`. In Phase 3 they are mapped to named `@`-prefixed aliases for video prompts, e.g. `@韩立=韩立，@Jane=Jane`. Never convert them into numbered image aliases.
5. **Group asset entries** under sub-headings only when there are 5+ items in a category (e.g., props split into 武器 / 载具 / 个人物品). Otherwise flat list.
6. **Style References** — only include if there's an obvious reuse value (multi-class wardrobe sheet, recurring vehicle three-view, recurring HUD detail). If nothing rises to that bar, omit the section entirely.
7. **Length budget:** the asset sheet is a working doc, not a novel. Each visual description ≈ 1–4 sentences. Cut purple prose. The user will read this 20+ times during a project.

---

## Anti-patterns

- ❌ Adding camera moves into asset descriptions ("the camera slowly orbits the character"). Camera goes into shotlist prompts (Phase 4), not the asset sheet.
- ❌ Adding scene-specific behavior ("standing nervously while waiting for the train"). Asset is reusable across scenes; behavior is per-shot.
- ❌ Inventing physical details the script doesn't imply. If the script says "old man," don't add "with a scar over his left eye." Ask the user.
- ❌ Mixing image-prefix block with the video `STYLE_BLOCK.md` block. They are two different prefixes for two different pipelines.
