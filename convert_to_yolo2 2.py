import xml.etree.ElementTree as ET
import os

def convert_bbox_to_yolo(img_width, img_height, xtl, ytl, xbr, ybr):
    x_center = (xtl + xbr) / 2
    y_center = (ytl + ybr) / 2
    bbox_width = xbr - xtl
    bbox_height = ybr - ytl

    x_center_norm = x_center / img_width
    y_center_norm = y_center / img_height
    bbox_width_norm = bbox_width / img_width
    bbox_height_norm = bbox_height / img_height
    return(x_center_norm, y_center_norm, bbox_width_norm, bbox_height_norm)

def process_frames(xml_file, class_mapping):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    img_width = int(root.find('.//original_size/width').text)
    img_height = int(root.find('.//original_size/height').text)

    yolo_annotations = {}

    for track in root.findall('.//track'):
        class_name = track.get('label')
        class_id = class_mapping.get(class_name, -1)  # Default to -1 if class name not found

        for box in track.findall('.//box'):
            frame_num = box.get('frame')
            xtl = float(box.get('xtl'))
            ytl = float(box.get('ytl'))
            xbr = float(box.get('xbr'))
            ybr = float(box.get('ybr'))

            yolo_bbox = convert_bbox_to_yolo(img_width, img_height, xtl, ytl, xbr, ybr)

            if frame_num not in yolo_annotations:
                yolo_annotations[frame_num] = []
            yolo_annotations[frame_num].append([class_id]+list(yolo_bbox))

    return yolo_annotations

def save_yolo_annotations(yolo_annotations, output_dir):
    for frame_num, annotations in yolo_annotations.items():
        yolo_file_name = f"frame_{frame_num.zfill(6)}.txt"
        yolo_file_path = os.path.join(output_dir, yolo_file_name)

        with open(yolo_file_path, 'w') as file:
            for annotation in annotations:
                annotation_str = " ".join(map(str, annotation))
                file.write(annotation_str+'\n')

# Definer en mapping mellom klassenavn i XML-filen og deres tilsvarende klasse-IDer
class_mapping = {
    'class_name_1': 0,
    'class_name_2': 1,
    'class_name_2': 2,
    'class_name_2': 3,
    # Legg til flere klasser etter behov
}

xml_file = '/Users/didiermupenda/ANADROM_Datasets/Annotation/task_fish_detection-2024_02_01_18_41_23-cvat for video 1.1/annotations.xml'
yolo_annotations = process_frames(xml_file, class_mapping)
output_dir = '/Users/didiermupenda/ANADROM_Datasets/Annotation/task_fish_detection-2024_02_01_18_41_23-cvat for video 1.1/labels'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

save_yolo_annotations(yolo_annotations, output_dir)
