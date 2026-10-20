#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
通过 CDP 远程调试端口接管前台真实 Edge/Chrome 浏览器，完成全自动导出与复盘分析
"""

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# 确保脚本内访问抖音/直连时不受本地代理影响
for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'ALL_PROXY', 'http_proxy', 'https_proxy', 'all_proxy']:
    if k in os.environ:
        del os.environ[k]

import time
import json
import urllib.request
import subprocess
import argparse
from datetime import datetime, timedelta
from pathlib import Path

from playwright.sync_api import sync_playwright

DOWNLOAD_DIR = Path(os.environ.get("USERPROFILE", "")) / "Downloads"
VAULT_ROOT = Path(__file__).resolve().parents[3]
SKILL_ROOT = VAULT_ROOT / ".agents" / "skills" / "douyin-video-analyzer"
PYTHON_EXE = sys.executable

def wait_for_cdp_ready(port=9225, timeout=600):
    print(f">>> 正在等待前台浏览器启动并开启调试端口 {port}...", flush=True)
    for i in range(timeout):
        try:
            url = f"http://127.0.0.1:{port}/json/version"
            opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
            with opener.open(url, timeout=1) as resp:
                if resp.status == 200:
                    print(f">>> √ 前台浏览器已就绪，成功建立 CDP 连接！", flush=True)
                    return True
        except Exception:
            pass
        if i % 10 == 0 and i > 0:
            print(f">>> 等待浏览器启动中...（请双击桌面的『启动采集浏览器.bat』）已等待 {i} 秒", flush=True)
        time.sleep(1)
    print(">>> 等待浏览器启动超时！", flush=True)
    return False

def get_douyin_page(context):
    for page in context.pages:
        if "creator.douyin.com" in page.url:
            return page
    return context.pages[-1] if context.pages else None

def wait_for_user_login(page):
    print(">>> 检测浏览器登录状态...", flush=True)
    for i in range(300):
        try:
            txt = page.inner_text("body")
            if "扫码登录" not in txt and ("首页" in txt or "内容管理" in txt or "作品发布" in txt):
                print(">>> √ 检测到已成功登录创作者中心！", flush=True)
                return True
            if "接收短信验证码" in txt:
                print(">>> 提示：浏览器弹出了二次验证，请在浏览器中直接完成验证！", flush=True)
        except Exception:
            pass
            
        if i % 10 == 0 and i > 0:
            print(f">>> 正在等待登录完成（已等待 {i*2} 秒）... 请在屏幕上的浏览器窗口中扫码！", flush=True)
        time.sleep(2)
        
    print(">>> 登录等待超时！", flush=True)
    return False

def export_datacenter_tables(page):
    print(">>> [步骤 1/4] 开始导出数据中心两张表（短视频 + 粉丝）...", flush=True)
    page.goto("https://creator.douyin.com/creator-micro/data-center/operation", wait_until="domcontentloaded")
    time.sleep(4)
    
    # 点击“昨天”
    try:
        page.evaluate("""() => {
            const btns = [...document.querySelectorAll('div, span')].filter(el => 
                el.innerText && el.innerText.trim() === '昨天' && el.offsetParent !== null
            );
            btns.forEach(b => b.click());
        }""")
        print(">>> √ 已点击【昨天】按钮", flush=True)
        time.sleep(3)
    except Exception as e:
        print(f">>> 日期选择提示: {e}", flush=True)
        
    export_buttons = page.query_selector_all("button:has-text('导出数据')")
    print(f">>> 找到 {len(export_buttons)} 个导出数据按钮", flush=True)
    
    for i, btn in enumerate(export_buttons):
        try:
            name = "短视频全量指标" if i == 0 else "粉丝全量指标"
            print(f">>> 正在导出: {name} ...", flush=True)
            btn.click()
            time.sleep(3)
        except Exception as e:
            print(f">>> 导出第 {i+1} 张表异常: {e}", flush=True)
            
    time.sleep(3)

def export_works_list(page):
    print(">>> [步骤 2/4] 开始导出作品管理页全量作品列表...", flush=True)
    page.goto("https://creator.douyin.com/creator-micro/content/manage", wait_until="domcontentloaded")
    time.sleep(4)
    
    try:
        btn = page.locator("text='导出数据'").first
        btn.click()
        time.sleep(3)
        modal_btns = page.locator("button:has-text('确定'), button:has-text('导出')").all()
        for mb in modal_btns:
            try:
                mb.click()
            except Exception:
                pass
        print(">>> √ 已触发作品列表导出", flush=True)
        time.sleep(4)
    except Exception as e:
        print(f">>> 作品列表导出异常: {e}", flush=True)

def download_period_video(context, page, target_date, period_dir):
    print(f">>> [步骤 3/4] 正在定位 {target_date} 作品并捕获视频流...", flush=True)
    if "creator-micro/content/manage" not in page.url:
        page.goto("https://creator.douyin.com/creator-micro/content/manage", wait_until="domcontentloaded")
        time.sleep(4)
        
    formatted_date = target_date.replace("-", "年") + "日" if "-" in target_date else target_date
    covers = page.locator(".video-card-cover-QkeRHf").all()
    
    clicked = False
    cards = page.query_selector_all("div[class*='video-card']")
    for idx, card in enumerate(cards):
        txt = card.inner_text()
        if target_date in txt or formatted_date in txt or (idx == 1 and len(cards) > 1):
            print(f">>> 匹配到目标作品卡片 (索引 {idx})，正在触发播放预览...", flush=True)
            if idx < len(covers):
                covers[idx].click()
            else:
                card.click()
            clicked = True
            break
            
    if not clicked and covers:
        print(">>> 默认点击首个作品封面触发播放...", flush=True)
        covers[0].click()
        
    time.sleep(5)
    
    video_url = None
    preview_page = None
    for pg in context.pages:
        if "douyin.com/user/self" in pg.url or "modal_id" in pg.url:
            preview_page = pg
            vids = pg.query_selector_all("video")
            for v in vids:
                src = v.get_attribute("src") or pg.evaluate("el => el.currentSrc", v)
                if src and ("douyinvod.com" in src or "tos-cn-v" in src):
                    video_url = src
                    break
            if video_url:
                break
                
    if video_url:
        print(f">>> √ 成功捕获真实视频流 URL: {video_url[:80]}...", flush=True)
        filename = f"{target_date.replace('-', '')}-发布视频.mp4"
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        req = urllib.request.Request(video_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://www.douyin.com/"
        })
        try:
            with opener.open(req) as resp:
                data = resp.read()
                (period_dir / filename).write_bytes(data)
                (DOWNLOAD_DIR / filename).write_bytes(data)
                print(f">>> √ 视频已保存至周期目录与下载目录: {filename} ({len(data)} 字节)", flush=True)
        except Exception as e:
            print(f">>> 视频下载失败: {e}", flush=True)
            
        if preview_page:
            try:
                preview_page.close()
            except Exception:
                pass
    else:
        print(">>> 提示: 未能自动截获视频流，可手动下载后放入周期目录。", flush=True)

def run_local_pipeline(target_date, period_dir):
    print(">>> [步骤 4/4] 启动本地分析流水线（归一化 -> 解析 -> Whisper转写 -> 抽帧 -> 报告）...", flush=True)
    scripts_dir = SKILL_ROOT / "scripts"
    
    # 1. normalize_names.py
    subprocess.run([PYTHON_EXE, str(scripts_dir / "normalize_names.py"), "--start", target_date, "--end", target_date])
    
    # 2. parse_data.py
    subprocess.run([PYTHON_EXE, str(scripts_dir / "parse_data.py"), "--start", target_date, "--end", target_date])
    
    # 3. media_pipeline.py
    subprocess.run([PYTHON_EXE, str(scripts_dir / "media_pipeline.py"), "--start", target_date, "--end", target_date])
    
    # 4. extract_frames.py
    subprocess.run([PYTHON_EXE, str(scripts_dir / "extract_frames.py"), "--start", target_date, "--end", target_date])
    
    # 5. build_report.py
    subprocess.run([PYTHON_EXE, str(scripts_dir / "build_report.py"), "--start", target_date, "--end", target_date, "--force"])
    print(">>> √ 全部本地流水线已处理完毕！", flush=True)

def main():
    parser = argparse.ArgumentParser(description="抖音自动化采集与分析 (CDP 前台浏览器接管模式)")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    parser.add_argument("--date", default=yesterday, help="目标分析日期 (YYYY-MM-DD)，默认为昨天")
    parser.add_argument("--port", type=int, default=9225, help="CDP 远程调试端口")
    args = parser.parse_args()
    
    target_date = args.date
    period_dir = VAULT_ROOT / "视频分析" / "视频素材" / target_date.replace("-", "")
    period_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print(f" 抖音自动化采集分析器（CDP 前台真实浏览器接管模式）")
    print(f" 目标日期: {target_date}")
    print("=" * 60)
    
    if not wait_for_cdp_ready(port=args.port, timeout=600):
        sys.exit(1)
        
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{args.port}")
        context = browser.contexts[0]
        page = get_douyin_page(context)
        
        if not page:
            print(">>> 错误: 未能在浏览器中找到可用页面！", flush=True)
            sys.exit(1)
            
        client = page.context.new_cdp_session(page)
        client.send('Page.setDownloadBehavior', {
            'behavior': 'allow',
            'downloadPath': str(DOWNLOAD_DIR)
        })
        
        if not wait_for_user_login(page):
            sys.exit(1)
            
        export_datacenter_tables(page)
        export_works_list(page)
        download_period_video(context, page, target_date, period_dir)
        
    run_local_pipeline(target_date, period_dir)
    print(">>> 采集与管线处理全部顺利完成！", flush=True)

if __name__ == "__main__":
    main()
