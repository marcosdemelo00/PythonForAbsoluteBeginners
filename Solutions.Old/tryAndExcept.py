# Try and Except Problems:
"""
1.Try and Except to handle divide by zero and type errors
a.Use input() to have the user enter two integers as inputs. Assign these to 2 different variables.
b.Define a function that takes two inputs. This function should print the result of the first input divided by the
 second input. Use your knowledge of Try and Except statements to print messages for the errors that would occur if
the
 second input of the function is 0 or if one or both of the inputs cannot be converted to integers.
c.call the function from step 1.b. with the 2 variables from step 1.a. as inputs.
"""

while True:
    int1 = input("Please, insert a integer: ")
    int2 = input("Now, insert another integer to divide the first: ")
    def testdiv(i1, i2):
        bk = True
        try:
            try:
                print('Your result is: {:.2}'.format(int(i1) / int(i2)))
            except ZeroDivisionError:
                print("You can't divide by zero.")
                bk = False
        except:
            print("Sorry, but you must to input just integers")
            bk = False
        return bk
    bbk = testdiv(int1, int2)
    if bbk == True:
        break

print("Thanks for using our code")