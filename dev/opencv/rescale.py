import cv2 as cv
# img= cv.imread('images/Aircraft.jpg')
# cv.imshow('cat2',img)
def rescaleFrame(frame, scale=0.50):
    width= int (frame.shape[1]*scale)
    height= int (frame.shape[0]*scale)
    dimensions= (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
img= cv.imread('images/Aircraft.jpg')
cv.imshow('cat2',img)
img_resized= rescaleFrame(img)
cv.imshow('cat2_resized',img_resized)
cv.waitKey(0)
# capture= cv.VideoCapture('videos/Namo.mp4')
# while True:
#     isTrue, frame=capture.read()
#     frame_resized= rescaleFrame(frame)
#     cv.imshow('video',frame)
#     cv.imshow('Video_resized',frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()