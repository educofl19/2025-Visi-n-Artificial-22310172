import cv2
import mediapipe as mp
import serial
import time

# Configura el puerto serial (ajusta el nombre del puerto si es necesario)
arduino = serial.Serial('COM3', 9600)  # CAMBIA 'COM3' si tu Arduino está en otro puerto
time.sleep(2)  # Espera a que el puerto se estabilice

# Configuración de MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # Solo una mano
mp_draw = mp.solutions.drawing_utils

# Inicia la cámara
cap = cv2.VideoCapture(0)

def detectar_mano_abierta(landmarks):
    dedos_abiertos = 0

    # Dedos índice, medio, anular, meñique (puntas: 8, 12, 16, 20 / base: 6, 10, 14, 18)
    tips_ids = [8, 12, 16, 20]

    for i in range(4):
        if landmarks[tips_ids[i]].y < landmarks[tips_ids[i] - 2].y:
            dedos_abiertos += 1

    # Pulgar (tip: 4, base: 2)
    if landmarks[4].x > landmarks[3].x:  # Para mano derecha
        dedos_abiertos += 1

    return dedos_abiertos >= 4  # Consideramos “abierta” si 4 o más dedos están extendidos

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = hands.process(frame_rgb)

    if resultado.multi_hand_landmarks:
        for mano in resultado.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, mano, mp_hands.HAND_CONNECTIONS)

            if detectar_mano_abierta(mano.landmark):
                arduino.write(b'1')  # Enciende LED
                cv2.putText(frame, "LED ENCENDIDO", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                arduino.write(b'0')  # Apaga LED
                cv2.putText(frame, "LED APAGADO", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        arduino.write(b'0')  # Sin mano: apaga

    cv2.imshow("Gesto LED", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
