# Veriables

""" In Python, a variable is a name that represents a value stored in memory. It acts as a container for storing data of different types, such as numbers, strings, lists, or more complex objects. Variables allow you to manipulate and work with data in your programs.

To create a variable in Python, you simply assign a value to a name using the assignment operator (=) """

hello = "Hello World"
print(hello)

print(hello[0])  # This will print the first letter of the string
print(hello[-1])  # This will print the last letter of the string
print(hello[0:2])  # This will print the first 2 letters of the string
print(hello[2:4])  # This will print letters 2 and 3 of the string
print(hello[::-1])  # This will print the in reversed order

hello = "Hello"  # When you change a variable, it will overwrite the value of the variable from before
world = "World"

print(hello, world)  # This will print Hello World
print(f"{hello} {world}")  # This will also print Hello World (This is an f string)
print(hello + " " + world)  # This will also print Hello World (Another way to do this)

hello_world = (
    "Hello World"  # Convention in python is to separate a variable with an underscore
)
# You can't start a variable with an underscore or a number or special characters
