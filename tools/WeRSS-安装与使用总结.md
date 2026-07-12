# WeRSS（we-mp-rss）安装与使用总结

> 本文件由安装过程自动生成，记录了工具的理解、完整安装步骤，以及如何用它分析
> **刘润 / 洞见 / 粥左罗** 三个微信公众号。

---

## 一、这个工具是什么

**WeRSS（we-mp-rss）** 是一个「微信公众号 RSS 订阅助手」，用于**抓取、管理微信公众号内容并生成 RSS 订阅源**。

- 仓库地址：https://github.com/rachelos/we-mp-rss
- 许可协议：MIT
- 技术架构（前后端分离）：
  - 后端：Python 3 + FastAPI（本次实际用 Python 3.12 运行）
  - 前端：Vue 3 + Vite（仓库已内置**编译好的前端**到 `static/`，无需 Node 也能用）
  - 数据库：默认 SQLite（可选 MySQL / PostgreSQL）
  - 抓取引擎：搜索/列表均为微信 HTTP 接口（`requests`，默认 `gather.model=web`，也可切 `app`/`api`）；仅**正文全文抓取**与 **PDF 导出** 会用到 Playwright/WebKit 浏览器

### 核心能力
- 微信公众号文章抓取与解析、生成 RSS 订阅源
- Web 管理界面（登录、扫码授权、添加订阅、主题切换等）
- 定时自动更新、授权到期提醒、自定义通知渠道（钉钉/企业微信/飞书/自定义 Webhook）
- 文章导出为 **md / docx / pdf / json**
- HTML 内容过滤规则（全局规则 + 指定公众号规则）
- API 接口 + WebHook，支持接入 Folo 等 RSS 客户端

### 工作原理（关键点）
微信没有公开的「按名称搜索公众号并拉取历史文章」的开放接口。WeRSS 的做法是：
**你用一个微信公众平台账号扫码授权 → WeRSS 拿到登录态（Cookie/Token）→ 借此调用微信后台的搜索/图文接口** 来搜索公众号、拉取文章列表和正文。因此「扫码授权」是使用前的必要步骤。

---

## 二、安装到了哪里 / 做了哪些步骤

工具安装在当前工程的子目录：

```
/host/workdir/projects/official-account/we-mp-rss/
```

### 环境事实（本机）
- 无法直连外网，也无法直连 GitHub / PyPI；
- 你提供的 `10.158.101.1:8000` HTTP 代理**不可用**（端口拒绝连接）；
- 探测发现 `10.158.101.1:1080` 为**可用的 SOCKS5 代理**，全程改用它联网。

### 实际执行的步骤
1. **克隆源码**（通过 SOCKS5 代理）
   ```bash
   git -c http.proxy=socks5://10.158.101.1:1080 \
       -c https.proxy=socks5://10.158.101.1:1080 \
       clone --depth 1 https://github.com/rachelos/we-mp-rss.git
   ```

2. **创建 Python 3.12 虚拟环境**
   ```bash
   python3.12 -m venv .venv
   ```

3. **让 pip 能走 SOCKS 代理**：pip 原生不支持 SOCKS，先用 `curl`（支持 SOCKS）下载 `PySocks` whl 并装入 venv，随后 pip 即可用 `--proxy socks5h://...` 联网。

4. **安装后端依赖**
   ```bash
   PIP_CONSTRAINT= .venv/bin/pip install --proxy socks5h://10.158.101.1:1080 -r requirements.txt
   ```
   （fastapi / uvicorn / SQLAlchemy / playwright / bs4 / markitdown 等全部安装成功）

5. **生成配置文件** `config.yaml`（由 `config.example.yaml` 复制，关闭了内置 Redis 服务端以简化启动）。配置支持 `${环境变量:-默认值}` 语法，默认使用 SQLite：`sqlite:///./data/db.db`。

6. **Playwright 浏览器下载**：已成功下载 WebKit 浏览器（142 MB）。
   > 当时只探测到 SOCKS 端口而 Playwright 下载器不支持 SOCKS，曾临时用一个 HTTP→SOCKS 桥完成下载；
   > 现已确认 `10.158.101.1:8080` 为可用 HTTP 代理，后续直接用它即可（`HTTPS_PROXY=http://10.158.101.1:8080`）。

7. **初始化数据库并启动服务验证**
   ```bash
   ./run.sh          # 首次启动，自动建表 + 创建管理员账号
   ```
   验证结果：
   - `GET /` → **HTTP 200**（Web 界面可访问）
   - `POST /api/v1/wx/auth/login`（admin / admin@123）→ **成功返回 JWT Token**
   - 数据库文件已生成：`data/db.db`
   - Uvicorn 正常监听 `http://0.0.0.0:8001`

### 新增/生成的文件
| 文件 | 说明 |
|------|------|
| `we-mp-rss/.venv/` | Python 3.12 虚拟环境（含全部依赖，另装了可选的 `jieba` 用于中文分词） |
| `we-mp-rss/config.yaml` | 运行配置（SQLite、关闭内置 Redis） |
| `we-mp-rss/data/db.db` | 初始化后的数据库（含 admin 账号） |
| `we-mp-rss/run.sh` | 一键启动脚本（新增） |
| `we-mp-rss/tools/wx_login.py` | 纯API扫码授权命令（新增，无需浏览器；见第六节） |
| `we-mp-rss/tools/analyze_accounts.py` | 从文件批量分析公众号的脚本（新增，见第六节） |

