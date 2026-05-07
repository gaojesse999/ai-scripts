# 常见问题 (FAQ)

## 基础问题

### Q: 这个 skill 现在到底是怎么理解视频内容的？
A: 当前优先级是：
1. **先用平台字幕**建立内容主线
2. **字幕不可用时**直接退回仅图片分析

### Q: 分析一个视频需要多长时间？
A: 现在主要取决于这些因素：
- 视频长度
- 抽帧间隔和最终关键帧数量
- 是否有平台字幕
- AI 分析并行度

一般来说：
- **有字幕**时更容易快速建立章节主线
- **无字幕**时会更多依赖纯视觉分析，整体推断成本更高

### Q: `images_raw/` 和 `images/` 有什么区别？
A: `images_raw/` 保存按目标 `fps` 抽出的全部原始帧；`images/` 保存去重后的保留帧。AI 分析和文档插图应优先使用 `images/`。

### Q: `text_segments.json` 是做什么的？
A: 它是字幕模式下统一的时间轴文本输入：
- 如果有字幕，它来自平台字幕
- 如果没有字幕，就不会生成这个文件，后续会直接走图片分析

## 文本与图片

### Q: 如果视频有字幕，会怎么处理？
A: 默认优先使用字幕，并生成 `subtitles.json`、`subtitles.txt` 和 `text_segments.json` 供后续分析读取。

### Q: 如果视频没有字幕，会怎么办？
A: `text_prepare.py` 会返回 `mode=image_only`，后续分析直接基于 `images/` 中的关键帧进行，不会再尝试其他文本回退链路。

### Q: 如果字幕和图片冲突怎么办？
A: 当前规则是：
- **章节顺序 / 口播解释**优先参考字幕（前提是字幕存在）
- **代码 / UI / 按钮名 / 报错文案**优先以图片为准
- 冲突必须显式标注，不能强行合并

## 合集相关

### Q: 支持哪些类型的合集？
A:
- **UGC 合集**：`channel/collectiondetail`
- **系列**：`channel/seriesdetail`
- **单视频中的 UGC 合集检测**：通过 `ugc_season` 字段识别

### Q: 合集中每个视频都会单独处理吗？
A: 会。合集里的每个视频都会独立执行：
1. 下载与抽帧
2. 读取字幕或进入仅图片模式
3. 联合分析
4. 生成单视频文档

### Q: 合集中某个视频分析失败怎么办？
A: 系统会跳过失败的视频继续分析后续视频。失败的视频会在 `合集视频分析.md` 中标注失败信息。

## 错误处理

### Q: 遇到 "URL 无效" 错误怎么办？
A: 请确保 URL 格式正确：
- 标准格式：`https://www.bilibili.com/video/BV1xx411c7mD`
- 合集页面：`https://space.bilibili.com/{mid}/channel/collectiondetail?sid={season_id}`
- 系列页面：`https://space.bilibili.com/{mid}/channel/seriesdetail?sid={series_id}`
- 短链接：`https://b23.tv/xxxxx`

### Q: `text_prepare.py` 返回 `image_only` 是什么意思？
A: 表示当前没有成功建立字幕主线，常见原因：
1. 平台字幕不存在
2. 字幕轨道地址不可用
3. 字幕接口返回异常

### Q: OpenCV 或 ImageHash 报错怎么办？
A:
1. 确认安装的是 `opencv-python-headless`
2. 重新安装依赖：`python -m pip install --upgrade opencv-python-headless pillow ImageHash`
3. 确认当前运行的 `python` 与安装依赖的环境一致

### Q: AI 分析失败怎么办？
A: 系统会自动重试失败的分析任务。如果仍然失败：
1. 检查当前对话环境是否能读取图片
2. 查看 `metadata.json`、`frames.json`、`text_segments.json`
3. 先确认关键帧或字幕主线是否已经正常生成

## 高级用法

### Q: 如何提高分析速度？
A:
1. 降低 `fps`，减少关键帧数量
2. 保持去重开启
3. 若字幕可用，优先依赖字幕主线，减少纯视觉推断成本
4. 请求时指定“使用subagent”或“并行分析”以启用并行模式

### Q: 如何获取更详细的分析？
A:
1. 提高 `fps`
2. 调高 `--similarity` 阈值，让更多相邻帧被保留下来
3. 如有需要，可使用 `--no-dedup` 保留全部原始帧
4. 确保关键帧覆盖到完整流程，这样能补足字幕缺失时的视觉证据

### Q: 分析中断后如何恢复？
A: 当前脚本不会做完整检查点恢复，需要重新运行命令。但已生成的这些文件可用于排查和复用：
- `video.mp4`
- `images_raw/`
- `images/`
- `metadata.json`
- `frames.json`
- `subtitles.json` / `text_segments.json`

## 输出相关

### Q: 报告中的图片路径应该怎么写？
A:
- **单视频**：使用相对路径 `./images/frame_0001.jpg`
- **合集文档**：使用 `./<BV号>/images/frame_0001.jpg`

### Q: 如何知道最终保留帧来自哪些原始帧？
A: 查看 `frames.json`。其中会记录 `file`、`source_file`、`timestamp` 和 `adjacent_similarity`。

### Q: 如何知道当前视频最终走的是字幕还是仅图片？
A: 查看 `text_prepare.py` 的输出或相关中间产物：
- 有 `subtitles.json` 和 `text_segments.json` → 字幕模式
- 返回 `mode=image_only` → 仅图片模式

## 错误代码

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `URLValidationError` | URL格式不正确 | 使用正确的 B 站视频 URL |
| `MetadataFetchError` | 无法获取视频信息 | 检查视频是否存在 / 私有 |
| `DownloadError` | 下载失败 | 检查网络，增加重试次数 |
| `OpenCVError` | 视频读取或抽帧失败 | 检查 OpenCV 安装和视频文件 |
| `ImageHashError` | 图像去重失败 | 检查 Pillow / ImageHash 安装 |
| `SubtitleFetchError` | 字幕获取失败 | 检查视频是否有字幕或接口是否正常 |
| `AnalysisError` | AI分析失败 | 检查图片 / 文本中间产物是否正常 |
| `ReportGenerationError` | 报告生成失败 | 检查输出目录权限 |
| `CollectionAPIError` | 合集 API 调用失败 | 检查网络或 URL 格式 |
