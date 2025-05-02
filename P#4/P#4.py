import numpy as np
import cv2
#Cargar imagen
img = cv2.imread('manzana.jpg',cv2.IMREAD_COLOR)
#Dibujar formas
cv2.line(img,(0,0),(200,300),(255,255,255),50)
cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)
cv2.circle(img,(447,63), 63, (0,255,0), -1)
#Interpolacion de puntos
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
#Escribir en la imagen
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img,'Eduardo CF',(10,500), font, 4, (200,255,155), 5, cv2.LINE_AA)
#Mostrar la imagen
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
