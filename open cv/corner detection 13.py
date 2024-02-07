import numpy as np
import cv2
from multipledispatch import dispatch


img = cv2.imread('images/corner3.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,4,0.01,10)
corners = np.int0(corners)
print(corners.shape[0])

pts = corners.reshape(4, -1)
p1 = pts[0]
p2 = pts[1]
p3 = pts[2]
p4 = pts[3]

heightCorner1 = p1
heightcorner2 = 0
height = 0
width = 0



def findDist(point):
    x1, y1 = p1.ravel()
    x2, y2 = point.ravel()
    dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist



def findDist2(point1, point2):
    x1, y1 = point1.ravel()
    x2, y2 = point2.ravel()
    distn = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distn


def findHeightCorner():
    if (findDist(p2) < findDist(p3)):
        if (findDist(p2) < findDist(p4)):
            heightcorner2 = p2
        else:
            heightcorner2 = p4
    elif (findDist(p3) < findDist(p4)):
        heightcorner2 = p3
    else:
        heightcorner2 = p4

    return heightcorner2


def findWidthCorner():
    if (findDist(p2) > findDist(p3)):
        if (findDist(p2) > findDist(p4)):
            widthcorner2 = p2
        else:
            widthcorner2 = p4
    elif (findDist(p3) > findDist(p4)):
        widthcorner2 = p3
    else:
        widthcorner2 = p4

    return widthcorner2


def findHeight():
    height = findDist2(p1, findHeightCorner())
    return height


def findwidth():
    width = findDist2(p1, findWidthCorner())
    return width




print(findHeight(), findwidth())






for i in corners:
    #print(i)
    #print(i.ravel())
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)

#print(corners[0])
cv2.imshow("corners",img)

cv2.waitKey(0)
cv2.destroyAllWindows()