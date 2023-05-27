# If / Else / Elif statements

""" In Python, chained conditionals refer to a series of if-elif-else statements that are linked together to evaluate multiple conditions in a sequential manner. They allow you to check for multiple conditions and execute different blocks of code based on the outcome of those conditions. """

x = 5

if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
elif x > 0 and x <= 10:
    print("x is a positive number between 1 and 10")
else:
    print("x is a positive number greater than 10")


x = input("Name: ")

if x == "John":
    print("Hello John")
elif x == "Mary":
    print("Hello Mary")
elif x == "Barry":
    print("Hello Barry")
else:
    print(f"Your name is {x}")
