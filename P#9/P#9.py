import cv2
import numpy as np
#cargar imagen
img_rgb = cv2.imread('EXAMPLE.jpg')
#Convertir a grises
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#Cargar plantilla
template = cv2.imread('TTTemplate.jpg',0)
#Tamaño de plantilla y propiedades
w, h = template.shape[::-1]

#Procesamiento y deteccion de las similitudes en objetos
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#Umbral
threshold = 0.85
loc = np.where( res >= threshold)
#Ciclo para mas de una coincidencia
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#Mostrar la imagen con las similitudes detectadas
cv2.imshow('Detected',img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
