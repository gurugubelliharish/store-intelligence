from ultralytics import YOLO
from collections import defaultdict

model = YOLO("yolov8n.pt")

results = model.track(
    source="data/raw_videos/store2/zone.mp4",
    classes=[0],
    persist=True,
    stream=True
)

FPS = 30

LEFT_END = 420
CENTER_END = 630

zone_frames = defaultdict(lambda: {
    "LEFT": 0,
    "CENTER": 0,
    "RIGHT": 0
})

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
            zone = "LEFT"

        elif center_x < CENTER_END:
            zone = "CENTER"

        else:
            zone = "RIGHT"

        zone_frames[track_id][zone] += 1

print("\n===== DWELL TIME ANALYTICS =====\n")

left_total = 0
center_total = 0
right_total = 0

valid_visitors = 0

for visitor_id, zones in zone_frames.items():

    total_time = (
        zones["LEFT"] +
        zones["CENTER"] +
        zones["RIGHT"]
    ) / FPS

    # Ignore visitors tracked for less than 3 seconds
    if total_time < 3:
        continue

    valid_visitors += 1

    left_time = zones["LEFT"] / FPS
    center_time = zones["CENTER"] / FPS
    right_time = zones["RIGHT"] / FPS

    left_total += left_time
    center_total += center_time
    right_total += right_time

    print(
        f"VIS_{visitor_id} | "
        f"LEFT={left_time:.1f}s "
        f"CENTER={center_time:.1f}s "
        f"RIGHT={right_time:.1f}s "
        f"TOTAL={total_time:.1f}s"
    )

print("\n===== AVERAGE DWELL TIME =====\n")

if valid_visitors > 0:
    print(f"LEFT   : {left_total / valid_visitors:.2f} sec")
    print(f"CENTER : {center_total / valid_visitors:.2f} sec")
    print(f"RIGHT  : {right_total / valid_visitors:.2f} sec")

print("\nTotal Visitors:", valid_visitors)