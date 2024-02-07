# 4)Write a function which takes a list of integers and no. of rotations as input and returns a list rotated in anticlockwise order.
# example:
# input: [1,2,3,4,5], 1 rotation
# output: [2,3,4,5,1]
# example 2:
# input: [1,2,3,4,5], 2 rotations
# output: [3,4,5,1,2]

def rotate_list(list1 , m):
    for k in range(m):
        temp = list1[0]
        a = -1
        b = 0
        for i in range(n):
            list1[b] = temp
            temp = list1[b]
            if i <= n - 2:
                list1[b] = list1[b + 1]
                a = a + 1
                b = b + 1
    return list1



n = int(input('Enter the number of elements in the list: '))
m = int(input('Enter the number of rotations: '))
list1 = []

for i in range(n):
    a = int(input('Enter element: '))
    list1.append(int(a))


print(rotate_list(list1,m))
