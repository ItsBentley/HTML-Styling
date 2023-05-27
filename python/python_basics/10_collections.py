# Collections

""" In Python, a collection refers to a group of objects or values that are stored together. Python provides several built-in collection types that allow you to store, organize, and manipulate multiple elements efficiently. The commonly used collection types in Python include lists, tuples, sets, and dictionaries.

1. Lists: A list is an ordered collection of items enclosed in square brackets ([]). It allows you to store elements of different types and supports operations like adding, removing, or modifying items. Lists are mutable, meaning you can change their content.

Example: fruits = ['apple', 'banana', 'orange']

2. Tuples: A tuple is an ordered collection of items enclosed in parentheses (()). Similar to lists, tuples can store elements of different types. However, tuples are immutable, meaning you cannot modify their content after creation.

Example: point = (3, 4)

3. Sets: A set is an unordered collection of unique elements enclosed in curly braces ({}). Sets do not allow duplicate values, and they support mathematical set operations like union, intersection, and difference.

Example: numbers = {1, 2, 3, 4, 5}

4. Dictionaries: A dictionary is an unordered collection of key-value pairs enclosed in curly braces ({}). Each element in a dictionary consists of a key and its associated value. Dictionaries are commonly used for fast retrieval of values based on their unique keys.

Example: person = {'name': 'John', 'age': 30, 'city': 'New York'}

Collections in Python provide various methods and operations to perform tasks like accessing elements, iterating over items, searching, sorting, and more. Depending on your specific needs, you can choose the appropriate collection type to store and manipulate your data efficiently. """

x = [4, True, "hi"]  # List can store elements of different types.
print(len(x))
print(x[2])

x.append("John")  # Will add an element to the end of the list.
x.extend([1, 2, 3])  # Will add multiple elements to the end of the
print(x)

x.insert(0, "John")  # Will add an element to the beginning of the list.
print(x)

x.pop()  # Will remove the last element from the list.
print(x)

x.pop(0)  # Will remove the first element from the list.
print(x)

x.remove("hi")  # Will remove the first occurrence of the element.
print(x)

x.reverse()  # Will reverse the order of the list.
print(x)

x.sort()  # Will sort the list.
print(x)

x.sort(reverse=True)  # Will sort the list in reverse order.
print(x)

x[0] = 10  # Will change the first element of the list.
print(x)

y = x[:]  # Will return a shallow copy of the list.
print(y)

y = x.copy()  # Will return a deep copy of the list.
print(y)

x.clear()  # Will clear the list.
print(x)

x = (0, 1, 2, 3)  # Tuple can store elements of different types but they are immutable.
print(x[0])
