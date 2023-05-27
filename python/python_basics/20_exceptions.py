# Exceptions

""" In Python, an exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. It is a way to handle errors and exceptional situations that may arise while the program is running.

When an exception occurs, it typically causes the program to terminate and displays an error message, unless it is caught and handled properly. Exceptions can be raised explicitly by the programmer or raised automatically by the Python interpreter when it encounters an error.

Common examples of exceptions in Python include:

1. `SyntaxError`: Raised when the code violates Python's syntax rules.
2. `NameError`: Raised when an identifier (variable, function, etc.) is not found.
3. `TypeError`: Raised when an operation is performed on an object of an inappropriate type.
4. `ValueError`: Raised when a function receives an argument of the correct type but an invalid value.
5. `IndexError`: Raised when trying to access an index that is out of range in a sequence (e.g., list, string).
6. `KeyError`: Raised when trying to access a non-existent key in a dictionary.
7. `FileNotFoundError`: Raised when a file cannot be found or opened.
8. `ZeroDivisionError`: Raised when division or modulo operation is performed with zero as the divisor.

To handle exceptions and prevent program termination, you can use the `try-except` statement. It allows you to catch and handle specific exceptions that may occur within a block of code. By handling exceptions gracefully, you can display custom error messages, log the error, or perform alternative actions to recover from the exception and continue program execution. """

raise SyntaxError("This is a syntax error.")

raise NameError("This is a name error.")

raise TypeError("This is a type error.")

raise ValueError("This is a value error.")

raise IndexError("This is an index error.")

raise KeyError("This is a key error.")

raise FileNotFoundError("This is a file not found error.")

raise ZeroDivisionError("This is a zero division error.")