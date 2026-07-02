# Asset Image-Generation STYLE PREFIX

Universal style prefix for **single-image** asset generation — Nano Banana, Soul, Midjourney, 即梦, Flux, etc.

It is intentionally **different** from `STYLE_BLOCK.md` (that one drives the Seedance 2.0 *video* pipeline: multi-shot, 24fps, camera moves). This file drives *static image* generators, where the goal is a single frame that is **indistinguishable from a real photograph** (realistic tier) or a **top-tier animated-feature frame** (animation tier).

---

## 0. Core principles (read first)

The old prefix was one giant monolith pasted onto every asset. It caused two failures we are fixing here:

1. **AI look.** Tokens like `CG`、`3D渲染`、`数字角色重建`、`8K`、`超高清微观细节` and video tokens (`24fps`、`180度快门`、`运动模糊`) push image models *toward* the crunchy, over-sharpened, plastic "AI render" look — the opposite of a photograph. A real photo has lens softness and grain, not uniform micro-detail everywhere.
2. **Prompt too long.** Image models allocate attention across the whole prompt. A 2000-character prefix dilutes every instruction into "AI soup" (averaged, generic). Effective image prompts are **short, ordered, camera-first**.

**The six rules that make an image read as a real photo (not AI):**

- **取景就是真实感（对人物最关键，是头号变量）。** 近景 / 中近景 / **胸上 · 头肩**肖像 + 四分之三侧身角度 + 抓拍视线，让脸在画面里**足够大**，真实肤质（毛孔、油光、年龄感、不对称）才落得下（半身及更远对年轻脸会被磨平）。**全身正面「立正站姿·直视镜头」会把脸压到几十像素**，模型只能回退到「AI 默认美颜脸」——这是全身立绘看起来最假的根因。要看全身服装 / 身形，就**单独出一张三视图 / 全身图作为 costume-lock**，别指望同一张既真实又交代全身。⚠️主参考里**让手放松、别抬到脸前正中**——抬手 / 看表 / 复杂手势最易出 AI 橡皮手，手部戏留给视频。
- **对抗模型的「美颜默认脸」（年轻 / 漂亮角色尤其关键，是脸显 AI 的头号原因）。** GPT-image / DALL·E 类对年轻脸有强烈「网红美颜」偏置——光滑无瑕、五官完美对称、眼睛放大、精致全妆。**只写「毛孔 / 禁磨皮」压不住它**，必须用**正向、去美化**的措辞：`真实素人 / 路人纪实抓拍 / 普通真实长相 / 五官有个性不完美 / 非网红脸 / 非完美对称 / 素颜或极淡妆`，并写出具体真实瑕疵（可见毛孔、肤色不均、眼睛大小自然不放大）。⚠️**去美化 ≠ 干瘪**：皮肤仍要**水润健康、有油脂光泽与次表面湿润感**，别矫枉过正成干哑脱水 / 砂纸 /「一层干皮」的过度纹理（这是往回滑向 AI 的另一头）。**同时脸要够大**——半身构图对年轻脸仍会被磨平；锁肤质 / 身份用**胸上 / 头肩的更紧构图**。
- **Say it IS a photograph.** Lead with `真实照片 / 实拍剧照 / 抓拍`, and explicitly negate `CG / 3D渲染 / 插画 / AI绘画`. Never describe the pipeline as "CG" or "render" in a realistic asset.
- **Camera language, not resolution hype.** Real cameras + real lenses + real light. Drop `8K / 超高清 / 微观细节 / 4K / 高清`（这些是过干净数字感的触发词）；keep `照片 + 镜头自然柔化 + 轻微胶片颗粒`. Over-detail is an AI tell. ⚠️提醒用户**不要在提示前面手动加「生成 4K 高清图 / 超清」**——它会抵消写实词。
- **Calibrated imperfection.** The realistic reference photos read real because of *moderate* pore/oil/asymmetry and real age — not waxy-smooth (too AI) and not moon-crater rough (too AI). Aim for the middle.
- **Negatives are tool-dependent, and must never name a renderable *look*.** 有负面框的工具（Midjourney / SD / 即梦）→ 负面词放负面框，一行、简短。**无负面框、弱解析否定的工具（GPT-image / DALL·E / 多数文生图）→ 整行负面都不要粘**——它会被当正向，你写什么它画什么。⚠️**尤其：任何"皮肤 / 外观质感名词"（塑料皮肤、蜡像、磨皮、干皮、砂纸皮肤、过度皮肤纹理、网红脸、精致全妆…）绝不能进负面行**——泄漏成正向时正好召唤出该效果（本项目的"皮肤变干"回归就是负面行加了 `干皮/砂纸/过度皮肤纹理` 被 GPT 当正向所致）。皮肤 / 长相**只在正文用正向措辞控制**（水润有纹理、素人非网红脸）；负面行只保留结构类（多余手指、肢体畸形）与纯管线类（CG、插画），且仅给负面框工具。

