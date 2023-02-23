import cv2
import numpy as np 
from matplotlib import pyplot as plt

imgEscale = cv2.imread('portada2.jpg', 1)
cv2.imshow('result', imgEscale)
cv2.waitKey(0)

gris = cv2.cvtColor(imgEscale, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagenGRIS', gris)
cv2.waitKey(0)


gris = cv2.cvtColor(imgEscale, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagenGRIS', gris)
cv2.waitKey(0)

plt.hist(gris.ravel(),256)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


hsv = cv2.cvtColor(imgEscale, cv2.COLOR_BGR2HSV)
cv2.imshow('ImagenHSV', gris)
cv2.waitKey(0)

hsv = cv2.cvtColor(imgEscale, cv2.COLOR_BGR2HSV)
cv2.imshow('ImagenHSV', hsv)
cv2.waitKey(0)

plt.hist(hsv.ravel(),256)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


yuv = cv2.cvtColor(imgEscale, cv2.COLOR_BGR2YUV)
cv2.imshow('imagenyuv', yuv)
cv2.waitKey(0)

yuv = cv2.cvtColor(imgEscale, cv2.COLOR_BGR2YUV)
cv2.imshow('imagenyuv', yuv)
cv2.waitKey(0)

plt.hist(yuv.ravel(),256)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


ycrcb = cv2.cvtColor(imgEscale, cv2.COLOR_BGR2YCR_CB)
cv2.imshow('imagenCRCB' , ycrcb)
cv2.waitKey(0)

ycrb = cv2.cvtColor(imgEscale, cv2.COLOR_BGR2YCR_CB)
cv2.imshow('imagenCRCB', ycrb)
cv2.waitKey(0)

plt.hist(ycrb.ravel(),256)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

b, g, r = cv2.split(imgEscale)
cv2.imshow('blue', b)
cv2.waitKey(0)
cv2.imshow('green', g)
cv2.waitKey(0)
cv2.imshow('red', r)
cv2.waitKey(0)

src = cv2.merge([r,g,b])
cv2.imshow('ImagenMerge', src)
cv2.waitKey(0)

src = cv2.merge([r,g,b])
cv2.imshow('ImagenMerge', src)
cv2.waitKey(0)

plt.hist(src.ravel(),256)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()







