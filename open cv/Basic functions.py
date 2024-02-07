import cv2 as cv
import numpy as np

img = cv.imread('images/img1.jpg')
#grey
imgGrey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey scale',imgGrey)
cv.waitKey(0)

#blur

imgBlur = cv.GaussianBlur(imgGrey,(5,5),0)
cv.imshow('blur',imgBlur)
cv.waitKey(0)

#blur

imgCanny = cv.Canny(imgBlur,70,70)
cv.imshow('Canny',imgCanny)
cv.waitKey(0)

#Dialation

kernel = np.ones((5,5),np.uint8)
imgDialation = cv.dilate(imgCanny,kernel,iterations=1 )
cv.imshow('dilation',imgDialation)
cv.waitKey(0)

#erode = same as dilation just use cv.erode()

