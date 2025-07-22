import cv2

def capture_camera(timeout=6):
    cap = cv2.VideoCapture(0)
    frame = None
    for _ in range(timeout * 10):
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow('Scan Face', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame