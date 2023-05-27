# While loops

""" In Python, a while loop is a control flow statement that allows you to repeatedly execute a block of code as long as a specified condition is true. It is called a "while" loop because the code block continues to execute while the condition remains true. Once the condition becomes false, the loop terminates, and the program continues with the next line of code after the loop.

The general syntax of a while loop in Python is as follows:

while condition:
    # Code block

Here, `condition` is an expression that evaluates to either True or False. The code block, indicated by indentation, contains the statements that are executed repeatedly as long as the condition is true.

Here's an example that demonstrates a simple while loop that counts from 1 to 5: """

count = 1
while count <= 5:
    print(count)
    count += 1

""" In this example, the initial value of `count` is 1. The while loop continues to execute as long as `count` is less than or equal to 5. Within the loop, the current value of `count` is printed, and then `count` is incremented by 1 using the `+=` operator. The loop terminates when `count` becomes 6.

It's important to ensure that the condition in a while loop eventually becomes false; otherwise, the loop will run indefinitely, resulting in an infinite loop. """

x = [3,4,42,3,2,4]

i = 0
while i < 10:
    print("run")
    i += 1

