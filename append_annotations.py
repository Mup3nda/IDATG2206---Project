import os
import shutil
import numpy as np


src_labels_path = '/Users/didiermupenda/ANADROM_Datasets/Annotation/task_fish_detection-2024_02_01_18_41_23-cvat for video 1.1/labels'
dest_labels_path = '/Users/didiermupenda/ANADROM_Datasets/Annotation/task_fish_detection-2024_02_01_18_41_23-cvat for video 1.1/aug_labels'

os.makedirs(dest_labels_path, exist_ok=True)

for filename in os.listdir(src_labels_path):
    file_name_no_ext, ext = os.path.splitext(filename)
    for i in range(3):
        new_filename = f'{file_name_no_ext}_aug{i+1}{ext}'
        copy_file_path = os.path.join(dest_labels_path, new_filename)
        original_file_path = os.path.join(src_labels_path, filename)

        shutil.copy(original_file_path, copy_file_path)
    

print("Appending annotations complete.")