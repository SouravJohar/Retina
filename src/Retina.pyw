import cv2
import numpy as np
import pyautogui as pag
import psutil
import os

face_cascade = cv2.CascadeClassifier('appData/haarcascade_frontalface_default.xml')
previousEyes = currentEyes = "0"
runningState = False
f = open(r"\\VBOXSVR\Code\Retina\src\ForceStopRetina", "w+")
while "ForceStopRetina" in os.listdir(r"\\VBOXSVR\\Code\\Retina\\src\\"):
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
        currentEyes = ["1", "0"][len(faces) < 1]
        
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
else:
    pag.alert(text='Retina is stopped', title='Retina', button='OK')
    

    
