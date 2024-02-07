# 3) Ask the user to enter 4 points and arrange them in order of their distances from the origin.

points = [[0 for i in range(2)] for j in range(4)]


for i in range(4):
    for j in range(1):
        points[i][j] = int(input("Enter X: "))
        points[i][j+1] = int(input("Enter Y: "))

dist_list= []
dist = 0


for i in range(4):
    for j in range(1):
        dist = ((points[i][j]**2 + points[i][j+1]**2 )**1/2)
        dist_list.append(dist)
dist_list.sort()
print(dist_list)