**Split by subject type.** A location does not need pores/SSS/eyelashes; a prop does not need skin/hair/eyes. Applying the character skin block to a scene is pure waste and bleeds skin-texture artifacts onto walls and water. Use the **subject-scoped** prefix below — 人物 / 场景 / 道具 — never the character block on everything.

---

## 1. Choosing the prefix (2 axes)

Pick by **subject type** × **tier**:

| Subject | Realistic tier (default) | Animation tier |
|---|---|---|
| 人物 Character | §2A | §2B |
| 场景 Location | §3A | §3B |
| 道具 Prop | §4A | §4B |

- **Tier is locked once per project** from the project aesthetic (see §6). Live-action / photoreal / cinematic-realism → **Realistic**. 2D / anime / cel-shaded / painterly / stylized-3D (宫崎骏, Arcane, 皮克斯, ink-wash) → **Animation**.
- **Realistic bar:** indistinguishable from real footage.
- **Animation bar:** unmistakably the art style, but at the fidelity of the best animated feature ever made in that style — realistic materials & light logic, near-photoreal texture. Cheap / flat / plastic is never acceptable in either tier.

---

## 2. 人物 Character

### 2A — Realistic 写实人物 (default)

```
**风格前缀 · 写实人物**
真实电影剧照 / 纪实抓拍人像，像真实相机拍下的**普通真人**——真实素人长相、五官有个性不完美、**非网红脸 / 非完美对称 / 非美颜**；不是CG、不是3D渲染、不是插画、不是AI绘画。<项目美学一句话>
· 相机：全画幅电影相机 + 85mm 人像镜头，浅景深、自然焦外虚化、真实镜头光学与轻微暗角，画面带**轻微但可见的真实胶片颗粒与微反差**（避免被抹成零颗粒的数字平滑感）；真实照片、保留镜头自然柔化，不要数字过锐、不要处处均匀的微观锐度。
· 光线：自然光 / 窗光 / 场景内实用灯光（台灯 / 路灯 / 窗内灯 / 屏幕 / 烛光等画面内可见的动机光源），**明确的单向主光 + 相机在阴影侧、低补光**（宁可欠曝也别平光），逆光或侧逆光，脸上有清晰的亮面 / 暗面分界与立体感；柔和真实的明暗过渡与氛围薄雾，HDR 高光暗部都有层次。
· 皮肤：真实演员肤质、**素颜或极淡妆（不要精致全妆）**——**皮肤水润健康、有自然油脂光泽与次表面透光的湿润感（真实但有生命力，不是干哑脱水）**；自然毛孔、细纹、绒毛、T区油光、微量雀斑或痣（面部≤3颗）、毛细血管血色、轻微肤色不均与真实年龄感，物理准确 SSS 的半透明感，左右脸自然不对称。⚠️**质感要平衡**：既不要蜡像般光滑 / 磨皮，也不要坑洼粗糙、干燥起皮、砂纸感或「脸上蒙一层干皮」的过度纹理。
· 眼睛：湿润泪膜、清晰角膜反射(catchlight)、虹膜纹理、自然巩膜（细微血丝）；**眼睛大小与间距自然、非美颜放大**。
· 毛发：发丝根根分明、有碎发飞散与自然毛躁；睫毛根根独立（浓密卷翘长睫默认仅女性），胡须/胡茬默认仅男性。
· 服装：真实织物纤维、缝线、重力褶皱与自然贴合、轻微穿旧痕迹，不要展示级完美无瑕。
· 背景：简洁的情境化真实环境（符合角色所处世界），浅景深虚化、不喧宾夺主；面部完整不遮挡。
· 取景与姿势（写实最关键）：**锁脸 / 锁质感的主参考默认取胸上 / 头肩的中近景**（脸要大到能看清毛孔——半身对年轻脸仍会被磨平）、**四分之三侧身**、视线自然（可不直视镜头）、重心偏移的**抓拍瞬间**（走动 / 回头 / 整理头发 / 侧望等），真人比例、放松不摆拍。⚠️避免全身正面「立正站姿·直视镜头」的证件照 / 三视图姿势——脸会太小、必然出 AI 娃娃脸；要看全身服装用单独的三视图资产。⚠️**手部放松下垂 / 扶包带 / 插兜 / 部分出画**，不要把手抬到脸前正中或做复杂手势（抬手 / 看表 / 比划最易出 AI 橡皮手，且抢脸）——手部动作留给分镜视频，主参考只负责锁脸 / 锁质感 / 锁服装。
```

