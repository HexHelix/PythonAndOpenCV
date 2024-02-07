import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)

#cap.set(3,640)
#cap.set(4,480)

while True:
    temp, img = cap.read()
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    kernel = np.zeros((21,21),np.uint8)

    lower_green = np.array([30, 11, 4])
    upper_green = np.array([95, 255, 223])
    mask = cv.inRange(hsv, lower_green, upper_green)
    openning = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

    result = cv.bitwise_and(img, img, mask=mask)


    cv.imshow("img", img)
    cv.imshow("mask", mask)
    cv.imshow("maskOpenning", openning)
    cv.imshow("result", result)
    if (cv.waitKey(1) & 0xFF) == ord('q'):
        break

cv.destroyAllWindows()
cap.release()