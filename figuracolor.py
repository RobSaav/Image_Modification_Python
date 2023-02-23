import cv2
import numpy as np


def figColor(imagenHSV):
    yellowBajo = np.array([15, 100, 20], np.uint8)
    yellowAlto = np.array([45, 255, 255], np.uint8)

    blueBajo = np.array([100, 100, 20], np.uint8)
    blueAlto = np.array([125, 255, 255], np.uint8)

    greenBajo = np.array([35, 100, 20], np.uint8)
    greenAlto = np.array([75, 255, 255], np.uint8)

    redBajo1 = np.array([0, 100, 20], np.uint8)
    redAlto1 = np.array([0, 255, 255], np.uint8)

    redBajo2 = np.array([175, 100, 20], np.uint8)
    redAlto2 = np.array([179, 255, 255], np.uint8)

    maskYellow = cv2.inRange(imagenHSV, yellowBajo, yellowAlto)

    maskBlue = cv2.inRange(imagenHSV, blueBajo, blueAlto)

    maskGreen = cv2.inRange(imagenHSV, greenBajo, greenAlto)

    maskred1 = cv2.inRange(imagenHSV, redBajo1, redAlto1)

    maskred2 = cv2.inRange(imagenHSV, redBajo2, redAlto2)

    maskred = cv2.add(maskred1, maskred2)

    contornoYellow = cv2.findContours(
        maskYellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornoGreen = cv2.findContours(
        maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornoBlue = cv2.findContours(
        maskGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornored = cv2.findContours(
        maskred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    color = 'x'
    if len(contornoYellow) > 0:
        color = 'Amarillo'
    elif len(contornoGreen) > 0:
        color = 'Verde'
    elif len(contornoBlue) > 0:
        color = 'Azul'
    elif len(contornored) > 0:
        color = 'Rojo'
        return color


def figName(contorno, width, heigth):
    nameFig = 'x'
    epsilon = 0.01 * cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno, epsilon, True)

    if len(approx) == 3:
        nameFig = 'Triangulo'
    elif len(approx) == 4:
        divMedida = float(width/heigth)
        if divMedida >= 1:
         nameFig = 'Cuadrado'
        else:
         nameFig = 'Rectangulo'
    elif len(approx) == 5:
         nameFig = 'Pentagono'
    elif len(approx) == 6:
         nameFig = 'Hexano'
    elif len(approx) >= 10:
         nameFig = 'Circulo'
    return nameFig

image = cv2.imread('figuras.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations =1)
canny = cv2.erode(canny, None, iterations=1)
contorno, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

for c in contorno:
    x, y, w, h = cv2.boundingRect(c)
    imgAux = np.zeros(image.shape[:2], dtype = 'uint8')
    imgAux = cv2.drawContours(imgAux, [c], -1, 255, -1)
    maskHSV = cv2.bitwise_and(imageHSV, imageHSV, mask=imgAux)
    figAll = figName(c, w, h) + figColor(maskHSV) 
    cv2.putText(image, figAll, (x,y -5), 1,1, (0,255,0),1)

    cv2.imshow('imagen',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
