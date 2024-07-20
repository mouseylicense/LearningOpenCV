import cv2 as cv
# img = cv.imread('../Photos/cat_large.jpg')
#
# cv.imshow('Cat', img)

vid = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = vid.read()
    if isTrue:
        cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
vid.release()
cv.destroyAllWindows()