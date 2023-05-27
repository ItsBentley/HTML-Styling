# Arithmetic operations

""" Arithmetic operations in Python are mathematical operations that can be performed on numeric values, such as integers and floating-point numbers. Python provides several arithmetic operators that allow you to perform addition, subtraction, multiplication, division, and more. Here are the commonly used arithmetic operators in Python:

Addition (+): Adds two operands together.
Subtraction (-): Subtracts the second operand from the first operand.
Multiplication (*): Multiplies two operands together.
Division (/): Divides the first operand by the second operand. The result is always a floating-point number.
Floor Division (//): Performs integer division by dividing the first operand by the second operand and discarding any fractional part. The result is always an integer.
Modulo (%): Returns the remainder of the division between the first operand and the second operand.
Exponentiation (**): Raises the first operand to the power of the second operand.
Unary minus (-): Negates the value of the operand. """

x = 9
y = 3.5  # Doesn't need to be a whole number

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus (gives remainder)
print(x**y)  # Exponentiation (to the power of y)
print(x // y)  # Floor division (to the nearest integer)

# Order of operations is important BODMAS (Brackets, Operators, Division & Multiplication, Addition & Subtract)

num = input("Number: ")  # This won't work because input is a string
print(int(num) - 5)  # This will work because input is converted into a integer
print(float(num) - 5)  # This will work because input is converted into a float
