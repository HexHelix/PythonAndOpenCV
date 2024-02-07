import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

#cap.set(3,640)
#cap.set(4,480)

while True:
    success,img = cap.read()
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    lower_red = np.array([150,150,50])
    upper_red = np.array([255,255,255])


    mask = cv.inRange(hsv,lower_red,upper_red)
    res = cv.bitwise_and(img,img,mask = mask)

    kernel = np.ones((5,5),np.uint8)

    #openning
    openning = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
    closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)


    cv.imshow('webcam',img)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    cv.imshow('open', openning)
    cv.imshow('close', closing)
    if (cv.waitKey(1) & 0xFF) == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
