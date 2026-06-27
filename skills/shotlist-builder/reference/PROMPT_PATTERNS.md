# Prompt Patterns

Every Chinese Seedance 2.0 prompt follows the same structural order. Hit every section in sequence; don't skip; don't reorder.

## Structural order

1. **Named asset reference declarations** — visual assets (`@韩立=韩立`, `@Jane=Jane`, ...) **and** sound assets (`@银月=银月`, `@开罐头声=开罐头声`, ...)
2. **Universal warnings** (`⚠️空间布局`, `⚠️对白规则`, `⚠️本视频严格只有N个镜头`)
3. **Per-shot blocks** (`【镜头1】` `【镜头2】` ...) OR a single-shot block
4. **Style block** (`风格：...`)
5. **Background activity & sound design** (`环境活动：...`, `声音设计：...`)
6. **Closing footer** (`15秒。21:9。`)

## Section 1 — Named asset reference declarations

Every prompt opens by declaring its named asset references — both **visual assets** (characters / locations / props / inserts / pose refs) and **sound assets** (voice timbre / SFX / ambient bed). Do not use numbered image aliases. The first line is a Chinese-comma-separated map from `@`-prefixed alias to the exact asset name, followed (when the prompt has audio assets) by a `声音资产` line in the same `@`-prefixed format:

```
资产引用：@Roko=Roko，@Old Apartment=Old Apartment，@PolaroidPhoto=PolaroidPhoto。
@Roko — 混血亚裔白，深色中长湿发贴额碎刘海，发梢滴水，淡小胡，鼻梁红创可贴微潮，左颊痣，黑紧身T恤肩部和上背湿透颜色加深贴身，军绿腰带，黑工装裤大腿和裤脚湿痕，黑靴湿润，红手套微潮，腰间战术包，右腰挂红色小泰迪熊挂件，左前臂纹身，面部薄水雾。
@Old Apartment — 三视图参考：上图=客厅全景向走廊方向...
@PolaroidPhoto — 一张拍立得横版照片11cm×8.5cm——自拍合照...
声音资产：@Roko声线=Roko声线，@城市夜环境声=城市夜环境声，@拍立得快门声=拍立得快门声。
@Roko声线 — 男声，低沉略沙哑，疲惫感，中速节奏，气声较多。
@城市夜环境声 — 远处城市低频嗡鸣+偶尔车流呼啸，持续低音床，无音乐。
@拍立得快门声 — 机械咔嚓声紧接卷出照片的滚轮摩擦声，干、近、清脆。
```

⚠️**Alias convention:** the `@`-prefix is used **only inside this declaration block** — both the visual `资产引用` lines and the `声音资产` lines (the `@name=name` map lines and the per-asset `@name — ...` description lines). **Everywhere else in the prompt** (机位 / 空间布局 / 动作 / 微表演 / 环境活动 / 对白 / warnings, etc.) reference the asset with **bracket form `[name]`**, e.g. `[Roko]`, `[Old Apartment]`, `[城市夜环境声]`.

Rules:
- Character references always describe height, build, hair, distinctive face marks, full wardrobe head-to-toe, props on the body
- For wet/dry/blood/dust state changes between scenes, **explicitly note the state** in the asset reference (`湿发贴额`, `溅血渍`, `面部薄水雾`)
- Location references describe the reference image layout in detail (multi-view → say which view is which: `上图=`, `下图=`, `中图=`)
- Prop references include exact dimensions when relevant (`11cm×8.5cm`), text on props verbatim, color/material specs
- **Sound assets** go on a separate `声音资产：` line in the same `@name=name` format. Use them for character voice timbre (`@Roko声线`), key diegetic SFX (`@开罐头声`, `@拍立得快门声`), and the ambient bed (`@城市夜环境声`). Describe each with character/texture/distance/pace; respect the style block — `禁音乐`, so never declare a music asset. Omit the `声音资产` line entirely for a silent prompt.
- Before writing the reference lines, run an **asset-reference audit**: required assets = the exact union of all visible characters, location/background references, key props, screens/documents/inserts, pose references, **and audible sound assets (voice / SFX / ambient)** used anywhere in this prompt.
- The reference lines must contain every required asset and no extra assets. Do not include offscreen-only speakers (unless their voice is heard), props not visible in the prompt, previous-scene locations, style references, inaudible sounds, or "just in case" assets.
- If a multi-shot prompt uses an asset in only one internal `【镜头N】` block, include it. If an asset is never visible or visually referenced in any internal block, remove it.
- If the exact asset set becomes too large or ambiguous, split the prompt rather than padding the reference list.
- For static-pose references (used for body posing only, not full image generation), use `@`-prefixed aliases with explicit warnings:
  ```
  @Roko Pose A=Roko pose reference A。
  @Roko Pose A — ❌NOT A VIDEO FRAME❌ 此图仅用于提取@Roko的身体姿势角度数据。⚠️@Roko Pose A是静态姿势参考——禁止将@Roko Pose A渲染/复制/再现为视频的任何一帧。
  ```

