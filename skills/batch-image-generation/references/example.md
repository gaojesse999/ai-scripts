# Example Prompt File

This example shows the supported section, variant, prompt label, and incremental variant format.

```text
**风格前缀 (STYLE PREFIX)**

*   风格 (Style) ：8K IMAX。电影级写实CG —— 高精度3D渲染
*   光照 (Lighting)：仅限自然光 —— 逆光/背光 (contre-jour)，摄像机位于阴影侧，画面中始终带有氛围感薄雾。主光源仅来自天空和窗户。无人工照明（注：原图拼写为lightning，结合语境应为lighting照明）。
*   色彩 (Color)： 60:30:10 法则 —— 主色调 / 辅助色 / 点缀色。
*   镜头 (Camera)：物理电影镜头。180度快门运动模糊。
*   皮肤 (Skin)：毛孔级真实感 —— 面部绒毛，不对称的痣，毛细血管泛红，毛孔阴影与环境光照相匹配。
*   表演 (Acting)：好莱坞级别 —— 做出反应前的微小停顿，精准的视线，带有眼神光的灵动双眸，呼吸引起的胸部起伏。
*   物理 (Physics)： 遵循重力和惯性 —— 物体有真实的重量感，正确的接触阴影。不要悬浮的道具。
*   构图 (Composition)：三分法 + 黄金比例。每个人从第一帧开始就处于运动状态。
*   连贯性 (Continuity)：角色、道具、环境在每个切换镜头中保持完全一致。无身份/特征偏移 (No identity drift)。
*   技术 (Technical)： 24fps 平滑运动。8K 细节。画面无抖动。
*   音频 (Audio)： 仅有环境音效 (SFX)。无音乐。无字幕。


1.6 苗铁山 MIAO TIESHAN — 秃鹰帮大当家
 
状态：待生成
优先级：★★★★☆
关键设定：重型机甲义肢（右臂，展开比躯干还粗），墨绿军大衣，两道旧伤疤
 
变体 A — 机甲义肢展开（场景7进门）
【角色 · 场景7】
英文提示词（Midjourney）：
A powerfully built Western man in his mid-forties, standing in the entrance of a
dim desert inn. Short-cropped hair, two old battle scars on the face — one across the
left cheekbone, one through the right brow. Wearing a faded military-green heavy cotton
greatcoat, collar up.
Right arm: a massive heavy-duty mech combat prosthetic — fully deployed, hydraulic
arm twice the diameter of his torso, exposed piston cylinders, armored plating,
the thing takes up as much space as a small engine block. Left arm is human.
Expression: completely calm, patient. He is not threatening you. He is informing you.
Warm amber practical light catching one side of his face, deep shadow the other.
35mm, F4, full body, low camera angle looking up to emphasize the arm's scale.
No neon. --ar 2:3 --style raw --v 6
 
中文提示词（Flux）：
欧美男性，四十五岁，壮实，站在昏暗荒漠客栈入口。短发，脸上两道旧战斗伤疤——
一道穿过左颧骨，一道穿过右眉。穿褪色墨绿色厚棉军大衣，领子立起。
右臂：重型机甲战斗义肢，完全展开状态，液压臂粗度是他躯干的两倍，
裸露活塞筒，装甲覆盖，整体体积像一块小型发动机。左臂是人类原装。
表情：完全平静，耐心。他不是在威胁你，他在告知你。
暖琥珀实用光打在脸部一侧，另一侧深阴影。35mm，F4，全身，低机位仰拍强调义肢体积。
禁霓虹。2:3竖幅。
 
变体 B — 机甲义肢锁死（场景9混战后）
【角色 · 场景9】
 
英文提示词-变体（Midjourney）：
right mech arm locked in half-deployed position — hydraulics seized from electromagnetic
pulse, arm frozen at an awkward mid-extension angle, he is pressing the unlock button
on the arm's side panel with his left hand, jaw tight, looking down at his own arm,
the only moment of frustration he will show

1.8 执法机甲兵 × 4 — 战略司

状态：待生成
优先级：★★★☆☆
关键设定：制式装甲，统一配置，深灰色，鹰纹

变体 A — 门口展开队形
【角色 · 场景8】

英文提示词（Midjourney）：
Four enforcement mech-soldiers in formation outside a desert inn at night, standardized
deep charcoal-grey powered armor — full body coverage, integrated helmet with visor,
eagle-crest insignia on left shoulder plate, uniform and identical. No color markings.
Two flanking the door, two visible at the sides, professional tactical spacing.
Practical amber light from the inn doorway catching their front plates, night desert
behind them, dust in the air. 35mm, F5.6, wide establishing shot. No neon.
--ar 16:9 --style raw --v 6

中文提示词（Flux）：
四名执法机甲兵在荒漠客栈门外夜间展开队形，制式深炭灰色动力装甲——全身覆盖，
整合头盔带面罩，左肩甲鹰纹徽章，统一，完全一致，无色彩标记。
两人侧翼门口，两人在外侧可见，专业战术间距。
客栈门廊实用琥珀光打在他们正面装甲上，身后是夜晚荒漠，空气中有沙尘。
35mm，F5.6，宽幅建立镜头。禁霓虹。16:9画幅。
```
