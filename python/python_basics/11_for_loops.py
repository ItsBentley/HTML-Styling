# For loops

""" In Python, a "for loop" is a control flow statement that allows you to iterate over a sequence of elements such as a list, tuple, string, or other iterable objects. It is used to repeatedly execute a block of code for each item in the sequence.

The general syntax of a for loop in Python is as follows:

for item in sequence:
    # Code block to be executed

Here's how it works:

1. The `sequence` can be any iterable object that contains a collection of elements.
2. The `item` is a variable that takes on the value of each element in the `sequence` during each iteration of the loop. You can choose any valid variable name you like.
3. The code block following the colon (`:`) is indented and represents the set of instructions to be executed for each item in the sequence.

During each iteration of the loop, the value of the `item` variable is updated to the next element in the sequence, and the code block is executed. This process continues until all the elements in the sequence have been processed.

Here's an example that demonstrates the usage of a for loop: """

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# Output: apple, banana, orange

""" In this example, the `fruits` list contains three elements. The for loop iterates over each element in the list, assigns it to the `fruit` variable, and then prints the value of `fruit` in each iteration.

For loops are a powerful construct in Python that allow you to automate repetitive tasks and process collections of data efficiently. """

for i in range(10): # range function doesn't include the end value, (start, stop, step)
    print(i)

for i in [3,4,5,6,7,8,9,10]:
    print(i)

x = ["john", "dave", "jane", "john"]
for i in x:
    print(i)

for i, element in enumerate(x):
    print(i, element)
    