## Section 2 — Universal warnings (top of prompt)

Always declare the shot count and dialogue rules at the top, before the shot blocks:

```
⚠️空间布局 / 人物位置：[reference top-down schema, see SPATIAL_BLOCKING.md]
⚠️对白规则：一句台词=一个镜头——每个角色的台词严格只出现在该角色的特写镜头内。
⚠️本视频严格只有N个镜头——禁止添加额外镜头。
```

The shot-count warning prevents the model from adding spurious cuts.

## Section 3 — Per-shot blocks (multi-shot prompts)

When a prompt contains multiple internal cuts, each one is a `【镜头N】` block with its own internal structure:

```
【镜头1】
机位：35mm广角，全景wide shot。⚠️持续时间⚠️严格约0.3-0.5秒（split-second flash establishing shot）。
背景：[location detail].
动作：[step-by-step].
⚠️0.3-0.5秒后⚠️立刻硬切（hard cut）到镜头2——无过渡、无淡出、无停留。

【镜头2】（紧接镜头1硬切而来）
机位：⚠️85mm长焦，⚠️F1.4极浅景深，⚠️[Roko]侧面紧凑特写。
摄影机运动：[handheld / dolly / static + camera-emotion sync clause from CAMERA_EMOTION.md].
背景：[detail].
动作：[step-by-step].
⚠️⚠️⚠️微表演细节（actor performance micro-beats）：
- ① ...
- ② ...
- ③ ...
```

Each shot block always has:
- **机位** — lens + aperture + shot type (wide / mid / close / ECU) + handheld/static/dolly modifier
- **摄影机运动** (when relevant) — camera move synchronized to emotion
- **摄影机位置** (when relevant) — east/west/south/north of the character
- **背景** — what's in the background (or "blurred to soft color blocks" for tight close-ups)
- **动作** — step-by-step action with numbered beats (① ② ③ ...) when there's an arc
- **微表演细节** — performance micro-beats, see MICRO_BEATS.md

For a single-shot prompt (one continuous take, no internal cuts), skip the `【镜头N】` headers and write the same structure as a single block. Prepend with `单镜头（one-shot，无剪辑）。`

## Section 4 — Spatial blocking

For any prompt with 2+ characters in frame, declare the spatial relationship explicitly using the approved top-down schema (see [SPATIAL_BLOCKING.md](SPATIAL_BLOCKING.md)):

```
⚠️空间布局（MAIN VIEW=从天桥入口看向巨型屏幕）：
位置A：[Gandelfina]站在中央通道最前方靠近屏幕，面朝三人。
位置B：[Roko]和[Lulu]在通道中间并肩站立，距[Gandelfina]约3米，面朝[Gandelfina]方向。
[Rein]站在[Roko]和[Lulu]正后方1.5米处——不在他们旁边，严格在他们背后，被他们的身体部分遮挡——也面朝[Gandelfina]方向。
```

Use precise distances in meters. Use cardinal directions or "north/south/east/west" relative to the main view axis. Note who occludes whom, who faces which direction, and any heights/eyelines the model might get wrong.

## Section 5 — Camera/move direction

