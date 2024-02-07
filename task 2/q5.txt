# 5) Ask the user to enter two numbers and find the LCM and HCF ?

a = int(input('First number: '))
b = int(input('Second number: '))
H_number = a if (a>b) else b

while not (H_number%a == 0 and H_number%b == 0):
    H_number += 1
HCF = (a*b)//H_number
print('LCM is = ',H_number,'\nHCF is = ',HCF)