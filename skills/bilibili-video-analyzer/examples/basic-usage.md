# 基本使用示例

## 快速开始

```bash
cd .agents/skills/bilibili-video-analyzer
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output
```

## 常用场景

### 1. 默认参数（fps 自动选择）

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output
```

### 2. 长视频降低帧率

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./long-video --fps 0.2
```

### 3. 合集分P视频（第4集）

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD?p=4" -o ./episode-4
```

### 4. 只下载视频，不拆帧

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --video-only
```

### 5. 已有 video.mp4，只重新拆帧（必须显式 `--fps`）

```bash
python scripts/prepare.py dummy-url -o ./output --frames-only --fps 0.5
```

### 6. 调整去重阈值

```bash
# PPT 类视频，更激进去重
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./ppt --similarity 0.60

# 动态演示，避免误删
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./demo --similarity 0.80
```

### 7. 禁用去重

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output --no-dedup
```

## 输出示例

执行完成后，输出目录结构：

```
./output/
├── video.mp4              # 下载的视频
├── dedup_manifest.json    # raw → output 帧号映射
├── images_raw/            # 全部原始帧
│   ├── frame_0001.jpg
│   └── ...
└── images/                # 去重后的分析帧
    ├── frame_0001.jpg
    └── ...
```
