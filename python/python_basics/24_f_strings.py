# f-strings

""" In Python, an f-string is a way to format strings that allows you to embed expressions directly into string literals. The "f" in f-string stands for "formatted". F-strings were introduced in Python 3.6 as a concise and readable way to combine variables or expressions with string values.

To create an f-string, you prefix the string with the letter "f" or "F" and enclose the expressions you want to include within curly braces {}. The expressions are then evaluated and their values are inserted into the string. Here's an example: """

name = "Alice"
age = 25
message = f"Hello, my name is {name} and I am {age} years old."
print(message)

""" Output: """
# Hello, my name is Alice and I am 25 years old.

""" In the example above, the variables `name` and `age` are included in the string using f-string syntax. The expressions `{name}` and `{age}` are evaluated and their values are inserted into the resulting string.

F-strings also support formatting options, such as specifying the number of decimal places for floating-point numbers or the minimum width of an integer. Here's an example that demonstrates formatting options: """

pi = 3.14159265359
formatted_pi = f"Value of pi: {pi:.2f}"
print(formatted_pi)

""" Output: """
# Value of pi: 3.14

""" In the example above, the expression `{pi:.2f}` formats the value of `pi` as a floating-point number with two decimal places.

F-strings are a powerful and convenient way to create formatted strings in Python, making it easier to combine variables and expressions with textual content. They provide a more readable and concise alternative to older string formatting methods like the `%` operator or the `str.format()` method. """