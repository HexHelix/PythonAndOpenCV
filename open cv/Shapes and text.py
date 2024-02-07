import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[:] = 255,0,0

print(img.shape )


# line
cv.line(img,(0,0),(300,300),(0,255,0),3)
cv.imshow('black img',img)
cv.waitKey(0)

#rectangle
cv.rectangle(img,(0,0),(300,300),(0,255,0),3)
cv.imshow('black img',img)
cv.waitKey(0)
#rectangle filled
cv.rectangle(img,(0,0),(300,300),(0,255,0),cv.FILLED)
cv.imshow('black img',img)
cv.waitKey(0)

#circle
cv.circle(img,(300,50),30,(0,0,255),2)
cv.imshow('black img',img)
cv.waitKey(0)

#text
cv.putText(img,"HELLO WORLD",(100,400),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,255,255),1)
cv.imshow('black img',img)
cv.waitKey(0)