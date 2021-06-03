import cv2
import numpy as np

#Creamos el objetto de video
captura = cv2.VideoCapture(0)
marca = cv2.imread('marca_2.png',1)

while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break
        suma  =  cv2.addWeighted(imagen,0.9,marca,0.1,0)
        #Mostramos imagen  
        cv2.imshow('Video', suma)
        #Capturamos teclado
        tecla = cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla == 27:
                 break
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()

