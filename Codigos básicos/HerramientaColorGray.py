import cv2
import numpy as np

# Funcion asociado al evento Mouse
def gray_color(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        
        i = img_gray[y,x]
       
        color[0:150,:] = [i,i,i]
        color[151:200,:] = [255,255,255]
        cv2.putText(color,'Intensidad:'+str(i),(10,175), font, 0.5,(0,0,255),1,cv2.LINE_AA)
        

font = cv2.FONT_HERSHEY_SIMPLEX
#Lectura de la imagen a analizar
img = cv2.imread('2.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Imagen RGB')
#Creacion de imagen Negra
color= np.zeros((200,200,3), np.uint8)
cv2.setMouseCallback('Imagen RGB',gray_color)

while(1):
    cv2.imshow('Imagen RGB',img)
    cv2.imshow('Intensidad',color)
    cv2.imshow('Imagen Escala de Grises',img_gray)
    if cv2.waitKey(30) & 0xFF == 27:
        break
cv2.destroyAllWindows()
