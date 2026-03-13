import cv2
import numpy as np

# Image size (chosen values)
height = 500
width = 500

# Create white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Box size (1/10 of image)
box_h = height // 10
box_w = width // 10

# Top-left corner (Black)
img[0:box_h, 0:box_w] = (0, 0, 0)

# Top-right corner (Blue)
img[0:box_h, width-box_w:width] = (255, 0, 0)

# Bottom-left corner (Green)
img[height-box_h:height, 0:box_w] = (0, 255, 0)

# Bottom-right corner (Red)
img[height-box_h:height, width-box_w:width] = (0, 0, 255)

# Show image
cv2.imshow("Colored Boxes Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()