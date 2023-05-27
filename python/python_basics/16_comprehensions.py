# Comprehensions

"""In Python, comprehension refers to a concise and expressive way to create new lists, dictionaries, or sets based on existing iterables. It allows you to combine loops and conditional statements into a single line of code.

There are three types of comprehensions in Python:

1. List Comprehension: It is used to create a new list by iterating over an existing iterable and applying certain conditions or transformations to each element. The resulting list is constructed within square brackets."""

# Example:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers if x % 2 == 0]
print(squared_numbers)  # Output: [4, 16]

"""2. Dictionary Comprehension: It allows you to create a new dictionary by iterating over an iterable and defining key-value pairs based on certain conditions or transformations. The resulting dictionary is constructed within curly braces."""

# Example:
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x**2 for x in numbers if x % 2 == 0}
print(square_dict)  # Output: {2: 4, 4: 16}

"""3. Set Comprehension: It is used to create a new set by iterating over an iterable and applying certain conditions or transformations to each element. The resulting set is constructed within curly braces."""

# Example:
numbers = [1, 2, 3, 4, 5]
even_squares = {x**2 for x in numbers if x % 2 == 0}
print(even_squares)  # Output: {16, 4}

"""Comprehensions offer a concise and readable way to perform common operations on iterables, eliminating the need for explicit loops and conditional statements. They are widely used in Python for their simplicity and efficiency."""

x = [x for x in range(10)]
print(x)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = [i for i in range(100) if i % 5 == 0] # List
print(x)  # Output: [0, 20, 40, 60, 80]

x = {i for i in range(100) if i % 5 == 0} # Dictionary
print(x)  # Output: {0, 20, 40, 60, 80}

x = tuple(i for i in range(100) if i % 5 == 0) # Tuple
print(x)  # Output: (0, 20, 40, 60, 80)