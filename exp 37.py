import cv2
import numpy as np

# Read input image
image = cv2.imread("virat kohli.jpg")

# Convert image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Chosen HSV range for red foreground
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Create mask for foreground color
mask = cv2.inRange(hsv, lower_red, upper_red)

# Remove foreground using inverted mask
result = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Foreground Removed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()