# douyin-video-analyzer（抖音视频全流程复盘分析器）

给一个日期区间，自动完成「扫码登录 → 导出官方三表 → 下载本人视频 → 转 MP3 →
Whisper 转口播脚本 → 抽关键帧 → 数据/脚本/视觉三层归因 → 产出复盘报告」的闭环。
服务于**个人知识口播账号的自我复盘**。

## 工作原理（视频为什么能下载）

- 官方三表：创作者中心「导出数据」按钮直接下载 xlsx（数据中心 + 作品管理）。
- 视频：网页分享面板的「下载」可能提示“不支持下载”，但视频要能播放，浏览器必然已从
  抖音官方 CDN（`douyinvod.com`）取到真实视频文件。本技能在已登录浏览器里读取
  播放器的网络请求（相当于 F12 的 Network 面板），把“已经能播放的本人视频”另存为 mp4，
  再用 ffprobe 校验音视频完整。**不是破解、不碰 DRM、不下载他人内容**。
- CDN 地址带时效签名（约数小时），需现抓现下；偶尔遇到音视频分离流，用 ffmpeg 合并。

## 依赖

1. `ffmpeg` / `ffprobe`（PATH 或 `.skill.env` 的 `FFMPEG_PATH`）。
2. Python ≥ 3.9，安装 `openpyxl`：`pip install openpyxl`（其余只用标准库）。
3. 工程根 `.skill.env` 配置 `GROQ_API_KEY`、`PYTHON_EXE`（模板见 `.skill.env.example`）。
   转写复用 `audio-stt`，转换复用 `video-to-mp3`，这两个技能需一并存在。
4. 浏览器自动化 `computer_use_tool(plane="bu")`；登录需用户用抖音 App 扫码一次。

## 目录结构

```
douyin-video-analyzer/
├── SKILL.md                     # 编排入口（七阶段流程）
├── README.md
├── .skill.env.example
├── scripts/
│   ├── common.py                # 环境/路径/命名/ffprobe 公共库
│   ├── parse_data.py            # 三表解析、作品对齐、衍生指标、台账/数据底稿
│   ├── normalize_names.py       # 下载目录三表与视频归档到周期目录
│   ├── media_pipeline.py        # 复用 video-to-mp3 + audio-stt（MP3/脚本，断点续跑）
│   ├── extract_frames.py        # 前5秒钩子帧 + 中段 + 结尾帧
│   └── build_report.py          # 套用模板生成复盘报告骨架（数据/脚本/帧自动填）
├── references/
│   ├── BROWSER_RUNBOOK.md       # 登录/导出/抓CDN/选流合并 的浏览器操作手册
│   ├── DATA_DICTIONARY.md       # 三表字段与衍生指标口径
│   ├── ANALYSIS_FRAMEWORK.md    # 数据/脚本/视觉三层归因方法
│   └── METRICS_BENCHMARK.md     # 指标基准与冷启动校准
└── templates/
    └── 复盘报告模板.md
```

产物统一落在 `视频分析/视频素材/<YYYYMMDD-YYYYMMDD>/`：三表、mp4/mp3/txt、
`frames/`、`_采集清单.json`、`_数据底稿.md`、复盘报告。

## 全流程（由 Agent 驱动）

用户只需给出区间并扫码。本地脚本依次为：

```powershell
# 3. 导出三表后归档（浏览器步骤见 BROWSER_RUNBOOK.md）
python scripts/normalize_names.py --start 2026-10-09 --end 2026-10-15
# 4. 解析三表、对齐作品，得到待下载清单
python scripts/parse_data.py       --start 2026-10-09 --end 2026-10-15
# 5. 按清单在浏览器抓 CDN 下载视频（Agent 操作），再次 normalize + parse 校验
# 6. 转 MP3 / 转脚本 / 抽帧
python scripts/media_pipeline.py   --start 2026-10-09 --end 2026-10-15
python scripts/extract_frames.py   --start 2026-10-09 --end 2026-10-15
# 7. 生成报告骨架，Agent 按 ANALYSIS_FRAMEWORK 完成三层归因
python scripts/build_report.py     --start 2026-10-09 --end 2026-10-15
```

## 其它用法

- 三表/视频已在本地：直接从 `parse_data.py` 开始。
- 无三表、只分析已下载视频：`parse_data.py --offline`。
- 所有脚本幂等、支持断点续跑（跳过已生成的 mp3/txt/帧）。
- 区间内的断更日（投稿 0）与一天多条（自动 01/02 编号）都会被正确处理。

## 合规

仅限下载、分析**本人账号**作品用于自我复盘；禁止批量抓取他人视频、禁止公开 CDN 签名。
若平台改版导致抓取失效，按 `references/BROWSER_RUNBOOK.md` 重新定位页面元素。
