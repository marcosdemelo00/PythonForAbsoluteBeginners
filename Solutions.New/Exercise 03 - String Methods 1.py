'''
string methods 1 exercises
Do all of this in a .py file in Pycharm:

1- Create a variable called mixed_case and assign it the string "A Song of Ice
 and Fire"
2- Use .isupper() to check if mixed_case is a string of all upper case letters.
 print() the result.

3- Use .islower() to check if mixed_case is a string of all lower case letters.
 print() the result.

4- Change all of the letters in mixed_case to upper case letters using .upper()
 and print() the result.

5- Change all of the letters in mixed_case to lower case letters using .lower()
 and print() the result.

6- Use the .istitle() method to check if mixed_case is title case and print the
 result.

7- Create a variable called title_case and assign it the result of .title()
 being called on mixed_case.

8- print() title_case

9- Call startswith() on mixed_case with the letter mixed_case starts with as
 its argument.  print() the result.

10- Call endswith() on mixed_case with the letter mixed_case ends with as its
 argument.  print() the result.

11- Create a variable called words and assign it the result of split() being
 used on mixed_case.

12 - print the variable "words"

13 - Use the .join() method to join together all of the items in the list assigned to words as a single string.  Use .isalpha() to check if the string is made up entirely of letters.  Finally, use print() to display the result.
'''

mixed_case = 'A Song of Ice and Fire'
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith('A'))
print(mixed_case.endswith('e'))
words = mixed_case.split()
print(words)
print("".join(words).isalpha())