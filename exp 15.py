import cv2
import numpy as np
image = cv2.imread("virat kohli.jpg")  
if image is None:
    print("Error: Image not found!")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
image[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow("Harris Corner Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()