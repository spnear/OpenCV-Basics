import cv2
import numpy as np

import cv2
import numpy as np

#Creamos el objetto de video
captura = cv2.VideoCapture(0)
w = int(captura.get(3))
h = int(captura.get(4))
w = int(w/2)
h = int(h/2)
planos = np.zeros((2*h, 2*w,3), dtype="uint8")
print(planos.shape)
while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Redimensionar imagen
        imagen = cv2.resize(imagen,(w,h))
        img_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
        # Si hemos llegado al final del v�deo salimos
        if not grabbed:
            break
        # Division de canales
        H , S , V  =  cv2.split(img_hsv )
        plano_H = cv2.merge((H,H,H))
        plano_S = cv2.merge((S,S,S))
        plano_V = cv2.merge((V,V,V))
        planos[0:h,0:w]=imagen
        planos[0:h,w:2*w]=plano_H
        planos[h:2*h,0:w]=plano_S
        planos[h:2*h,w:2*w]=plano_V
        cv2.putText(planos,"Entrada", (10, 20),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1, cv2.LINE_AA)
        cv2.putText(planos,"Plano-H", (w+10, 20),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),1, cv2.LINE_AA)
        cv2.putText(planos,"Plano-S", (10,h+20),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),1, cv2.LINE_AA)
        cv2.putText(planos,"Plano-V", (w+10,h+20),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0),1, cv2.LINE_AA)
        
        #Mostramos imagen  
        cv2.imshow('Video', planos)
        #Capturamos teclado
        tecla = cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla == 27:
                 break
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()


