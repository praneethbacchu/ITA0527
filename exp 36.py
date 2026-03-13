import cv2
import numpy as np

# Read input image
image = cv2.imread("virat kohli.jpg")

# Convert image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Chosen HSV range for green background
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# Create mask
mask = cv2.inRange(hsv, lower_green, upper_green)

# Invert mask to keep foreground
mask_inv = cv2.bitwise_not(mask)

# Apply mask to remove background
result = cv2.bitwise_and(image, image, mask=mask_inv)

# Show images
cv2.imshow("Original Image", image)
cv2.imshow("Background Subtracted Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()