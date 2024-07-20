import cv2 as cv
from IPython.utils import capture

img = cv.imread('Photos/cat_large.jpg')


def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
cv.imshow('Cat', rescaleFrame(img,0.5))

vid = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = vid.read()
    if isTrue:
        cv.imshow('Video', rescaleFrame(frame,0.5))
    else:
        break
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
vid.release()
cv.destroyAllWindows()


cv.waitKey(0)