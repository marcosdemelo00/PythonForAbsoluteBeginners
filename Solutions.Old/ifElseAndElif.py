"""
For this problem you are going to make a program that simulates the output of a vending machine that only takes in
coins of American currency.
1.Your program should take an integer as an input from the user (either a 1, 2, or 3) that corresponds with an option
 for a drink from the vending machine outlined below and assign the corresponding price to a variable as a float.
 Use your knowledge of if, elif, and else statements to complete this part of the problem. Your code should
 have an else statement that prints a message and ends the program using sys.exit() if the user does not enter a valid
 input number.
 Vending Machine:
 1.water = $1.00
 2.cola = $1.50
 3.gatorade = $2.00
2.After placing an order, the user should be prompted to enter inputs 4 times:
 1.The first time, the user should be prompted to enter the number of quarters they put in the machine. Assign this
 number to a variable as an integer.
 2.The second time, the user should be prompted to enter the number of dimes they put in the machine. Assign this
 number to a variable as an integer.
 3.The third time, the user should be prompted to enter the number of nickles they put in the machine. Assign this
 number to a variable as an integer.
 4.The fourth time, the user should be prompted to enter the number of pennies they put in the machine. Assign this
 number to a variable as an integer.
3.Create a variable to hold the total value of all the coins the user has put into the machine.
4.Use flow control statements to print the user's change or output a message asking the user to try again depending
 on whether the total value of the coins the user has put into the machine is enough to pay for the item they ordered.
New knowledge for this problem:
1.%f format specifier
2.import sys and sys.exit()
3.int()
"""
import sys
print(
    """Vending Machine:
    1. Water = $1.00
    2. Cola = $1.50
    3. Gatorade = $2.00""")
order = int(input("Please enter your order: "))

if order == 1:
    price = 1.00
    print("You choose = Water $1.00")
elif order == 2:
    price = 1.50
    print("You choose = Cola $1.50")
elif order == 3:
    price = 2.00
    print("You choose = Gatorade $2.00")
else:
    sys.exit("Please try again. You must enter a valid option: 1, 2 or 3")

quarters = int(input("Now, enter the number of quarters you will insert: "))
dimes = int(input("Enter the number of dimes: "))
nickel = int(input("Enter the number of nickel: "))
pennies = int(input("Enter the number of pennies: "))
total = quarters * 0.25 + dimes * .10 + nickel * .05 + pennies * 0.01

if total == price:
    print("Thank you, your order is ready.")
elif total > price:
    print("Thank you, your order is ready. Your change is $%.2f"%(total - price))
else:
    print("Your payment is not enough. Please try again.")