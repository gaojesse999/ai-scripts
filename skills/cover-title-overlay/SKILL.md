---
name: cover-title-overlay
description: 在无文字封面底图上叠加两行居中中文标题，生成视频封面图，背景像素保持完全不变。字体、字号、颜色、描边、行距全部锁定，多次生成结果一致。当用户要求做封面、生成封面图、加封面标题、换封面文字、出某一集的封面，或提到「封面标题」「封面加字」「封面模板」「cover」时使用。也适用于为系列视频的各集生成风格统一的封面。
---

# 封面标题叠加

## 核心前提：不要用生图模型

生图/以图生图模型无法在原图上加字，它只能整张重画。底图送进去之后，分辨率、景别、光影、雾气浓淡每次都会漂，提示词写得再细也约束不住。

**必须用本 skill 的脚本做像素叠加。** 脚本只合成一个文字图层，底图其余像素原样保留，并在每次运行后校验这一点。

## 快速开始

只有两行标题是必填的。在本项目里底图和输出名都能省：

```bash
python .cursor/skills/cover-title-overlay/scripts/make_cover.py "自动习惯设计" "系统｜01"
```

省略时的默认行为：

- `--base` 省略 → 依次找当前目录下的 `cover/封面.png`、`封面.png`
- `-o` 省略 → 写到当前目录的 `image-outputs-YYMMDD-HHMMSS.png`，例如 `image-outputs-260819-135556.png`

需要固定文件名时再显式给：

```bash
python .cursor/skills/cover-title-overlay/scripts/make_cover.py "自动习惯设计" "系统｜01" \
  --base "cover/封面.png" -o "image-outputs-20260819/ep1.png"
```

用在别的项目时给绝对路径调用脚本，并显式传 `--base`：

```bash
python /abs/path/to/.cursor/skills/cover-title-overlay/scripts/make_cover.py "其他项目" "封面｜A" \
  --base "assets/mybase.png" -o "out/cover.png"
```

底图不限尺寸和比例。所有排版量都按底图高度的百分比计算，换一张 1536x1024 或竖版底图同样成立。

输出：

```text
base: cover/封面.png
output: image-outputs-260819-135556.png
size: 1672x941 (与底图一致)
title_box: x408-1270 y316-641
background: 标题区域以外 0 像素改动
font: NotoSerifSC-VF.ttf @ 142.5px
ink_h_ratio: 0.1413 (目标 0.1416)
```

看到 `background: 标题区域以外 0 像素改动` 才算成功。脚本会自己校验，出问题直接非零退出并说明原因，不会静默产出错图。

标题太长时：超出画面宽度直接报错，占到 92% 以上会打印提醒但仍然出图。两种情况都应该改短标题，不要去缩字号。

## 锁定的排版参数

这些数值是从一张模型生成的参考封面上实测反推的，已经写死在脚本里。**不要为了迁就某个标题去改它们**，否则各集封面就不一致了。

| 项目 | 值 |
|---|---|
| 字体 | Noto Serif SC（宋体/明朝体），字重 700 |
| 单行汉字字高 | 画面高度的 14.16% |
| 两行加行距总高 | 画面高度的 31.8% |
| 填充色 | `#E0CBA8` |
| 描边 | `#3A281F`，约 1.5px |
| 阴影 | 偏下、低透明度、柔和，不发光 |
| 对齐 | 整体居中；两行左右边缘对齐成矩形 |

两行用同一个字号。字数少的那行会**拉开字距**去对齐另一行的宽度，而不是把字放大。所以「系统｜01」看起来比「自动习惯设计」松，是设计如此。

## 一次做多集

分别调用即可，底图和参数相同，各集封面自然统一。多集建议显式给 `-o`，否则默认名只带时间戳，分不清哪集：

```bash
python .cursor/skills/cover-title-overlay/scripts/make_cover.py "自动习惯设计" "系统｜01" -o "out/ep1.png"
python .cursor/skills/cover-title-overlay/scripts/make_cover.py "落地用 Skill" "系统｜02" -o "out/ep2.png"
```

## 依赖与资源

只需要 `Pillow`。缺失时装它：

```bash
python -m pip install pillow
```

如果所在环境需要走代理，代理地址在项目根目录 `.skill.env` 的 `SKILL_PROXY`（不要打印它的值）。

字体随 skill 一起打包在 `assets/NotoSerifSC-VF.ttf`（约 24MB），换电脑不需要额外安装。文件缺失时脚本会明确报错。想临时换字体用 `--font`，但字形会和既有封面不一致。

字体是 Noto Serif SC 2.02，版权 Adobe，SIL Open Font License 1.1，许可全文见 [assets/OFL.txt](assets/OFL.txt)。原样打包未作修改。
