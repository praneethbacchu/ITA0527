import cv2

car_cascade = cv2.CascadeClassifier("C:\Users\prane\Downloads\cars.xml")

cap = cv2.VideoCapture("C:\Users\prane\Videos\Video 1.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Vehicle Detection', frame)