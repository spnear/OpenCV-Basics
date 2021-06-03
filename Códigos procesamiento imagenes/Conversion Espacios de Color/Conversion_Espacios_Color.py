import cv2
import numpy as np

"""
Conversion Espacios de Color
-BGR2GRAY
-BGR2HSV
-BGR2YCrCb
"""

#Creamos el objetto de video
captura = cv2.VideoCapture(0)
espacio = "BGR"
bgr = True
hsv = False
gray = False
ycrcb = False
lab = False
while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break       
         

        #Capturamos teclado
        tecla = cv2.waitKey(25) & 0xFF
        if tecla == ord("l"):
                 lab = True 
                 ycrcb = True
                 bgr = False
                 gray = False
                 hsv = False
        if tecla == ord("y"):
                 ycrcb = True
                 bgr = False
                 gray = False
                 hsv = False
                 lab = False
        if tecla == ord("b"):
                 bgr = True
                 gray = False
                 hsv = False
                 ycrcb = False
                 lab = False
        if tecla == ord("g"):
                 gray = True
                 bgr = False
                 hsv = False
                 ycrcb = False
                 lab = False
        if tecla == ord("h"):
                 hsv = True
                 bgr = False
                 gray = False
                 ycrcb = False
                 lab = False
        #Salimos si la tecla presionada es ESC
        if tecla == 27:
                 break

        if bgr == True:
                imagen = imagen
                espacio = "BGR"
        if gray == True:
                img_gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
                imagen = cv2.merge((img_gray,img_gray,img_gray))
                espacio = "GRAY"
        if hsv == True:
                img_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
                imagen = img_hsv
                espacio = "HSV"
        if ycrcb == True:
                img_ycrcb = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb)
                imagen = img_ycrcb
                espacio = "YCrCb"
        if lab == True:
                img_lab = cv2.cvtColor(imagen, cv2.COLOR_BGR2Lab)
                imagen = img_lab
                espacio = "Lab"
                
        imagen[0:50,0:100] = (10,10,10)
        cv2.putText(imagen,espacio, (20, 30),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255),1, cv2.LINE_AA)
        #Mostramos imagen 
        cv2.imshow('Espacios de Color', imagen)
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()

