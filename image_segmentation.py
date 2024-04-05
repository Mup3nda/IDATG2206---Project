import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "/Users/didiermupenda/Desktop/NTNU/CV/Assigment/Tesla_roadster.jpeg"  
image = cv2.imread(image_path)

# Converts the image to RGB befor converting to HSV color space
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# Define range of red color in HSV
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Create masks for red color
mask1 = cv2.inRange(image_hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(image_hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

# Create an image with the masked areas filled with light purple color
light_purple = [191, 128, 255]  
image_with_mask = image_rgb.copy()
image_with_mask[red_mask != 0] = light_purple

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(red_mask, cmap='gray')
plt.title('Masked')

plt.subplot(1, 3, 3)
plt.imshow(image_with_mask)
plt.title('Purple Mask Overlaid')

plt.show()
