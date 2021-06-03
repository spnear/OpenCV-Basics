import cv2
import numpy as np

# Funcion asociado al evento Mouse
def rgb_color(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        
        blue = img[y,x,0]
        green  = img[y,x,1]
        red = img[y,x,2]
        color[0:150,:] = [blue,green,red]
        color[151:200,:] = [255,255,255]
        cv2.putText(color,'R:'+str(red),(10,175), font, 0.5,(0,0,255),1,cv2.LINE_AA)
        cv2.putText(color,'G:'+str(green),(75,175), font, 0.5,(0,255,0),1,cv2.LINE_AA)
        cv2.putText(color,'B:'+str(blue),(140,175), font, 0.5,(255,0,0),1,cv2.LINE_AA)
        #print blue
        #print green
        #print red

font = cv2.FONT_HERSHEY_SIMPLEX
#Lectura de la imagen a analizar
img = cv2.imread('2.jpg')
cv2.namedWindow('Imagen RGB')
cv2.namedWindow('RGB')
#Creacion de imagen Negra
color= np.zeros((200,200,3), np.uint8)
cv2.setMouseCallback('Imagen RGB',rgb_color)

while(1):
    cv2.imshow('Imagen RGB',img)
    cv2.imshow('RGB',color)
    if cv2.waitKey(30) & 0xFF == 27:
        break
cv2.destroyAllWindows()
