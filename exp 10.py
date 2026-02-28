import cv2
image = cv2.imread("virat kohli.jpg")  
if image is None:
    print("Error: Image not found!")
    exit()
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image (90° Clockwise)", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()