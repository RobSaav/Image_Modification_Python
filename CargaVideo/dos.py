import cv2
import numpy as np

# Función para determinar la forma de un contorno
def detect_shape(cnt):
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
    x, y, w, h = cv2.boundingRect(approx)
    aspect_ratio = float(w)/h
    if len(approx) == 3:
        return "Triangulo"
    elif len(approx) == 4:
        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
            return "Cuadrado"
        else:
            return "Rectangulo"
    elif len(approx) == 5:
        return "Pentagono"
    elif len(approx) == 6:
        return "Hexagono"
    else:
        return "Circulo"

# Función para determinar el color predominante en un objeto
def detect_color(frame, cnt):
    mask = np.zeros(frame.shape[:2], np.uint8)
    cv2.drawContours(mask, [cnt], -1, 255, -1)
    hist = cv2.calcHist([frame], [0, 1, 2], mask, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    color = hist.argmax()
    if color == 0:
        return "Rojo"
    elif color == 1:
        return "Verde"
    else:
        return "Azul"

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar un fotograma
    ret, frame = cap.read()

    # Convertir el fotograma a una imagen en escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar el algoritmo Canny para detectar los bordes de los objetos
    edges = cv2.Canny(gray, 50, 150)

    # Encontrar los contornos de los objetos en la imagen de bordes
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtrar los contornos por área y perímetro
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100 and cv2.arcLength(cnt, True) > 100]

    # Dibujar los contornos y etiquetar
    for cnt in contours:
        shape = detect_shape(cnt)
        color = detect_color(frame, cnt)
        cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.putText(frame, shape + " " + color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Mostrar la imagen resultante
    cv2.imshow("Reconocimiento de Figuras y Colores", frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()