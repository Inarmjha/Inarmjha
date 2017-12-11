import subprocess
import numpy as np
import cv2
import sys
from socket import *
import server
face_cascade = cv2.CascadeClassifier('charan1.xml')
video_capture = cv2.VideoCapture(0)
recognizer=cv2.createLBPHFaceRecognizer();
recognizer.load("recognizer/trainingData.yml")
id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,6,1,0,1)
s=server.sendbind()
#s1=server.receivebind()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
       
        server.datasend(str(id),s,frame)
        #server.datareceive(s1)
        cv2.cv.PutText(cv2.cv.fromarray(frame),str(id),(x,y+h),font,255);
        #subprocess.call('espeak '+str(id),shell=True)     
    #cv2.imshow('img', frame)
    if(cv2.waitKey(1)==ord('q')):
          break; 
video_capture.release()
cv2.destroyAllWindows()
