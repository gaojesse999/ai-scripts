# baoyu-post-to-wechat 使用说明

> 本文档介绍 Cursor Skill `baoyu-post-to-wechat` 的功能、前置条件与完整使用流程。  
> Skill 路径：`.cursor/skills/baoyu-post-to-wechat/`

---

## 第一章 功能概述

`baoyu-post-to-wechat` 是一个面向**微信公众号（WeChat Official Account）**的发布自动化 Skill。它帮助你将 Markdown、HTML 或纯文本内容，转换为公众号可用的格式，并通过 **API** 或 **Chrome 浏览器自动化** 两种方式保存为草稿。

### 1.1 能做什么

| 能力 | 说明 |
|------|------|
| 文章发布（文章） | 支持 Markdown / HTML / 纯文本，带主题样式、封面图、摘要等元数据 |
| 贴图发布（贴图，原「图文」） | 短内容 + 多图（最多 9 张），适合朋友圈式图文消息 |
| Markdown 转 HTML | 将 Markdown 转为公众号编辑器兼容的 HTML，含代码高亮与主题 |
| 环境自检 | 检查 Chrome、Bun、API 凭证、剪贴板等依赖是否就绪 |

### 1.2 触发方式

在 Cursor 对话中提及以下关键词时，Agent 会自动启用该 Skill：

- 「发布公众号」
- 「post to wechat」
- 「微信公众号」
- 「贴图 / 图文 / 文章」

也可在对话中显式调用：`/baoyu-post-to-wechat`

---

## 第二章 两种发布模式对比

### 2.1 贴图（Image-Text）

适用于**短内容 + 多图**场景（最多 9 张图）。

- 需要 Chrome 浏览器
- 不需要 API 凭证
- 不支持主题样式
- 标题最长 20 字，正文最长 1000 字（超长会自动压缩）

### 2.2 文章（Article）

适用于**长文、带排版**的公众号文章。

| 子方式 | 速度 | 需要 Chrome | 需要 API 凭证 | 特点 |
|--------|------|-------------|---------------|------|
| **API（推荐）** | 快 | 否 | 是 | 支持评论开关、封面图、主题配色 |
| **Browser** | 慢 | 是 | 否 | 通过浏览器粘贴 HTML，需扫码登录 |

### 2.3 功能对照表

| 功能 | 贴图 | 文章（API） | 文章（Browser） |
|------|------|-------------|-----------------|
| 纯文本输入 | ✗ | ✓ | ✓ |
| HTML 输入 | ✗ | ✓ | ✓ |
| Markdown 输入 | 仅标题/正文 | ✓ | ✓ |
| 多图 | ✓（最多 9 张） | ✓（文内插图） | ✓（文内插图） |
| 主题样式 | ✗ | ✓ | ✓ |
| 自动生成标题/摘要 | ✗ | ✓ | ✓ |
| 默认封面回退 | ✗ | ✓ | ✗ |
| 评论控制 | ✗ | ✓ | ✗ |

---

## 第三章 前置条件

### 3.1 通用依赖

- **Bun 运行时**：脚本通过 `bun` 执行  
  安装：`curl -fsSL https://bun.sh/install | bash`
- **脚本依赖**：首次使用前在 skill 目录执行  
  `cd .cursor/skills/baoyu-post-to-wechat/scripts/md && bun install`

### 3.2 API 方式额外要求

