"""
In a Python file, use input() to ask the user to enter an integer that 10 will be added to.  
Assign what they type to a variable.
print() the sum of the integer they entered and 10.
"""

user_int = int(input("Enter a number that will de added to 10: \n").strip())
print("\nThe number \"" + str(user_int) + "\" plus \"10\" is equal to: " + str(user_int + 10) + ".")