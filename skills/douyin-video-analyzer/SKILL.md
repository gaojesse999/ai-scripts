---
name: douyin-video-analyzer
description: >-
  输入一个日期区间，全流程复盘用户自己的抖音知识口播短视频：扫码登录创作者中心 →
  导出官方三表（每日视频数据、粉丝数据、作品列表）→ 批量下载区间内本人视频 →
  转 MP3 并用 Whisper 转口播脚本 → 抽关键帧 → 从「数据层 / 脚本层 / 视觉层」做三层归因，
  回答每条视频为什么表现好或不好，并产出可执行的迭代复盘报告。
  当用户提到“分析/复盘我的抖音视频、抖音作品数据、播放量/完播率/2秒跳出/5秒完播怎么样、
  哪条视频为什么火/为什么没流量、导出抖音创作者数据、批量分析某几天的视频、口播脚本复盘、
  数据中心/作品管理导出、抖音视频分析”，哪怕只给出一个日期区间，都应使用本技能。
  仅用于下载和分析用户本人账号的作品，禁止用于抓取他人内容。
compatibility: "需要 computer_use_tool(plane=bu) 浏览器、ffmpeg、Python(openpyxl) 与 .skill.env 的 GROQ_API_KEY。"
---

# 抖音视频全流程复盘分析器

给一个**日期区间**，完成「取数 → 取视频 → 转脚本 → 抽帧 → 三层归因 → 复盘报告」的闭环。
分析对象是用户自己的抖音知识口播账号，产物落在 `视频分析/视频素材/<周期目录>/`。

## 适用边界与合规

- **只处理用户本人账号**（创作者中心已登录的那个账号）。视频通过浏览器已授权会话中
  播放器实际请求的官方 CDN 地址保存（`douyinvod.com`），等价于“把能正常播放的本人视频
  另存下来”，**不破解、不绕 DRM、不碰他人作品**。
- 不要把该方法用于批量下载他人视频，也不要公开 CDN 签名地址。
- 分析是自我复盘，数据解读需区分“已查证事实”和“推断”，并对冷启动期做口径校准。

## 环境依赖（开工前先确认）

- `ffmpeg` / `ffprobe` 可用（PATH 或 `.skill.env` 的 `FFMPEG_PATH`）；
- Python 及 `openpyxl`（`.skill.env` 的 `PYTHON_EXE` 指向的环境）；
- `.skill.env` 已配 `GROQ_API_KEY`（语音转写用，`audio-stt` 直连 `api.groq.com`，无需代理）；
- 浏览器自动化 `computer_use_tool(plane="bu")` 可用，登录扫码需用户配合。

环境缺失时先停下报告，不要用“大概能跑”继续。

## 输入

- **必需**：分析日期区间（起止日）。用户只给“最近一周”“上周”时，先换算为明确日期。
- **无需用户准备**：视频、三表、周期目录都由本技能自动下载/创建；用户只需扫码登录一次。
- 区间内允许**断更日**（日历日有、投稿量为 0）与**一天多条**（按发布时间加 01/02 编号），
  脚本会自动处理，不要让用户手工挑。

## 目录与命名约定

- 素材根：`视频分析/视频素材/`；周期目录：`YYYYMMDD-YYYYMMDD`（单天 `YYYYMMDD`）。
- 视频/音频/脚本同名：单条 `YYYYMMDD-标题简码`；一天多条 `YYYYMMDD-01-标题`、`-02-`。
- 关键帧：`frames/<视频主名>/`；台账 `_采集清单.json`；数据底稿 `_数据底稿.md`。
- 浏览器下载先落系统下载目录，再由 `normalize_names.py` 归档进周期目录。

脚本调用统一用 `.skill.env` 里的 Python：`$py = .skill.env 的 PYTHON_EXE`，
脚本目录：`.agents/skills/douyin-video-analyzer/scripts/`。

## 执行流程总览

