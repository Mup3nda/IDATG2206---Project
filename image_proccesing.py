import cv2
import numpy as np

# Load the image
image = cv2.imread('images/test/frame_000248.PNG')

# Convert to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define a range for the color of the fish
# You need to adjust these thresholds to match the color of the fish
lower_bound = np.array([0, 50, 50])
upper_bound = np.array([10, 255, 255])

# Threshold the HSV image to get only the colors of the fish
mask = cv2.inRange(hsv, lower_bound, upper_bound)

# Display the mask to verify that it looks correct
cv2.imshow('Mask', mask)

# Optional: apply morphology close and open to refine the mask
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Find contours on the mask
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Check the size of the contours
for cnt in contours:
    area = cv2.contourArea(cnt)
    print(f'Contour area: {area}')

# Assume fish has a significant size and filter out smaller contours
min_area = 1000  # Adjust this value based on your specific image
fish_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

# Draw contours on the original image
for cnt in fish_contours:
    cv2.drawContours(image, [cnt], -1, (0, 255, 0), 3)

# Display the original image with the contours if any contours are detected
if fish_contours:
    cv2.imshow('Fish Detection', image)
else:
    print("No fish contours detected.")

cv2.waitKey(0)
cv2.destroyAllWindows()
