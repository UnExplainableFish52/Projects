print('Hello Mathematically Challenged Lazy Human!')
print('Welcome to Calculator.IO program.')
will = int(input('Enter 1 to commence with the calculator and 0 to exit:\n '))
while will == 1:
    num1 = float(input('Enter the first number:\n '))
    operator = input('Enter the operator (+, -, *, /):\n ')
    num2 = float(input('Enter the second number:\n '))
    if operator == '+':
        result = num1 + num2
        print(f'The result is: {result}')
    elif operator == '-':
        result = num1 - num2
        print(f'The result is: {result}')
    elif operator == '*':
        result = num1 * num2
        print(f'The result is: {result}')
    elif operator == '/':
        if num2 == 0:
            print('Error: Division by zero is not allowed.')
        else:
            result = num1 / num2
            print(f'The result is: {result}')
    will = int(input('Do you want to perform another calculation? (1 for yes, 0 for no):\n '))
print('Thank you for using Calculator.IO program. Goodbye!')