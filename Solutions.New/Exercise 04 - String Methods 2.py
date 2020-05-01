'''
string methods 2 exercises
Do all of this in a .py file:

1- Create a variable called the_string and assign it the string "North Dakota".

2- Call .rjust() on the_string with 17 as its argument and print() the result.

3- Call .ljust() on the_string with the arguments 17 and "*" then print() the result.

4- Create a variable called center_plus and assign it the result of .center() being
 called on the_string with 16 and "+" as arguments.

5- Use print() to display the string assigned to center_plus.

6- Call .lstrip() on the_string to remove "North" then print() the result.

7- Call .rstrip() on center_plus with "+" as its argument and print() the result.

8- Call .strip() on center_plus with "+" as its argument and print() the result.

9- Call .replace() on the_string and replace "North" with "South".  print() the
 result.
'''

the_string = 'North Dakota'
print(the_string.rjust(17))
print(the_string.ljust(17, '*'))
center_plus = the_string.center(16, '+')
print(center_plus)
print(the_string.lstrip('North'))
print(center_plus.rstrip('+'))
print(center_plus.strip('+'))
print(the_string.replace('North', 'South'))