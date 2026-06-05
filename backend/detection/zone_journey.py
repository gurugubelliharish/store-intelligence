from ultralytics import YOLO
import cv2
from collections import defaultdict

model = YOLO("yolov8n.pt")

results = model.track(
    source="data/raw_videos/store2/zone.mp4",
    classes=[0],
    persist=True,
    stream=True
)

last_zone = {}

journey_counts = defaultdict(int)

LEFT_END = 420
CENTER_END = 630

for result in results:

    if result.boxes.id is None:
        continue

    boxes = result.boxes.xyxy.cpu().numpy()
    ids = result.boxes.id.cpu().numpy()

    for box, track_id in zip(boxes, ids):

        track_id = int(track_id)

        x1, y1, x2, y2 = box

        center_x = int((x1 + x2) / 2)

        if center_x < LEFT_END:
            current_zone = "LEFT"

        elif center_x < CENTER_END:
            current_zone = "CENTER"

        else:
            current_zone = "RIGHT"

        if track_id not in last_zone:

            last_zone[track_id] = current_zone

        else:

            previous_zone = last_zone[track_id]

            if previous_zone != current_zone:

                transition = f"{previous_zone} -> {current_zone}"

                journey_counts[transition] += 1

                print(
                    f"ID {track_id}: "
                    f"{previous_zone} -> {current_zone}"
                )

                last_zone[track_id] = current_zone

print("\nZone Journey Summary\n")

for transition, count in sorted(journey_counts.items()):

    print(f"{transition}: {count}")