> 注：早期为绕过「只探测到 SOCKS 端口」的问题曾新增过 `tools/http2socks.py`（HTTP→SOCKS 桥）。
> 后确认 `10.158.101.1:8080` 是可直接使用的 **HTTP 代理**，已**删除该桥**，`run.sh` 改为直接用 8080。

### 已知限制（重要）
- **WebKit 浏览器无法在本机运行**：本机是 RHEL 系发行版且非 root、无 `apt`，缺少 WebKit 运行所需的 Ubuntu 系统库（`libgtk-3`、`libEGL` 等）。**但它只影响很小一部分功能，不影响搜索/列表/分析。**

  经核对源码，真正用到浏览器（Playwright/WebKit）的只有：
  - **文章正文（全文）抓取**：`driver/wxarticle.py` + `driver/playwright_driver.py`（仅当 `gather.content=True` 且用浏览器渲染正文时）
  - **PDF 导出**：`tools/mdtools/pdf.py`

  **不需要浏览器**的部分（全是 HTTP `requests`）：
  - 搜索公众号 `core.wx.search_Biz`
  - 拉取文章列表 `get_Articles`（`app`/`web` 模式都是 `session.get(...)`）
  - 扫码授权取 Token（走微信 HTTP 接口，非浏览器自动化）
  - 元数据统计分析（读数据库）

  另外 `config.yaml` 中 **`gather.content` 默认就是 `False`**（默认不抓正文），所以正常抓取流程根本不会调用浏览器。

- **批量分析在本机可用**：`tools/analyze_accounts.py` 的分析维度（篇数、时间跨度、每周发文、原创比、标题平均字数、标题高频词、最近标题）都来自**文章列表的元数据**（标题 / 发布时间 / 原创标记），不依赖正文，因此**在本机可正常运行**（前提是已扫码授权拿到 Token）。
  - 只有当你想做**正文级分析**（全文文本、正文关键词、正文字数）时，才需要正文抓取，那部分在本机受 WebKit 限制。
  - 建议本机把 `GATHER.CONTENT_AUTO_CHECK=False`（默认 True，会后台周期性尝试补正文→在本机失败刷日志，但不阻塞主流程）。

- **若确需正文抓取，解决 WebKit 限制的方式**：
  1. **改用官方 Docker 镜像运行**（镜像自带浏览器与系统库）——最省事，见第五节；
  2. 本机用 root 通过 `dnf/yum` 安装浏览器系统库（注意配置默认 `browser_type=firefox`，在 RHEL 上凑齐依赖较麻烦）；
  3. 保持只做**元数据分析**（`GATHER.CONTENT=False`，本机现状即如此）。

- **联网依赖代理**：抓取微信内容必须联网。**代理由你自己配置**，`run.sh`、`tools/*.py` 均**不硬编码代理**；运行前自行：
  ```bash
  export HTTPS_PROXY=http://<代理IP>:<端口>   # 本环境实际用的是 http://10.158.101.1:8080
  export HTTP_PROXY=http://<代理IP>:<端口>
  ```
  脚本会原样继承你设置的这些环境变量。

---

## 三、如何使用它分析公众号（刘润 / 洞见 / 粥左罗）

### 步骤 0：启动服务
```bash
cd /host/workdir/projects/official-account/we-mp-rss
# 先配置代理（run.sh 不硬编码代理，需你自己 export）
export HTTPS_PROXY=http://<代理IP>:<端口>   # 例如本环境：http://10.158.101.1:8080
export HTTP_PROXY=http://<代理IP>:<端口>
./run.sh              # 首次
# 之后再启动可用：./run.sh noinit
```
浏览器访问：`http://<本机IP>:8001/`
默认管理员：**用户名 `admin` / 密码 `admin@123`**（可用环境变量 `USERNAME`/`PASSWORD` 覆盖）。

> 📌 这里的「本机 / `<本机IP>`」= **运行服务的那台机器**。本项目跑在**远程 updev 容器**里
> （容器内网 IP `172.17.0.2`，主机名 `l1sw-env-zhigao-8d33aa32`），服务监听容器内 `0.0.0.0:8001`。
> **不是你自己的 PC**；而且该容器内网 IP 你 PC 一般直连不到，需要做**端口转发**才能在 PC 浏览器打开。

### 步骤 0.5：从你的 PC 访问远程 updev 上的界面（端口转发）

> 先分清**服务端口暴露在哪一层**，方式 A / C 是否直接可用取决于此：
> - **情形①（本项目当前用法）**：用 `./run.sh` 直接在**这个 updev 环境里**跑（venv），VS Code 终端也在同一环境。
>   服务就在**这台环境的 `localhost:8001`**，VS Code 能直接看到，**无需任何额外 docker 操作**。
> - **情形②（另起官方镜像）**：用 `docker run` 单独跑 WeRSS 容器。容器内部的 8001 默认**对外不可见**，
>   必须用 **`-p 8001:8001`** 把它**发布到 updev 宿主机的 `localhost:8001`**，方式 A / C 才能看到它。

