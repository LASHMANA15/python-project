import face_recognition
import os
import cv2

def scan_face():
    known_encodings = []
    known_names = []
    for folder in os.listdir("data_set"):
        folder_path = os.path.join("data_set", folder)
        for file in os.listdir(folder_path):
            img = face_recognition.load_image_file(os.path.join(folder_path, file))
            encodings = face_recognition.face_encodings(img)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(folder)

    cam = cv2.VideoCapture(0)
    matched_user = None
    for _ in range(60):
        ret, frame = cam.read()
        if not ret:
            continue
        rgb = frame[:, :, ::-1]
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)
        for (top, right, bottom, left), enc in zip(faces, encodings):
            matches = face_recognition.compare_faces(known_encodings, enc, tolerance=0.45)
            if True in matches:
                index = matches.index(True)
                name_parts = known_names[index].split("_")
                matched_user = name_parts
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, f"{matched_user[0]} ({matched_user[2]})", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        cv2.imshow("Face Match", frame)
        if matched_user:
            break
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    return matched_user