Every shot block declares lens + camera move + emotion sync. See [CAMERA_EMOTION.md](CAMERA_EMOTION.md) for the full mapping.

Always specify:
- Lens (in mm)
- Aperture if shallow DOF matters (`F1.4极浅景深`)
- Camera move (handheld呼吸 / dolly / crane / static / push-in / pull-out)
- For handheld, specify the breathing rhythm based on the focal character's emotion
- For multi-shot, name the cut type (`hard cut` / `dissolve`) and forbid the others

Forbidden moves are explicit:
- `禁zoom变焦` (no zoom — physical movement only)
- `禁稳定器` (no stabilizer — handheld means handheld)
- `禁焦点漂移` (no focus drift on locked inserts)

## Section 6 — Performance direction

This is the cinematographer's main creative output. Direct emotion as physical micro-events. See [MICRO_BEATS.md](MICRO_BEATS.md) for the full catalog by emotion.

Tactics:
- Eyeline shifts ("目光从[Gandelfina]方向微微移开向下")
- Breath ("胸腔深深起伏——一次漫长的吸气，然后缓慢呼出")
- Throat/jaw micro-tells ("一次喉结上下吞咽", "颧骨处咬肌慢慢收缩")
- Suppressed emotion as physical resistance ("他在试图忍住——每一块面部肌肉都在对抗涌上来的情绪")
- Eye state ("眼睛逐渐湿润，眼眶积聚泪水使眼球开始泛光")
- Posture/weight ("肩膀低沉下塌", "双臂无力挂在身侧")
- Staged emotional arcs with numbered beats (① ② ③ ④ ⑤ ⑥ ⑦) for complex reaction shots

Every dialogue line gets a pre-line beat, mid-line emphasis cues, and a post-line beat (see MICRO_BEATS.md §4).

## Section 7 — Dialogue rules

### Base rule
```
⚠️对白规则：一句台词=一个镜头——每个角色的台词严格只出现在该角色的特写镜头内。
```

### Interruption (one character cuts another off)
If character A interrupts character B mid-word:
```
⚠️例外（对白打断）：第N镜头中[A]说"[start of A's line]——[word at break]"⚠️被第N+1镜头中[B]的台词强行打断——硬切发生在[A]说"[word]"中间，[A]的声音被[B]的台词覆盖切断。⚠️这是有意的对白打断（interruption），制造紧张冲突感。
```

Then in shot N+1's description: `镜头第一帧时[B]通过鼻孔大幅度急吸气（sharp inhale）——抓取空气准备打断。`

### Line addressing
Every line must explicitly state **whom it's directed at**:
```
严格朝向 [character X] 说（视线、声音方向都明确指向 [X]，不是对其他人说的）。
```

### Lines from bokeh
If a character in bokeh speaks — sound is allowed, but the silhouette must match: head angled toward the speech direction, breath before words readable even through blur.

## Section 8 — Background activity & sound design

For any scene with extras or environmental movement, callout what's happening in the background. Forbid empty backgrounds:

```
环境活动（匹配[Underground Base Main Hall]）：⚠️背景必须充满大量活动的工作人员——禁止空旷背景。多名白衬衫分析员在工作站旁快速打字、站起交接文件、弯腰核对屏幕数据、两人并排讨论。多名白大褂科研人员透过显微镜观察古代文物。银色铰接机械臂全程持续运动。多人在通道和工作台之间来回走动。
```

For empty/quiet scenes (apartments, exteriors at night), still callout the *absence* — what isn't moving, what kind of silence:

```
完全寂静——禁背景音乐、禁画外人声。仅环境SFX：远处城市低频嗡鸣、暖气管道轻响、湿靴踩在拼花地板上的回响。
```

When the prompt declares sound assets in Section 1, **reference them here in bracket form** (`@` only in the declaration) and place each cue on its beat:

```
声音设计：[城市夜环境声]全程作为低音床。第N镜头[Roko]开口——[Roko声线]"line"。拍立得弹出瞬间触发[拍立得快门声]。⚠️禁音乐、禁字幕——仅画面内SFX与人声。
```

## Section 9 — Lighting overrides per shot

