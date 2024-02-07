# 7) WAP and create a dictionary to hold information about pets. Each key is an what kind of animal it is, and each
# value is the pet�s name

n = int(input('Enter the number of pets: '))
itr = [None in range(n)]
pets = {}

for i in range(n):
    a = input('Enter the type of pet: ')
    itr.insert(i,a)
    b = input('Enter the name of the pet: ')
    pets[itr[i]] = b

print(pets)
del pets