**方式 A：VS Code 端口转发（推荐，你正在用 VS Code 远程）**
1. 打开「端口 / PORTS」面板。它和 **终端 TERMINAL** 在同一排标签里（窗口**底部**的面板区）。
   - 如果没看到这个标签：按 `Ctrl+Shift+P`（Mac 用 `Cmd+Shift+P`）打开命令面板 →
     输入并选择 **`Ports: Focus on Ports View`**（或 **`Forward a Port`**）；
   - 或者在底部面板标签栏（PROBLEMS / OUTPUT / TERMINAL 那一排）**右键** → 勾选 **Ports**；
   - 前提：当前窗口是通过 **Remote-SSH / Dev Container / WSL** 连到远程的（左下角有绿色远程标识）。
2. 在 Ports 面板点 **Forward a Port / 转发端口** → 输入 `8001` → 回车。
3. 转发成功后，那一行的 **Local Address** 会显示 `localhost:8001`，点它（或在 PC 浏览器打开
   `http://localhost:8001/`）即可访问。

   **Docker 场景怎么配合方式 A：**
   - **情形①**（就是本项目现在的跑法）：VS Code 转发的 `8001` 正是服务端口，**直接生效，不用改任何东西**。
   - **情形②**（另起 `docker run` 容器）：VS Code 能转发的是 **updev 宿主机的 `localhost:8001`**，
     它**看不到容器内部端口**。所以 `docker run` 必须带 **`-p 8001:8001`** 把端口发布到宿主机，
     VS Code 再转发这个 `8001` 即可。若没写 `-p`，Ports 面板里转发 8001 会连不上。

**方式 B：SSH 隧道**（在你的 PC 上执行）
```bash
# 情形①（服务在 updev 环境本身，等同宿主机 localhost）：
ssh -L 8001:127.0.0.1:8001 <你登录updev的用户名>@<updev宿主机地址>
# 情形②（另起容器且已 -p 8001:8001 发布到宿主机）：同上，指向宿主机 127.0.0.1 即可
ssh -L 8001:127.0.0.1:8001 <你登录updev的用户名>@<updev宿主机地址>
# 情形②但没做 -p 端口发布、只知道容器内网IP时（需宿主机能路由到该容器）：
ssh -L 8001:172.17.0.2:8001 <你登录updev的用户名>@<updev宿主机地址>
```
连上后在 PC 浏览器打开 `http://localhost:8001/`。

**方式 C：直接用 IP**（仅当你 PC 与 updev 网络互通时）
- 容器**内网 IP**（如 `172.17.0.2`）只在 updev 宿主机的 docker 网络内可达，**你 PC 直连不到**，别用它。
- **情形①**：用 updev 宿主机在你 PC 网段上的可达 IP → `http://<updev宿主机IP>:8001/`
  （前提：服务 `0.0.0.0:8001` 已监听在宿主机、且宿主机防火墙放行 8001）。
- **情形②**：`docker run` 带 `-p 8001:8001` 后，同样用 `http://<updev宿主机IP>:8001/`
  （`-p` 已把容器端口发布到宿主机；不带 `-p` 则外部无法访问）。

> 说明：下文所有 `http://<本机IP>:8001/...`（含二维码 `…/static/wx_qrcode.png`、RSS 地址等）
> 在远程场景下都要经上面的转发才能在 PC 打开；或改用「直接查看容器内文件」的方式（见第六节看二维码）。

### 步骤 1：扫码授权（关键前提）
登录后台后，进入「**扫码授权**」页面，用**微信公众平台账号**扫码授权。
> 只有完成授权，WeRSS 才拿到微信登录态，才能「搜索公众号 / 拉取文章」。
> 未授权时，搜索/抓取会提示「请先扫码登录公众号平台 / 请重新扫码授权」。

**是否需要先“关注”这三个公众号？——不需要。**
- 授权登录的是**你自己的微信公众平台账号**（`mp.weixin.qq.com`）。你只要拥有/能管理**任意一个公众号**即可（个人免费注册的**订阅号**就行），扫码用的微信必须是该公众号的**管理员/运营者**。
- 登录后 WeRSS 借用平台后台的「搜索 + 引用文章」接口，可搜索并抓取**任意**公众号（刘润/洞见/粥左罗）的历史文章，**与你是否关注它们无关**。

**前提：需自备一个公众号（免费订阅号即可）用于扫码登录。**
- WeRSS 授权登录的是**微信公众平台后台**（`mp.weixin.qq.com`），该后台只对**已注册公众号的管理员/运营者**开放，因此你**必须拥有（或能管理）至少一个公众号**。
- 用**个人主体的订阅号（免费）**即可，无需认证服务号。注册：`mp.weixin.qq.com` → 立即注册 → 选「订阅号」→ 个人实名（身份证）。
- 这个号**发不发文章、有没有粉丝都无所谓**，它只用于登录后台、借用后台接口；与是否关注目标公众号无关。

