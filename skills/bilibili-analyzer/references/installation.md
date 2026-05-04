# 安装指南

## 系统依赖

### Python（必需）

本 skill 使用 Python 直接调用 Bilibili 公共接口、OpenCV 抽帧、ImageHash 去重，不依赖 `.NET` 或 `ffmpeg`。

#### 验证安装

```bash
python --version
```

## Python依赖

```bash
# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# 安装依赖
pip install opencv-python-headless pillow ImageHash
```

### 依赖说明

| 包 | 版本 | 用途 |
|---|------|------|
| `opencv-python-headless` | >=4.8.0 | 打开视频并按目标 fps 抽帧 |
| `pillow` | >=10.0.0 | 图像读取 |
| `ImageHash` | >=4.3.0 | 计算相邻帧 pHash，相似度去重 |

### 开发依赖（可选）

```bash
pip install pytest
```

| 包 | 版本 | 用途 |
|---|------|------|
| `pytest` | >=7.0.0 | 单元测试 |

## 额外说明

- Linux 环境推荐使用 `opencv-python-headless`，避免桌面图形依赖问题。
- 如果你已有项目虚拟环境，直接在该环境中安装上述依赖即可。
