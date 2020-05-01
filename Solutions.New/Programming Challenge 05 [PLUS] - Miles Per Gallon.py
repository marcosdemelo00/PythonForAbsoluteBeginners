"""
Programming Challenge: Miles Per Gallon
For this exercise, you will create a program that approximates the number of miles per gallon that a car gets.

In a .py file, create two variables, one which will hold a randomly generated integer between 10 and 25
(inclusive of both 10 and 25), and another which will hold a randomly generated integer between and inclusive of 200 and 400.
The first variable represents the number of gallons of gas that the car's fuel tank holds.
The second variable represents the miles that the car can travel on a full tank before needing a refuel.

Using the formula miles per gallon (MPG) = miles driven/gallons used,
calculate the car's MPG and display it in the output using print().
Use floor division instead of regular division for this calculation to get an integer instead of a float.
This will give a realistic approximation of miles per gallon even though floats
such as 19.8 round down a large amount when using floor division since sometimes,
car manufacturers sometimes exaggerate miles per gallon.
In addition, display the values held in the variables you created for gallons of gas in the car's fuel tank
and miles it can travel on a full tank with two different print statements.
"""
from random import randint


def sumlist(list):
    temp = 0
    for i in list:
        temp += i
    return temp


count = int(input("Enter de quantity of car that you want to evaluate: "))
innercount = 0
tfuel = []
tmiles = []
tmpg = []

while innercount < count: #generating random values lists
    gallons = randint(10, 25)
    tfuel.append(gallons)
    miles_driven = randint(200, 400)
    tmiles.append(miles_driven)
    mpg = miles_driven // gallons
    tmpg.append(mpg)
    innercount += 1
print(tfuel)
print(tmiles)
print(tmpg)
print ("The average of " + str(count) + " cars can hold ", str(sumlist(tfuel) // count) , " gallons of gas")
print ("The average of " + str(count) + " cars can travel", str(sumlist(tmiles) // count) , "with a full tank")
print ("The average of " + str(count) + " cars can travel", str(sumlist(tmpg) // count) , "per gallons")