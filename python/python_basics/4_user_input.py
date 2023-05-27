# User input

""" In Python, a user input is a way for the user to interact with a program by providing data or information during its execution. It allows the program to receive input from the user and process it accordingly. The input can be text, numbers, or any other type of data.

The built-in function used to obtain user input in Python is input(). When this function is called, it displays a prompt or a message to the user, and then waits for the user to enter some text followed by pressing the Enter key. The text entered by the user is returned as a string by the input() function. """

input("Please enter your name: ")  # User input asking for name

name = input(
    "Please enter your name: "
)  # User input asking for name and assigning it to name
age = input(
    "Please enter your age: "
)  # User input asking for age and assigning it to age

print(name, age)  # Printing the name and age
print(f"Hello {name}, you are {age} years old!")  # Printing the name and age
