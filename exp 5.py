import cv2
import numpy as np
import matplotlib.pyplot as plt
def analyze_color_histogram(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return
    b, g, r = cv2.split(image)
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
    plt.figure(figsize=(10,6))
    plt.title("Color Histogram Analysis")
    plt.xlabel("Intensity Value")
    plt.ylabel("Pixel Count")
    plt.plot(hist_b, color='blue', label='Blue Channel')
    plt.plot(hist_g, color='green', label='Green Channel')
    plt.plot(hist_r, color='red', label='Red Channel')
    plt.xlim([0, 256])
    plt.legend()
    plt.show()
    print("Blue Channel - Min:", np.min(b), "Max:", np.max(b))
    print("Green Channel - Min:", np.min(g), "Max:", np.max(g))
    print("Red Channel - Min:", np.min(r), "Max:", np.max(r))
analyze_color_histogram("virat kohli.jpg")