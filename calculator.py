
#calculator that works with 2  numbers
import math

amount = int(input('How many numbers will you be operating with? '))


op = input('Operation? ')
num1 = int(input('Enter first num'))
num2 = int(input('Enter second num'))
if op == 'Addition' or op == '+':
    print(num1+num2)
elif op == 'Subtraction' or op == '-':
    print(num1-num2)
elif op == 'Multiplication' or op == 'x':
    print(num1*num2)
elif op == 'Division' or op == '/':
    print(num1/num2)
elif op == 'Power' or op == '^':
    print(math.pow(num1,num2))
else:
    print('Please enter a valid operation')
        


