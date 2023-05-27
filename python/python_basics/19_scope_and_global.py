# Scope and Global

""" In Python, "scope" refers to the region or part of a program where a variable or name is recognized and can be accessed. The scope determines the visibility and lifetime of a variable within a program. It defines the boundaries within which a variable can be referenced or modified.

Python has different types of scopes, including global scope, local scope, and nested scope. Here are the two main types you asked about:

1. Global scope: Variables defined in the global scope are accessible from anywhere within the program. They are not limited to a specific function or block of code. Global variables are typically defined outside of any function or class, at the top level of a module. They can be accessed and modified by any part of the program, including functions, classes, or other modules. """

# Example:
global_var = 10  # Global variable


def my_function():
    print(global_var)  # Accessing global variable


my_function()  # Output: 10

""" 2. Local scope: Variables defined within a function have a local scope. They are accessible only within that specific function. Local variables are created when the function is called and are destroyed when the function execution completes. They cannot be accessed from outside the function. """


# Example:
def my_function():
    local_var = 20  # Local variable
    print(local_var)


my_function()  # Output: 20
# print(local_var)  # Error: NameError: name 'local_var' is not defined

""" It's important to note that if you want to modify a global variable from within a function, you need to use the `global` keyword to explicitly declare that you are referring to the global variable and not creating a new local variable with the same name. """

# Example:
global_var = 10


def my_function():
    global global_var
    global_var = 20


my_function()
print(global_var)  # Output: 20

""" Understanding variable scopes is crucial for writing organized and maintainable code, as it helps you manage the visibility and lifetime of variables throughout your program. """
