import numpy as np
import cv2

cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

# Ajusta history y varThreshold a tu escena; sin sombras para más limpieza
fgbg = cv2.createBackgroundSubtractorMOG2(
            history=500, varThreshold=50, detectShadows=False)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
while(1):
    ret, frame = cap.read()
    
    fgmask = fgbg.apply(frame)                  # 1) sustractor

    # 2) binarizar para asegurar fondo = 0, objeto = 255
    _, fgmask = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

    # 3) opening para eliminar píxeles sueltos
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=2)

    # 4) closing para tapar huecos (opcional)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    fgrmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgrmask)
    cv2.imshow('fgmask', fgmask)      # máscara limpia

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()
