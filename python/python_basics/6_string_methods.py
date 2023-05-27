# String methods

""" In Python, a string method is a function that can be called on a string object to perform various operations or manipulations on the string. String methods allow you to easily modify, analyze, or extract information from strings. """

hello = "hello world, how are you?"

print(type(hello))  # type() is the method
print(hello.upper())  # .upper() is the method
print(hello.lower())  # .lower() is the method
print(hello.capitalize())  # .capitalize() is the method
print(
    hello.count("l")
)  # .count() is the method, you put what you want to count between the brackets
print(
    hello.find("l")
)  # .find() is the method, you put what you want to find between the brackets
print(
    hello.replace("l", "4")
)  # .replace() is the method, you put what you want to replace between the brackets

my_string = "Hello, World!"

# Using string methods to manipulate and analyze the string
print(my_string.upper())  # Output: "HELLO, WORLD!"
print(my_string.lower())  # Output: "hello, world!"
print(my_string.startswith("Hello"))  # Output: True
print(my_string.endswith("World!"))  # Output: True
print(my_string.split(","))  # Output: ["Hello", " World!"]
print(len(my_string))  # Output: 13
