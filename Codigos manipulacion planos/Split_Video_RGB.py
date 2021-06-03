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
print planos.shape
while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Redimensionar imagen
        imagen = cv2.resize(imagen,(w,h))
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break
        # Division de canales
        b , g , r  =  cv2.split(imagen)
        plano_b = cv2.merge((b,b,b))
        plano_g = cv2.merge((g,g,g))
        plano_r = cv2.merge((r,r,r))
        planos[0:h,0:w]=imagen
        planos[0:h,w:2*w]=plano_r
        planos[h:2*h,0:w]=plano_g
        planos[h:2*h,w:2*w]=plano_b
        cv2.putText(planos,"Entrada", (10, 20),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1, cv2.LINE_AA)
        cv2.putText(planos,"Plano-R", (w+10, 20),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),1, cv2.LINE_AA)
        cv2.putText(planos,"Plano-G", (10,h+20),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),1, cv2.LINE_AA)
        cv2.putText(planos,"Plano-B", (w+10,h+20),
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


