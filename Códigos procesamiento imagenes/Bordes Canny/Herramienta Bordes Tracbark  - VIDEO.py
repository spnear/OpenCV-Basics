import cv2
import numpy as np
from matplotlib import pyplot as plt
 
def nothing(x):
    pass



captura = cv2.VideoCapture(0)

w = int(captura.get(3))
h = int(captura.get(4))

resultado = np.zeros((h, 2*w,3), dtype="uint8") 
cv2.namedWindow('canny_edge',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('min_value','canny_edge',0,300,nothing)
cv2.createTrackbar('max_value','canny_edge',0,300,nothing)

while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break
        
        min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
        max_value = cv2.getTrackbarPos('max_value', 'canny_edge')
 
        canny_edge = cv2.Canny(imagen, min_value, max_value)
        canny_edge = cv2.merge((canny_edge,canny_edge,canny_edge))
        resultado[0:h,0:w]=imagen
        resultado[0:h,w:2*w]=canny_edge
        #Mostramos imagen  
        cv2.imshow('canny_edge', resultado)
        
        #Capturamos teclado
        tecla = cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla == 27:
                 break
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()
