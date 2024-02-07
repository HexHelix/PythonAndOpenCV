# 5)write a program to calculate the distance between two given points (x1,y1) and (x2,y2) using lambda functions

points = [[0 for i in range(2)] for j in range(2)]
for i in range(2):
    for j in range(1):
        print('Enter X{}: '.format(i+1),end="")
        points[i][j] = int(input(''))
        print('Enter Y{}: '.format(i + 1), end="")
        points[i][j+1] = int(input(''))
print(points)

dist = lambda point_list : ((point_list[0][0]-point_list[1][0])**2 + (point_list[0][1]-point_list[1][1])**2 )**(1/2)

print("Distance Between Points Is: {}".format(dist(points)))