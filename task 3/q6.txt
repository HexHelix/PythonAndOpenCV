# 6) Write a program to copy element 44 and 55 from the following tuple into a new tuple
# tuple1 = (98, 67, 33, 44, 55, 78)
tuple1 = (98, 67, 33, 44, 55, 78)

tuple2 = tuple(tuple1[3:5])
print(tuple2)