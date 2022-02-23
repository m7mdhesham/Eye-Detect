import cv2
import numpy as np
import pygame.mixer
pygame.init()
pygame.mixer.music.load("beep-01a.wav")

cap = cv2.VideoCapture(0)
path = "haarcascade_eye.xml"


while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx = 1.25, fy = 1.25)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eye_cascade = cv2.CascadeClassifier(path)
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors =20, minSize =(10,10))
    
    if (len(eyes) == 0):
        pygame.mixer.music.play()

    for (x,y,w,h) in eyes:
        xc = int(((2*x) +w)/2)
        yc = int(((2*y) +h)/2)
        radius = int(w/2)
        
        cv2.circle(frame, (xc, yc), radius, (0,255,0), 2)

    cv2.imshow("cam", frame) 
    w = cv2.waitKey(1)

    if w & 0xFF == ord('k'):
        break

cap.release()
cv2.destroyAllWindows()