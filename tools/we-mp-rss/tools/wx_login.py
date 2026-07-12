#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号平台「扫码授权」命令行工具（纯 API，不需要浏览器）
=========================================================

适用于无浏览器 / 无头环境（容器、宿主机未装 Playwright 浏览器）。
它会：
  1. 向微信申请登录二维码并保存到 static/wx_qrcode.png
  2. 阻塞等待你用【公众号管理员微信】扫码 + 手机确认
  3. 等后台把 token/cookie 抓全后持久化（Redis + data/wx.lic）；
     若后台线程未及时写入，则用内存中的 token/cookie 兜底手动持久化
  4. 打印最终是否拿到 token

前提：
  - 需自备一个微信公众号（免费订阅号即可），扫码微信须为其管理员/运营者
  - 需设置代理以访问 mp.weixin.qq.com（由用户自行配置，本脚本不硬编码），例如：
        export HTTPS_PROXY=http://<代理IP>:<端口>
        export HTTP_PROXY=http://<代理IP>:<端口>

用法：
    .venv/bin/python tools/wx_login.py
    .venv/bin/python tools/wx_login.py --timeout 300   # 等待扫码的秒数，默认 300
"""
import argparse
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def main():
    parser = argparse.ArgumentParser(description="微信公众平台扫码授权（API 方式）")
    parser.add_argument("--timeout", type=int, default=300, help="等待扫码的最长秒数，默认 300")
    args = parser.parse_args()

    from driver.wx_api import WeChat_api as W
    from driver.token import set_token, get

    # 清掉可能残留的二维码（check_lock 以该文件是否存在判断“是否在运行”）
    qr_path = os.path.join(ROOT, "static", "wx_qrcode.png")
    try:
        if os.path.exists(qr_path):
            os.remove(qr_path)
    except Exception:
        pass

    r = W.get_qr_code()
    code = r.get("code")
    if not code:
        print(f"❌ 获取二维码失败: {r.get('msg')}")
        print("   请检查：是否设置了代理、能否访问 mp.weixin.qq.com、static/wx_qrcode.png 是否被占用")
        sys.exit(1)

    print("=" * 56)
    print("二维码已生成：", qr_path)
    print("请用【公众号管理员微信】扫码，并在手机上确认登录")
    print("（在 VS Code 资源管理器里打开该 png，或经端口转发访问 /static/wx_qrcode.png）")
    print("=" * 56)

    # 1) 等扫码确认
    deadline = time.time() + args.timeout
    while time.time() < deadline:
        if getattr(W, "is_logged_in", False):
            break
        time.sleep(2)
    if not getattr(W, "is_logged_in", False):
        print("⏰ 超时未完成扫码，请重跑本命令")
        sys.exit(1)
    print("✅ 扫码确认完成，正在保存登录态…")

    # 2) 等后台线程把 token 写入（最多再等 ~40s）
    for _ in range(20):
        if get("token"):
            break
        time.sleep(2)

    # 3) 兜底：后台没写成但内存里有 token，则手动持久化
    tok = get("token")
    if not tok and getattr(W, "token", None):
        try:
            set_token({
                "token": W.token,
                "cookies_str": W._format_cookies_string(),
                "fingerprint": W.fingerprint,
                "expiry": {},
            })
            tok = get("token")
        except Exception as e:
            print(f"手动持久化失败: {e}")

    if tok:
        print(f"🎉 授权成功，token 已持久化：{tok[:24]}…")
        print("   现在可到网页按【名称】搜索公众号，或运行 tools/analyze_accounts.py 批量分析。")
    else:
        print("❌ 仍未拿到 token。请确认扫码微信是某个已注册公众号的管理员/运营者后重试。")
        sys.exit(1)


if __name__ == "__main__":
    main()
