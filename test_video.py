import os
from ultralytics import YOLO
import cv2
import torch


VIDEOS_DIR = os.path.join('videos')
video_path = os.path.join(VIDEOS_DIR, '20230617171213_20230617171220_3.mp4')

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

model_path = os.path.join('runs/detect/train2/weights/best.pt')

# Load a model
model = YOLO(model_path)  # load a custom model
#model = YOLO("yolov8m.pt") # load yolo model

threshold = 0.5

while ret:
    results = model(frame,  device='mps')[0] #, device = "mps"

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            label = f"{results.names[int(class_id)].upper()} {score:.2f}"
            cv2.putText(frame, label, (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('YOLO Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break
    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()
