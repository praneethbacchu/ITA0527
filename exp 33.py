import cv2
import numpy as np

# Image size (chosen values)
height = 400
width = 400

# Create a white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Rectangle coordinates
start_point = (100, 100)
end_point = (300, 300)

# Rectangle color (Green)
color = (0, 255, 0)

# Thickness
thickness = 3

# Draw rectangle
cv2.rectangle(img, start_point, end_point, color, thickness)

# Display image
cv2.imshow("Rectangle Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()