The default style block forbids fill light, but each scene may need additional lighting overrides specific to that location. See [STYLE_BLOCK.md](STYLE_BLOCK.md) for variants.

Be specific about:
- What lights are ON (windows, screens, practicals)
- What lights are OFF (with explicit `禁` for each forbidden source)
- Direction of key light
- Whether contre-jour or side-lit
- Spill rules ("禁止蓝色色溢打在人物皮肤上")

## Section 10 — Failure-mode warnings (`⚠️` markers)

Anticipate what Seedance will get wrong. Add ⚠️-marked rules to prevent it. Use single `⚠️` for important, triple `⚠️⚠️⚠️` for critical-critical.

What to mark with `⚠️`:
- Any distance ("距G约2米")
- Position of any object ("放在BL桌边正中央")
- Forbiddens ("禁止", "不允许")
- Key blocking (where each character stands)
- Eyeline lock ("目光始终锁定在 X 上")
- Timing of any line or action
- Any exception to a general rule

### Standard forbid block (drop into every prompt)
```
禁3D渲染。
禁游戏引擎、禁游戏CG过场质感。
禁正面光、禁侧面补光、禁反光板、禁柔光箱。
禁LED灯带、禁霓虹。
禁屏幕蓝光溢出。
禁可见光束（god rays）。
禁光学畸变、禁桶形畸变、禁鱼眼。
禁漂浮道具。
禁身份漂移。
禁抖动（除手持呼吸感外）。
禁音乐。禁字幕。
```

### Common failure modes to counter

- **Asset-reference contamination** — model uses one character's wardrobe on another or blends assets. Counter: re-state each character's exact wardrobe in the named asset reference.
- **Identity drift across cuts** — counter: `连续性：角色、道具、环境每个镜头完全一致。禁身份漂移。`
- **Pose-reference contamination** — counter: explicit `❌NOT A VIDEO FRAME❌` rules
- **Light spill on skin** — counter: `禁止蓝色色溢打在人物皮肤和服装上`
- **Wide-angle distortion** — counter: `禁光学畸变——禁桶形畸变、禁枕形畸变、禁鱼眼效果、禁广角变形`
- **Floating props** — counter: `禁漂浮道具`
- **God rays / volumetric beams** — counter: `禁止可见光束（god rays）`
- **Empty background** — counter: explicit background activity callouts (Section 8)
- **Hand chaos** — for shots with hand close-ups, specify finger count and exact action
- **Scale mismatch** — for shots with multiple characters, restate heights
- **Camera pass-through** — for handheld, note "禁稳定器" but also "画面带有机呼吸感微晃" so it doesn't go wild
- **Spurious cuts** — counter: `⚠️本视频严格只有N个镜头——禁止添加额外镜头`
- **Focus drift on inserts** — counter: `⚠️焦平面严格锁定在 [object]——绝对禁止焦点漂移、绝对禁止 rack focus、绝对禁止 autofocus 跳变`

### Rule-replacement hierarchy

If a new rule contradicts an earlier one — **the new rule replaces the old**. Don't silently delete the old one; write the replacement explicitly:
```
⚠️替换规则：原规则[X]替换为新规则[Y]——[reason if non-obvious]。
```

## Section 11 — Closing footer

Always end with:
```
15秒。21:9。
```

For multi-shot prompts (one prompt with internal `【镜头1】【镜头2】【镜头3】` cuts), still 15 seconds total — divide internally.

## Length

Don't be precious about prompt length. Prompts in production range from ~150 Chinese characters (simple inserts) to ~2000+ characters (complex reaction shots with 7-step emotional arcs). The complex reaction shots ARE that long because they need to be — micromanaging the performance is what makes them work. Don't truncate to be neat.

## Tone

You are a cinematographer who has worked with Lubezki and Deakins. You think in shadows, lenses, and controlled physical reality. You direct actors with the precision of a stage director and write camera direction with the muscularity of someone who has actually held a steadicam. Don't write generic AI-video prose ("a beautiful shot of..."). Write blocking notes ("Roko 2m from the fridge, back to camera, weight on left foot, right hand still holding the polaroid at thigh height").
