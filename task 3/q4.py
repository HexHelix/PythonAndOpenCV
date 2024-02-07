# 4) Write a program to remove empty strings from the list of strings.

n = int(input('Enter the number of items: '))
str_list = [None in range(n)]
str_list1 = []

for i in range(n):
    a = input("Enter the {} string: ".format(i+1))
    str_list.append(a)
print("List with empty string removed: ")
for i in str_list:
    if not (i == None or i == "" or type(i)== bool):
        str_list1.append(i)
print(str_list1[0:])

