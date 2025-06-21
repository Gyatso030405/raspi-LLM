from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import subprocess, requests, json, time, atexit
import RPi.GPIO as GPIO

from camera_stream import router as video_router, capture_frame

app = FastAPI()
app.include_router(video_router)  # 挂载摄像头视频流路由

# 舵机GPIO配置
PIN_VERTICAL = 17
PIN_HORIZONTAL = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_VERTICAL, GPIO.OUT)
GPIO.setup(PIN_HORIZONTAL, GPIO.OUT)

pwm_vertical = GPIO.PWM(PIN_VERTICAL, 50)
pwm_horizontal = GPIO.PWM(PIN_HORIZONTAL, 50)
pwm_vertical.start(7.5)
pwm_horizontal.start(7.5)

# 舵机控制函数
def move_servo(servo, angle):
    duty = 2.5 + (angle / 18.0)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

def rolling():
    print("转动舵机开始")
    move_servo(pwm_horizontal, 45)
    time.sleep(1)
    move_servo(pwm_horizontal, 135)
    time.sleep(1)
    move_servo(pwm_vertical, 45)
    time.sleep(1)
    move_servo(pwm_vertical, 135)
    print("转动舵机结束")

# 拍照函数（从视频流抓帧）
def take_photo():
    filename = "/home/pi/onenetcam/photo.jpg"
    if capture_frame(filename):
        print(f"照片已保存：{filename}")
    else:
        print("拍照失败！")

# 网页界面
@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
    <head><title>树莓派控制台</title></head>
    <body>
        <h2>实时摄像头画面</h2>
        <img src="/video" width="640" height="480"/>
        <h2>输入自然语言指令</h2>
        <form action="/submit" method="post">
            <textarea name="instruction" rows="4" cols="50" placeholder="例如：请帮我拍照或转动摄像头"></textarea><br>
            <input type="submit" value="提交">
        </form>
    </body>
    </html>
    """

# 指令处理
@app.post("/submit", response_class=HTMLResponse)
def submit(instruction: str = Form(...)):
    prompt = {
        "model": "qwen2.5",
        "messages": [
            {
                "role": "system",
                "content": (
                    "你是一个助手，负责将用户指令解析为 JSON。\n"
                    "支持命令：\n"
                    "- 拍照：{\"cmd\": \"take_photo\"}\n"
                    "- 转动：{\"cmd\": \"rolling\"}\n"
                    "只输出JSON格式。"
                )
            },
            {"role": "user", "content": instruction}
        ],
        "temperature": 0.0,
        "response_format": "json"
    }

    try:
        res = requests.post("http://127.0.0.1:8080/v1/chat/completions", json=prompt)
        data = json.loads(res.json()['choices'][0]['message']['content'])
        cmd = data.get("cmd")

        if cmd == "take_photo":
            take_photo()
        elif cmd == "rolling":
            rolling()
        else:
            return f"<html><body><p>未知命令：{cmd}</p></body></html>"

        return f"<html><body><p>命令执行成功：{cmd}</p></body></html>"

    except Exception as e:
        return f"<html><body><p>处理失败：{e}</p></body></html>"

# 清理 GPIO
def cleanup():
    pwm_vertical.stop()
    pwm_horizontal.stop()
    GPIO.cleanup()

atexit.register(cleanup)
