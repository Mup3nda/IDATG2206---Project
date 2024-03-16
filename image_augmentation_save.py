
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torchvision.transforms as transforms
import torch

# Configuration: adjust these paths and settings according to your dataset and requirements
original_dataset_path = '/Users/didiermupenda/ANADROM_Datasets/Annotation/task_fish_detection-2024_02_01_18_41_23-cvat for video 1.1/images'
augmented_dataset_path = '/Users/didiermupenda/ANADROM_Datasets/Annotation/task_fish_detection-2024_02_01_18_41_23-cvat for video 1.1/aug_images'
img_height = 640  
img_width = 640

# Create the augmented dataset directory if it doesn't exist
os.makedirs(augmented_dataset_path, exist_ok=True)
#------------------------------------------------------------------------------------
# image_path = 'test_data/images/frame_000112.PNG'
# image = Image.open(image_path)

def adjust_hue(img, min_hue, max_hue):
    img_hsv = img.convert("HSV")
    np_img = np.array(img_hsv)
    h, s, v = np_img[:,:,0], np_img[:,:,1], np_img[:,:,2]

    h_new = np.where((h >= min_hue) & (h <= max_hue), h, h)

    img_hsv_adjusted = Image.fromarray(np.stack([h, s, v], axis=-1), "HSV").convert("RGB")

    return img_hsv_adjusted

transform = transforms.Compose([
    transforms.Lambda(lambda img: adjust_hue(img, min_hue=30, max_hue=60)),
    transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5),
])
#------------------------------------------------------------------------------------
def augment_and_save(image_path, output_path, save_prefix, transform):
    img = Image.open(image_path)
    for i in range(3):
        augmented_img = transform(img)
        augmented_img.save(os.path.join(output_path, f"{save_prefix}_aug{i+1}.PNG"))

for filename in os.listdir(original_dataset_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(original_dataset_path, filename)
        filename_no_ext = os.path.splitext(filename)[0]
        augment_and_save(input_path, augmented_dataset_path ,filename_no_ext, transform)

print("Image augmentation complete.")