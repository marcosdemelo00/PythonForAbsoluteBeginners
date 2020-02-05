# Functions Problems:
"""
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input
"""
# ----------------------------------------------------------------------------------------------------------------------

def zero():
    print('chupacabra')
int = 5
def par(o):
    print(o)
zero()
par(int)

# ----------------------------------------------------------------------------------------------------------------------
"""
multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1
"""
# ----------------------------------------------------------------------------------------------------------------------

int1 = 1
int2 = 2
int3 = 4
def dif(a, b):
    print(a - b)
def prod(c, d, e):
    print(c * d * e)

dif(int3, int2)
prod(int1, int2, int3)

# ----------------------------------------------------------------------------------------------------------------------
"""
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
 parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 3 variables you created in step 1
"""
# ----------------------------------------------------------------------------------------------------------------------

fl1, fl2, fl3 = 12.0, 3.0, 2.0
def quo(f, g):
    return f / g
def quo2(h, i, j):
    return quo(h, i) / j
print(quo(fl1, fl2))
print(quo2(fl1, fl3, fl2))

# ----------------------------------------------------------------------------------------------------------------------
