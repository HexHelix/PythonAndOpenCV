# 5) Write a program to take two numbers (x and y) as input and solve the following
# 	a) add x and y
# 	b) subtract x from y
# 	c) multiply x and y
# 	d) integer division: x by y
# 	e) float division: y by x
# 	f) square the numbers x and y
# 	g) raise x to the power y
# 	h) (x+y)^3 + (y^3)*6 - (x^y) + (x/y)


import numpy as np
num1 = input('Enter your first num')
num2 = input('Enter your second num')

try:
    num1 = int(num1)
    num2 = int(num2)
    print('add x and y: ',(num1+num2),"\n")
    print('subtract x from y: ', (num2 - num1), "\n")
    print('multiply x and y: ', (num1 * num2), "\n")
    print('integer division: x by y: ', int(num1 / num2), "\n")
    print('float division: y by x: ', float(num1 / num2), "\n")
    print('square the numbers x and y: ',np.power(num1,2)," ",np.power(num2,2), "\n")
    print('raise x to the power y: ',np.power(num1,num2), "\n")
    print('(x+y)^3 + (y^3)*6 - (x^y) + (x/y): ',(np.power(num1+num2,3) + np.power(num2,3)*6 - np.power(num1,num2) + (num1/num2)), "\n")

except ValueError:
    try:
        a = float(num1)
        b = float(num2)
        num1 = float(num1)
        num2 = float(num2)
        print('add x and y: ', (num1 + num2), "\n")
        print('subtract x from y: ', (num2 - num1), "\n")
        print('multiply x and y: ', (num1 * num2), "\n")
        print('integer division: x by y: ', int(num1 / num2), "\n")
        print('float division: y by x: ', float(num1 / num2), "\n")
        print('square the numbers x and y: ', np.power(num1, 2), " ", np.power(num2, 2), "\n")
        print('raise x to the power y: ', np.power(num1, num2), "\n")
        print('(x+y)^3 + (y^3)*6 - (x^y) + (x/y): ',(np.power(num1 + num2, 3) + np.power(num2, 3) * 6 - np.power(num1, num2) + (num1 / num2)), "\n")

    except ValueError:
        print('Please enter a valid number')