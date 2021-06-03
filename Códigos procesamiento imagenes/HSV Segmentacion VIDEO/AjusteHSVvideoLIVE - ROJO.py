
import cv2
import numpy as np
"""
Valores HSV para colores

ROJO
Habrá que crear dos rangos diferentes para los rojos:
uno que tenga el Hue entre 0 y 20 y el otro entre 240 y 255.

rojo_bajos1 = [0,65,75]
rojo_altos1 = [12, 255, 255]
rojo_bajos2 = [240,65,75]
rojo_altos2 = [256, 255, 255]


"""

cap = cv2.VideoCapture(0)
 
def nothing(x):
   pass
 
#Creamos una ventana para ROJOS BAJOS
cv2.namedWindow('HSV Color ROJOS BAJOS',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('H Minimo','HSV Color ROJOS BAJOS',0,179,nothing)
cv2.createTrackbar('H Maximo','HSV Color ROJOS BAJOS',0,179,nothing)
cv2.createTrackbar('S Minimo','HSV Color ROJOS BAJOS',0,255,nothing)
cv2.createTrackbar('S Maximo','HSV Color ROJOS BAJOS',0,255,nothing)
cv2.createTrackbar('V Minimo','HSV Color ROJOS BAJOS',0,255,nothing)
cv2.createTrackbar('V Maximo','HSV Color ROJOS BAJOS',0,255,nothing)

#Creamos una ventana para ROJOS ALTOS
cv2.namedWindow('HSV Color ROJOS ALTOS',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('H Minimo','HSV Color ROJOS ALTOS',0,179,nothing)
cv2.createTrackbar('H Maximo','HSV Color ROJOS ALTOS',0,179,nothing)
cv2.createTrackbar('S Minimo','HSV Color ROJOS ALTOS',0,255,nothing)
cv2.createTrackbar('S Maximo','HSV Color ROJOS ALTOS',0,255,nothing)
cv2.createTrackbar('V Minimo','HSV Color ROJOS ALTOS',0,255,nothing)
cv2.createTrackbar('V Maximo','HSV Color ROJOS ALTOS',0,255,nothing)

 
while(1):
        grabbed,frame = cap.read() #Leer un frame
        if not grabbed:
              break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convertirlo a espacio de color HSV
 
       #Los valores maximo y minimo de H,S y V se guardan en funcion de la posicion de los sliders
        hMin_1 = cv2.getTrackbarPos('H Minimo','HSV Color ROJOS BAJOS')
        hMax_1 = cv2.getTrackbarPos('H Maximo','HSV Color ROJOS BAJOS')
        sMin_1 = cv2.getTrackbarPos('S Minimo','HSV Color ROJOS BAJOS')
        sMax_1 = cv2.getTrackbarPos('S Maximo','HSV Color ROJOS BAJOS')
        vMin_1 = cv2.getTrackbarPos('V Minimo','HSV Color ROJOS BAJOS')
        vMax_1 = cv2.getTrackbarPos('V Maximo','HSV Color ROJOS BAJOS')

        hMin_2 = cv2.getTrackbarPos('H Minimo','HSV Color ROJOS ALTOS')
        hMax_2 = cv2.getTrackbarPos('H Maximo','HSV Color ROJOS ALTOS')
        sMin_2 = cv2.getTrackbarPos('S Minimo','HSV Color ROJOS ALTOS')
        sMax_2 = cv2.getTrackbarPos('S Maximo','HSV Color ROJOS ALTOS')
        vMin_2 = cv2.getTrackbarPos('V Minimo','HSV Color ROJOS ALTOS')
        vMax_2 = cv2.getTrackbarPos('V Maximo','HSV Color ROJOS ALTOS')

        
 
        #Se crea un array con las posiciones minimas y maximas
        lower_1=np.array([hMin_1,sMin_1,vMin_1])
        upper_1=np.array([hMax_1,sMax_1,vMax_1])

        lower_2=np.array([hMin_2,sMin_2,vMin_2])
        upper_2=np.array([hMax_2,sMax_2,vMax_2])
 
        #Deteccion de colores
        
        mask_1 = cv2.inRange(hsv, lower_1, upper_1)
        mask_2 = cv2.inRange(hsv, lower_2, upper_2)
        mask = cv2.add(mask_1,mask_2)
        
           
 
        #Mostrar los resultados y salir
        cv2.imshow('camara',frame)
        cv2.imshow('mask',mask)
        k = cv2.waitKey(55) & 0xFF
        if k == 27:
         break
cap.release() 
cv2.destroyAllWindows()

