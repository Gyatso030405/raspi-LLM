��Ŀ���ƣ����ڴ�����ģ����������ݮ���������Ŀ���ϵͳ

 ��ĿĿ¼�ṹ˵����

llm_selfie_cam/
������ chat_pi.py                 �� ��ҳ����������FastAPI��
������ camera_stream.py           �� ����ͷ��Ƶ��ģ��
������ models/                    �� ��� Qwen2.5 ģ�� .gguf �ļ�
��   ������ qwen2.5-0.5b-instruct-q2_k.gguf
������ llama.cpp-master/          �� ��ѹ llama.cpp ���Դ��Ŀ¼
��   ������ build/bin/llama-server����������ɣ�
������ photo/                     �� ����ͼƬ����Ŀ¼
������ run_llm.sh                 ��  �������ش�ģ��
������ run_web.sh                 ��  ������ҳ����
������ run_all.sh                 ��  һ������ģ�� + ��ҳ����

�0�0 ����׼����

1. �������⻷����
   python3 -m venv ~/myenv_sys --system-site-packages

2. �������⻷����
   source ~/myenv_sys/bin/activate

3. ��װ������
   pip install fastapi uvicorn python-multipart openai requests -i https://pypi.org/simple

4. ��װϵͳ��������δ��װ����
   sudo apt install cmake build-essential python3-opencv -y   ��cmake��һ��C/C++��Ŀ�Ĺ���ϵͳ���ߣ�����
   
   llama.cpp������Ҫ��

 ���� llama.cpp��
   unzip llama.cpp-master.zip
   cd llama.cpp-master
   cmake -B build -DLLAMA_CURL=OFF
   cmake --build build --target llama-server --config Release

  �ű�ʹ��˵�����״�ʹ���踳��Ȩ�ޣ���

   chmod +x run_web.sh run_llm.sh run_all.sh

  ��������ģ�ͣ��˿� 8080����
    ./run_llm.sh

  ������ҳ���񣨶˿� 8000����
    ./run_web.sh

  һ�����У��Ƽ�����
   ./run_all.sh

  Ȼ������������ʣ�
http://<��ݮ��IP>:8000

������Ȼ����ָ��磺
- �����������Ƭ
- ����ͷ����ת
- ��һ�ŷ羰��
ϵͳ��ͨ����ģ�ͽ����� JSON ָ����ƶ�������ա�

�0�6 ֹͣ���У�ʹ�� Ctrl+C ���ɹرշ���