### 2B — Animation 动画人物（高质感·接近写实）

```
**风格前缀 · 动画人物（高质感·接近写实）**
<画风> 的顶级动画长片质感（皮克斯 / 剧场版 / Arcane 级），材质与光影接近写实，画面干净通透、有电影感。<项目美学一句话>
· 相机：电影感构图，浅景深与焦外虚化，柔和真实的镜头光学。
· 光线：与写实同一套逻辑的自然光 / 逆光 / 场景内实用灯光，柔和真实明暗过渡与氛围感，HDR 层次。
· 皮肤：风格化但高保真——干净通透的 SSS 式光影与柔和绒毛光泽，底子均匀健康、仅细腻毛孔质感（不追真人级油脂 / 瑕疵），保留画风。
· 眼睛：按画风风格化，但通透湿润、有清晰眼神光。
· 毛发：纤维级丝理、成束但根根有层次、有碎发飞散（浓密长睫默认女性、胡须默认男性）。
· 服装：PBR 材质、真实褶皱与重力垂坠、有手感和重量，不要扁平塑料贴图。
· 背景：情境化环境，浅景深、不喧宾夺主；面部完整不遮挡。
· 取景与姿势：默认中近景 / 胸上、四分之三侧身、自然视线的抓拍感，比例与姿态自然；手放松、别抬到脸前做复杂手势；避免全身正面立正摆拍（要看全身用单独三视图）。
```

**Character negative line** — ⚠️**仅用于有负面框的工具（Midjourney / SD / 即梦），放进负面框。GPT-image / DALL·E / 文生图无负面框 → 整行都不要粘**（会被当正向，见 §0 第 5 条）。⚠️已**移除所有"皮肤 / 长相外观名词"**（塑料皮肤 / 蜡像 / 磨皮 / 干皮 / 砂纸 / 网红脸 / 精致全妆等）——这些只在正文正向控制，绝不进负面行。负面行只留**结构类 + 管线类**：

- 写实档：`CG, 3D渲染, 插画, 二次元, 多余手指, 缺指, 肢体畸形, 五官扭曲, 纯色影棚背景, 正面立正证件照姿势`
- 动画档：`廉价扁平, 低模, 锯齿毛边, 劣质渲染, 多余手指, 肢体畸形, 五官扭曲`

---

## 3. 场景 Location / Environment

Scenes carry **no** skin/eye/hair/eyelash/beard clauses — those are the #1 source of bloat and artifacting on environments.

### 3A — Realistic 写实场景 (default)

