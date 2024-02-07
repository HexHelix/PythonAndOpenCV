# 4) Write a program to ask the user to enter a number and then print their data type (string, integer or float). [Hint: Study the function 'type'.]

inp = input('type your data')

try:
    a = int(inp)
    print('Your data type is: ', type(a))

except ValueError:
    try:
        a = float(inp)
        print('Your data type is: ', type(a))

    except ValueError:
        print('Your data type is: ', type(inp))
