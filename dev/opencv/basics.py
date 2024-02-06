import cv2 as cv
import numpy as np

img= cv.imread('images/Aircraft.jpg')
cv.imshow('Aircraft',img)

grey= cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('grey',grey)

blur= cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

cv.waitKey(0) 