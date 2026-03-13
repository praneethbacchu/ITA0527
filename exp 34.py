import cv2
import numpy as np

# Image size (chosen values)
height = 400
width = 400

# Create white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Circle parameters
center = (200, 200)
radius = 80
color = (255, 0, 0)   # Blue in BGR
thickness = 3

# Draw circle
cv2.circle(img, center, radius, color, thickness)

# Display image
cv2.imshow("Circle Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()