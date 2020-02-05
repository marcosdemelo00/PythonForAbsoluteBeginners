# Using Functions With Lists Problems:
"""
0.Setup:
a.create a list of integers and assign it to a variable
b.create a list of strings and assign it to a variable
c.create a list of floats and assign it to a variable
"""
intli = [5, 4, 3, 2, 1]
strli = ["five", "four", "three", "two", "one"]
floli = [5.0, 4.0, 3.0, 2.0, 1.0]
"""
1.Passing A List to A Function:
a.create a function that takes and returns an input
b.print a call of the function you created in step 1.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 1.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 1.a. with the list of floats from step 0.c. as the input
"""
def take(alist):
    return alist
print(take(intli))
print(take(strli))
print(take(floli))
"""2.Accessing An Element In A list using A Function:
a.create a function that takes a list as an input and returns one of that lists elements
b.print a call of the function you created in step 2.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 2.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 2.a. with the list of floats from step 0.c. as the input
"""
def takeone(elem):
    return elem[1]
print(takeone(intli))
print(takeone(strli))
print(takeone(floli))
"""3.Modifying A List Element Within A Function:
a.create and call a function that prints the product of all the integers from the list you created in step 0.a.
b.create and call a function that concatenates all the strings from the list you create in step 0.b and prints the
 result
c.create and call a function that prints the quotient of all the floats from the list you created in step 0.c.
"""
def prod(pd):
    mult = 1
    for int in pd:
        mult *= int
    return mult
print(prod(intli))

def conc(word):
    ww = ""
    for w in word:
        ww += w
    return ww
print(conc(strli))

def quoc(dv):
    divi = 1
    for flo in dv:
        divi /= flo
    return divi
print(quoc(floli))
"""4.Manipulating Lists Within Functions:
a.create a list that uses 3 of the following functions on one of the lists you created in part 0 of this problem set:
 .index(), .append(), .remove(), .insert, or .pop(). Also, make sure that the function prints the resulting list
b.call the function from part 4.a. using one of the lists you made in part 0 of this problem set.
"""
def lastlist(f):
    f.append(0)
    f.insert(0, 6)
    f.remove(3)
    print(f)
lastlist(intli)