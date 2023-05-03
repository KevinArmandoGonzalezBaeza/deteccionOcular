#fintro de suavizado
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
blur = 15 # nivel de blur de 1 a 15
multFilt = 1 # multipilcar el filtro GausBlur de 1 a 100

while True:
    _, frame = cap.read()

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar diferentes filtros para agregar blur a la imagen
    frame_blur = cv2.GaussianBlur(gray, (blur, blur), 0)
    frame_blur = cv2.bilateralFilter(frame_blur, 9, multFilt, multFilt)

    cv2.imshow('video', frame_blur)

    # Presione la tecla "q" para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()