# 安装指南

## 系统依赖

### Python（必需）

本 skill 使用 Python 完成视频下载、抽帧、去重、合集检测和字幕准备。

#### 验证安装

```bash
python --version
```

## Python 依赖

### 基础依赖（必需）

```bash
# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# 安装基础依赖
pip install opencv-python-headless pillow ImageHash
```

| 包 | 版本 | 用途 |
|---|------|------|
| `opencv-python-headless` | >=4.8.0 | 打开视频并按目标 fps 抽帧 |
| `pillow` | >=10.0.0 | 图像读取 |
| `ImageHash` | >=4.3.0 | 计算相邻帧 pHash，相似度去重 |

## 开发依赖（可选）

```bash
pip install pytest
```

| 包 | 版本 | 用途 |
|---|------|------|
| `pytest` | >=7.0.0 | 单元测试 |

## 额外说明

- Linux 环境推荐使用 `opencv-python-headless`，避免桌面图形依赖问题。
- 当前 skill 的内容理解链路是：**字幕 -> 仅图片**。
- `collection.py` 与 `text_prepare.py` 仅使用 Python 标准库访问 Bilibili 接口与字幕数据。
- 如果你已有项目虚拟环境，直接在该环境中安装上述依赖即可。
