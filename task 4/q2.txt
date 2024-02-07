# 2)Write a program to input a sentence (a string without any special characters other than whitespace)
# and generate a list with the words in the input sentence as its elements.
# 	Input: Hello there I am XYZ
# 	Output : [‘Hello’,’there’,’I’, ’am’, ’XYZ’]

a = input('Enter your sentence: ')

b = []

for i in a.split():
    b.append(i)

print(b)

