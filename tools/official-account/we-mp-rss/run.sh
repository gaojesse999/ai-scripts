#!/bin/bash
# WeRSS 本地启动脚本
# 用法:
#   ./run.sh            首次启动（自动初始化数据库与管理员账号 admin / admin@123）
#   ./run.sh noinit     已初始化过，跳过初始化
#
# 代理：抓取微信内容需联网。本脚本【不硬编码代理】，请在运行前自行设置，例如：
#   export HTTPS_PROXY=http://<你的代理IP>:<端口>
#   export HTTP_PROXY=http://<你的代理IP>:<端口>
# 脚本会原样继承你设置的这些环境变量。
set -e
cd "$(dirname "$0")"

# 本地回环不走代理（沿用你已设置的 NO_PROXY，未设置时给个安全默认）
export NO_PROXY=${NO_PROXY:-localhost,127.0.0.1,::1}

# 管理员账号（首次初始化时写入数据库）
export USERNAME=${USERNAME:-admin}
export PASSWORD=${PASSWORD:-admin@123}
export PIP_CONSTRAINT=

INIT="True"
if [ "$1" = "noinit" ]; then INIT="False"; fi

echo "服务启动中，访问地址: http://<本机IP>:8001/"
exec .venv/bin/python main.py -job True -init "$INIT"