> ⚠️ 别把两个“订阅/关注”搞混（它们是**不同层面**的事）：
> - **微信里的“关注”**：用个人微信在微信 App 里 follow 公众号 —— **本工具不需要**。
> - **WeRSS 里的“添加订阅”（下方步骤 2）**：在 WeRSS 应用内部把公众号登记进它的抓取列表（写数据库 `feeds` 表），好让 WeRSS 去替你抓它的文章 —— 这是**软件内的动作，跟微信关注无关**。
>
> 一句话：**不用在微信里关注它们，但要在 WeRSS 里“添加订阅”它们**（手动加或用第六节的批量脚本自动加）。

> 本机（WebKit 不可用）请用下方第六节「完整执行步骤」里的**纯 API 扫码方式**授权；后台页面的「扫码授权」按钮走的是浏览器自动化（`driver/wx.py`），在本机可能失败。

### 步骤 2：搜索并添加这三个公众号（这是 WeRSS 内的“添加订阅”，非微信关注）
在「**添加订阅**」页面依次搜索并添加：**刘润**、**洞见**、**粥左罗**。
添加时选择正确的账号（注意同名，认准头像/简介）。添加后系统会自动抓取最近 `max_page` 页（默认 5 页）历史文章入库。

对应 API（也可脚本化，`{token}` 为登录返回的 access_token）：
```bash
BASE=http://127.0.0.1:8001/api/v1/wx

# 1) 登录拿 token
TOKEN=$(curl -s -X POST $BASE/auth/login \
  -d "username=admin&password=admin@123" \
  | python3 -c "import sys,json;print(json.load(sys.stdin)['data']['access_token'])")

# 2) 搜索公众号（需已扫码授权）
curl -s "$BASE/mps/search/刘润"  -H "Authorization: Bearer $TOKEN"
curl -s "$BASE/mps/search/洞见"  -H "Authorization: Bearer $TOKEN"
curl -s "$BASE/mps/search/粥左罗" -H "Authorization: Bearer $TOKEN"

# 3) 添加公众号（把搜索结果里的 mp_name / mp_id / avatar 等回填）
curl -s -X POST "$BASE/mps" -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"mp_name":"刘润","mp_id":"<搜索结果里的id>","avatar":"<头像url>","mp_intro":"<简介>"}'
```

### 步骤 3：获取文章 / 订阅 RSS
- 后台「文章列表」按公众号筛选查看已抓取文章。
- 每个公众号都有独立 RSS 源，可在 RSS 客户端（如 Folo）订阅：
  ```
  # RSS 订阅列表
  GET  http://<本机IP>:8001/api/v1/wx/rss
  # 某公众号的文章 RSS（feed_id 为添加后返回的公众号 id，如 MP_WXS_xxx）
  GET  http://<本机IP>:8001/api/v1/wx/rss/{feed_id}
  # 手动刷新并抓新文章
  GET  http://<本机IP>:8001/api/v1/wx/rss/{feed_id}/fresh
  ```

### 步骤 4：导出用于分析
后台支持将文章批量导出为 **md / docx / pdf / json**（`导出` 功能，对应 `/api/v1/wx/export/...`）。
把三个号的文章导出为 JSON/Markdown 后，即可做进一步的内容分析（选题分布、发文频率、标题风格、高频词等）。

### 步骤 5（可选）：内容清洗
在「过滤规则」里为这三个号配置 HTML 过滤规则（去广告位、推荐位、引导关注块等），让抓取到的正文更干净，便于后续文本分析。

---

## 四、常用运维命令速查

```bash
cd /host/workdir/projects/official-account/we-mp-rss

# 启动 / 重启（首次会初始化 DB）
./run.sh
./run.sh noinit          # 已初始化后启动，不重复初始化

# 停止服务（最简单）
pkill -f "main.py -job"   # 停掉 WeRSS；前台运行时也可在其终端按 Ctrl+C

# 查看日志
tail -f /tmp/werss.log            # 服务日志

# 临时给某条命令设置代理（HTTP 代理，直接用 8080）
export HTTPS_PROXY=http://10.158.101.1:8080 HTTP_PROXY=http://10.158.101.1:8080

# 补装/更新依赖
HTTPS_PROXY=http://10.158.101.1:8080 .venv/bin/pip install <包名>
```

### 常见问题：能打开网页但登录失败 / 端口转发是否成功

**现象**：PC 浏览器能打开 `localhost:8001` 页面，但用 admin 登录没反应。
**原因**：多半是**后端服务没在跑**（例如被停掉/崩了）。页面是 Vue 单页应用，被**浏览器缓存**了所以还能显示，但登录要调后端 API，后端不在就失败。

**排查/验证步骤：**
1. **先在 updev 上确认服务在跑、且登录正常**（在容器里执行）：
   ```bash
   pgrep -af "main.py -job"                       # 有输出=在跑
   ss -ltn | grep :8001                           # 有 LISTEN=端口在监听
   curl -s -X POST http://127.0.0.1:8001/api/v1/wx/auth/login \
     -d "username=admin&password=admin@123" | head -c 120   # 返回 access_token=后端正常
   ```
   若没在跑：`./run.sh noinit`（或 `nohup ./run.sh noinit > /tmp/werss.log 2>&1 &`）重新启动。

