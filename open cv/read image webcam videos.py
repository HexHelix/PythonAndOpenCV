import cv2 as cv

#images

img = cv.imread('images/img1.jpg')
cv.imshow('bean',img)
print('hello')
cv.waitKey(0)

#videos

cap = cv.VideoCapture("videos/highway.mp4")

while True:
    success, img1 = cap.read()
    cv.imshow('video',img1)
    if (cv.waitKey(1) & 0xFF) == ord('q'):
        break

#webcam
cap = cv.VideoCapture(0)


while True:
    success, img1 = cap.read()
    cv.imshow('video',img1)
    if (cv.waitKey(1) & 0xFF) == ord('q'):
        break

