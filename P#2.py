import numpy as np
import cv2

ruta_imagen = r'C:\Users\educo\OneDrive\Escritorio\Ceti\6to Semestre\Vision Artificial\GitHub\2025-Visi-n-Artificial-22310172\watch.jpg'

img = cv2.imread(ruta_imagen, cv2.IMREAD_COLOR)

if img is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta y la extensión del archivo.")
    exit()

img[55,55] = [255,255,255]
px = img[55,55]

img[100:150, 100:150] = [255,255,255]

watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