| 阶段 | 动作 | 谁来做 |
|---|---|---|
| 1 | 建周期目录、确认区间 | 脚本（parse_data 会自动建） |
| 2 | 登录创作者中心（用户扫码） | 浏览器 + 用户交接 |
| 3 | 导出官方三表并归档 | 浏览器 + normalize 脚本 |
| 4 | 解析三表、对齐作品、生成清单 | 脚本 `parse_data.py` |
| 5 | 逐条下载区间视频、校验完整性 | 浏览器 + 脚本校验 |
| 6 | 转 MP3、转口播脚本、抽关键帧 | 脚本 `media_pipeline.py`、`extract_frames.py` |
| 7 | 三层归因 + 生成复盘报告 | 脚本出骨架，Agent 写分析 |

浏览器操作**必须**由你在 `computer_use_tool(plane="bu")` 里实时执行，不能做成无人值守脚本
（页面要扫码、有动态加载、下载地址带时效签名）。具体操作步骤见
**[references/BROWSER_RUNBOOK.md](./references/BROWSER_RUNBOOK.md)**，每一步都先观察再操作。

---

## Stage 1-2：初始化与登录

1. 与用户确认区间起止日（例如 2026-10-09 至 2026-10-15）。
2. 用 `computer_use_tool(plane="bu")` 打开数据中心：
   `https://creator.douyin.com/creator-micro/data-center/operation`。
3. 若出现扫码/验证码登录页（`blocked=auth`），**立即**调用
   `interaction.request_action(type="browserControl")`，请用户用抖音 App 扫码，
   完成后回到浏览器重新观察确认登录成功（能看到账号昵称、数据看板）。
4. 告知用户：整个过程只需要这一次扫码。

## Stage 3：导出三表

按 [BROWSER_RUNBOOK.md](./references/BROWSER_RUNBOOK.md) 操作：
- 数据中心选「自定义时间」覆盖区间（含首尾），分别在**作品数据区**和**粉丝数据区**
  点「导出数据」，得到「数据表现_短视频全量指标.xlsx」「数据表现_粉丝全量指标.xlsx」。
  粉丝画像因粉丝量小未开放是正常的——有则用、无则跳过。
- 作品管理页 `https://creator.douyin.com/creator-micro/content/manage` 点「导出数据」，
  得到全量「作品列表导出.xlsx」（本地按区间筛）。
- 导出按钮点击后直接下载、无弹窗；同区可能有多个同名按钮，用 RUNBOOK 里的 JS 打标定位。

归档：
```powershell
& $py .agents/skills/douyin-video-analyzer/scripts/normalize_names.py --start 2026-10-09 --end 2026-10-15
```

## Stage 4：解析三表、对齐作品

```powershell
& $py .agents/skills/douyin-video-analyzer/scripts/parse_data.py --start 2026-10-09 --end 2026-10-15
```

产出 `_采集清单.json`（每条作品的标准文件名与本地文件状态）和 `_数据底稿.md`。
脚本末尾会打印：区间作品数、断更日、一天多条、**待下载视频清单**。以这个清单作为 Stage 5
的下载目标，逐条对照，不要漏条也不要多下载区间外的作品。

## Stage 5：逐条下载视频并校验

关键背景：网页分享面板的「下载」按钮可能提示“该视频不支持下载”（作者关闭了下载权限），
但视频要在浏览器里播放，播放器必然向官方 CDN 请求过真实视频地址。做法是：
1. 打开该作品播放页，让视频真正播放几秒；
2. 用 `bu.network_requests()` 找到 `douyinvod.com` 下 `/video/tos/` 的真实地址；
3. 用 `bu.download(url, filename="标准名.mp4")` 保存（文件名用台账里的 file_base）。

**选流坑（务必遵守）**：网络里同时存在「音视频合一的完整 mp4」和「HEVC 纯视频 + AAC 音频
两条分离 DASH 流」，还可能混入异常拼接的超长流。**不能只按码率选**。下载后必须用
ffprobe 校验“同时含视频流和音频流、时长与作品时长误差 ≤ 2.5s”。优先找含
`mime_type=video_mp4` 的完整流；分离流需要 ffmpeg 合并，步骤见 RUNBOOK。

