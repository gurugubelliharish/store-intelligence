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

        boxes = result.boxes.xyxy.cpu().numpy()
        ids = result.boxes.id.cpu().numpy()

        for box, track_id in zip(boxes, ids):

            x1, y1, x2, y2 = box

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            print(
                f"ID={int(track_id)} "
                f"Center=({center_x}, {center_y})"
            )

        break