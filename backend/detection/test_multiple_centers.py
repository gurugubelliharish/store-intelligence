from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.track(
    source="data/raw_videos/store2/entry 1.mp4",
    classes=[0],
    persist=True,
    stream=True
)

LINE_Y = 450

entry_count = 0
exit_count = 0

last_positions = {}
track_state = {}

for result in results:

    if result.boxes.id is None:
        continue

    boxes = result.boxes.xyxy.cpu().numpy()
    ids = result.boxes.id.cpu().numpy()

    for box, track_id in zip(boxes, ids):

        track_id = int(track_id)

        x1, y1, x2, y2 = box
        center_y = int((y1 + y2) / 2)

        if track_id in last_positions:

            prev_y = last_positions[track_id]

            state = track_state.get(track_id, "UNKNOWN")

            # Person moving downward across line
            if prev_y < LINE_Y and center_y > LINE_Y:

                if state != "INSIDE":
                    entry_count += 1
                    track_state[track_id] = "INSIDE"
                    print(f"ENTRY = {entry_count}")

            # Person moving upward across line
            elif prev_y > LINE_Y and center_y < LINE_Y:

                if state != "OUTSIDE":
                    exit_count += 1
                    track_state[track_id] = "OUTSIDE"
                    print(f"EXIT = {exit_count}")

        last_positions[track_id] = center_y

print("Finished")
print("Entries:", entry_count)
print("Exits:", exit_count)