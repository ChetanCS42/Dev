import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank',blank)

blank[250:500, 250:500] = 115,147,179
cv.imshow('Blue',blank)


cv.rectangle(blank, (0,0), (250,250),(0,255,0),-1)
cv.imshow('rectangle',blank)

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(255,255,255),-1)
cv.imshow('circle',blank)

cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),3)
cv.imshow('Line',blank)

cv.putText(blank,'Hello its CHETAN!!',(0,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,150,255),2)
cv.imshow('Text',blank)






# img= cv.imread('images/Aircraft.jpg')
# cv.imshow('Aircraft',img)

cv.waitKey(0)