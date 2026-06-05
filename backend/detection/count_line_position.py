from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video_path = "data/raw_videos/store2/entry 1.mp4"

cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()

if ret:
    height, width = frame.shape[:2]

    print("Width =", width)
    print("Height =", height)

    line_y = height // 2

    print("Line Y =", line_y)

cap.release()