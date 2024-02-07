import cv2 as cv

img = cv.imread('img1.jpg')
resized = cv.resize(img,(500,500))
#cv.imshow('image', img)
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
blured = cv.GaussianBlur(gray,(1,1), cv.BORDER_DEFAULT)
canny = cv.Canny(blured ,125,175)

cv.imshow('Canny',canny)
cv.imshow('grey',gray)
cv.waitKey(0)

