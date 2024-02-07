# 3) Write a program which asks the user to enter three points (i.e (x1,y1), (x2, y2), (x3, y3)) and find whether they are collinear.

import numpy as np

p = [[0 for i in range(3)] for j in range(3)]

for i in range(3):
    print("(x"+str(i)+","+"y"+str(i)+"):")
    for j in range(2):
        p[i][j] = int(input(""))

for i in range(3):
    for j in range(3):
        if j == 2:
            p[i][j] = 1

area = 0.5*np.linalg.det(p)

print("Points are collinear") if area == 0 else print("Points are non-collinear")
