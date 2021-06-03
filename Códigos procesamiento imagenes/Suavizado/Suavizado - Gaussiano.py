
import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
def sp_noise(image,prob):
    '''
    Adiciona ruido sal y pimienta a imagen
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def nothing(x):
    
    pass

#Creamos el objetto de video
captura = cv2.VideoCapture(0)
cv2.namedWindow('Filtro Gaussiano',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('Tipo','Filtro Gaussiano',0,10,nothing)
while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break
        imagen = sp_noise(imagen,0.05)
        N = cv2.getTrackbarPos('Tipo', 'Filtro Gaussiano')
        if N!=0:
            
            N= 2*N + 1
            imagen = cv2.GaussianBlur(imagen, (N,N),0)
            dimension = 'kernel: '+str(N)+'x'+str(N)
            
            imagen[0:50,0:180] = (10,10,10)
            cv2.putText(imagen,dimension, (20, 30),
                                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255),1, cv2.LINE_AA)
        #Mostramos imagen  
        cv2.imshow('Filtro Gaussiano', imagen)
        
        #Capturamos teclado
        tecla = cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla == 27:
                 break
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()


 





 

#img = cv2.blur(img_noblur, (7,7))
 

cv2.destroyAllWindows()
