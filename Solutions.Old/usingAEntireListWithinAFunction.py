# Using An Entire List Within A Function Problems:
"""
0.initial setup:
a.create a variable and assign it a list of all integers
"""
intlist = [7, 8, 9, 0]
"""
1.printing a list's elements using a for loop in a function:
a.create a function that will take a list as its input and prints that list's elements using a for loop
b.call the function you created in step 1.a. with the list you created in step 0.a. as its input.
"""
def printlist(p):
    for intg in p:
        print(intg)
printlist(intlist)
"""
2.generating lists using range():
a.use range() to generate a list that starts at 0 and ends at and includes 9 (range should only have 1 input.)
Assign
 this range() to a variable
b.use range () to generate a list that starts at 4 and ends at and includes 7 (range should only have 2 inputs.)
Assign
 this range() to a variable
c.use range to generate a list that starts at 5, increments up in steps of 5, and ends at and includes 20 (range
should
 have 3 inputs.) Assign this range() to a variable.
"""
range1list = range(10)
range2list = range(4, 8)
range3list = range(5, 21, 5)
print(range1list, range2list, range3list)
"""
3.passing a list made using a range into a function:
a.create a function that takes and returns 1 input
b.print a call of the function you created in step 3.a. with the range you made in step 2.a. as its input
"""
def function1(a):
    return a
print(function1(range1list))
"""
4.iterating through a list using range() and a for loop:
a.create a function that uses a for loop and a range (as was shown in the lecture video) to print all of the
elements
 from a list.
b.call the function you created in step 4.a. with the range you made in step 2.b. as its input.
"""
def allnum(a):
    for num in range(0, len(a)):
        print(a[num])
allnum(range2list)
"""
5.modifying elements from a list using range:
a.Create a function that uses a for loop and a range() to iterate through and add 3 to each of the elements
from a list.
 The function should print the modified list.
b.call the function you created in step 5.a. with the list you made in step 0.a. as its input.
"""
def modlist(a):
    for x in range(0, len(a)):
        a[x] += 3
    print(a)
    return a[x]
modlist(intlist)

"""
6.passing multiple lists into a function:
a.Create a function that takes and prints 2 inputs.
b.Call the function you created in step 6.a. with the list you modified in step 5.b. and the range() you made in
step
 2.c.
"""
def print2list(a, b):
    print(a, b)
print2list(intlist, range3list)
"""
7.Iterating through a list of lists using a function:
a.Create a list that contains 3 lists. Each of those lists should be composed of all strings.
b.Create a function that appends all of the strings from the list you made in step a into a new, single list.
(This
 function should use 2 for loops.) This function should print the new list.
c.Call the function you made in step 7.b. using the list you created in step 7.a. as its input.
"""
listoflists = [["hello", "good", "morning"],["my", "name", "is"], ["what is", "your", "name"]]
def allinone(itens):
    allin = []
    for post in itens:
        for word in post:
            allin.append(word)
    print(allin)
allinone(listoflists)