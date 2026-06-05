import cv2

video_path = "data/raw_videos/store2/entry 1.mp4"

cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()

if ret:
    height, width = frame.shape[:2]

    line_y = height // 2

    cv2.line(frame, (0, line_y), (width, line_y), (0, 255, 0), 3)

    cv2.imshow("Line Test", frame)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()