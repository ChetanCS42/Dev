import cv2 as cv
#img= cv.imread('images/Aircraft.jpg')
#cv.imshow('cat2',img)'
capture= cv.VideoCapture('videos/Namo.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()


