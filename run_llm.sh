#!/bin/bash

echo "[LLM] 正在启动本地大模型 llama-server..."
cd "$(dirname "$0")/llama.cpp-master"

./build/bin/llama-server \
  -m ../models/qwen2.5-0.5b-instruct-q2_k.gguf \
  --host 0.0.0.0 --port 8080
