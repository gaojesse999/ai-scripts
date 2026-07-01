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
*   质感 (Fidelity)：⚠️极高角色质感 —— 人物 / 动物 / 怪物 / 生物一律同一标准。真人（真实生物）级实拍质感，非动画/非插画/非二次元/非塑料CG感，呈现高预算电影的真实剧照效果。Arri Alexa 65 大画幅电影摄影机成像风格：真实镜头光学、自然镜头畸变、真实焦外虚化。8K 超高清微观细节，所有材质遵循物理基础渲染 (PBR) 与真实世界物理规律。（动画 / 风格化项目请换用 `ASSET_PROMPT_PREFIX.md` 的动画档质感行 —— 保留画风，但仍需最高保真度。）
*   光照 (Lighting)：仅限自然光 —— 逆光/背光 (contre-jour)，摄像机位于阴影侧，画面中始终带有氛围感薄雾。主光源仅来自天空和窗户。无人工照明。HDR 高动态范围，完整保留高光与阴影细节，呈现电影胶片般的层次感。
*   色彩 (Color)：60:30:10 法则 —— 主色调 / 辅助色 / 点缀色。
*   镜头 (Camera)：物理电影镜头。180度快门运动模糊。浅景深，真实焦外虚化，背景带空气透视与电影级虚化。
*   皮肤/表皮 (Skin)：毛孔级真实感 + 物理准确的次表面散射 (SSS)，作用于**面部及一切裸露在外的肌肤**（颈部、锁骨、肩、手臂、手部、腿部、脚等）。人物 —— 面部与所有裸露皮肤均有绒毛、不对称的小痣、毛细血管轻微泛红、自然油脂高光反射，以及真实静脉/关节褶皱/指节与指甲细节，毛孔阴影与环境光照相匹配，⚠️禁麻子、禁痘坑、禁坑洼、禁凹凸不平、禁粗糙糙皮、禁过度纹理/过度锐化。动物/怪物/生物 —— 皮肤 / 鳞片 / 甲壳 / 兽皮 / 黏膜 / 角质等全身表皮同样物理准确：真实厚度、湿润度、皱褶、疤痕、SSS 透光与角质高光，符合该物种的生理结构。（动画档追加「面部整体保持光滑干净、底子均匀健康，仅细腻毛孔质感」，写实档不加，见 `ASSET_PROMPT_PREFIX.md` 质感分级。）
*   毛发/羽/鬃 (Hair & Fur)：纤维级真实度，适用于头发、**眉毛、睫毛、胡须/胡子（男性）**、体毛、兽毛、鬃毛、羽毛、须。单根纤维清晰可见，真实毛鳞片/羽枝结构、自然粗细变化、随机方向分布与真实密度；纤维间存在自然间隙与透光，具真实反射/折射/吸收与高光变化；根部、尖端与不同区域层次分明，具自然蓬松度、柔韧性与重量感；受风力/重力/运动产生真实物理摆动。**面部细毛**：眉毛按自然生长方向排布、根根分明、疏密自然；睫毛（尤指女性）根根独立、自然弯曲卷翘、根部渐深；男性胡须/胡茬有真实软硬粗细、毛囊根部质感与自然生长范围。⚠️禁塑料感、禁 CG 假毛/假羽/假睫毛感、禁过度光滑、禁统一梳理排列、禁刷子状/成缕结块的睫毛。
*   材质 (Materials)：所有织物、装甲、外壳与表面遵循 PBR —— 真实纤维/材料纹理、自然褶皱、重力下垂、材质差异；真实粗糙度、反射率与光泽变化。
*   表演 (Acting)：好莱坞级别 —— 做出反应前的微小停顿，精准的视线，带有眼神光的灵动双眸，呼吸引起的胸部起伏。
*   物理 (Physics)：遵循重力和惯性 —— 物体有真实的重量感，正确的接触阴影。不要悬浮的道具。
*   背景 (Background)：⚠️**角色/生物资产 = 纯色背景** —— 单一纯色背景，无场景/道具/图案/纹理/渐变内容/环境等任何其他背景元素；主体面部完整不遮挡（除非角色设定本身要求，如始终戴面具/头盔）。**场景/环境资产不受此限**，按世界内真实环境正常呈现。
*   构图 (Composition)：三分法 + 黄金比例。人物比例真实准确、姿态自然，避免僵硬摆拍。每个人从第一帧开始就处于运动状态。
*   连贯性 (Continuity)：角色、道具、环境在每个切换镜头中保持完全一致。无身份/特征偏移 (No identity drift)。
*   技术 (Technical)：24fps 平滑运动。8K 细节，真实微观细节。画面无抖动。

