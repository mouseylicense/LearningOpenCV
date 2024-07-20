import numpy as np
import cv2 as cv


img = cv.imread('Photos/cat.jpg')


img[200:300] = 0,0,255

cv.rectangle(img,(0,0),(img.shape[1]//2,img.shape[0]//2),(0,255,0),thickness=cv.FILLED)
cv.circle(img,(img.shape[1]//2,img.shape[0]//2),40,(255,0,0),thickness=cv.FILLED)

cv.line(img,(img.shape[1]//2,img.shape[0]//2),(img.shape[1],img.shape[0]),(255,0,0),thickness=3)

cv.putText(img,"Hello",(img.shape[1]//2,img.shape[0]//2),cv.FONT_HERSHEY_PLAIN,2,(0,255,255),5)

cv.imshow('Cat', img)



cv.waitKey(0)
