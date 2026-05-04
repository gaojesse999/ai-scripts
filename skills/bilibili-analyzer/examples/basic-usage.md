# 基本使用示例

## 快速开始

以下示例默认当前工作目录是 skill 根目录；如果不是，请把 `scripts/prepare.py` 和 `scripts/collection.py` 替换成实际相对路径或绝对路径。

### 检测链接类型

```bash
python scripts/collection.py "https://www.bilibili.com/video/BV1xx411c7mD"
```

### 分析单个视频

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output
```

## 常用场景

### 1. 分析短视频

```bash
python scripts/collection.py "https://www.bilibili.com/video/BV1xx411c7mD"
# 输出: {"type": "single", ...}

python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./short-video --fps 1
```

### 2. 分析中等长度视频

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./mid-video --fps 0.5
```

### 3. 分析长视频

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./long-video --fps 0.2
```

### 4. 调整去重阈值

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./strict-dedup --similarity 0.85
```

### 5. 保留全部原始帧

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./no-dedup --no-dedup
```

### 6. 分析带 `p=` 的分集链接

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=3" -o ./episode-3 --fps 0.5
```

### 7. 分析 UGC 合集

```bash
# 先检测合集
python scripts/collection.py "https://space.bilibili.com/12345/channel/collectiondetail?sid=67890"
# 输出: {"type": "collection", "collection_title": "...", "total": 5, "videos": [...]}

# 逐个分析
python scripts/prepare.py "https://www.bilibili.com/video/BV1aaa" -o ./my-collection/BV1aaa/
python scripts/prepare.py "https://www.bilibili.com/video/BV1bbb" -o ./my-collection/BV1bbb/
# ... 对每个视频生成 视频分析.md，最后合并为 合集视频分析.md
```

### 8. 分析系列视频

```bash
python scripts/collection.py "https://space.bilibili.com/12345/channel/seriesdetail?sid=67890"
# 输出: {"type": "collection", ...}

# 后续流程同合集
```

### 9. 通过单视频 URL 检测合集

```bash
# 如果视频属于某个 UGC 合集，collection.py 会自动检测到
python scripts/collection.py "https://www.bilibili.com/video/BV1xx411c7mD"
# 可能输出: {"type": "collection", "collection_title": "...", "videos": [...]}
```

## 输出示例

### 单视频输出

```
./output/
├── video.mp4
├── images_raw/
│   ├── frame_0001.jpg
│   ├── frame_0002.jpg
│   └── ...
├── images/
│   ├── frame_0001.jpg
│   ├── frame_0002.jpg
│   └── ...
├── metadata.json
└── frames.json
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
│   └── 视频分析.md
├── BV1bbb/
│   ├── video.mp4
│   ├── images_raw/
│   ├── images/
│   ├── metadata.json
│   ├── frames.json
│   └── 视频分析.md
└── 合集视频分析.md
```
