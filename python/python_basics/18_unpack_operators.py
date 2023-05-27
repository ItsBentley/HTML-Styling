# Unpack Operators

""" In Python, the unpacking operator, also known as the asterisk (*) operator, is a powerful feature that allows you to extract elements from iterable objects like lists, tuples, or dictionaries. It enables you to assign multiple values to multiple variables or collect multiple elements into a single variable.

Here are some common use cases of the unpacking operator: """

# 1. Unpacking a sequence into variables
a, b, c = [1, 2, 3]
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# 2. Unpacking a sequence with an arbitrary number of elements
a, b, *rest = [1, 2, 3, 4, 5]
print(a)  # Output: 1
print(b)  # Output: 2
print(rest)  # Output: [3, 4, 5]

# 3. Unpacking a tuple into separate variables
coordinates = (3.14, 2.71)
x, y = coordinates
print(x)  # Output: 3.14
print(y)  # Output: 2.71

# 4. Collecting multiple elements into a single variable
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)  # Output: 5

# 5. Unpacking dictionary items
person = {"name": "Alice", "age": 25, "city": "New York"}
name, age, city = person.items()
print(name)  # Output: ("name", "Alice")
print(age)  # Output: ("age", 25)
print(city)  # Output: ("city", "New York")


def func(*args, **kwargs):
    print(args, kwargs)


func(1, 2, 3, 4, 5, one=1, two=2)  # Output: (1, 2, 3, 4, 5, one=1, two=2)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*x)  # Output: 1 2 3 4 5 6 7 8 9 10


def func2(x, y):
    print(x, y)


pairs = [(1, 2), (3, 4), (5, 6)]

for pair in pairs:
    func2(*pair)  # Output: (1, 2) (3, 4) (5, 6)