2. **在你 PC 上验证“端口是否真的转发过来了”**（PC 终端执行）：
   ```bash
   curl -i http://localhost:8001/                 # 返回 HTTP/1.1 200 + uvicorn 响应头 = 转发成功且后端在跑
   # 直接测登录接口：
   curl -s -X POST http://localhost:8001/api/v1/wx/auth/login -d "username=admin&password=admin@123"
   ```
   - 返回 **200 / access_token** → 转发正常、后端正常，问题只是页面缓存 → **强制刷新**浏览器（`Ctrl+Shift+R` / Mac `Cmd+Shift+R`）再登录。
   - 返回 **Connection refused / 无法连接** → 端口**没转发过来**或**后端没跑**：
     - 看 VS Code 底部 **PORTS** 面板里 `8001` 那行是否还在（服务停了时**自动转发会消失**，需重开服务后重新转发）；
     - 确认第 1 步里 updev 上的服务确实在跑。
   - 返回 **Connection was reset（连接被重置）** → 转发通道存在但**转发条目已失效/陈旧**（常见于服务重启过几次后）。后端其实正常，需**重建转发**：
     - PORTS 面板 → `8001` 那行 **右键 → Stop Forwarding Port** 删除 → 再 **Forward a Port** 输入 `8001` 重新转发；
     - 若仍 reset，可能 PC 本地 8001 被占用：改用别的本地端口（转发时用 `8002:8001`，访问 `http://localhost:8002/`），或在 PC 上 `netstat -ano | findstr :8001` 查占用；
     - 兜底用 SSH 隧道：`ssh -L 8002:127.0.0.1:8001 <用户名>@<updev地址>` 后访问 `http://localhost:8002/`。

3. **浏览器里更直观的判断**：按 `F12` → **Network（网络）** 面板 → 点登录 → 看 `auth/login` 这条请求：
   - 状态 `200` = 后端正常（多半是缓存/前端问题，强刷即可）；
   - `(failed) ERR_CONNECTION_REFUSED` / `502` / `504` = 转发断了或后端没跑。

> 关键点：**VS Code 的端口转发是跟着“运行中的服务”走的**。一旦 `main.py` 停止，转发通常会自动消失，
> 你再打开 `localhost:8001` 看到的其实是浏览器缓存的旧页面 → 表现为“能打开、登不上”。
> 解决：先在 updev 重新启动服务，必要时在 PORTS 面板重新转发 8001，再强刷浏览器。

### 端口与账号
- Web / API 端口：**8001**
- 默认管理员：**admin / admin@123**
- 配置文件：`config.yaml`（数据库、端口、抓取页数 `max_page`、RSS 参数等都在这里）

---

## 五、可选：用官方 Docker 镜像（若本机装了 Docker，最省事）
README 推荐方式，可一并解决 WebKit 系统库问题：
```bash
docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data \
  ghcr.io/rachelos/we-mp-rss:latest
# 国内加速镜像：
# docker run -d --name we-mp-rss -p 8001:8001 -v ./data:/app/data docker.1ms.run/rachelos/we-mp-rss:latest
```

---

## 五之补充：在 Docker 外（宿主机 / 另一台机器）直接运行

WeRSS 代码本身**不依赖 docker**（就是 Python + SQLite + HTTP）。但**容器里造好的 `.venv` 不能直接搬到宿主机用**，原因有两点：

1. **venv 里的 python 是软链接**，指向容器的解释器：
   `.venv/bin/python → python3.12 → /usr/bin/python3.12`。
   宿主机若没有同路径的 `/usr/bin/python3.12`，执行就报 `No such file or directory`（“文件在”只是链接文件在，目标不在）。
2. **venv 是“瘦”的**，真正依赖的东西都在 venv 外的系统目录：解释器二进制、运行时库
   `libpython3.x.so`、整套标准库 `/usr/lib*/python3.x`。所以**只把软链接换成拷贝也没用**——
   宿主机得有一整套可用的 Python。

另外容器路径 `/host/workdir/...` 与宿主机路径（如 `/var/work/...`）不同，venv 里写死的绝对路径也对不上。

### 正确做法：在宿主机**重建 venv**（数据无需重来）
数据文件（`config.yaml`、`data/db.db`）在同一目录里、跨机器/跨 Python 版本通用，**不用重装依赖之外的东西、不用重新扫码登录**。

```bash
cd <宿主机上的 we-mp-rss 目录>        # 例如 /var/work/zhigao/projects/official-account/we-mp-rss

# 1) 确认宿主机的 Python（3.11/3.12 均可；本项目在 3.11、3.12 上都能跑）
python --version            # 例如 pyenv 提供的 3.11.7
# 或 which python3.12 / python3.11

# 2) 删掉容器造的 venv，用宿主机 Python 重建
rm -rf .venv
python -m venv .venv        # 用当前 python（如 pyenv 的 3.11.7）
# 若要精确对齐 3.12：pyenv install 3.12.13 && pyenv local 3.12.13 && python -m venv .venv

# 3) 装依赖（先确认宿主机能连代理）
curl -x http://10.158.101.1:8080 -sI https://mp.weixin.qq.com | head -1   # 通=有 HTTP/1.1 200/302
HTTPS_PROXY=http://10.158.101.1:8080 .venv/bin/pip install -r requirements.txt

# 4) 启动（已初始化过，用 noinit）
./run.sh noinit
```

