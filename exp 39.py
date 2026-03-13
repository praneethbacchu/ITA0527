import cv2

# Read the video
cap = cv2.VideoCapture("sail.mp4")

frames = []

# Store all frames in a list
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play video in reverse with slow motion
for frame in reversed(frames):
    cv2.imshow("Reverse Slow Motion Video", frame)
    
    # Delay for slow motion (100 ms)
    if cv2.waitKey(100) & 0xFF == 27:
        break

cv2.destroyAllWindows()