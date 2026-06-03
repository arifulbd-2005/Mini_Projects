number1 = input('Enter the number: ')
num1 = float(number1)
sign = input('Enter the sign example[+, -, *, /]: ')
number2 = input('Enter the number: ')
num2 = float(number2)
if sign == '+':
    print('Your result is =' + str(num1 + num2))
elif sign == '-':
    print('Your result is =' + str(num1 - num2))
elif sign == '*':
    print('Your result is =' + str(num1 * num2))
elif sign == '/':
    print('Your result is =' + str(num1 / num2))
else:
    print('please enter { + , - , * , / }')