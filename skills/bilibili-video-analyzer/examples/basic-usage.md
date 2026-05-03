# 基本使用示例

## 快速开始

以下示例默认当前工作目录是 skill 根目录；如果不是，请把 `scripts/prepare.py` 替换成实际相对路径或绝对路径。

```bash
python scripts/prepare.py "https://www.bilibili.com/video/BV1xx411c7mD" -o ./output
```

## 常用场景

### 1. 分析短视频

```bash
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

## 输出示例

分析完成后，输出目录结构：

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
