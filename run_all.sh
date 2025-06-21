#!/bin/bash

cd "$(dirname "$0")"

echo "[ALL] 启动 LLM + 网页服务..."

# 启动 LLM（后台）
echo "[1/2] 启动本地大模型 llama-server..."
cd llama.cpp-master
./build/bin/llama-server -m ../models/qwen2.5-0.5b-instruct-q2_k.gguf --host 0.0.0.0 --port 8080 > ../llm.log 2>&1 &
cd ..

# 启动 Web 服务
echo "[2/2] 启动网页控制台..."
source ~/myenv_sys/bin/activate
uvicorn chat_pi:app --host 0.0.0.0 --port 8000
