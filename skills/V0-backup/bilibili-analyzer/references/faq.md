# 常见问题 (FAQ)

## 基础问题

### Q: 为什么需要FFmpeg？
A: FFmpeg是一个强大的多媒体处理工具，本工具使用它从视频中提取关键帧。没有FFmpeg，帧提取功能将无法工作。

### Q: 分析一个视频需要多长时间？
A: 取决于多个因素：
- 视频长度
- 帧提取间隔和最大帧数
- 网络速度（下载阶段）
- AI分析并行度

一般来说，10分钟视频（默认设置）约需5-10分钟完成分析。

### Q: 支持哪些视频格式？
A: 支持B站所有可播放的视频格式。脚本通过 Bilibili 官方 API 获取播放地址并直接下载，会使用 qn=80 的清晰度。

## 错误处理

### Q: 遇到"URL无效"错误怎么办？
A: 请确保URL格式正确：
- 标准格式: `https://www.bilibili.com/video/BV1xx411c7mD`
- 短链接: `https://b23.tv/xxxxx`
- 不支持番剧、直播等其他类型链接

### Q: 下载失败怎么办？
A: 可能的原因和解决方案：
1. **网络问题**: 脚本内置 12 次重试 + 断点续传 + `backup_url` 兜底，多数 CDN 中断会自动恢复；如果仍失败，请检查网络连通性
2. **视频不存在**: 确认视频未被删除或设为私有
3. **地区限制**: 某些视频可能有地区限制

### Q: FFmpeg报错怎么办？
A: 
1. 确认FFmpeg已正确安装: `ffmpeg -version`
2. 确认FFmpeg在系统PATH中
3. 尝试重新安装FFmpeg

### Q: AI分析失败怎么办？
A: 系统会自动重试失败的分析任务。如果仍然失败：
1. 检查 agent 配置（vision 是否可用）
2. 如果模型不支持图片 vision，请先用 OCR（如 `rapidocr-onnxruntime`）建立文字索引

## 高级用法

### Q: 如何只分析视频的特定部分？
A: 目前 prepare.py 不直接支持指定时间范围，但可以：
- 调整 `--fps` 控制密度
- 自行用 ffmpeg `-ss/-to` 裁剪 `video.mp4` 后再用 `--frames-only` 重新拆帧

### Q: 如何提高拆帧/去重速度？
A: 
1. 降低 `--fps`（如 0.5 或 0.2）
2. 调高 `--similarity` 减少保留帧
3. 必要时使用 `--no-dedup` 跳过相似度计算

### Q: 如何获取更详细的分析？
A: 
1. 提高 `--fps`
2. 降低 `--similarity` 保留更多差异帧
3. 在 vision 分析阶段增加每张图片的描述维度

### Q: 分析中断后如何恢复？
A: prepare.py 的下载阶段支持断点续传；拆帧/去重阶段需要重新执行。

## 输出相关

### Q: 报告中的图片路径是什么格式？
A: 使用相对路径，格式为 `./images/frame_XXXX.jpg`（去重后的帧），确保报告与 `images/` 目录在同一位置时图片可正常显示。

### Q: `dedup_manifest.json` 是做什么的？
A: 它记录原始帧（`images_raw/frame_XXXX.jpg`）与去重后帧（`images/frame_XXXX.jpg`）之间的映射，便于追溯任意一张分析帧来自原始的第几帧。

## 错误代码

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `Invalid Bilibili URL` | 无法从 URL 中提取 BV 号 | 使用正确的B站视频URL |
| `Failed to get video info` | 无法获取视频信息 | 检查视频是否存在/私有 |
| `Failed to get playback URL` | API 拒绝 | 检查登录态/地区限制 |
| `ffmpeg not found` | 未安装或未加入 PATH | 安装并配置 ffmpeg |
| `Frame extraction failed` | ffmpeg 拆帧失败 | 检查 `video.mp4` 是否完整 |
