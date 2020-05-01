'''
Programming Challenge: Roman Numeral Equivalent
For this exercise, start by creating a variable and assigning it a randomly
generated integer between and inclusive of both 1 and 10.

Then, using your knowledge of if, elif, and else statements, create a program
which prints the roman numeral equivalent of the randomly generated number.

For example, if the randomly generated integer was 9, then the program would
say that the roman numeral equivalent of 9 is IX in the output.
'''
from random import randint

var = randint(1, 10)
if var == 10:
    roman = 'X'
elif var == 9:
    roman = 'IX'
elif var == 8:
    roman = 'VIII'
elif var == 7:
    roman = 'VII'
elif var == 6:
    roman = 'VI'
elif var == 5:
    roman = 'V'
elif var == 4:
    roman = 'IV'
elif var == 3:
    roman = 'III'
elif var == 2:
    roman = 'II'
else:
    roman = 'I'
print(f'\nThe roman numeral equivalent of \033[34m{var}\033[m is \033[33m{roman}\033[m.')