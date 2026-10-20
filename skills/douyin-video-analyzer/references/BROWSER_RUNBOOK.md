# 浏览器操作手册（BROWSER_RUNBOOK）

本手册指导 Agent 执行创作者中心的登录、导出三表与下载视频。
支持两种环境分支：
- **分支 A（豆包/Coze 等内置沙盒环境）**：在 `computer_use_tool(plane="bu")` 里实时执行，遵循 `import aha_browser_use as bu` 操作规范。
- **分支 B（Antigravity 等本地系统级 Agent）**：无原生内置浏览器沙盒，统一调用 `scripts/auto_douyin_sync.py`（基于 Playwright），由系统直接唤起前台 Edge/Chrome 进行全自动导出与 CDN 抓流。

---

## 0. 页面入口

- 数据中心：`https://creator.douyin.com/creator-micro/data-center/operation`
- 作品管理：`https://creator.douyin.com/creator-micro/content/manage`
- 个人主页（下视频用）：`https://www.douyin.com/user/self`
- 单条作品播放页：`https://www.douyin.com/user/self?modal_id=<aweme_id>` 或 `/video/<aweme_id>`

---

## 1. 登录（必须用户扫码）

1. `bu.navigate(数据中心URL)`；`bu.wait_for_load()`；`time.sleep(3)`；`bu.snapshot()`。
2. 若页面是扫码/验证码/密码登录，或 `blocked=auth`：
   - **立刻**调用 `interaction.request_action(type="browserControl")`，
     display_message 写明：「请在浏览器里用抖音 App 扫码登录创作者中心，完成后把控制权交回」。
   - 不要输密码、不要碰验证码。
3. 控制权回来后重新 `bu.snapshot()` / `bu.get_page_text()`，确认能看到数据看板和账号昵称
   （本人账号，如「钩玄纪」），才算登录成功。
4. 登录态在当前浏览器会话内通常持续一段时间；中途过期就重新交接扫码。

---

## 2. 导出三表

### 2.1 数据中心：作品数据 + 粉丝数据（两张按日表）

1. 打开数据中心，等待数据看板加载。
2. 若要完整周期，先找到「自定义时间/日期选择」，设为区间首日到末日（含首尾），应用。
   - 平台每天中午更新前一天数据，分析最近周期时提醒用户当天数据可能未出齐。
3. 页面上「作品数据」与「粉丝数据」两个区域各有一个「导出数据」按钮。
   - 按钮 class 含 `douyin-creator-pc-button`，文案为「导出数据」，同页可能有多个。
   - **稳定定位法（JS 打标，再点 CSS）**：
     ```python
     bu.js("""
       const btns = [...document.querySelectorAll('button, a, span, div')]
         .filter(el => el.textContent.trim() === '导出数据' && el.offsetParent !== null);
       btns.forEach((b, i) => b.setAttribute('data-exp', 'exp' + i));
       return btns.length;
     """)
     bu.snapshot(within="viewport")  # 先观察有几个、分别在哪个区
     # 作品数据区的导出（按需点第 0 个；粉丝区滚动到该区域后再点）
     bu.click(bu.css('[data-exp="exp0"]', match="first"))
     ```
   - 点击后按钮可能短暂 loading，随后直接触发下载，**没有弹窗**。
4. 用 `bu.wait_for_download(timeout=30)` 或下载后检查系统下载目录，确认 xlsx 落盘。
5. 滚动到「粉丝数据」区，对其「导出数据」重复一次。粉丝画像若因粉丝量少未开放，跳过即可。

### 2.2 作品管理：作品列表（全量，16 列）

1. 打开作品管理页，等待作品列表加载。
2. 找到「导出数据」按钮，同样用 JS 打标后点击，直接下载「作品列表导出.xlsx」。
3. 该表是**全量作品**（含区间外的），本地由 `parse_data.py` 按区间筛，无需在页面上筛。
4. 确认下载完成。

### 2.3 归档到周期目录

回到普通 shell，运行：
```powershell
& $py .agents/skills/douyin-video-analyzer/scripts/normalize_names.py --start <起> --end <止>
```
脚本会把下载目录里最新的三张表（以及按标准命名下载的视频）移入周期目录，重名跳过。

---

## 3. 下载区间视频（重点、易踩坑）

### 3.1 生成待下载清单

先跑 `parse_data.py`，它会打印“待下载视频 N 条”及标准名（file_base，如
`20261011-单点突破法`、`20261007-01-知识缝接`）。下载时就用这个标准名做文件名。

### 3.2 为什么不能用页面的「下载」按钮

