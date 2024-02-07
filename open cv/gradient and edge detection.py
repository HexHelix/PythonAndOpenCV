import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

#cap.set(3,640)
#cap.set(4,480)

while True:
    success,img = cap.read()
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    gimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #laplasian gradient
    lap = cv.Laplacian(hsv,cv.CV_64F)

    #soble
    soblex = cv.Sobel(gimg,cv.CV_64F,1,0,ksize=5)
    sobley = cv.Sobel(gimg, cv.CV_64F, 0, 1, ksize=5)

    #canny edge detector
    canny = cv.Canny(img,120,120)

    cv.imshow("laplacian",lap)
    cv.imshow("soblex", soblex)
    cv.imshow("sobley", sobley)
    cv.imshow("canny", canny)

    if (cv.waitKey(1) & 0xFF) == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
