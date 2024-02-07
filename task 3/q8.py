# 8)  WAP to find the highest 3 values in a dictionary.

my_dict = {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}
print(my_dict)

ordered_val = list(my_dict.values())
ordered_val.sort()
ordered_val = ordered_val[len(ordered_val)-3:]




print('The 3 largest values in dictionary are: ')
print(ordered_val)






