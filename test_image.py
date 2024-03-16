from ultralytics import YOLO
import cv2
import torch

model = YOLO('runs/detect/train2/weights/last.pt')
#model = YOLO('yolov8m.pt')
results = model("/Users/didiermupenda/ANADROM_Datasets/Annotation/task_fish_detection-2024_02_02_06_13_45-cvat for video 1.1/images/frame_000092.PNG", show=True)
print(results)

cv2.waitKey(0)

