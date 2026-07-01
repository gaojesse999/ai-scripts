# Asset Image-Generation STYLE PREFIX

This is the universal style prefix for **single-image** asset generation tools — Nano Banana, Soul, Midjourney, 即梦, Flux, etc.

It is intentionally **different** from `STYLE_BLOCK.md`. That one targets the Seedance 2.0 video pipeline (forbids 3D / game-engine looks, 60fps, multi-shot). This one targets static-image generators where the constraints are different (3D-rendered cinematic CG is acceptable, 24fps not relevant, multi-shot doesn't apply).

Drop the canonical block verbatim at the top of every asset sheet. Per-asset descriptions are written below it; when the user pastes any single asset entry into an image tool, they prepend this block.

---

## Canonical STYLE PREFIX (paste into every asset sheet)

```
**风格前缀 (STYLE PREFIX)**
*   风格 (Style)：8K IMAX。电影级写实CG —— 高精度3D渲染，写实皮肤与布料材质，写实配色，画面干净优雅。
*   质感 (Fidelity)：⚠️极高角色质感 —— 人物 / 动物 / 怪物 / 生物一律同一标准。真人（真实生物）级实拍质感，非动画/非插画/非二次元/非塑料CG感，呈现高预算电影的真实剧照效果。Arri Alexa 65 大画幅电影摄影机成像风格：真实镜头光学、自然镜头畸变、真实焦外虚化。8K 超高清微观细节，所有材质遵循物理基础渲染 (PBR) 与真实世界物理规律。（动画 / 风格化项目请改用下方「质感分级」的动画档 —— 保留画风，但仍需最高保真度。）
*   光照 (Lighting)：仅限自然光 —— 逆光/背光 (contre-jour)，摄像机位于阴影侧，画面中始终带有氛围感薄雾。主光源仅来自天空和窗户。无人工照明。HDR 高动态范围，完整保留高光与阴影细节，呈现电影胶片般的层次感。
*   色彩 (Color)：60:30:10 法则 —— 主色调 / 辅助色 / 点缀色。
*   镜头 (Camera)：物理电影镜头。180度快门运动模糊。浅景深，真实焦外虚化，背景带空气透视与电影级虚化。
*   皮肤/表皮 (Skin)：毛孔级真实感 + 物理准确的次表面散射 (SSS)，作用于**面部及一切裸露在外的肌肤**（颈部、锁骨、肩、手臂、手部、腿部、脚等）。人物 —— 面部与所有裸露皮肤均有绒毛、不对称的小痣、毛细血管轻微泛红、自然油脂高光反射，以及真实静脉/关节褶皱/指节与指甲细节，毛孔阴影与环境光照相匹配，⚠️禁麻子、禁痘坑、禁坑洼、禁凹凸不平、禁粗糙糙皮、禁过度纹理/过度锐化。动物/怪物/生物 —— 皮肤 / 鳞片 / 甲壳 / 兽皮 / 黏膜 / 角质等全身表皮同样物理准确：真实厚度、湿润度、皱褶、疤痕、SSS 透光与角质高光，符合该物种的生理结构。
*   毛发/羽/鬃 (Hair & Fur)：纤维级真实度，适用于头发、**眉毛、睫毛、胡须/胡子（男性）**、体毛、兽毛、鬃毛、羽毛、须。单根纤维清晰可见，真实毛鳞片/羽枝结构、自然粗细变化、随机方向分布与真实密度；纤维间存在自然间隙与透光，具真实反射/折射/吸收与高光变化；根部、尖端与不同区域层次分明，具自然蓬松度、柔韧性与重量感；受风力/重力/运动产生真实物理摆动。**面部细毛**：眉毛按自然生长方向排布、根根分明、疏密自然；睫毛（尤指女性）根根独立、自然弯曲卷翘、根部渐深；男性胡须/胡茬有真实软硬粗细、毛囊根部质感与自然生长范围。⚠️禁塑料感、禁 CG 假毛/假羽/假睫毛感、禁过度光滑、禁统一梳理排列、禁刷子状/成缕结块的睫毛。
*   材质 (Materials)：所有织物、装甲、外壳与表面遵循 PBR —— 真实纤维/材料纹理、自然褶皱、重力下垂、材质差异；真实粗糙度、反射率与光泽变化。
*   表演 (Acting)：好莱坞级别 —— 做出反应前的微小停顿，精准的视线，带有眼神光的灵动双眸，呼吸引起的胸部起伏。
*   物理 (Physics)：遵循重力和惯性 —— 物体有真实的重量感，正确的接触阴影。不要悬浮的道具。
*   背景 (Background)：⚠️**角色/生物资产 = 纯色背景** —— 单一纯色背景，无场景/道具/图案/纹理/渐变内容/环境等任何其他背景元素；主体面部完整不遮挡（除非角色设定本身要求，如始终戴面具/头盔）。**场景/环境资产不受此限**，按世界内真实环境正常呈现。
*   构图 (Composition)：三分法 + 黄金比例。人物比例真实准确、姿态自然，避免僵硬摆拍。每个人从第一帧开始就处于运动状态。
*   连贯性 (Continuity)：角色、道具、环境在每个切换镜头中保持完全一致。无身份/特征偏移 (No identity drift)。
*   技术 (Technical)：24fps 平滑运动。8K 细节，真实微观细节。画面无抖动。
```

---

## Project-specific aesthetic line

The canonical block is intentionally **aesthetic-neutral**. A project usually has a one-line aesthetic signature (e.g. *"徐克式武侠赛博美学"*, *"塔可夫斯基风格末日工业"*, *"宫崎骏湿漉漉的童话"*, *"Lubezki × Deakins现实主义"*). Append this line to the **风格 (Style)** bullet of the canonical block before delivering the sheet.

How to derive the aesthetic line:

1. Read the script's tone register (Phase 1).
2. Look for the user's references — past shotlists, mood boards, "make it feel like X" comments.
3. If genuinely unclear, ask **one binary question** with two strong options before writing the sheet — never ask "what aesthetic do you want?" (open-ended overload).

   ❌ "What aesthetic do you want for this project?"
   ✅ "Aesthetic — 徐克武侠赛博 (high-saturation neon + ink-wash silhouettes), or 末日工业写实 (rust + sand + practicals only)?"

Once locked, the aesthetic line is **frozen for the project** unless the user explicitly asks to change it. Same line appears at the top of every asset sheet for that project.

---

## Texture tiers 质感分级 (realistic vs. animation)

Character texture must always be **the maximum the aesthetic allows**. This applies to **every kind of character — humans, animals, monsters, and non-human creatures alike** (skin/scales/carapace/hide/mucous/keratin, fur/feathers/mane/whiskers). No creature type gets a lower texture bar. Pick one of two tiers based on the locked project aesthetic.

Two bullets differ between the tiers — **质感 (Fidelity)** and **皮肤 (Skin)**. Everything else in the prefix is identical. Swap both when you switch tiers.

### Tier A — Realistic 写实档 (default)

For any live-action / photoreal / cinematic-realism aesthetic (Lubezki × Deakins, 末日工业写实, documentary, etc.). The bar is **indistinguishable from real footage** — real-person skin (pores, SSS, oil sheen), fiber-level hair, PBR fabric, Arri Alexa 65 large-format optics, HDR. Use these two bullets verbatim (this is the canonical default):

```
*   质感 (Fidelity)：⚠️极高角色质感 —— 人物 / 动物 / 怪物 / 生物一律同一标准。真人（真实生物）级实拍质感，非动画/非插画/非二次元/非塑料CG感，呈现高预算电影的真实剧照效果。Arri Alexa 65 大画幅电影摄影机成像风格：真实镜头光学、自然镜头畸变、真实焦外虚化。8K 超高清微观细节，所有材质遵循物理基础渲染 (PBR) 与真实世界物理规律。
*   皮肤/表皮 (Skin)：毛孔级真实感 + 物理准确的次表面散射 (SSS)，作用于**面部及一切裸露在外的肌肤**（颈部、锁骨、肩、手臂、手部、腿部、脚等）。人物 —— 面部与所有裸露皮肤均有绒毛、不对称的小痣、毛细血管轻微泛红、自然油脂高光反射，以及真实静脉/关节褶皱/指节与指甲细节，毛孔阴影与环境光照相匹配，⚠️禁麻子、禁痘坑、禁坑洼、禁凹凸不平、禁粗糙糙皮、禁过度纹理/过度锐化。动物/怪物/生物 —— 皮肤 / 鳞片 / 甲壳 / 兽皮 / 黏膜 / 角质等全身表皮同样物理准确：真实厚度、湿润度、皱褶、疤痕、SSS 透光与角质高光，符合该物种的生理结构。
```

⚠️ 写实档**不加**「面部整体保持光滑干净、底子均匀健康」这类理想化磨皮 —— 真人皮肤要有真实毛孔/油脂/微瑕的自然变化。

### Tier B — Animation / stylized 动画·风格化档

For any 2D / anime / cel-shaded / painterly / stylized-3D aesthetic (宫崎骏, Arcane, 皮克斯, ink-wash, etc.). Keep the art style, but hold the fidelity bar at **top-tier animated-feature production quality** — never cheap, flat, or low-effort. Swap in these two bullets:

```
*   质感 (Fidelity)：⚠️高保真风格化（人物/动物/怪物/生物同一标准）—— 保留 <画风> 的动画/风格化外观，同时达到顶级动画长片（皮克斯 / 剧场版 / Arcane 级）的最高制作质感：纤维级毛发/羽毛丝理、PBR 一致的皮肤/鳞甲/材质与布料、干净通透的高分辨率细节、真实光影层次与景深虚化、有重量与手感的表面。⚠️禁廉价感、禁扁平塑料感、禁低模、禁锯齿毛边、禁劣质渲染、禁 AI 糊感。
*   皮肤/表皮 (Skin)：风格化肌肤，作用于**面部及一切裸露皮肤**（颈、锁骨、手臂、手、腿、脚等）—— 干净通透的 SSS 式光影过渡与柔和绒毛光泽，整体保持光滑干净、底子均匀健康，仅细腻毛孔质感（不追求真人级毛孔/油脂/微瑕）。动物/怪物/生物 —— 皮肤/鳞片/甲壳/兽皮等全身表皮同样干净高保真，符合该物种结构与画风。⚠️禁廉价扁平塑料感。
```

**皮肤差异一句话：** 写实档 = 真人级完整肤质（真实毛孔/油脂/微瑕，禁磨皮）；动画档 = 风格化干净肌肤（光滑均匀 + 细腻毛孔，带画风）。**毛发 / 材质** bullet 两档共用，Tier B 下按画风读作「风格化但高保真」。

**Rule of thumb:** realistic aesthetic → indistinguishable from a real person; animation aesthetic → unmistakably that art style, but at the fidelity of the best animated feature ever made in that style. Cheap/flat/plastic is never acceptable in either tier.

---

## How a single-asset prompt is composed

For any single asset entry in the asset sheet, the paste-ready image prompt is the concatenation of:

1. **STYLE PREFIX** (canonical block, with project aesthetic line appended)
2. **Asset description** (the bullet content from the sheet — character / location / prop)
3. **Output spec** — one closing line:

   ```
   输出：单张图，<比例>，<背景指令>。
   ```

   Defaults:
   - Character single-figure refs: `1:1`, 纯色背景（single solid color，无任何其他背景内容/道具/图案/纹理/环境元素）
   - Character three-view sheets: `16:9`, 纯色背景（single solid color，无其他内容）, 前/侧/背 三视图
   - Locations / establishing: `21:9`, in-world environment
   - Props on white: `1:1`, white seamless studio
   - Props in context: `1:1`, in-world surface

   ⚠️ **Character asset rules (always):**
   - **纯色背景 (pure solid-color background).** Every character/creature single-figure ref and three-view sheet must be generated on a single flat solid-color backdrop — no scenery, no props, no patterns, no gradients-as-content, no environment. State it in the output line, e.g. `输出：单张图，1:1，纯色背景，无其他背景内容。`
   - **Face unobstructed (面部不遮挡).** The character's face must be fully visible and unobstructed — no hands, hair, props, masks, shadows, or crop cutting across the face — **unless the character's canonical design explicitly requires it** (e.g., a masked villain, a helmet that never comes off, hair covering one eye by design). When occlusion is part of the design, keep it; otherwise the face reads clean and clear for downstream identity consistency.

The user copies the whole composed string (block + description + output line) into Nano Banana / Soul / etc.

---

## Forbidden in the prefix

Do **not** add to the prefix:
- Specific character names (those go in the per-asset description)
- Specific locations
- Specific props
- Camera moves (this is a still image)
- Per-scene mood (the asset is reusable across scenes)

The prefix is the **invariant**; everything project- and asset-specific lives in the description.

---

## When the user uploads a custom style override

If the user uploads a custom style sheet / reference HTML / past asset doc in Phase 1, treat its style prefix as the **override** for this project. Use it verbatim instead of the canonical block above. Keep the same composition rule (prefix + description + output line).
