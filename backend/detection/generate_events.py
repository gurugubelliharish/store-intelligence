from ultralytics import YOLO
import json
import uuid
from datetime import datetime
from pathlib import Path

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

events_dir = Path("backend/data/events")
events_dir.mkdir(parents=True, exist_ok=True)

output_file = events_dir / "store2_events.jsonl"

with open(output_file, "w") as f:

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

                # ENTRY
                if prev_y < LINE_Y and center_y > LINE_Y:

                    if state != "INSIDE":

                        entry_count += 1
                        track_state[track_id] = "INSIDE"

                        event = {
                            "event_id": str(uuid.uuid4()),
                            "store_id": "STORE_BLR_002",
                            "camera_id": "CAM_ENTRY_01",
                            "visitor_id": f"VIS_{track_id}",
                            "event_type": "ENTRY",
                            "timestamp": datetime.utcnow().isoformat(),
                            "confidence": 0.90
                        }

                        f.write(json.dumps(event) + "\n")

                        print(f"ENTRY = {entry_count}")

                # EXIT
                elif prev_y > LINE_Y and center_y < LINE_Y:

                    if state != "OUTSIDE":

                        exit_count += 1
                        track_state[track_id] = "OUTSIDE"

                        event = {
                            "event_id": str(uuid.uuid4()),
                            "store_id": "STORE_BLR_002",
                            "camera_id": "CAM_ENTRY_01",
                            "visitor_id": f"VIS_{track_id}",
                            "event_type": "EXIT",
                            "timestamp": datetime.utcnow().isoformat(),
                            "confidence": 0.90
                        }

                        f.write(json.dumps(event) + "\n")

                        print(f"EXIT = {exit_count}")

            last_positions[track_id] = center_y

print("Finished")
print("Entries:", entry_count)
print("Exits:", exit_count)
print("Events saved to:", output_file)