# 1) Create a nested dictionary, with the following fields and take input from the user and print .
# sample:
# {
# 	'abc': {'address':__,
# 	'phone number':__,
# 	'email':__
# }
# Take n no.of inputs from the user, where n is also given by the user.

n = int(input('Enter the number of entries: '))
p_name = []

for i in range(n):
    print('Enter person {} name'.format(i+1))
    p_name.append(input(''))
print(p_name)

p_info = ['address','phone number','email']

p_dict = {}

for i in p_name:
    print('Please Enter Following details for {}: '.format(i))
    for j in p_info:
        p_dict.update(i=j)
print(p_dict)
