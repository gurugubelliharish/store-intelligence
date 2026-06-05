from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.track(
    source="data/raw_videos/store2/entry 1.mp4",
    classes=[0],
    persist=True,
    stream=True
)

for result in results:
    if result.boxes.id is not None:
        ids = result.boxes.id.tolist()

        print("Tracked IDs:", ids)

        break