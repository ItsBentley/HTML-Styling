# Sets

""" In Python, a "set" is an unordered collection of unique elements. It is a built-in data type that is used to store multiple items in a single variable. The elements in a set can be of different data types such as integers, floats, strings, and even other sets.

Sets are defined by enclosing a comma-separated sequence of elements within curly braces `{}`. Here's an example of creating a set in Python: """

my_set = {1, 2, 3, 4, 5}

""" In this example, `my_set` is a set containing the elements 1, 2, 3, 4, and 5. Notice that the elements are unordered, meaning that the order in which they appear in the set may not be preserved.

One of the main characteristics of sets is that they only store unique elements. If you try to add duplicate elements to a set, they will be automatically ignored. For example: """

my_set = {1, 2, 3, 4, 5, 5, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

""" In this case, the duplicate value of 5 is not included in the set. This uniqueness property of sets makes them useful for tasks such as removing duplicates from a list and performing mathematical operations like union, intersection, and difference between sets.

Sets also support various methods and operations for manipulation, such as adding elements, removing elements, checking membership, and performing set operations. """

x = set() # Use this to create a empty set
s = {1, 2, 3, 4, 5} # Use this to create a set containing the elements 1, 2, 3, 4, 5

# If you create an empty set using x = {} it will actually be an empty dictionary.

s.add(6) # Add 6 to the set
s.remove(6) # Remove 6 from the set
s.discard(6) # Remove 6 from the set if it is present
s.pop() # Remove and return the last element in the set
s.clear() # Remove all elements from the set
s.update([1, 2, 3, 4, 5]) # Update the set with the elements 1, 2, 3, 4, 5
s.intersection(s) # Return the intersection of the two sets
s.difference(s) # Return the difference of the two sets

# To check if an element is in the set, you can use the in operator.
print(6 in s) # Output: False
print(9 in s) # Output: True