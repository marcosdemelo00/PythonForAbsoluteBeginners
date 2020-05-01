'''
Programming Challenge: Sum of Numbers From A Positive Integer
Write a program which gets a positive integer from a user using input() and
assigns it to a variable.

The program should then use a while loop to get the sum of all of the integers
from the integer that was entered by the user down to 1.  For example, if the
integer entered by the user was 6, the while loop would find the
sum of 6, 5, 4, 3, 2, and 1, which is 21.

At the bottom of your program create two print statements.
One will display the user entered integer and the other will display the sum
found by the while loop.
'''


def intpos():
    while True:
        try:
            num = int(input('Enter a positive integer: '))

        except:
            print('\033[31mInvalid value.\033[m')
        else:
            if num >= 0:
                return num
            else:
                print('\033[31mInvalid value.\033[m')


var = count = intpos()
sum = 0
while count > 0:
    sum += count
    count -= 1

print('The sum of number above {2}{0}{3} is {2}{1}{3}.'
      .format(var, sum, '\033[34m', '\033[m'))
