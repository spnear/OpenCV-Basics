
import cv2
import numpy as np
from matplotlib import pyplot as plt

# calculo de histograma

img = cv2.imread('4.jpg',0)

plt.subplot(2,1,1), plt.imshow(img,cmap = 'gray')
plt.title('Imagen Escala de Grises'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2), plt.hist(img.ravel(), 256)
plt.title('Histograma'), plt.xticks(np.arange(0, 255, step=25)), plt.yticks([])
plt.xlabel('Valor de los pixels (Intensidad)')
plt.ylabel('Cantidad de pixeles')
plt.xlim(0,260)

plt.show()