作品播放页右侧分享面板里的下载图标，点击常弹 toast「该视频不支持下载」（发布时关闭了
允许下载权限）。这不影响取片：视频要播放，播放器必然已经从官方 CDN 取到真实视频文件。

### 3.3 打开作品并抓真实地址

作品列表/主页里没有直接的“复制链接”可靠入口时，用 aweme_id 打开播放页；也可从作品
管理页点进播放。关键是**让视频真实播放几秒**，再读网络请求：

```python
import time
bu.navigate("https://www.douyin.com/user/self?modal_id=<aweme_id>")
bu.wait_for_load(timeout=20)
time.sleep(6)  # 让播放器发起视频请求
# 尝试点一下播放/清掉遮罩，确保 video 在加载
reqs = bu.network_requests()
vids = [r["url"] for r in reqs
        if "douyinvod.com" in r.get("url","") and "/video/tos/" in r.get("url","")]
```

注意：`<video>.src` 是 `blob:https://www.douyin.com/...`，这是页面内部引用，外部打不开；
真实地址只在 `network_requests()` 里。

### 3.4 选流（最重要的坑）

抓到的候选通常有两类：

- **音视频合一的完整 mp4**：URL 参数含 `mime_type=video_mp4`，路径里不是
  `media-video-hvc1` / `media-audio-und-mp4a`。**优先用这种**。
- **DASH 分离流**：一条 `media-video-hvc1`（HEVC，**只有画面无声音**）+
  一条 `media-audio-und-mp4a`（只有声音）。
- 还可能混入**异常拼接的超长流**（时长数百秒，明显长于作品），绝对不能选。

**不要只按码率（br）高低选**——最高码率往往是那条 HEVC 无音频流。

策略：
1. 先在候选里找合一完整 mp4（`mime_type=video_mp4` 且不是 media-audio/media-video），
   下载后校验。
2. 若只有分离流，下载视频流和音频流，用 ffmpeg 合并（见 3.6）。
3. 每条都必须过 3.5 的 ffprobe 校验。

### 3.5 下载并校验（合一完整流）

```python
url = "<含 mime_type=video_mp4 的完整流地址>"
rec = bu.download(url, filename="20261011-单点突破法.mp4", timeout=60)
print(rec["path"], rec["bytes"])
```

下载后（在 shell）用 ffprobe 校验，必须同时含视频流和音频流，且时长与作品时长误差 ≤ 2.5s：
```powershell
& $py -c "import sys; sys.path.insert(0, r'.agents/skills/douyin-video-analyzer/scripts'); from common import is_complete_video; from pathlib import Path; print(is_complete_video(Path(r'<下载目录或周期目录/xxx.mp4>'), expect_duration=63.0))"
```
- 返回 True：合格。
- 无音频：选到 HEVC 分离流，走 3.6。
- 时长对不上：选到了拼接流/别的码流，重选。

### 3.6 分离流合并（兜底）

分别下载 `...media-video-hvc1...`（存 v.mp4）与 `...media-audio-und-mp4a...`（存 a.mp4），
合并并转成通用 H.264 + AAC：
```powershell
& ffmpeg -y -i v.mp4 -i a.mp4 -map 0:v:0 -map 1:a:0 -c:v libx264 -crf 20 -c:a aac -b:a 192k "标准名.mp4"
```
合并后再用 3.5 校验。HEVC 直存会导致部分播放器没声音/不兼容，所以这里要转 H.264。

### 3.7 逐条完成与复核

- 每条作品用台账 file_base 命名，重复执行 `normalize_names.py` 归位。
- 全部下完后重跑 `parse_data.py`，看到“√ 全部视频已就位”，且每条 `has_audio=true`、
  分辨率/时长合理（当前账号网页最高画质通常为 720×1280，和本地原片一致，不影响分析）。
- CDN 地址带时效签名（约数小时），必须**现抓现下**，不要跨会话复用旧地址。
- 一天多条：作品按发布时间顺序下载，文件名用台账里的 01/02，不要自行编号。

---

## 4. 兜底

- 列表加载不全：滚动加载更多，再抓；作品页是分页/懒加载。
- `network_requests` 没有 douyinvod：确认视频确实开始播放、没有被暂停；重新进入播放页再等几秒。
- 找不到作品的 aweme_id：作品列表导出表不含 ID；可从播放页 URL 的 `modal_id` 读取，
  或在个人主页逐条点开，按发布时间和标题与台账对应。
- `BU_REF_STALE` / 页面跳转后 ref 失效：重新 `bu.snapshot()`，用新 ref。
- 任何登录/验证卡点：始终用 `interaction.request_action` 交接，不要自行尝试绕过。
