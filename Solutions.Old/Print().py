"""
String Concatenation:
1.create a variable and assign it the phrase "hello world" by concatenating the strings "hello" and " world"
2.create a variable and assign it the integer 11
3.create a variable and assign it the integer 38
4.create a variable and use the variables from steps 2 and 3 and string concatenation to assign it the string
"1138"
"""
# type your code for "String Concatenation" below this comment and above the one below it.------------------------------

phrase = "hello " + "world"
int1 = 11
int2 = 38
intConc = str(int1) + str(int2)
print(phrase, intConc)
# ----------------------------------------------------------------------------------------------------------------------
"""
%s and input():
1.create a variable to hold a user's favorite restaurant (use input() for this.)
2.create a variable to hold the name of a place a user wants to visit.
3.create a variable to hold the user's nickname or first name if they don't have a nickname.
4.use the %s operator to assign the string "Your favorite restaurant is [name of favorite restaurant], you want
to visit
 [name of place the user wants to visit], and your nickname or first name is [nickname or first name]" to a
variable
5.print that variable
"""
# type your code for "%s and input()" below this comment and above the one below it.------------------------------------

rest = input("What is your favorite restaurant?")
place = input("what is the place that you must to visit?")
nick = input("What is your nickname? If you don't have a nickname write your first name")
print("Your favorite restaurant is %s, you want to visit %s, and your nickname or first name is %s"%(rest, place, nick))

# ----------------------------------------------------------------------------------------------------------------------