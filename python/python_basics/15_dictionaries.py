# Dictionaries

""" In Python, a dictionary is a built-in data structure that allows you to store and retrieve values based on keys. It is also known as an associative array, hash map, or hash table in other programming languages.

A dictionary is created using curly braces `{}` or by using the `dict()` constructor. Each element in a dictionary consists of a key-value pair, where the key is unique and associated with a specific value. The keys in a dictionary must be immutable objects such as strings, numbers, or tuples, while the values can be of any data type, including lists, dictionaries, or even functions.

Here's an example of creating a dictionary in Python: """

# Creating a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing values using keys
print(person["name"])  # Output: John
print(person["age"])  # Output: 30

# Modifying a value
person["city"] = "San Francisco"
print(person["city"])  # Output: San Francisco

# Adding a new key-value pair
person["occupation"] = "Engineer"
print(
    person
)  # Output: {'name': 'John', 'age': 30, 'city': 'San Francisco', 'occupation': 'Engineer'}

# Removing a key-value pair
del person["age"]
print(
    person
)  # Output: {'name': 'John', 'city': 'San Francisco', 'occupation': 'Engineer'}

""" Dictionaries provide fast access to values by using keys instead of numerical indices like lists or arrays. They are commonly used to represent real-world objects or to store data where the retrieval of values based on a specific identifier or key is important. """

x = {"Key": "Value"}
print(x["Key"])  # Output: Value

""" Dictionaries are mutable, which means that they can be changed after they are created. """

x["Key2"] = "New Value"
print(x["Key2"])  # Output: New Value

""" Dictionaries are unordered, which means that the order of the key-value pairs in a dictionary is not guaranteed. """

x["Key3"] = "New Value"
print(x["Key3"])  # Output: New Value

print("key" in x)  # Output: True
print(list(x.keys()))  # Output: ['Key', 'Key2', 'Key3']
print(list(x.values()))  # Output: ['Value', 'New Value', 'New Value']

del x["Key"] # Deleting a key-value pair
print(x)  # Output: {'Key2': 'New Value', 'Key3': 'New Value'}'

for key, value in x.items():
    print(key, value)  # Output: Key2 New Value \n Key3 New Value