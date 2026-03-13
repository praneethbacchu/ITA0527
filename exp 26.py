import cv2
cap = cv2.VideoCapture("sail.mp4")
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()
frames.reverse()
height, width, layers = frames[0].shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("reverse_video.avi", fourcc, 30, (width, height))
for frame in frames:
    out.write(frame)
    cv2.imshow("Reversed Video", frame)
    cv2.waitKey(30)
out.release()
cv2.destroyAllWindows()