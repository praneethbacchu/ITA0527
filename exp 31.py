import cv2

# Read input image
image = cv2.imread("virat kohli.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply threshold segmentation
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Show original and segmented image
cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()