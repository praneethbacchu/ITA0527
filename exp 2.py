import cv2
image = cv2.imread("virat kohli.jpg")
if image is None:
    print("Error: Image not found. Please check file path.")
else:
    print("Image Shape (Height, Width, Channels):", image.shape)
    print("Image Size (Total Pixels):", image.size)
    print("Image Data Type:", image.dtype)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.imshow("Gaussian Blurred Image", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()