- 微信公众号 **AppID** 与 **AppSecret**（官方免费提供，**不需要购买第三方 API Key**）
- 在 [微信开发者平台](https://developers.weixin.qq.com/console) 获取后，写入 `.baoyu-skills/.env`（详见 **第四章 4.2**）

### 3.3 浏览器方式额外要求

- 安装 **Google Chrome**
- 首次运行需扫码登录公众号后台（会话会保留）
- Linux 可选：`xdotool`（X11）或 `ydotool`（Wayland），用于粘贴快捷键

### 3.4 环境自检（可选）

```bash
SKILL_DIR=".cursor/skills/baoyu-post-to-wechat"
npx -y bun ${SKILL_DIR}/scripts/check-permissions.ts
```

---

## 第四章 首次配置

**推荐配置顺序**：

1. **4.1** 配置 `EXTEND.md`（发布偏好，含 `default_publish_method`）
2. **4.2** 若选择 `api` 发布，配置并验证 `.env` 中的 API 凭证
3. **4.3** 注意安全，勿将 `.env` 提交到 Git

### 4.1 配置 EXTEND.md

`EXTEND.md` 用于保存发布偏好（主题、配色、发布方式、作者、评论开关等）。Skill 按以下优先级查找：

| 优先级 | 路径 | 作用域 |
|--------|------|--------|
| 1 | `.baoyu-skills/baoyu-post-to-wechat/EXTEND.md` | 当前项目 |
| 2 | `~/.baoyu-skills/baoyu-post-to-wechat/EXTEND.md` | 所有项目 |

若不存在，Agent 会引导你完成**首次设置**，再进入发布流程。

#### 首次生成（三选一）

| 方式 | 说明 |
|------|------|
| **命令行创建（推荐）** | 在项目根目录执行下方命令，按需修改字段 |
| **手动创建** | 按路径新建文件，内容参考下方**推荐示例** |
| **对话式引导** | 不提前创建也行；首次说「发布公众号」时，Agent 会逐项询问并自动保存 |

```bash
mkdir -p .baoyu-skills/baoyu-post-to-wechat

cat > .baoyu-skills/baoyu-post-to-wechat/EXTEND.md << 'EOF'
default_theme: default
default_color: blue
default_publish_method: api
default_author: 你的名字（推荐使用公众号名称）
need_open_comment: 1
only_fans_can_comment: 0
EOF
```

后续可直接编辑该文件；删除后再次发布，Agent 会重新引导生成。

#### 推荐示例

```md
default_theme: default
default_color: blue
default_publish_method: api
default_author: 你的名字（推荐使用公众号名称）
need_open_comment: 1
only_fans_can_comment: 0
chrome_profile_path: /path/to/chrome/profile
```

> `chrome_profile_path` 为可选项，仅浏览器发布方式需要。

#### 可配置项说明

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `default_theme` | `default` | 主题：`default` / `grace` / `simple` / `modern` |
| `default_color` | 主题默认 | 配色：`blue` / `green` / `red` 等，或十六进制色值 |
| `default_publish_method` | — | 默认发布方式，见下表 |
| `default_author` | 空 | 文章作者署名，推荐使用公众号名称 |
| `need_open_comment` | `1` | 是否开启评论 |
| `only_fans_can_comment` | `0` | 是否仅粉丝可评论 |
| `chrome_profile_path` | — | Chrome 用户数据目录（浏览器发布时需要） |

**`default_publish_method` 可选值**：

| 值 | 说明 |
|----|------|
| `api` | API 发布（推荐，速度快；须先完成 **4.2** 的 API 凭证配置与验证） |
| `browser` | 浏览器自动化发布（需 Chrome + 扫码登录） |

未在 `EXTEND.md` 中指定时，发布流程会询问你选择 `api` 或 `browser`。

### 4.2 配置并验证 API 凭证

#### 说明

API 方式使用的是**你自己微信公众号**在官方平台提供的凭证，不是 OpenAI、阿里云等第三方付费 API。

| 项目 | 说明 |
|------|------|
| **需要什么** | 已注册的微信公众号 + AppID + AppSecret |
| **是否需要购买 API Key** | 否，AppID/AppSecret 在公众平台**免费获取** |
| **可能需要花钱的部分** | 公众号注册/认证本身（如企业认证约 300 元/年），与 API Key 无关 |

#### 获取路径

1. 登录 [微信开发者平台](https://developers.weixin.qq.com/console)
2. 在控制台中进入 **我的业务**，选择 **公众号**
3. 进入对应公众号，在开发配置中复制 **AppID** 和 **AppSecret**（Secret 首次生成后只显示一次，请妥善保存）

#### 配置

**选择存放位置**（二选一）：

| 方式 | 路径 | 适用场景 |
|------|------|----------|
| **项目级（推荐）** | `项目根目录/.baoyu-skills/.env` | 仅当前项目使用 |
| **用户级** | `~/.baoyu-skills/.env` | 所有项目共用 |

**读取优先级**：环境变量 > 项目 `.baoyu-skills/.env` > 用户 `~/.baoyu-skills/.env`

**方式一：命令行创建**（将占位符替换为你的真实值）：

```bash
mkdir -p .baoyu-skills

cat > .baoyu-skills/.env << 'EOF'
WECHAT_APP_ID=你的AppID
WECHAT_APP_SECRET=你的AppSecret
EOF
```

**方式二：手动创建**

在项目根目录新建 `.baoyu-skills/.env`，内容如下：

```env
WECHAT_APP_ID=wx1234567890abcdef
WECHAT_APP_SECRET=你的32位AppSecret
```

格式注意：

- 不要加引号
- `=` 两侧不要空格
- 每行一个变量

#### 验证

在项目根目录执行：

```bash
# 确认文件存在且包含配置项
grep WECHAT_APP_ID .baoyu-skills/.env

# 运行环境检查（可选）
export PATH="$HOME/.bun/bin:$PATH"
SKILL_DIR=".cursor/skills/baoyu-post-to-wechat"
bun ${SKILL_DIR}/scripts/check-permissions.ts
```

若 API 凭证配置正确，`API credentials` 检查项应显示通过。

### 4.3 安全提醒

`.env` 包含敏感信息，**不要提交到 Git**。建议在项目 `.gitignore` 中加入：

```
.baoyu-skills/.env
```

---

## 第五章 文章发布完整流程

以下为 Skill 内置的**文章发布**标准步骤（Agent 会按此 checklist 执行）。

### Step 0：加载偏好

读取 EXTEND.md，解析默认主题、配色、发布方式、作者、评论开关等。  
**若未配置**，须先完成 **第四章 4.1** 的偏好设置；若使用 API 发布，还须完成 **4.2**。

### Step 1：确定输入类型

| 输入类型 | 识别方式 | 处理 |
|----------|----------|------|
| HTML 文件 | 路径以 `.html` 结尾且文件存在 | 跳到 Step 3 |
| Markdown 文件 | 路径以 `.md` 结尾且文件存在 | 进入 Step 2 |
| 纯文本 | 非文件路径或文件不存在 | 保存为 `post-to-wechat/yyyy-MM-dd/[slug].md` 后继续 |

纯文本 slug 示例：

- "Understanding AI Models" → `understanding-ai-models`
- "人工智能的未来" → `ai-future`（英文 kebab-case）

### Step 2：选择发布方式并配置凭证

- 优先使用 EXTEND.md 中的 `default_publish_method`（配置见 **第四章 4.1**）
- 未在 EXTEND.md 中指定时，询问用户选择 `api` 或 `browser`
- 选 API 时检查 `.env` 中是否已配置 `WECHAT_APP_ID`；缺失则引导按 **第四章 4.2** 填写

### Step 3：解析主题与校验元数据

**主题解析优先级**（命中即停，不必再问用户）：

1. CLI 参数 `--theme`
2. EXTEND.md 的 `default_theme`
3. 回退为 `default`

**配色解析优先级**：

1. CLI `--color`
2. EXTEND.md 的 `default_color`
3. 未设置则使用主题默认色

**元数据校验**：

| 字段 | 缺失时处理 |
|------|------------|
| 标题 | 提示输入，或从内容自动生成（首个 H1/H2 或首句） |
| 摘要 | 提示输入，或自动生成（首段截断至 120 字） |
| 作者 | CLI → frontmatter → EXTEND.md `default_author` |

**封面图（API `news` 类型必填）** 查找顺序：

1. CLI `--cover`
2. frontmatter：`coverImage` / `featureImage` / `cover` / `image`
3. 文章目录 `imgs/cover.png`
4. 文内第一张图
5. 仍无则停止，要求用户提供封面

### Step 4：发布到微信

> **重要**：发布脚本内部会处理 Markdown 转换，**不要**事先手动转成 HTML 再传入。

**API 方式**：

```bash
SKILL_DIR=".cursor/skills/baoyu-post-to-wechat"
npx -y bun ${SKILL_DIR}/scripts/wechat-api.ts <file> \
  --theme <theme> \
  [--color <color>] \
  [--title <title>] \
  [--summary <summary>] \
  [--author <author>] \
  [--cover <cover_path>]
```

**浏览器方式**：

```bash
npx -y bun ${SKILL_DIR}/scripts/wechat-article.ts --markdown <file> --theme <theme> [--color <color>]
npx -y bun ${SKILL_DIR}/scripts/wechat-article.ts --html <file>
```

### Step 5：完成报告

发布成功后，Agent 会汇总：输入类型、发布方式、主题、标题、摘要、图片数量、评论设置、草稿 `media_id`（API）及后续管理链接（[微信公众平台草稿箱](https://mp.weixin.qq.com)）。

---

## 第六章 贴图发布用法

贴图适合短文案 + 多图，需 Chrome。

```bash
SKILL_DIR=".cursor/skills/baoyu-post-to-wechat"

# 从 Markdown 提取标题/正文，并上传目录内所有图片
npx -y bun ${SKILL_DIR}/scripts/wechat-browser.ts \
  --markdown article.md \
  --images ./images/

# 显式指定标题、正文与图片
npx -y bun ${SKILL_DIR}/scripts/wechat-browser.ts \
  --title "标题" \
  --content "内容" \
  --image img1.png \
  --image img2.png \
  --submit
```

| 参数 | 说明 |
|------|------|
| `--markdown` | 从 MD 提取标题与正文 |
| `--images` | 图片目录（按文件名排序） |
| `--title` / `--content` | 手动指定（有长度上限） |
| `--image` | 单张图片，可重复 |
| `--submit` | 保存为草稿（默认仅预览） |

---

## 第七章 脚本一览

Skill 目录：`SKILL_DIR=.cursor/skills/baoyu-post-to-wechat`

| 脚本 | 用途 |
|------|------|
| `scripts/wechat-browser.ts` | 贴图发布 |
| `scripts/wechat-article.ts` | 文章发布（浏览器） |
| `scripts/wechat-api.ts` | 文章发布（API） |
| `scripts/md-to-wechat.ts` | Markdown → 公众号 HTML |
| `scripts/check-permissions.ts` | 环境与权限检查 |

### 7.1 Markdown 文章格式示例

```markdown
---
title: 文章标题
author: 作者名
cover: ./imgs/cover.png
---

# 标题

正文段落，支持 **粗体**、*斜体*。

## 小节

![配图说明](./image.png)

> 引用块

- 列表项
```

### 7.2 主题与配色

- **主题**：`default`（经典）、`grace`（优雅）、`simple`（简约）、`modern`（现代）
- **配色预设**：`blue`、`green`、`vermilion`、`yellow`、`purple`、`sky`、`rose`、`olive`、`black`、`gray`、`pink`、`red`、`orange`，或任意 hex 色值

---

## 第八章 配置优先级总览

同一选项多处配置时，生效顺序为：

1. **CLI 命令行参数**（最高）
2. **文件 frontmatter / HTML meta**
3. **EXTEND.md**
4. **Skill 内置默认值**（最低）

API 凭证优先级见 **第四章 4.2**。

---

## 第九章 常见问题

| 问题 | 处理建议 |
|------|----------|
| 缺少 API 凭证 | 按 **第四章 4.2** 配置并验证 `.env` |
| Access Token 错误 | 检查 AppID/AppSecret 是否正确、是否过期 |
| 浏览器未登录 | 首次运行打开 Chrome，扫码登录公众号后台 |
| 找不到 Chrome | 设置环境变量 `WECHAT_BROWSER_CHROME_PATH` |
| 缺少封面图 | 在 frontmatter 指定 cover，或放置 `imgs/cover.png` |
| 评论默认值不对 | 检查 EXTEND.md 中 `need_open_comment`、`only_fans_can_comment` |
| 粘贴失败 | 检查剪贴板权限；Linux 安装 `xdotool` / `ydotool` |
| Bun 未安装 | `curl -fsSL https://bun.sh/install \| bash` |

---

## 第十章 快速上手示例

### 10.1 对话式（推荐）

在 Cursor 中直接说：

```
帮我把这篇文章发布到微信公众号，用 API 方式
文件路径：./my-article.md
```

Agent 会按第五章流程自动处理：读配置 → 校验元数据 → 调用脚本 → 返回草稿结果。

### 10.2 命令行（文章 + API）

```bash
SKILL_DIR=".cursor/skills/baoyu-post-to-wechat"
npx -y bun ${SKILL_DIR}/scripts/wechat-api.ts ./my-article.md \
  --theme grace \
  --color purple \
  --author "作者" \
  --summary "文章摘要"
```

### 10.3 命令行（贴图）

```bash
SKILL_DIR=".cursor/skills/baoyu-post-to-wechat"
npx -y bun ${SKILL_DIR}/scripts/wechat-browser.ts \
  --markdown ./short-post.md \
  --images ./photos/ \
  --submit
```

---

## 附录 相关文件路径

| 类型 | 路径 |
|------|------|
| Skill 主文件 | `.cursor/skills/baoyu-post-to-wechat/SKILL.md` |
| 首次设置说明 | `.cursor/skills/baoyu-post-to-wechat/references/config/first-time-setup.md` |
| 贴图参考 | `.cursor/skills/baoyu-post-to-wechat/references/image-text-posting.md` |
| 文章参考 | `.cursor/skills/baoyu-post-to-wechat/references/article-posting.md` |
| 项目偏好 | `.baoyu-skills/baoyu-post-to-wechat/EXTEND.md` |
| 用户偏好 | `~/.baoyu-skills/baoyu-post-to-wechat/EXTEND.md` |
| API 凭证 | `.baoyu-skills/.env` 或 `~/.baoyu-skills/.env` |
