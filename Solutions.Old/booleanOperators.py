"""
and, or, and not:
1.create a variable and set it equal to True using a statement containing an "and" Boolean operator
2.create a variable and set it equal to False using a statement containing an "and" Boolean operator
3.create a variable and set it equal to True using a statement containing an "or" Boolean operator
4.create a variable and set it equal to False using a statement containing an "or" Boolean operator
5.create a variable and set it equal to True using a statement containing an "not" Boolean operator
6.create a variable and set it equal to False using a statement containing an "not" Boolean operator
"""
# type your code for "and, or, and not" below this comment and above the one below it.----------------------------------

bool1 = 67 != 32 + 4 and 4 ** 4 >= 160
bool2 = 4 * 2 == 3 and 2 + 2 < 5
bool3 = 8 % 7 < 2 or 9 * 8 >= 4
bool4 = 6 == 7 or 7 % 4 != 3
bool5 = not 6 < 2
bool6 = not 9 == 3 * 3
print(bool1,bool2,bool3,bool4,bool5,bool6)

# ----------------------------------------------------------------------------------------------------------------------
"""
order of operations for Boolean operators:
1.make var1 evaluate to False by changing or removing a single Boolean operator
2.make var2 evaluate to True by changing or removing a single Boolean operator
"""
# type your code for "order of operations for Boolean operators" below this comment and above the one below it. --------
var1 = not 3 > 1 and 5 != 2 or 6 == 7
var2 = 4 * 2 != 6 and not 6 % 6 == 1
print(var1, var2)
# ----------------------------------------------------------------------------------------------------------------------