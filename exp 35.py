import cv2
import numpy as np

# Image size (chosen values)
height = 400
width = 600

# Create white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Text to display
text = "OpenCV"

# Text parameters
position = (150, 200)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 0, 0)   # Black
thickness = 2

# Put text on image
cv2.putText(img, text, position, font, font_scale, color, thickness)

# Display image
cv2.imshow("Text on Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()