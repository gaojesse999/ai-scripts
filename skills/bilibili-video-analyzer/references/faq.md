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

## 错误处理

### Q: 遇到"URL无效"错误怎么办？
A: 请确保URL格式正确：
- 标准格式: `https://www.bilibili.com/video/BV1xx411c7mD`
- 短链接: `https://b23.tv/xxxxx`
- 不支持番剧、直播等其他类型链接

### Q: 下载失败怎么办？
A: 可能的原因和解决方案：
1. **网络问题**: 检查网络连接，稍后重试
2. **视频不存在**: 确认视频未被删除或设为私有
3. **地区限制**: 某些视频可能有地区限制

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

### Q: 如何获取更详细的分析？
A: 
1. 提高 `fps`，例如 `--fps 1`
2. 调高 `--similarity` 阈值，让更多相邻帧被保留下来
3. 如有需要，可使用 `--no-dedup` 保留全部原始帧

### Q: 分析中断后如何恢复？
A: 当前脚本不会做检查点恢复，需要重新运行命令。已生成的 `video.mp4`、`images_raw/`、`images/`、`metadata.json`、`frames.json` 可以作为人工排查依据。

## 输出相关

### Q: 报告中的图片路径应该怎么写？
A: 使用相对路径，格式为 `./images/frame_0001.jpg`。如果是总汇总文档，应写成对应课时目录下的相对路径，例如 `./bilibili-BVxxxx-p1/images/frame_0001.jpg`。

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
