import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)


translated = translate(img,100,-100)

cv.imshow('Translated',translated)

def rotate(img,angle,rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width,height)
    return cv.warpAffine(img,rotMat,dimension)

rotated1 = rotate(img,-45)
rotated2 = rotate(rotated1,45)

resize = cv.resize(img,(int(img.shape[1]//1.5),int(img.shape[0]//1.5)),interpolation=cv.INTER_CUBIC)

flipped = cv.flip(img,1)

cropped = img[200:400,300:400]
cv.imshow('Cropped',cropped)
cv.imshow('Flipped',flipped)
cv.imshow('Resized',resize)
cv.imshow('Rotated',rotated1)
cv.imshow('Rotated2',rotated2)

cv.waitKey(0)