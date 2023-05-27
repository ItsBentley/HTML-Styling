# Exception handling

""" In Python, you can handle exceptions using a try-except block. The try block contains the code that might raise an exception, and the except block specifies how to handle the exception if it occurs. Here's the general syntax: """

try:
    # Code that might raise an exception
    ...
except TypeError:
    # Exception handling code for TypeError, which prints a message. These errors can be anything.
    ...
except ValueError:
    # Exception handling code for ValueError, which prints a message. These errors can be anything.
    ...
else:
    # Optional: Code that executes if no exception occurs
    ...
finally:
    # Optional: Code that always executes, regardless of whether an exception occurred or not
    ...

""" Let's break down the different parts:

- The `try` block contains the code that you want to monitor for exceptions.
- If an exception of type `ExceptionType1` occurs within the `try` block, the corresponding `except` block for `ExceptionType1` is executed.
- You can have multiple `except` blocks to handle different types of exceptions. If the exception raised doesn't match any of the specified types, it will propagate up to the next enclosing try-except block or result in a program termination if unhandled.
- The `else` block is optional and contains code that executes only if no exceptions were raised within the `try` block.
- The `finally` block is also optional and contains code that always executes, regardless of whether an exception occurred or not. It's typically used for cleanup operations that must be performed regardless of exceptions.

Here's an example that demonstrates exception handling in Python: """

try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Division successful.")
finally:
    print("Finally block executed.")

""" In this example, the `try` block attempts to divide 10 by 0, which raises a `ZeroDivisionError`. The corresponding `except` block is executed, printing an error message. The `else` block is skipped since an exception occurred. Finally, the `finally` block executes, displaying the message "Finally block executed."

By using exception handling, you can gracefully handle errors and prevent your program from crashing unexpectedly. """