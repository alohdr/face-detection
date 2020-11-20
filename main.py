import cv2

cam = cv2.VideoCapture(1)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    retV, frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),5)
        frame2 = cv2.rectangle(gray, (x,y),(x+w,y+h),(0,0,255),5)
    cv2.imshow('webcameku', frame)
    cv2.imshow('webcameku 2', gray)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord ('q'):
        break
cam.release()
cv2.destroyAllWindows()