import numpy as np
import cv2


image = cv2.imread('4.jpg')

# Convertimos a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh = 55

# Umbral Binario
retVal1, dst1 = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
# Umbral Binario Invertido
retVal2, dst2 = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('umbral', image)
cv2.imshow('resultado', dst1)


cv2.waitKey(0)
cv2.destroyAllWindows()

"""
umbrales
8.jpg - 120
9.jpg - 120


utilizar imagen 12.jpg con umbral de 180 para analizar la utilidad de la erosion
como metodo de elimnacion de ruido


PREUBAS REALIZADAS
MALETIN     T = 220
HOMBRE SOLO T = 220
gorra       T = 220
tomates     T = 55


"""
