from ultralytics import YOLO
import torch

# if torch.cuda.is_available():
#  dev = "cuda:0"
# else:
#  dev = "cpu"
# device = torch.device(dev)

# Load a model
model = YOLO("yolov8m.pt")  # build a new model from scratch

# Use the model
model.train(data="config.yaml", epochs=10)  # train the model device='mps' with GPU