```
**风格前缀 · 写实场景**
真实电影剧照 / 实拍环境照片，像真实相机拍下的真实地点，不是CG、不是3D渲染、不是插画。<项目美学一句话>
· 相机：全画幅电影相机，establishing 用广角至标准镜头（24–35mm），真实景深与空气透视，轻微胶片颗粒；真实照片、保留镜头自然柔化，不要过锐。
· 光线：自然光 / 场景内实用灯光（路灯 / 窗内灯 / 招牌灯 / 屏幕等）为主，明确光向（晨昏侧逆光最佳），柔和真实明暗过渡、氛围薄雾、HDR 层次。
· 材质：地面 / 墙面 / 植被 / 水面等按 PBR 真实呈现——真实粗糙度、反射、磨损、脏污与使用痕迹，避免过于干净完美。
· 色彩：60:30:10 主色 / 辅色 / 点缀色，克制、不过饱和。
· 氛围：真实的居住 / 使用痕迹与环境细节，避免空旷无生气的CG场景。
```

### 3B — Animation 动画场景

```
**风格前缀 · 动画场景（高质感·接近写实）**
<画风> 顶级动画长片的美术场景，材质与光影接近写实、有电影感、干净通透。<项目美学一句话>
· 相机：电影感构图，广角至标准视野，真实景深与空气透视。
· 光线：自然光 / 场景内实用灯光为主，明确光向，柔和明暗过渡与氛围感，HDR 层次。
· 材质：PBR 一致的高保真材质与真实使用痕迹，保留画风，不要扁平塑料贴图。
· 色彩：60:30:10，克制不过饱和。
· 氛围：有生活感与环境细节，不要空旷廉价。
```

**Location negative line:** `CG, 3D渲染, 游戏场景, 插画, 过饱和, 过度锐化, HDR脏, AI感`（动画档改为 `廉价扁平, 低模, 劣质渲染, AI糊感`）。

---

## 4. 道具 Prop

Props carry **no** skin/eye/hair clauses. Short.

### 4A — Realistic 写实道具 (default)

```
**风格前缀 · 写实道具**
真实产品 / 静物照片，像相机实拍的真实物件，不是CG渲染、不是插画。<项目美学一句话>
· 相机：微距至标准镜头，浅景深聚焦主体，真实镜头光学，轻微颗粒。
· 光线：柔和自然光 / 实用光源，真实高光与接触阴影，物体有真实重量与落地感、不悬浮。
· 材质：PBR 真实材料——真实纹理、缝线、磨损、划痕、指纹 / 灰尘等使用痕迹，不要展示级完美无瑕。
· 背景：置于世界内真实表面 / 情境（默认），不强制纯白影棚。
```

### 4B — Animation 动画道具

```
**风格前缀 · 动画道具（高质感）**
<画风> 动画静物，高保真 PBR 材质与真实光影逻辑，保留画风、不要扁平塑料贴图。相机浅景深、柔和光线、真实接触阴影与重量感；置于世界内真实表面 / 情境。<项目美学一句话>
```

**Prop negative line:** `CG塑料感, 悬浮无阴影, 展示级完美无瑕, 过度锐化, AI感`。

---

## 5. How a single-asset prompt is composed

```
[subject-scoped prefix §2/§3/§4, correct tier]
+ [asset description from the sheet]
+ 输出：单张图，<比例>，<背景>。
```

Output-line defaults:

- **人物 · 主参考（realism hero shot，写实档默认先出这张）**：`4:5` 或 `2:3` 竖幅，**胸上 / 头肩的中近景、四分之三侧身、抓拍视线**——脸在画面里占比要大（半身对年轻脸仍会被磨平），才承载得住真实肤质。自然情境背景。例：`输出：单张图，4:5，胸上中近景、四分之三侧身抓拍，自然情境背景。`
- **人物 · 全身 / 三视图（costume-lock，可选、次要）**：`16:9` 或竖幅全身，前 / 侧 / 背或自然全身站姿，**仅用于锁定服装 / 身形 / 配色**。⚠️此图脸会小、偏摆拍，**不作为面部真实度依据**；面部真实度看「主参考」那张。
- **人物 · 面部特写（realism close-up，可选加强）**：比主参考**更紧的脸部主导特写**（脸占画面 30%+），`4:5` 或 `1:1`，四分之三侧脸、自然视线，手不入画。仅在主参考皮肤仍偏光滑 / 需要额外锁肤质与身份时才追加；年轻漂亮脸最容易需要这张。
- 场景 establishing：`21:9`，世界内环境；室内 `16:9`
- 道具：`1:1`，世界内真实表面 / 情境

