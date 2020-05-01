'''
Programming Challenge: String Reverser
For this challenge, you will be writing a program which uses a for loop to
reverse a string.

Start by creating a variable and assigning it a string as user input using
input().

Use a for loop to reverse the string.  You will need to use range with all
3 inputs for this.  In addition, you should create a variable before the for
loop and assign it an empty string.  The variable will be reassigned multiple
times within the for loop and end up holding the new reversed string.

Print the reversed string at the bottom of your program.
'''


def reverser(str):
    reverse = ''
    for l in range(0, len(str)):
        reverse = str[l] + reverse
    return reverse


line = input('Enter anything: \n>>> ').strip()
rline = reverser(line)
print('Reverse of {2}{0}{4} is: {3}{1}{4}'.format(line, rline, '\033[33m', '\033[35m', '\033[m'))