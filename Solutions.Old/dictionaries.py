# Dictionaries Problems:
"""
Creating Dictionaries, Accessing by Key, Adding to Dictionaries, and Length of a Dictionary:
1.create a 3 key: value pair dictionary and assign it to a variable
2.access and print a value from the list in step 1 by key
3.add a fourth key: value pair to the dictionary from step 1
4.print the dictionary from step 3
5.print the length of the dictionary from step 3
"""
# ----------------------------------------------------------------------------------------------------------------------

dic = {23:"duck", 22:"cat", 21:"rat"}
print(dic[22])
dic[20] = "turtle"
print(dic)
print(len(dic))

# ----------------------------------------------------------------------------------------------------------------------
"""
Reassignment by Key and Del:
1.create a 2 key: value pair dictionary and assign it to a variable
2.print the dictionary from step 1
3.reassign a key from the dictionary in step 1 a different value than its original value
4.print the dictionary from step 3
5.remove a key: value pair from the dictionary from step 3 using del
6.print the new dictionary
"""
# ----------------------------------------------------------------------------------------------------------------------

pair = {1:"first", 2:"second"}
print(pair)
pair[2] = "two"
print(pair)
del pair[1]
print(pair)

# ----------------------------------------------------------------------------------------------------------------------