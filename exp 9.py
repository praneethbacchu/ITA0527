import cv2
image = cv2.imread("virat kohli.jpg")  
if image is None:
    print("Error: Image not found!")
    exit()
height, width = image.shape[:2]
bigger_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)
cv2.waitKey(0)
cv2.destroyAllWindows()