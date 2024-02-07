# 1) Ask the user to enter the values of a 1 , a 2 , b 1 , b 2 , c 1 , and c 2 and
# find whether the lines are parallel, or if they overlap or intersect.

a1 = float(input('Value of a1: '))
a2 = float(input('Value of a2: '))
b1 = float(input('Value of b1: '))
b2 = float(input('Value of b2: '))
c1 = float(input('Value of c1: '))
c2 = float(input('Value of c2: '))

m1 = (-1*a1)/b1
m2 = (-1*a2)/b2

if m1 == m2:
    if a1==a2 and b1==b2 and c1==c2:
        print('Lines are parallel and overlapping')
    print("Lines are parallel")
else:
    x = (c2-c1)/(m1-m2)
    y = (m2*c1-m1*c2)/(m2-m1)
    print("Lines intersect at X = ",x," and Y = ",y)

