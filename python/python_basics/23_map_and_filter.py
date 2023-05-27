# Map and Filter functions

""" In Python, the "map" and "filter" functions are built-in higher-order functions that operate on iterables (such as lists, tuples, or strings) and provide a concise way to perform common operations on the elements within those iterables.

1. Map function:
The `map()` function applies a given function to each item in an iterable and returns an iterator containing the results. It takes two arguments: the function to apply and the iterable to operate on. The function is applied to each element in the iterable, and the results are returned as a map object or a list (if explicitly converted).

Here's the general syntax of the `map()` function: """

# map(function, iterable)

""" Example usage of `map()`: """

# Square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Convert a list of integers to strings
numbers = [1, 2, 3, 4, 5]
number_strings = list(map(str, numbers))
print(number_strings)  # Output: ['1', '2', '3', '4', '5']

""" 2. Filter function:
The `filter()` function constructs an iterator from elements of an iterable for which a given function returns true. It takes two arguments: the function that determines the filtering condition and the iterable to filter. Only the elements for which the function returns `True` will be included in the output.

Here's the general syntax of the `filter()` function: """

# filter(function, iterable)

""" Example usage of `filter()`: """

# Filter out even numbers from a list
numbers = [1, 2, 3, 4, 5]
filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(filtered_numbers)  # Output: [1, 3, 5]

# Filter out names starting with 'J'
names = ["John", "Jane", "Alice", "Bob", "James"]
filtered_names = list(filter(lambda name: name.startswith("J"), names))
print(filtered_names)  # Output: ['John', 'Jane', 'James']

""" In both cases, the functions passed to `map()` and `filter()` can be defined using lambda functions (anonymous functions) or regular named functions."""

# Lambda functions

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def func(i):
    i = i * 3
    return i % 2 == 0

mp = filter(func, x)
print(list(mp))

# But you can use lambda functions as well to get the same result

mp = map(lambda i: i + 2, x)
print(list(mp))

mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))

