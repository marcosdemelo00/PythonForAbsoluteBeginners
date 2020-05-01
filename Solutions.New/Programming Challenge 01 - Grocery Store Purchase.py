"""
Programming Challenge: Grocery Store Purchase
A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
Penne 16 oz Pack of 12 - $16.68
Arrabiata Pasta Sauce 24 oz - $6.98
Bag of 20 Organic Garlic Cloves - $16.78
Italian Seasoning 1.5 oz Bottle - $15.26
Artisan Baguettes Twin Pack - $3.00
12 oz Bag of Meatballs - $4.39

In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.  The subtotal is just the sum of all of their prices.
Use print() to display the result of the expression.
"""
#Wrong way

print('The products sum is {} \'wrongway\''.format(16.68 + 6.98 + 16.78 + 15.26 + 3.00 + 4.39))

#Integer Solution

prodint = (16.68 * 100) + (6.98 * 100) + (16.78 * 100) + (15.26 * 100) + (3.00 * 100) + (4.39 * 100)
print('The products sum is {} \'integerway\''.format(prodint / 100))

#Round Solution

prodlist = [16.68, 6.98, 16.78, 15.26, 3.00, 4.39]
prodval = 0
for val in prodlist:
  prodval += val
print('The products sum is {} \'roundway\''.format(round(prodval, 2)))