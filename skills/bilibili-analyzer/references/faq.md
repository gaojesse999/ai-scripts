# 常见问题 (FAQ)

## 基础问题

### Q: 为什么这个 skill 不再需要 `.NET` 和 `ffmpeg`？
A: 这个新 skill 改成了纯 Python 链路。视频下载走 Bilibili 公共接口，抽帧走 OpenCV，去重走 Pillow + ImageHash，因此不再依赖原先的 `.NET + ffmpeg` 组合。

### Q: 分析一个视频需要多长时间？
A: 取决于多个因素：
- 视频长度
- 帧提取间隔和最大帧数
- 网络速度（下载阶段）
- AI分析并行度

一般来说，10分钟视频按 `fps=1` 抽帧后，准备阶段通常只需要数分钟，后续 AI 分析耗时取决于帧数和并行分析方式。

### Q: `images_raw/` 和 `images/` 有什么区别？
A: `images_raw/` 保存按目标 `fps` 抽出的全部原始帧；`images/` 保存去重后的保留帧。AI 分析和文档插图应优先使用 `images/`。

### Q: 单视频和合集有什么区别？
A: 
- **单视频**: 一个 BV 号对应一个视频（可能有多个分P），分析后生成 `视频分析.md`
- **合集 (UGC 合集/系列)**: 多个独立 BV 视频组成的集合，每个视频单独分析后合并为 `合集视频分析.md`

### Q: 如何判断一个链接是单视频还是合集？
A: 使用 `collection.py` 自动检测：
```bash
python scripts/collection.py "<URL>"
```
脚本会通过 Bilibili API 检查视频是否属于 UGC 合集，并输出 JSON 结果。

## 合集相关

### Q: 支持哪些类型的合集？
A: 
- **UGC 合集**: UP 主创建的视频合集（`channel/collectiondetail`）
- **系列**: UP 主创建的视频系列（`channel/seriesdetail`）
- **单视频中的合集检测**: 如果视频属于某个 UGC 合集，`collection.py` 会通过 `view` API 的 `ugc_season` 字段自动识别

### Q: 合集中某个视频分析失败怎么办？
A: 系统会跳过失败的视频继续分析后续视频。失败的视频会在 `合集视频分析.md` 中标注失败信息，你可以之后单独重试失败的视频。

### Q: 合集视频数量很多（几十上百个）怎么办？
A: 
- 合集中每个视频都需要单独下载和分析，耗时会随视频数量线性增长
- 建议先运行 `collection.py` 查看视频总数，评估总耗时
- 可以考虑先分析部分视频，后续再补充

### Q: 合集的输出目录结构是怎样的？
A: 
```
<合集输出目录>/
├── <视频1 BV号>/       # 各视频独立目录
│   ├── images/
│   ├── 视频分析.md
│   └── ...
├── <视频2 BV号>/
│   └── ...
└── 合集视频分析.md     # 合并后的总文档
```

### Q: 可以只分析合集中的部分视频吗？
A: 当前版本不直接支持范围选择。你可以在 `collection.py` 输出视频列表后，手动选择要分析的视频逐个处理。

## 错误处理

### Q: 遇到"URL无效"错误怎么办？
A: 请确保URL格式正确：
- 标准格式: `https://www.bilibili.com/video/BV1xx411c7mD`
- 合集页面: `https://space.bilibili.com/{mid}/channel/collectiondetail?sid={season_id}`
- 系列页面: `https://space.bilibili.com/{mid}/channel/seriesdetail?sid={series_id}`
- 短链接: `https://b23.tv/xxxxx`
- 不支持番剧、直播等其他类型链接

### Q: 下载失败怎么办？
A: 可能的原因和解决方案：
1. **网络问题**: 检查网络连接，稍后重试
2. **视频不存在**: 确认视频未被删除或设为私有
3. **地区限制**: 某些视频可能有地区限制
4. **API 限流**: 合集模式下连续下载多个视频可能触发限流，稍等后重试

### Q: OpenCV 或 ImageHash 报错怎么办？
A: 
1. 确认安装的是 `opencv-python-headless` 而不是图形版 OpenCV
2. 重新安装依赖：`python -m pip install --upgrade opencv-python-headless pillow ImageHash`
3. 确认当前运行的 `python` 与安装依赖的环境一致

### Q: AI分析失败怎么办？
A: 系统会自动重试失败的分析任务。如果仍然失败：
1. 检查Claude Code配置
2. 查看生成目录中的 `metadata.json` 和 `frames.json`
3. 先确认 `images/` 中的关键帧是否已经正常生成

## 高级用法

### Q: 如何只分析视频的特定部分？
A: 当前脚本不支持按时间范围裁切，但可以通过降低 `fps` 来减少帧数，例如长视频使用 `--fps 0.2`。

### Q: 如何提高分析速度？
A: 
1. 降低 `fps`，例如从 `1` 改成 `0.5` 或 `0.2`
2. 保持去重开启，减少需要分析的关键帧数量
3. 只对 `images/` 中的去重后关键帧做 AI 分析
4. 请求时指定"使用subagent"或"并行分析"以启用 SubAgent 并行模式

### Q: 如何获取更详细的分析？
A: 
1. 提高 `fps`，例如 `--fps 1`
2. 调高 `--similarity` 阈值，让更多相邻帧被保留下来
3. 如有需要，可使用 `--no-dedup` 保留全部原始帧

### Q: 分析中断后如何恢复？
A: 当前脚本不会做检查点恢复，需要重新运行命令。已生成的 `video.mp4`、`images_raw/`、`images/`、`metadata.json`、`frames.json` 可以作为人工排查依据。合集模式下，已完成的视频不需要重新分析，只需重新处理未完成的视频。

### Q: 什么时候使用 SubAgent 模式？
A: 
- **默认模式**（推荐）：在当前会话中顺序分析，适合大多数场景
- **SubAgent 模式**：在请求时说"使用subagent"或"并行分析"来启用，适合图片数量多、希望加速分析的场景

## 输出相关

### Q: 报告中的图片路径应该怎么写？
A: 
- **单视频**: 使用相对路径 `./images/frame_0001.jpg`
- **合集文档**: 使用 `./<BV号>/images/frame_0001.jpg` 格式

### Q: 如何知道最终保留帧来自哪些原始帧？
A: 查看 `frames.json`。其中会记录 `file`、`source_file`、`timestamp` 和 `adjacent_similarity`。

## 错误代码

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `URLValidationError` | URL格式不正确 | 使用正确的B站视频URL |
| `MetadataFetchError` | 无法获取视频信息 | 检查视频是否存在/私有 |
| `DownloadError` | 下载失败 | 检查网络，增加重试次数 |
| `OpenCVError` | 视频读取或抽帧失败 | 检查 OpenCV 安装和视频文件 |
| `ImageHashError` | 图像去重失败 | 检查 Pillow / ImageHash 安装 |
| `AnalysisError` | AI分析失败 | 检查Claude Code配置 |
| `ReportGenerationError` | 报告生成失败 | 检查输出目录权限 |
| `CollectionAPIError` | 合集 API 调用失败 | 检查网络或 URL 格式 |
