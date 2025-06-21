#!/bin/bash

echo "[Web] 正在激活虚拟环境并启动 uvicorn..."
cd "$(dirname "$0")"
source ~/myenv_sys/bin/activate

uvicorn chat_pi:app --host 0.0.0.0 --port 8000
