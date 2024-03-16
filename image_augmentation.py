
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torchvision.transforms as transforms
import torch

# Configuration: adjust these paths and settings according to your dataset and requirements
original_dataset_path = '/Users/didiermupenda/Desktop/NTNU/CV/Prosject/test_data/images'
augmented_dataset_path = '/Users/didiermupenda/Desktop/NTNU/CV/Prosject/test_data/augmentad_images'
img_height = 640  
img_width = 640

#------------------------------------------------------------------------------------
image_path = 'test_data/images/frame_000005.PNG'
image = Image.open(image_path)

def adjust_hue(img, min_hue, max_hue):
    img_hsv = img.convert("HSV")
    np_img = np.array(img_hsv)
    h, s, v = np_img[:,:,0], np_img[:,:,1], np_img[:,:,2]

    h_new = np.where((h >= min_hue) & (h <= max_hue), h, h)
    img_hsv_adjusted = Image.fromarray(np.stack([h, s, v], axis=-1), "HSV").convert("RGB")

    return img_hsv_adjusted

transform = transforms.Compose([
    transforms.Lambda(lambda img: adjust_hue(img, min_hue=30, max_hue=60)),
    transforms.ColorJitter(brightness=0.5, contrast=1, saturation=0.5),
    #transforms.RandomRotation(degrees=(0,180))
])

def imageshow(img, ax, title=None):
    npimage = img.numpy()
    ax.imshow(np.transpose(npimage, (1, 2, 0)))
    if title is not None:
        ax.set_title(title)

fig, axes = plt.subplots(1, 3, figsize=(15,5))
to_tensor = transforms.ToTensor()

for i in range(3):
    augmented_img = transform(image)
    tensor_img = to_tensor(augmented_img)
    imageshow(tensor_img, axes[i],f'Augmented Image {i+1}')

plt.show()
print("Image augmentation complete.")
#------------------------------------------------------------------------------------
# # Create the augmented dataset directory if it doesn't exist
# os.makedirs(augmented_dataset_path, exist_ok=True)
# # Function to augment and save an image
# for filename in os.listdir(original_dataset_path):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#         input_path = os.path.join(original_dataset_path, filename)
#         filename_no_ext = os.path.splitext(filename)[0]
#         img = Image.open(input_path)
#         transformed_img = transform(img)
#         output_path = os.path.join(augmented_dataset_path, f'{filename_no_ext}_aug')

# # Create the augmented dataset directory if it doesn't exist
# os.makedirs(augmented_dataset_path, exist_ok=True)
# # Function to augment and save an image
# def augment_and_save_image(image_path, save_path, transform, save_prefix, num_agument_images=3):
#     img = Image.open(image_path).convert('RGB')
#     for i in range(num_agument_images):
#         augment_image = transform(img)
#         augment_image.save(os.path.join(save_path, f"{save_prefix}_aug_{i}.png"))

# # Process each file in the original dataset directory
# for filename in os.listdir(original_dataset_path):
#     if filename.lower().endswith((".png", ".jpg", ".jpeg")):
#         file_path = os.path.join(original_dataset_path, filename)
#         filename_no_ext = os.path.splitext(filename)[0]
#         augment_and_save_image(file_path, augmented_dataset_path, transform, filename_no_ext)
















