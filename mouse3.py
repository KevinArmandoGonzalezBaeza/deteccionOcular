import cv2
import pyautogui
from gaze_tracking import GazeTracking

# Inicializar el rastreador de mirada
gaze = GazeTracking()

# Inicializar la captura de video
cap = cv2.VideoCapture(0)

while True:
    # Leer un fotograma de la captura de video
    _, frame = cap.read()

    # Analizar el fotograma con el rastreador de mirada
    gaze.refresh(frame)

    # Obtener la posición del ojo izquierdo y derecho
    left_eye = gaze.pupil_left_coords()
    right_eye = gaze.pupil_right_coords()

    # Si se detectan ambos ojos, mover el mouse
    if left_eye is not None and right_eye is not None:
        # Calcular la posición promedio de los ojos
        x = (left_eye[0] + right_eye[0]) // 2
        y = (left_eye[1] + right_eye[1]) // 2

        # Obtener las dimensiones de la pantalla
        screen_width, screen_height = pyautogui.size()

        # Mapear la posición promedio de los ojos a las coordenadas de la pantalla
        target_x = int(x / frame.shape[1] * screen_width)
        target_y = int(y / frame.shape[0] * screen_height)

        # Mover el mouse a las nuevas coordenadas
        pyautogui.moveTo(target_x, target_y)

    # Mostrar el marco en una ventana
    cv2.imshow("Eye Tracking", frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) == ord("q"):
        break

# Liberar la captura de video y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
