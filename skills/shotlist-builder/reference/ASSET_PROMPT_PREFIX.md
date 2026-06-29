# Asset Image-Generation STYLE PREFIX

This is the universal style prefix for **single-image** asset generation tools — Nano Banana, Soul, Midjourney, 即梦, Flux, etc.

It is intentionally **different** from `STYLE_BLOCK.md`. That one targets the Seedance 2.0 video pipeline (forbids 3D / game-engine looks, 60fps, multi-shot). This one targets static-image generators where the constraints are different (3D-rendered cinematic CG is acceptable, 24fps not relevant, multi-shot doesn't apply).

Drop the canonical block verbatim at the top of every asset sheet. Per-asset descriptions are written below it; when the user pastes any single asset entry into an image tool, they prepend this block.

---

## Canonical STYLE PREFIX (paste into every asset sheet)

```
**风格前缀 (STYLE PREFIX)**
*   风格 (Style)：8K IMAX。电影级写实CG —— 高精度3D渲染，写实皮肤与布料材质，写实配色，画面干净优雅。
*   光照 (Lighting)：仅限自然光 —— 逆光/背光 (contre-jour)，摄像机位于阴影侧，画面中始终带有氛围感薄雾。主光源仅来自天空和窗户。无人工照明。
*   色彩 (Color)：60:30:10 法则 —— 主色调 / 辅助色 / 点缀色。
*   镜头 (Camera)：物理电影镜头。180度快门运动模糊。
*   皮肤 (Skin)：毛孔级真实感 —— 面部绒毛，不对称的痣，毛细血管泛红，毛孔阴影与环境光照相匹配；但面部整体保持光滑干净、底子均匀健康，仅细腻毛孔质感，⚠️禁麻子、禁痘坑、禁坑洼、禁凹凸不平、禁粗糙糙皮、禁过度纹理/过度锐化。
*   表演 (Acting)：好莱坞级别 —— 做出反应前的微小停顿，精准的视线，带有眼神光的灵动双眸，呼吸引起的胸部起伏。
*   物理 (Physics)：遵循重力和惯性 —— 物体有真实的重量感，正确的接触阴影。不要悬浮的道具。
*   构图 (Composition)：三分法 + 黄金比例。每个人从第一帧开始就处于运动状态。
*   连贯性 (Continuity)：角色、道具、环境在每个切换镜头中保持完全一致。无身份/特征偏移 (No identity drift)。
*   技术 (Technical)：24fps 平滑运动。8K 细节。画面无抖动。
*   音频 (Audio)：仅有环境音效 (SFX)。无音乐。无字幕。
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

## How a single-asset prompt is composed

For any single asset entry in the asset sheet, the paste-ready image prompt is the concatenation of:

1. **STYLE PREFIX** (canonical block, with project aesthetic line appended)
2. **Asset description** (the bullet content from the sheet — character / location / prop)
3. **Output spec** — one closing line:

   ```
   输出：单张图，<比例>，<背景指令>。
   ```

   Defaults:
   - Character single-figure refs: `1:1`, neutral seamless backdrop
   - Character three-view sheets: `16:9`, neutral seamless backdrop, 前/侧/背 三视图
   - Locations / establishing: `21:9`, in-world environment
   - Props on white: `1:1`, white seamless studio
   - Props in context: `1:1`, in-world surface

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
