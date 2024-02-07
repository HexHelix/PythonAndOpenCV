import cv2 as cv
import numpy as np

img = cv.imread('images/bookpage.jpg',cv.IMREAD_GRAYSCALE)

#normal threshold
retval, threshold = cv.threshold(img,12,255,cv.THRESH_BINARY)

#gaussian adaptive threshold
gaus = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)

#otsu threshold
retval, otsu = cv.threshold(img,12,255,cv.THRESH_BINARY+cv.THRESH_OTSU)


cv.imshow('original',img)
cv.imshow('threshold',threshold)
cv.imshow('gaus',gaus)
cv.imshow('otsu',otsu)
cv.waitKey(0)
cv.destroyAllWindows()