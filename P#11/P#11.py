import numpy as np
import cv2
import matplotlib.pyplot as plt

# Cargar Imagenes
img1 = cv2.imread('Cutter.jpg', 0)
img2 = cv2.imread('Imgcutter.jpg', 0)

# Detector ORB
orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Matcher BRUTEFORCE con norma Hamming
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Dibujar las mejores 10 coincidencias
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

# Mostrar imagen con coincidencias
plt.imshow(img3)
plt.title('Coincidencias ORB')
plt.axis('off')
plt.show()
