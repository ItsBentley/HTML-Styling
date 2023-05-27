# Lambdas

""" In Python, `lambda` is a keyword used to define anonymous functions, also known as lambda functions. These functions are defined without a name and are typically used for short, one-line operations where defining a separate named function would be unnecessary or cumbersome.

The general syntax of a lambda function is: """

# lambda arguments: expression

""" Here, `arguments` represent the input parameters of the function, and `expression` is the operation or calculation that is performed on the arguments. The result of the expression is then returned as the output of the lambda function.

Lambda functions can be assigned to variables or used directly within other functions. They are often used in combination with higher-order functions like `map()`, `filter()`, and `reduce()`, where a function is expected as an argument.

Here's an example to illustrate the usage of lambda functions: """

# Example 1: Lambda function assigned to a variable
multiply = lambda x, y: x * y
result = multiply(5, 3)
print(result)  # Output: 15

# Example 2: Lambda function used with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

""" In Example 1, a lambda function `multiply` is defined to multiply two numbers. The lambda function is assigned to the variable `multiply`, and it can be invoked like a regular function.

In Example 2, the lambda function is used with the `map()` function to square each element of the `numbers` list. The lambda function takes an argument `x` and returns `x ** 2`, which is applied to each element using `map()`. The resulting squared values are stored in the `squared` list.

Lambda functions provide a concise way to define simple functions without the need for explicitly naming them, making them convenient for certain scenarios. However, for more complex or reusable functions, it's generally recommended to use named functions defined using the `def` keyword. """