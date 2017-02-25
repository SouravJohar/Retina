import cv2
import numpy as np
import pyautogui as pag
import psutil

eye_cascade = cv2.CascadeClassifier('appData/haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('appData/haarcascade_frontalface_default.xml')
previousEyes = currentEyes = "0"
runningState = False

while True:
    try:
        processes = [psutil.Process(i).name for i in psutil.pids()]
        if "vlc.exe" in str(processes):
            runningState = True
        if runningState:
            cap = cv2.VideoCapture(0)
    except:
        pass
    while runningState:
        previousEyes = currentEyes
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) < 1:
            currentEyes = "0"
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                if ey > 40 and ey < 100:
                    currentEyes = "1"
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        if previousEyes + currentEyes == "01":
            pag.hotkey('Shift', '2') #resume
        if previousEyes + currentEyes == "10":
            pag.hotkey('Shift', '1') #pause
        try:
            processes = [psutil.Process(i).name() for i in psutil.pids()]
            cv2.namedWindow('Retina',cv2.WINDOW_NORMAL)
            cv2.imshow('Retina',frame)
            k = cv2.waitKey(10)
            if "vlc.exe" not in str(processes):
                pag.alert(text='Retina is haulted', title='Retina', button='OK')
                runningState = False
                cap.release()
                cv2.destroyAllWindows()
                break
        except:
            pass
