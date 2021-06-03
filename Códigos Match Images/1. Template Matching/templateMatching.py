#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

imagen = cv2.imread('Mario.jpg')
patron = cv2.imread('plantilla_mario.png')
 # Conversion a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
patron_gris = cv2.cvtColor(patron, cv2.COLOR_BGR2GRAY)

h,w = patron_gris.shape

resultado = cv2.matchTemplate(imagen_gris,patron_gris,cv2.TM_CCOEFF_NORMED)
umbral = 0.87

cv2.imshow('maximos',resultado)

ubicaciones = np.where( resultado >= umbral)
print(np.shape(ubicaciones))
#Finalmente, marcamos todas las coincidencias en la imagen original,
#usando las coordenadas que encontramos en la imagen gris:

for pt in zip(*ubicaciones[::-1]):
    cv2.rectangle(imagen, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

cv2.imshow("Imagen",imagen)
cv2.imshow("Plantilla",patron)
cv2.waitKey(0)
cv2.destroyAllWindows()

