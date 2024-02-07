# 3) Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

n = int(input('Enter the number of elements in list one: '))
m = int(input('Enter the number of elements in list two: '))

list1 = [None in range(n)]
list2 = [None in range(m)]
print('Enter values for first list')
for i in range(0,n):
    a = input('enter the {} element: '.format(i+1))
    list1.append(a)
print('Enter values for second list')
for i in range(m):
    a = input('enter the {} element: '.format(i + 1))
    list2.append(a)

for i,j in zip(list1,list2[::-1]):
    print('{}    {}'.format(i,j))