⚠️ **Character asset rules (always):**

- **取景优先出「主参考」肖像。** 写实档角色**先出一张胸上 / 头肩中近景、四分之三、抓拍**的主参考锁脸锁质感；全身 / 三视图作为可选的第二张只锁服装。不要用「全身正面立正」当唯一角色资产——那是全身立绘看着假的根因。
- **自然情境背景 (natural contextual background).** Character / creature refs are generated on a natural, simple, in-world background rendered with real-photo quality — **no forced pure / white / solid-color backdrop** (pure backdrops read as CG turnaround sheets, which is an AI tell). Keep it simple so it never competes with the subject.
- **Face unobstructed (面部不遮挡).** Face fully visible — no hands, hair, props, masks, shadows, or crop cutting across it — **unless the character's canonical design requires it** (masked villain, permanent helmet, hair over one eye by design).

The user copies the whole composed string into the image tool. **Model-specific:** 有负面框的工具（Midjourney / SD / 即梦）→ 把该分区的**负面行**放进负面框；**GPT-image / DALL·E / 文生图无负面框**→ **整行负面都不要粘**（会被当正向，你写"干皮/塑料皮肤"它就画什么），靠正文的正向写实措辞即可，也不要在开头手写「4K / 高清」。⚠️皮肤 / 长相类外观词永远只在正文正向写，绝不进负面。

---

## 6. Project-specific aesthetic line

The prefixes are aesthetic-**neutral**. A project has a one-line aesthetic signature (e.g. *"徐克式武侠赛博美学"*, *"塔可夫斯基末日工业"*, *"宫崎骏湿漉漉的童话"*, *"Lubezki × Deakins现实主义"*). Append it where each block shows `<项目美学一句话>`.

Derive it: (1) read the script's tone; (2) look at the user's references / "make it feel like X" comments; (3) if genuinely unclear, ask **one binary question** with two strong options — never open-ended.

❌ "What aesthetic do you want?"
✅ "Aesthetic — 徐克武侠赛博（霓虹高饱和 + 水墨剪影），还是末日工业写实（锈蚀 + 风沙 + 仅实用光）？"

Once locked, the aesthetic line **and the tier (realistic / animation)** are frozen for the project unless the user asks to change them.

---

## 7. Forbidden in the prefix

Do **not** put in the prefix (these are per-asset or per-shot, not invariant):

- Specific character names / locations / props (→ per-asset description)
- Camera moves, motion, `运动模糊`, fps, shutter angle, `呼吸起伏` (→ these are **video** directives; they smear a still reference and are pure waste here)
- 影视补光 / 柔光箱 / 反光板 / LED 影视灯 / 霓虹灯带 (→ 破坏阴影侧的自然光逻辑，显平、偏 AI；`灯光` 只用**画面内可见的实用 / 动机光源**：台灯 / 路灯 / 窗光 / 屏幕 / 烛光 / 车灯等)
- `8K / 超高清 / 微观细节` over-detail hype (→ AI tell; use "high-res photo + lens softness + slight grain")
- Per-scene mood (asset is reused across scenes)
- Long inline `禁…禁…` negative chains (→ use the one compact negative line per subject type)

The prefix is the **invariant**; everything project- and asset-specific lives in the description.

---

## 8. Custom style override

If the user uploads a custom style sheet / reference HTML / past asset doc in Phase 1, treat its prefix as the override for the project. Use it verbatim, but still: (a) split it by subject type if it is a monolith, (b) keep the composition rule (prefix + description + output line), and (c) keep negatives in the negative field.
