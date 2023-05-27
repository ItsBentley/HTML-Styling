# Chained conditionals

""" In Python, chain conditionals refer to combining multiple logical conditions using the logical operators "not," "and," and "or." These operators allow you to create complex conditional expressions by evaluating multiple conditions simultaneously. """

x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z - 2 < x + 2  # It will work out either side of the comparison first

# Order of conditions is not, and, or

result4 = result1 or result2 or result3
print(result4)

result4 = result1 or not result2 or result3
print(result4)

