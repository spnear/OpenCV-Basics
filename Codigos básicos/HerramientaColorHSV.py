import cv2
import numpy as np

# Funcion asociado al evento Mouse
def hsv_color(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        
        h = img_hsv[y,x,0]
        s  = img_hsv[y,x,1]
        v = img_hsv[y,x,2]
        color[0:150,:] = [h,s,v]
        color[151:200,:] = [255,255,255]
        cv2.putText(color,'H:'+str(h),(10,175), font, 0.5,(0,0,255),1,cv2.LINE_AA)
        cv2.putText(color,'S:'+str(s),(75,175), font, 0.5,(0,255,0),1,cv2.LINE_AA)
        cv2.putText(color,'V:'+str(v),(140,175), font, 0.5,(255,0,0),1,cv2.LINE_AA)
        #print blue
        #print green
        #print red

font = cv2.FONT_HERSHEY_SIMPLEX
#Lectura de la imagen a analizar
img = cv2.imread('colores.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('Imagen RGB')
cv2.namedWindow('HSV')
#Creacion de imagen Negra
color= np.zeros((200,200,3), np.uint8)
cv2.setMouseCallback('Imagen RGB',hsv_color)

while(1):
    cv2.imshow('Imagen RGB',img)
    cv2.imshow('HSV',color)
    cv2.imshow('HSV imagen',img_hsv)
    if cv2.waitKey(30) & 0xFF == 27:
        break
cv2.destroyAllWindows()