全部下载后再次归档并重跑 `parse_data.py`，确认“√ 全部视频已就位”，并检查每条
`has_audio=true`、时长合理。`is_complete_video()` 已内置校验逻辑，RUNBOOK 给了命令。

## Stage 6：转脚本、抽帧

```powershell
# MP4 -> MP3（video-to-mp3）-> 口播脚本（audio-stt / Groq Whisper），断点续跑
& $py .agents/skills/douyin-video-analyzer/scripts/media_pipeline.py --start 2026-10-09 --end 2026-10-15
# 抽前5秒钩子帧 + 中段 + 结尾帧
& $py .agents/skills/douyin-video-analyzer/scripts/extract_frames.py --start 2026-10-09 --end 2026-10-15
```

转写走外网若被阻断（403/超时），脚本会打印诊断，停下报告用户，不要自行换通道硬试。

## Stage 7：三层归因与报告

先生成报告骨架（自动填好数据、脚本原文、帧路径）：
```powershell
& $py .agents/skills/douyin-video-analyzer/scripts/build_report.py --start 2026-10-09 --end 2026-10-15
```

然后你必须完成“分析”这一步——脚本只负责数据和排版，判断由你做：

1. **先看** `_数据底稿.md` 和 `frames/` 关键帧，再逐条读脚本原文。
2. 按**三层归因**逐条诊断，方法论见 [references/ANALYSIS_FRAMEWORK.md](./references/ANALYSIS_FRAMEWORK.md)：
   - **数据层**：漏斗定位（2s 跳出→5s 完播→完播→平均播放时长占比→互动/收藏/转发→涨粉），
     用同周期其他条和基准做对照，不孤立看单条。
   - **脚本层**：0-2s 钩子、2-5s 承接、中段单点是否讲透、结尾 CTA，对照脚本逐句找症结。
   - **视觉层**：逐张看关键帧的花字、表情状态、动作、着装道具，判断钩子的视觉冲击与交付感。
3. 指标基准（2s 跳出 <40%、5s 完播 25%-30%、完播 >1%、时长 60-90s 等）与冷启动熟人流量
   校准，见 [references/METRICS_BENCHMARK.md](./references/METRICS_BENCHMARK.md)。
4. 字段口径见 [references/DATA_DICTIONARY.md](./references/DATA_DICTIONARY.md)。
5. 把结论填进报告骨架：执行摘要、逐条一句话结论、问题诊断、**可直接执行的迭代方案**
   （写清“改哪里、怎么改、预期影响哪个指标”）、下周期选题与 12 字开头钩子。

结论要自然、接地气、不浮夸，引用具体作品与数字；避免空话和“AI 味”。

## 常见模式

- **只给区间，全流程**：按 Stage 1→7 顺序执行，下载阶段需要用户扫码。
- **视频/表已在本地**：跳过 Stage 2-5，直接从 Stage 4 `parse_data.py` 开始。
- **无三表、只想分析已下载的视频**：`parse_data.py --offline` 扫本地 mp4 建清单，再转脚本抽帧。
- **断点续跑**：所有脚本带 `--skip-existing` / 幂等，失败修正后重跑即可。

## 异常处理速查

- 扫码/验证码/登录过期：重新 `interaction.request_action` 请用户扫码，不猜账号密码。
- 导出按钮点不动：用 RUNBOOK 的 JS 打标 `data-exp` 后再 `bu.click(css选择器)`。
- 视频下载得到无音频/时长异常：选到了 HEVC 分离流或拼接流，重选并 ffprobe 校验。
- CDN 地址过期（约数小时）：回到播放页重新 `network_requests` 现抓，不缓存旧地址。
- 找不到三表：确认已点导出，且 `normalize_names.py` 已归档；作品表为全量必须有。
- STT 网络失败：读错误里的进程/URL，停下让用户处理代理或网络。
