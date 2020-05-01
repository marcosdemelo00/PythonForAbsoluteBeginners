'''
Programming Challenge: Fizz Buzz
Write a program that prints the integers 1 through 50 using a loop.

However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in
the output. For numbers which are multiples of 3 but not 5 print “Fizz”
instead of the number and for the numbers that are multiples of 5 but not 3
print “Buzz” instead of the number.

All of the remaining numbers which are not multiples of 3 or 5 should just be
printed as themselves.
'''

for i in range(1, 51):
    if i % 3 == 0:
        if i % 5 == 0:
            i = 'FizzBuzz'
        else:
            i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    print(i)
