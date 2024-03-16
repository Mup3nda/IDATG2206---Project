import os
import shutil
from random import shuffle

# Configuration: adjust these paths according to your dataset
data_path = '/Users/didiermupenda/ANADROM_Datasets/1_Dataset'  # The directory containing all the data
train_images_path = '/Users/didiermupenda/ANADROM_Datasets/1_Dataset/images/train'  # Where training images will be placed
val_images_path = '/Users/didiermupenda/ANADROM_Datasets/1_Dataset/images/val'  # Where validation images will be placed
train_labels_path = '/Users/didiermupenda/ANADROM_Datasets/1_Dataset/labels/train'  # Where training labels will be placed
val_labels_path = '/Users/didiermupenda/ANADROM_Datasets/1_Dataset/labels/val'  # Where validation labels will be placed

image_ext = ['.PNG', '.png']
label_ext = ['.txt']

# Ensure the training and validation directories exist
os.makedirs(train_images_path, exist_ok=True)
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(train_labels_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)

# Get a list of all image files in the original data directory
all_files = os.listdir(data_path)
image_files = [f for f in all_files if any(f.endswith(ext) for ext in image_ext)]

shuffle(image_files)

# Split the files according to the 80/20 ratio
split_index = int(len(image_files)*0.8)
train_images = image_files[0:split_index]
val_images = image_files[split_index:]

# Function to move files to their designated directory
def move_files(files, source_path, dest_path):
    for filename in files:
        shutil.move(os.path.join(source_path, filename), os.path.join(dest_path, filename))

# Move the training images and labels
move_files(train_images, data_path, train_images_path)
for filename in train_images:
    label_file = os.path.splitext(filename)[0] + '.txt'
    if os.path.exists(os.path.join(data_path, label_file)):
        shutil.move(os.path.join(data_path, label_file), os.path.join(train_labels_path, label_file))

# Move the validation images and labels
move_files(val_images, data_path, val_images_path)
for filename in val_images:
    label_file = os.path.splitext(filename)[0] + '.txt'
    if os.path.exists(os.path.join(data_path, label_file)):
        shutil.move(os.path.join(data_path, label_file), os.path.join(val_labels_path, label_file))

print("Data splitting completed.")




