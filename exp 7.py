import cv2
cap = cv2.VideoCapture("sail.mp4")   
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
print("Press 'q' to exit")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Normal Video", frame)
    cv2.imshow("Slow Motion", frame)
    cv2.waitKey(100)   
    cv2.imshow("Fast Motion", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):  
        break
cap.release()
cv2.destroyAllWindows()