import cv2
image = cv2.imread("virat kohli.jpg")
if image is None:
    print("Image not found 😐 Check path or file name")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()