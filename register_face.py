import cv2
import os
import utils.logger as logger

def register(name, dept, roll):
    folder_name = f"{name}_{dept}_{roll}"
    path = os.path.join("data_set", folder_name)
    os.makedirs(path, exist_ok=True)

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Register Face")
    count = 0

    while count < 5:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Register Face", frame)
        k = cv2.waitKey(1)
        if k % 256 == 32:
            face_path = os.path.join(path, f"face_{count+1}.jpg")
            cv2.imwrite(face_path, frame)
            count += 1
    cam.release()
    cv2.destroyAllWindows()

    logger.log_action(name, dept, roll, "Registered")