# 基本使用示例

## 快速开始

以下示例默认当前工作目录是 skill 根目录；如果不是，请把脚本路径替换成实际相对路径或绝对路径。

### 先解析最终处理范围

```bash
# 单视频模式
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD" --mode single

# 合集模式
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD" --mode collection
```

说明：

- `resolve_scope.py` 会把原始链接解析成最终待处理单元列表
- 后续执行 `prepare.py` / `text_prepare.py` 时，应优先使用 `resolve_scope.py` 输出的 `targets[*].url`
- 对多P视频，不要再直接把模糊的多P总链接传给 `prepare.py` / `text_prepare.py`

### 分析单个视频（完整链路）

```bash
# 1. 先解析最终处理范围
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD" --mode single

# 2. 下载并拆帧（使用 targets[0].url）
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output

# 3. 读取平台字幕；如果没有字幕，会直接返回 image_only，后续改为纯图片分析
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output

# 4. 联合 text_segments.json（若存在）与 images/ 生成 视频分析.md
```

## 常用场景

### 1. 分析短视频

```bash
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD" --mode single
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./short-video --fps 1
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./short-video
```

### 2. 分析中等长度视频

```bash
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD" --mode single
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./mid-video --fps 0.5
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./mid-video
```

### 3. 分析长视频

```bash
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD" --mode single
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./long-video --fps 0.2
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./long-video
```

### 4. 分析带 `p=` 的分集链接

```bash
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD?p=3" --mode single
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=3" -o ./episode-3 --fps 0.5
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=3" -o ./episode-3
```

### 5. 分析 UGC 合集

```bash
# 先解析最终处理范围
python scripts/resolve_scope.py "https://space.bilibili.com/12345/channel/collectiondetail?sid=67890" --mode collection

# 按 resolver 返回的 targets 逐个分析
python scripts/prepare.py "https://www.bilibili.com/video/BV1aaa" -o ./my-collection/BV1aaa/
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1aaa" -o ./my-collection/BV1aaa/

python scripts/prepare.py "https://www.bilibili.com/video/BV1bbb" -o ./my-collection/BV1bbb/
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1bbb" -o ./my-collection/BV1bbb/

# ... 对每个视频生成 视频分析.md，最后合并为 合集视频分析.md
```

### 6. 分析系列视频

```bash
python scripts/resolve_scope.py "https://space.bilibili.com/12345/channel/seriesdetail?sid=67890" --mode collection
# 后续流程同合集，按 resolver 返回的 targets 逐个处理
```

### 7. 分析多P视频的全部分P

```bash
python scripts/resolve_scope.py "https://www.bilibili.com/video/BV1xx411c7mD" --mode collection

# 使用 resolver 返回的明确 ?p= URL
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=1" -o ./multi-p/P01/
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=1" -o ./multi-p/P01/

python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=2" -o ./multi-p/P02/
python scripts/text_prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=2" -o ./multi-p/P02/

# ... 最后合并为 分P视频分析.md
```

## 输出示例

### 单视频输出

```
./output/
├── video.mp4
├── images_raw/
├── images/
├── metadata.json
├── frames.json
├── subtitles.json / subtitles.txt     # 若平台字幕存在
├── text_segments.json                 # 若平台字幕存在
└── 视频分析.md
```

### 合集输出

```
./my-collection/
├── BV1aaa/
│   ├── video.mp4
│   ├── images_raw/
│   ├── images/
│   ├── metadata.json
│   ├── frames.json
│   ├── subtitles.json / text_segments.json
│   └── 视频分析.md
├── BV1bbb/
│   └── ...
└── 合集视频分析.md
```

### 多P输出

```
./multi-p/
├── P01/
│   ├── video.mp4
│   ├── images_raw/
│   ├── images/
│   ├── metadata.json
│   ├── frames.json
│   ├── subtitles.json / text_segments.json
│   └── 视频分析.md
├── P02/
│   └── ...
└── 分P视频分析.md
```
