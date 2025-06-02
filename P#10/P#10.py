import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar la imagen
img = cv2.imread('BACKGROUNDOFF.jpg')

# Eliminar fondo con grabCut
mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Rectángulo que contiene el primer plano (ajusta si es necesario)
rect = (480, 300, 500, 850)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Crear máscara para aplicar sobre la imagen
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img_nobg = img * mask2[:, :, np.newaxis]

# Convertir a escala de grises para detección de esquinas
gray = cv2.cvtColor(img_nobg, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Detectar esquinas
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.intp(corners)

# Dibujar las esquinas detectadas
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img_nobg, (x, y), 5, (0, 255, 0), -1)

# Mostrar imagen con esquinas detectadas
cv2.imshow('Esquinas detectadas', img_nobg)
cv2.waitKey(0)
cv2.destroyAllWindows()

