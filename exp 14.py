import cv2
import numpy as np
image = cv2.imread("virat kohli.jpg")  
if image is None:
    print("Error: Image not found!")
    exit()
rows, cols = image.shape[:2]
pts1 = np.float32([[100, 100],
                   [400, 100],
                   [100, 400],
                   [400, 400]])
pts2 = np.float32([[50, 150],
                   [450, 50],
                   [100, 450],
                   [400, 400]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
perspective_image = cv2.warpPerspective(image, matrix, (cols, rows))
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", perspective_image)
cv2.waitKey(0)
cv2.destroyAllWindows()