

import numpy as np
import cv2
import sys
face_cascade = cv2.CascadeClassifier('charan1.xml')
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    
    cv2.imshow('Video', frame)
    cv2.imwrite('facedetection.jpg',frame)
    if(cv2.waitKey(1)==ord('q')):
          break; 
video_capture.release()
cv2.destroyAllWindows()
