import cv2 as cv
import numpy as np

img = cv.imread('images/opencv.png')
img2 = cv.imread('images/logo.png')
imgResized = cv.resize(img2,(428,378))

add = img + imgResized
add1 = cv.add(img,imgResized)

#weighted

weighted = cv.addWeighted(img,0.6,imgResized,0.2,0)


cv.imshow("add",weighted)

cv.waitKey(0)
cv.destroyAllWindows()