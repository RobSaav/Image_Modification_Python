import cv2

# Cargar la imagen
img = cv2.imread('portada2.jpg')

# Convertir a diferentes modelos de color
img_green = cv2.cvtColor(img, cv2.COLOR_BGR2GREEN)
img_red = cv2.cvtColor(img, cv2.COLOR_BGR2RED)
img_blue = cv2.cvtColor(img, cv2.COLOR_BGR2BLUE)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_cr_cb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Mostrar las imágenes convertidas
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen en verde', img_green)
cv2.imshow('Imagen en rojo', img_red)
cv2.imshow('Imagen en azul', img_blue)
cv2.imshow('Imagen en HSV', img_hsv)
cv2.imshow('Imagen en YUV', img_yuv)
cv2.imshow('Imagen en gris', img_gray)
cv2.imshow('Imagen en CrCb', img_cr_cb)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()