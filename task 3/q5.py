# 5)Write a program to reverse a tuple

tuple1 = (98, 67, 33, 44, 55, 78)
rev_lst = []
print('Original tuple ')
print(tuple1)
print('Reversed tuple: ')
temp = list(tuple1)
for i in tuple1[::-1]:
    rev_lst.append(i)
rev_tup = tuple(rev_lst)
print(rev_tup)