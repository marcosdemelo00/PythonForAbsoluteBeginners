'''
Programming Challenge: Factorial
Create a function which takes one positive integer as its input and returns its
factorial.

To make sure that your function works correctly, you should call it with the
inputs 3, 4, and 5 and print what is returned by those calls.
For those inputs, you should get 6, 24, and 120, respectively.
'''


def factorial(num):
    val = 1
    for i in range(num, 1, -1):
        val *= i
    return val


def intnum():
    while True:
        try:
            num = int(input('Enter a positive integer: '))
        except ValueError:
            print('Invalid value.')
        else:
            if num <= 0:
                print('Invalid value.')
            else:
                return num

print(f'3! = {factorial(3)}')
print(f'4! = {factorial(4)}')
print(f'5! = {factorial(5)}')
num = intnum()
print(f'{num}! = {factorial(num)}')