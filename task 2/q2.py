# 2) Ask the user to enter a three digit number. Find the number obtained by reversing the order of the digits. Find the sum of the digits. Finally, find
# if they are a palindrome

num = input('Enter a 3 digit number: ')

rev_num = int(num[2])*100+int(num[1])*10+int(num[0])
sum_rev_num = int(num[2])+int(num[1])+int(num[0])

print('Number obtained reversing the digit =',rev_num)
print('Addition of digits of number =',sum_rev_num)
if int(num[0])==int(num[2]):
    print("Number is palindrome")