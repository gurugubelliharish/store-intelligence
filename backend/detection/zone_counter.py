from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

results = model.track(
    source="data/raw_videos/store2/zone.mp4",
    classes=[0],
    persist=True,
    stream=True
)

LEFT_ZONE_COUNT = 0
CENTER_ZONE_COUNT = 0
RIGHT_ZONE_COUNT = 0

counted_ids = set()

for result in results:

    frame = result.orig_img

    height, width = frame.shape[:2]

    LEFT_END = 420
    CENTER_END = 630

    cv2.line(frame, (LEFT_END, 0), (LEFT_END, height), (255, 0, 0), 3)
    cv2.line(frame, (CENTER_END, 0), (CENTER_END, height), (0, 255, 0), 3)

    if result.boxes.id is not None:

        boxes = result.boxes.xyxy.cpu().numpy()
        ids = result.boxes.id.cpu().numpy()

        for box, track_id in zip(boxes, ids):

            track_id = int(track_id)

            x1, y1, x2, y2 = map(int, box)

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            cv2.circle(frame, (center_x, center_y), 6, (0, 255, 255), -1)

            if track_id not in counted_ids:

                counted_ids.add(track_id)

                if center_x < LEFT_END:
                    LEFT_ZONE_COUNT += 1

                elif center_x < CENTER_END:
                    CENTER_ZONE_COUNT += 1

                else:
                    RIGHT_ZONE_COUNT += 1

            cv2.putText(
                frame,
                f"ID:{track_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.putText(
        frame,
        f"LEFT: {LEFT_ZONE_COUNT}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        f"CENTER: {CENTER_ZONE_COUNT}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"RIGHT: {RIGHT_ZONE_COUNT}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    cv2.imshow("Zone Tracking", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()

print("\nZone Summary")
print("Left Zone :", LEFT_ZONE_COUNT)
print("Center Zone :", CENTER_ZONE_COUNT)
print("Right Zone :", RIGHT_ZONE_COUNT)