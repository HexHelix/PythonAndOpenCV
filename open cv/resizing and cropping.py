import cv2 as cv

img = cv.imread("images/img1.jpg")

cv.imshow("img",img)
print(img.shape)
cv.waitKey(0)


#resize

imgResize = cv.resize(img,(300,300))
cv.imshow("img",imgResize)
cv.waitKey(0)

#crop
imgCrop = imgResize[0:200,200:500]
cv.imshow("img",imgCrop)
cv.waitKey(0)