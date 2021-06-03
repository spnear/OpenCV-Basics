
import cv2
import numpy as np
"""
Valores HSV para colores

VERDE
verde_bajos  = [49,50,50]
verdes_altos = [80, 255, 255]


AZUL
azul_bajos = [100,65,75]
azul_altos = [130, 255, 255]


ROJO
Habrá que crear dos rangos diferentes para los rojos:
uno que tenga el Hue entre 0 y 20 y el otro entre 240 y 255.

rojo_bajos1 = [0,65,75]
rojo_altos1 = [12, 255, 255]
rojo_bajos2 = [240,65,75]
rojo_altos2 = [256, 255, 255]

PIEL
piel_bajos = [0, 48, 80]
piel_altos = [20, 255, 255]

"""

cap = cv2.VideoCapture(0)
 
def nothing(x):
   pass
 
#Creamos una ventana para todos los sliders
cv2.namedWindow('HSV Color Range',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('H Minimo','HSV Color Range',0,179,nothing)
cv2.createTrackbar('H Maximo','HSV Color Range',0,179,nothing)
cv2.createTrackbar('S Minimo','HSV Color Range',0,255,nothing)
cv2.createTrackbar('S Maximo','HSV Color Range',0,255,nothing)
cv2.createTrackbar('V Minimo','HSV Color Range',0,255,nothing)
cv2.createTrackbar('V Maximo','HSV Color Range',0,255,nothing)
 
while(1):
        grabbed,frame = cap.read() #Leer un frame
        if not grabbed:
              break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convertirlo a espacio de color HSV
 
       #Los valores maximo y minimo de H,S y V se guardan en funcion de la posicion de los sliders
        hMin = cv2.getTrackbarPos('H Minimo','HSV Color Range')
        hMax = cv2.getTrackbarPos('H Maximo','HSV Color Range')
        sMin = cv2.getTrackbarPos('S Minimo','HSV Color Range')
        sMax = cv2.getTrackbarPos('S Maximo','HSV Color Range')
        vMin = cv2.getTrackbarPos('V Minimo','HSV Color Range')
        vMax = cv2.getTrackbarPos('V Maximo','HSV Color Range')

        print hMin
 
        #Se crea un array con las posiciones minimas y maximas
        lower=np.array([hMin,sMin,vMin])
        upper=np.array([hMax,sMax,vMax])
 
        #Deteccion de colores
        
        mask = cv2.inRange(hsv, lower, upper)
        
           
 
        #Mostrar los resultados y salir
        cv2.imshow('camara',frame)
        cv2.imshow('mask',mask)
        k = cv2.waitKey(55) & 0xFF
        if k == 27:
         break
cap.release() 
cv2.destroyAllWindows()

