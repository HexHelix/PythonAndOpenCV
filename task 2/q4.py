
# 4) WAP to a pattern for n
#      1
#    2  2
#   3  3  3
#    2  2
#      1
#

n = int(input('enter number of rows: '))

for i in range(0,n//2):
    for k in range(0,(n//2)-i):
        print(" ", end="")
    for j in range(0,i+1):
        print(i+1, end=" ")
    print("\n")

for i in range(n-(n//2),0,-1):
    for k in range((n//2)-i+1,0,-1):
        print(" ", end="")
    for j in range(i,0,-1):
        print(i, end=" ")
    print("\n")