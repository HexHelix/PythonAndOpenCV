import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)

while True:
    temp, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    corners = cv.goodFeaturesToTrack(gray, 4, 0.01, 10)
    corners = np.int0(corners)

    if (corners.shape[0] == 4):
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


        print('ratio of Height:Width = ',findHeight()/findwidth())





    else:
        print('4 points not found')

    for i in corners:
        # print(i)
        # print(i.ravel())
        x, y = i.ravel()
        cv.circle(img, (x, y), 5, (0, 255, 0), -1)

    cv.putText(img,'Ratio of Height:Width = '+ str(findHeight()/findwidth()),(10,430),cv.FONT_HERSHEY_PLAIN,1.5,(0,20,255),2)
    cv.putText(img, 'Height cm: ' + str(findHeight()/37.795275591), (10, 450), cv.FONT_HERSHEY_PLAIN, 1.5,(0, 20, 255), 2)
    cv.putText(img, 'Width cm: ' + str(findwidth()/37.795275591), (10, 470), cv.FONT_HERSHEY_PLAIN, 1.5,(0, 20, 255), 2)



    cv.imshow('cam', img)
    if (cv.waitKey(1)  & 0xFF) == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
