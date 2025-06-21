import cv2
from fastapi import APIRouter
from starlette.responses import StreamingResponse

router = APIRouter()
video_capture = cv2.VideoCapture(0)  # USB摄像头

def gen_frames():
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@router.get("/video")
def video_feed():
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

def capture_frame(filename="/home/pi/onenetcam/photo.jpg"):
    success, frame = video_capture.read()
    if success:
        cv2.imwrite(filename, frame)
        return True
    return False
