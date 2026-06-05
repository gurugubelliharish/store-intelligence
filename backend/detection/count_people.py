from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.track(
    source="data/raw_videos/store2/entry 1.mp4",
    classes=[0],
    persist=True,
    show=True
)