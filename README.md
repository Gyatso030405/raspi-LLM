项目名称：基于大语言模型驱动的树莓派智能自拍控制系统

 项目目录结构说明：

llm_selfie_cam/
├── chat_pi.py                 ← 网页控制主程序（FastAPI）
├── camera_stream.py           ← 摄像头视频流模块
├── models/                    ← 存放 Qwen2.5 模型 .gguf 文件
│   └── qwen2.5-0.5b-instruct-q2_k.gguf
├── llama.cpp-master/          ← 解压 llama.cpp 后的源码目录
│   └── build/bin/llama-server（编译后生成）
├── photo/                     ← 拍照图片保存目录
├── run_llm.sh                 ←  启动本地大模型
├── run_web.sh                 ←  启动网页服务
└── run_all.sh                 ←  一键启动模型 + 网页服务

🛠 环境准备：

1. 创建虚拟环境：
   python3 -m venv ~/myenv_sys --system-site-packages

2. 激活虚拟环境：
   source ~/myenv_sys/bin/activate

3. 安装依赖：
   pip install fastapi uvicorn python-multipart openai requests -i https://pypi.org/simple

4. 安装系统依赖（如未安装）：
   sudo apt install cmake build-essential python3-opencv -y   （cmake是一个C/C++项目的构建系统工具，这里
   
   llama.cpp编译需要）

 编译 llama.cpp：
   unzip llama.cpp-master.zip
   cd llama.cpp-master
   cmake -B build -DLLAMA_CURL=OFF
   cmake --build build --target llama-server --config Release

  脚本使用说明（首次使用需赋予权限）：

   chmod +x run_web.sh run_llm.sh run_all.sh

  启动本地模型（端口 8080）：
    ./run_llm.sh

  启动网页服务（端口 8000）：
    ./run_web.sh

  一键运行（推荐）：
   ./run_all.sh

  然后用浏览器访问：
http://<树莓派IP>:8000

输入自然语言指令，如：
- 请帮我拍张照片
- 摄像头向左转
- 拍一张风景照
系统会通过大模型解析出 JSON 指令并控制舵机或拍照。

🧼 停止运行：使用 Ctrl+C 即可关闭服务