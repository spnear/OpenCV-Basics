import cv2
import numpy as np

# Limite Inferior
color_RGB = np.uint8([[[40,50,44 ]]])
color_HSV = cv2.cvtColor(color_RGB,cv2.COLOR_BGR2HSV)
print("Limite Inferior: ", color_HSV )

# Limite Superior
color_RGB = np.uint8([[[170,255,0 ]]])
color_HSV = cv2.cvtColor(color_RGB,cv2.COLOR_BGR2HSV)
print("Limite Superior: ", color_HSV )

# Verificacion de color
color_HSV = np.uint8([[[80,255,255 ]]])
color_RGB = cv2.cvtColor(color_HSV,cv2.COLOR_HSV2BGR)
print( color_RGB )

