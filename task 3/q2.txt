# 2)Print the following pattern taking the number of rows as input from the user(mirror image of Z)
# 	Input: 5
# ******
#  *
#   *
#    *
# *****


n = int(input('Number of rows: '))

for i in range(n):
    print("*", end="")
for i in range(n-1):
    for j in range(i):
        print(" ", end="")
    print('*')
for i in range(n):
    print("*", end="")