> 把上面这段 STYLE PREFIX 与下面任意一条**资产描述**拼接，再在末尾加 `输出：单张图，<比例>，<背景>。`，就得到一条可直接粘贴到图像工具的提示词。
> 质感是硬指标：写实项目要与真人无法区分；动画/风格化项目保留画风但要顶级动画长片的最高保真度。二者都不接受廉价/扁平/塑料感。见 `ASSET_PROMPT_PREFIX.md` 的「质感分级」。

---

## Characters 人物

> 已有参考图请勿重做，标注 `[已存在: <path>]`。建议输出比例：单人立绘 `1:1` / 三视图 `16:9`。
> ⚠️ **纯色背景**：人物/生物立绘与三视图一律用单一纯色背景，无任何其他背景内容（无场景/道具/图案/纹理/环境）。输出行写 `纯色背景，无其他背景内容`。
> ⚠️ **面部不遮挡**：面部须完整清晰、无遮挡（手/头发/道具/面罩/阴影/裁切都不得挡脸），除非角色设定本身要求（如始终戴面具的反派、设计上遮住一只眼的发型）。

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

1. **STYLE PREFIX is verbatim from `reference/ASSET_PROMPT_PREFIX.md`** — only two things vary per project: (a) the project-aesthetic clause inside the **风格 (Style)** bullet, and (b) the **质感 (Fidelity)** bullet, which is swapped between the realistic tier (default) and the animation/stylized tier per the「质感分级」section. Lock both at the start of the project; reuse across scope. The **皮肤 / 毛发 / 材质** bullets are never dropped.
2. **Visual descriptions only.** No "Want / Need / Hamartia" — that is the screenwriting tool's job. If the script tells you a character is "afraid of fire," do not write that here. Write only what the camera will see.
3. **Mark `[已存在: path]`** for any asset that already has a reference image in the project. Do not regenerate. Pass the path in chat to the user as a reminder.
4. **Suggested filenames** must be `lowercase_with_underscores.png`. In Phase 3 they are mapped to named bracket aliases for video prompts, e.g. `[韩立]=韩立，[Jane]=Jane`. Never convert them into numbered image aliases.
5. **Group asset entries** under sub-headings only when there are 5+ items in a category (e.g., props split into 武器 / 载具 / 个人物品). Otherwise flat list.
6. **Style References** — only include if there's an obvious reuse value (multi-class wardrobe sheet, recurring vehicle three-view, recurring HUD detail). If nothing rises to that bar, omit the section entirely.
7. **Length budget:** the asset sheet is a working doc, not a novel. Each visual description ≈ 1–4 sentences. Cut purple prose. The user will read this 20+ times during a project.

---

## Anti-patterns

- ❌ Adding camera moves into asset descriptions ("the camera slowly orbits the character"). Camera goes into shotlist prompts (Phase 4), not the asset sheet.
- ❌ Adding scene-specific behavior ("standing nervously while waiting for the train"). Asset is reusable across scenes; behavior is per-shot.
- ❌ Inventing physical details the script doesn't imply. If the script says "old man," don't add "with a scar over his left eye." Ask the user.
- ❌ Mixing image-prefix block with the video `STYLE_BLOCK.md` block. They are two different prefixes for two different pipelines.
