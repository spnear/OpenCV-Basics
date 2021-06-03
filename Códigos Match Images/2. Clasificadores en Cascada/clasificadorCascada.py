#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:52:11 2019

@author: sebastian
"""
import cv2 as cv
import numpy as np
#Crear objeto de ideo
captura = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
while True:
    grabbed,image = captura.read()
    if not grabbed:
        break
    image = cv.flip(image, 2)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors=5,
            minSize=(30,30),
            flags=cv.CASCADE_SCALE_IMAGE)
    idx = 0
    for(x,y,w,h) in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        idx += 1
        cv.putText(image,"Face #"+str(idx),(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(2,255,0),1)
    
    cv.imshow('Rostro',image)
    k = cv.waitKey(25) & 0xFF
    if k == 27:
        break
captura.release()
cv.destroyAllWindows()