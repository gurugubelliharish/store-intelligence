from ultralytics import YOLO


def run_tracking(video_path):
    model = YOLO("yolov8n.pt")

    results = model.track(
        source=video_path,
        classes=[0],
        persist=True,
        save=True,
        conf=0.4
    )

    return results


if __name__ == "__main__":
    video_path = "data/raw_videos/store2/entry 1.mp4"

    run_tracking(video_path)

    print("Tracking completed!")