> 关于 `./run.sh` 与 `./run.sh noinit`：
> - **首次**不加参数 → `-init True`：建表 + 创建管理员（`data/db.db` 不存在时必须）。
> - **之后**加 `noinit` → `-init False`：跳过初始化，直接启动，**更快更干净**（避免重复建表/复位 admin）。

### “可搬运的 Python”做法（宿主机没装 Python 时）
若宿主机压根没有可用 Python，最省心的是用 **standalone 版 Python**（自带 libpython+标准库、单目录可搬）：
下载 [python-build-standalone](https://github.com/astral-sh/python-build-standalone) 的 3.12 包 → 解压到任意目录 →
用它 `.../bin/python3.12 -m venv .venv` 建环境即可。（有 pyenv 的话直接 `pyenv install 3.12.x` 更简单。）

### 注意事项
- **别容器内、宿主机同时各跑一个**：二者共享同一个 `data/db.db` 和 `8001` 端口，会**端口冲突 + SQLite 争锁**。一次只跑一个。
- **代理可达性可能不同**：容器里 `10.158.101.1:8080` 通，宿主机不一定通，装依赖/抓取前先用上面的 `curl -x` 测一下。
- **同一目录才通用**：宿主机与容器是同一份 bind mount 才共享数据；若是拷贝出来的另一份目录，则是各自独立的数据库。

---

## 六、批量分析脚本（新增：从文件一键分析多个公众号）

为满足「把要分析的公众号写进一个文件、直接跑脚本分析」的需求，新增了脚本
[we-mp-rss/tools/analyze_accounts.py](we-mp-rss/tools/analyze_accounts.py)。
项目原本只有 `tools/import.py`（仅批量导入订阅，不抓文章、不做分析），新脚本把
**搜索订阅 → 抓取文章 → 统计分析 → 生成报告** 串成一条龙。

### 前提
1. 已在后台完成 **扫码授权**（否则搜索/抓取会失败）。
2. 已设置代理环境变量（**需你自己 export**；`run.sh` 与 `tools/*.py` 都不硬编码代理）：
   ```bash
   export HTTPS_PROXY=http://<代理IP>:<端口>   # 例如本环境：http://10.158.101.1:8080
   export HTTP_PROXY=http://<代理IP>:<端口>
   ```

> ✅ 本脚本的分析均基于**文章元数据**（标题/发布时间/原创标记），**不需要浏览器**，在本机（WebKit 不可用）也能正常跑。仅当你要分析**正文全文**时才需要浏览器（见第二节「已知限制」）。

### 输入文件格式
每行一个公众号名称（支持制表符分隔取第一列，`#` 开头为注释）。已生成示例
`we-mp-rss/data/accounts.txt`：
```
刘润
洞见
粥左罗
```

### 使用方法
```bash
cd /host/workdir/projects/official-account/we-mp-rss
# 完整流程：搜索+订阅+抓取+分析（每号默认抓 config 里的 max_page 页）
.venv/bin/python tools/analyze_accounts.py data/accounts.txt

# 常用选项
.venv/bin/python tools/analyze_accounts.py data/accounts.txt --max-page 5
.venv/bin/python tools/analyze_accounts.py data/accounts.txt --no-gather      # 只分析已入库文章，不联网抓取
.venv/bin/python tools/analyze_accounts.py data/accounts.txt --top-keywords 30
```

### 完整执行步骤（含扫码授权，本机无浏览器适用）

如果你直接跑脚本遇到「请先扫码登录公众号平台」，是因为**还没拿到微信登录态**。按下面顺序做一遍即可：

**准备：一次性说明**
- 你需要一个**自己的微信公众平台账号**（能管理任意一个公众号；个人免费**订阅号**即可），扫码的微信要是它的**管理员/运营者**。
- **不需要关注**刘润/洞见/粥左罗；授权后可搜索并抓取任意公众号。

**① 设置代理（抓取必须联网）**
```bash
cd /host/workdir/projects/official-account/we-mp-rss
export HTTPS_PROXY=http://10.158.101.1:8080
export HTTP_PROXY=http://10.158.101.1:8080
export NO_PROXY=127.0.0.1,localhost
```

**② 纯 API 方式扫码授权（不需要浏览器，本机可用）—— 已固化为脚本 `tools/wx_login.py`**
> 网页那个「扫码授权」按钮走浏览器（`driver/wx.py`），在无浏览器机器上会卡在“正在获取二维码”，**别用**。
> 用下面这个纯 API 脚本（`driver.wx_api`）；它已处理好「等后台把 token 写完 + 兜底手动持久化」，避免拿不到 token。
```bash
cd /host/workdir/projects/official-account/we-mp-rss
export HTTPS_PROXY=http://10.158.101.1:8080 HTTP_PROXY=http://10.158.101.1:8080 NO_PROXY=127.0.0.1,localhost
.venv/bin/python tools/wx_login.py          # 生成二维码 -> static/wx_qrcode.png，等你扫码
# 可选：.venv/bin/python tools/wx_login.py --timeout 300
```
脚本流程：申请二维码 → 阻塞等你扫码确认 → 等后台抓全 token/cookie 并持久化（Redis + `data/wx.lic`）→
打印 `🎉 授权成功，token 已持久化：…`。**若服务在后台运行，不用重启即可生效。**

**如何看二维码**：
- 直接打开文件 `we-mp-rss/static/wx_qrcode.png`；
- 或先 `./run.sh` 启动服务，用浏览器访问 `http://<本机IP>:8001/static/wx_qrcode.png`。
- 注意：**登录成功后二维码文件会被自动删除**（正常现象）。

> 关于持久化位置：开了内置 Redis 时，token 优先存 Redis，服务读取也优先读 Redis，所以
> `cat data/wx.lic` 可能仍是 `{}` —— **不代表没授权**。用
> `.venv/bin/python -c "from driver.token import get; print(get('token'))"` 打印出非空即已授权。
> 若想让 token 落地到本地文件（重启不丢），可把 `config.yaml` 的 `redis.server.enabled` 设为 `False`。

**这一步到底“谁在跟 mp.weixin.qq.com 通信”？（重要，先看懂再操作）**
- **不需要任何浏览器**：API 方式下，是**运行脚本/服务的那台机器（本机或容器）用 HTTP `requests`（经代理）**去 mp.weixin.qq.com 申请二维码、并轮询扫码状态。本机/容器里都**不用装、不用跑浏览器**。
- **“登录 mp.weixin.qq.com”发生在你的手机上**：你用**手机微信**（某公众号的管理员/运营者）扫那张二维码图片并在手机确认，登录动作是手机微信和微信服务器之间完成的。手机用自己的普通网络即可，**不需要代理、也不需要和服务器同一网络**。
- **登录态存在“谁跑脚本谁那里”**：授权成功后 token/cookie 写入**运行脚本的那台机器/容器**的 `data/wx.lic`。所以：脚本在本机跑 → 登录态在本机；脚本在容器跑 → 登录态在容器。

**如果脚本在 Docker 中执行：**
- 容器需要能（经代理）访问 `mp.weixin.qq.com`（只是 **HTTP 请求**，不是浏览器）。给容器设代理即可，例如：
  ```bash
  docker run -d --name we-mp-rss -p 8001:8001 -v $PWD/data:/app/data \
    -e HTTPS_PROXY=http://10.158.101.1:8080 -e HTTP_PROXY=http://10.158.101.1:8080 \
    -e NO_PROXY=127.0.0.1,localhost ghcr.io/rachelos/we-mp-rss:latest
  ```
- **不需要在容器里放浏览器**（API 方式无浏览器）。二维码文件在容器内 `/app/static/wx_qrcode.png`，查看方式二选一：
  - 映射了 `8001` 端口后，浏览器打开 `http://<容器宿主机IP>:8001/static/wx_qrcode.png`；
  - 或 `docker cp we-mp-rss:/app/static/wx_qrcode.png .` 拷出来再打开。
- 然后照样用**手机微信扫这张图**、手机确认即可；登录态会写进容器里（挂载了 `-v .../data` 就能持久化）。
- ⚠️ 只有当你改用 `server.auth_web=True` 的**浏览器登录方式**时，才会在容器内跑一个**无头浏览器**去打开 mp.weixin.qq.com（官方镜像自带浏览器与系统库）——即便那样，浏览器也是在**容器内无头运行**，你依然是用**手机**扫码，而不是在容器里手动点网页。本机（WebKit 缺库）不建议用这种方式，用上面的 API 方式即可。

**③ 确认授权成功**
```bash
cat data/wx.lic        # 不再是 {}，而是包含 token/cookie 的内容即表示成功
```

**④ 运行批量抓取 + 分析**
```bash
.venv/bin/python tools/analyze_accounts.py data/accounts.txt
# 或指定抓取页数（每页≈5篇）：
.venv/bin/python tools/analyze_accounts.py data/accounts.txt --max-page 10
```
脚本会依次：搜索每个公众号 → 未订阅则加入 → 抓取最近若干页文章入库 → 统计分析 → 在
`data/analysis/` 生成 md + json 报告。

> 提示：授权是有有效期的（微信登录态会过期）。以后再抓取若又提示需要登录，重复第 ② 步即可。
> 抓取过程有防频控延时（每篇/每页随机等待），抓多个号时属正常，请耐心等待。

### ⚠️ 宿主机 / 无浏览器环境的重要提醒（含“搜不出结果 / 看不到二维码”排查）

在没有可用浏览器的机器（本容器、或宿主机未装 Playwright 浏览器）上，**只有纯 API 路径能用**：

1. **搜索公众号一定要用「按名称」搜**（`/mps/search/{kw}`，纯 `requests`）。
   **不要用「按文章链接」搜**（`/mps/by_article`）——它会启动浏览器抓正文，报
   `BrowserType.launch: Executable doesn't exist ... playwright install`。这属预期，换用按名称搜即可。

2. **「按名称搜索没反应、命令行也不打印」= 还没做微信扫码授权。**
   注意区分：WeRSS 后台的 **admin 登录** ≠ **微信扫码授权**。`search_Biz` 在没有微信 token 时会直接
   “请先扫码登录公众号平台”并返回空。**判断方法**：`cat data/wx.lic`，若是 `{}` 就是没授权。

3. **网页上的「扫码授权」按钮走浏览器**（`driver/wx.py`），在无浏览器机器会失败。
   **必须改用第 ② 步的纯 API 命令**（`driver.wx_api.get_qr_code`）来授权。

4. **看不到 `static/wx_qrcode.png` 的常见原因**：
   - 你其实没真正运行第 ② 步那条 API 命令（只点了网页按钮）——网页按钮不会生成这个文件；
   - 没在 `we-mp-rss` 目录内运行（二维码按**当前工作目录**的相对路径 `static/wx_qrcode.png` 保存）；
   - `static/wx_qrcode.png` 已存在：源码里 `check_lock()` 实际判断的是**这个 png 是否存在**，存在就返回
     “请勿重复运行”、不再生成 → 先 `rm -f static/wx_qrcode.png` 再重跑；
   - 命令返回的 `code` 为 None / 报请求错误：多半是该机器没走通代理，先
     `curl -x http://10.158.101.1:8080 -sI https://mp.weixin.qq.com | head -1` 测通再跑。

5. **想消除后台反复刷的浏览器错误日志**：把 `GATHER.CONTENT_AUTO_CHECK` 设为 `False`
   （默认 True，会周期性尝试用浏览器补正文，在无浏览器机器上只会刷错误，不影响搜索/列表/分析）。

6. **添加了多个公众号，却只显示第一个的文章**：经核实，**后端正常**——
   每个号的文章都已入库，`GET /api/v1/wx/articles?mp_id=<号ID>` 对每个号都能正确返回。
   所以这是**前端/浏览器缓存**的展示问题，试：
   - 浏览器**强制刷新** `Ctrl+Shift+R`；
   - 在侧栏重新点选每个公众号；
   - `F12 → Network` 看切换公众号时的 `articles?mp_id=...` 请求：mp_id 是否随之变化、响应 `total` 是否>0；
   - 验证后端（任意机器）：登录拿 token 后
     `curl "http://<IP>:8001/api/v1/wx/articles?mp_id=<号ID>&limit=2" -H "Authorization: Bearer <token>"`，
     能返回就说明只是前端展示问题。

### 参数说明

**`--max-page N`：抓取的「页数」，不是文章条数。**
- 微信后台接口 `appmsgpublish` 是**分页返回**的，脚本里每页固定 `count = 5` 篇
  （见 [core/wx/model/app.py](we-mp-rss/core/wx/model/app.py) 的 `get_Articles`）。
- 因此 `--max-page N` 表示最多翻 `N` 页，约等于 **`5 × N` 篇文章**（如 `--max-page 5` ≈ 25 篇）。
- 「页」的定义 = 接口一次请求返回的一批文章，`begin = 页号 × 5` 作为偏移量向后翻页。
- 实际条数可能少于 `5 × N`：翻到没有更多文章、或触发微信频率控制（ret=200013）时会提前停止。
- 不传 `--max-page` 时，取 `config.yaml` 里的 `max_page`（默认 **5 页 ≈ 25 篇**）。

**抓取顺序：始终「从最新到最旧」。**
- 接口默认 `begin=0` 返回最新一批，脚本按 `0,1,2…` 递增翻页，即**先抓最新、再往历史翻**。
- 这个顺序与 `--top-keywords` 无关，也不受它影响——`--top-keywords` 只作用于「分析报告」，不参与抓取。

**`--top-keywords N`：报告里展示的「标题高频词」数量（Top N）。**
- 含义是：把所有标题分词后按出现频次排序，**取最靠前的 N 个词**展示（`most_common(N)`）。
- **不是**「标题中包含高频词的个数」，而是「列出多少个高频词」。例如 `--top-keywords 30` = 展示前 30 个最常出现的词。
- 不传时默认 **20**。该参数只影响报告输出的详略，不影响抓取数量或顺序。

### 输出
在 `we-mp-rss/data/analysis/` 下生成带时间戳的两份报告：
- `analysis_YYYYmmdd_HHMMSS.md`（可读报告）
- `analysis_YYYYmmdd_HHMMSS.json`（结构化数据，便于二次处理）

每个公众号的分析维度：
- 文章总数、时间跨度（最早/最新/天数）
- 平均每周发文量
- 原创占比（基于 `copyright_stat`）
- 标题平均字数
- **每月发文数分布**
- **标题高频词 Top N**（优先用 `jieba` 分词；未安装则退回中文二字词统计）
- 最近 10 篇标题

### 实现要点（复用项目既有能力，未改动原有源码）
- 搜索：`core.wx.search_Biz`
- 订阅入库：写 `core.models.feed.Feed`（逻辑与 `apis/mps.py::add_mp` 一致）
- 抓取：`core.wx.WxGather().Model().get_Articles(..., CallBack=jobs.article.UpdateArticle)`
- 统计：直接查 `core.models.article.Article` 表聚合
- 分词：可选依赖 `jieba`（已装；缺失时脚本自动降级，不报错）

> 说明：`jieba` 属可选增强，未写入 `requirements.txt`；如需在别的环境复现更好的分词，
> 执行 `HTTPS_PROXY=http://10.158.101.1:8080 .venv/bin/pip install jieba` 即可。
