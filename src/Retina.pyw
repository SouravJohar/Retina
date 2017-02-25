import cv2
import numpy as np
import pyautogui as pag

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face = False
currentEyes = False
previousEyes = False
videoState = ""
cap = cv2.VideoCapture(0)
while True:
    previousEyes = currentEyes
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) >= 1:
        face = True
    else:
        face = False
        currentEyes = False
    for (x,y,w,h) in faces:
        face = True
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        i = 0
        for (ex,ey,ew,eh) in eyes:
            if ey > 40 and ey < 100:
                currentEyes = True
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
         
    
    if previousEyes and currentEyes:
        print "playing"
    if not previousEyes and not currentEyes:
        "stopped"
    if not previousEyes and currentEyes:
        print "resume"
        pag.typewrite(" ")
    if previousEyes and not currentEyes:
        print "pause"
        pag.typewrite(" ")
    #cv2.imshow('frame',frame)
    k = cv2.waitKey(10)
    if k == 27:
        cv2.destroyAllWindows()
        break
