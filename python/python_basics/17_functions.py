# Functions

""" In Python, a function is a block of reusable code that performs a specific task. It is a way to organize and encapsulate a set of instructions into a single unit. Functions take input arguments (parameters), perform some operations, and can optionally return a value.

Functions provide modularity and code reusability, allowing you to break down complex programs into smaller, more manageable pieces. They promote clean code by separating different tasks into distinct functions, making the code easier to read, understand, and maintain.

Here's an example of a simple function in Python: """


def greet(name):
    # A function that greets the user by name.
    print(f"Hello, {name}!")


# Calling the function
greet("Alice")
greet("Bob")

""" In this example, we define a function named `greet` that takes one parameter `name`. Inside the function, it prints a greeting message using the provided name. When we call the `greet` function with different names, it executes the code inside the function and displays the appropriate greeting.

Output:
Hello, Alice!
Hello, Bob!

Functions can also have a `return` statement to send a value back to the caller. For example: """


def add_numbers(a, b):
    # A function that adds two numbers and returns the result.
    return a + b


# Calling the function and storing the result in a variable
result = add_numbers(5, 3)
print(result)  # Output: 8

""" In this case, the `add_numbers` function takes two parameters `a` and `b`, adds them together, and returns the result. The returned value is then stored in the `result` variable and printed. """


def func():
    print("Hello, world!")


func()


def func2(x, y):
    print(x, y)


func2(1, 2)


def func3(x, y):
    return x * y, x / y, x ** y, x % y, 


print(func3(2, 5))

r1, r2, r3, r4 = func3(2, 5)
print(r1, r2, r3, r4)