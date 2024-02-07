import cv2 as cv
import numpy as np

img = cv.imread('images/img1.jpg',cv.IMREAD_COLOR)

#cv.imshow('img',img)

#convert a region off image to a color

img[200:400,400:800] = [255,255,255]
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()

#cut and paste a region of image
a = img[200:400,400:800]
img[0:200,0:400] = a
cv.imshow("cut",img)
cv.waitKey(0)
cv.destroyAllWindows()

