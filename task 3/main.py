# 1) Print
# the
# following
# pattern
# taking
# the
# number
# of
# rows as input
# from the user
#
# Input: 4
#
#        *
#        * *
#        * * *
#        * * * *

n = int(input('Number of rows'))

for i in range(0,n+1):
    for j in range(0,i):
        print("*",end="")
    print("\n")