import cv2 as cv

img = cv.imread('Photos/park.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

canny = cv.Canny(blur,125,175)

dilated = cv.dilate(canny,(3,3),iterations=3)

eroded = cv.erode(dilated,(3,3),iterations=3)

resize = cv.resize(img,(img.shape[1]//2,img.shape[0]//2),interpolation=cv.INTER_CUBIC)

cropped = img[50:200,200:400]


cv.imshow("cropped",cropped)
cv.imshow("resize",resize)
cv.imshow("eroded",eroded)
cv.imshow("dilated",dilated)
cv.imshow('canny',canny)
cv.imshow('blur',blur)
cv.imshow('Gray', gray)
cv.waitKey(0)