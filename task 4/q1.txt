# 1) Write a program to input a list from the user and output a list of unique elemtents.

n = int(input('Enter number of elements in the list'))
list1 = [None in range(n)]
for i in range(n):
    a = input('Enter the {} element'.format(i+1))
    list1.append(a)
dict1 = {list1[i]: "" for i in range(0, len(list1))}
list2 = list(dict1.keys())
print(list2[1:])