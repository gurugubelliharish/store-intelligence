import cv2

video_path = "data/raw_videos/store2/entry 1.mp4"

cap = cv2.VideoCapture(video_path)

frame_number = 100

cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

ret, frame = cap.read()

if ret:
    cv2.line(frame, (0, 540), (960, 540), (0, 255, 0), 3)

    cv2.imshow("Frame 100", frame)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()