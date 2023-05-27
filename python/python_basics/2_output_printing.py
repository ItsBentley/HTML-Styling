# Output and printing functions

print("Hello World!")
print(4.5)

# Print multiple values

print("Hello", "World")
print("Hello", 4.5)
print("Hello", 4.5, "World")
print("Hello", 4.5, "World", "!")

# Print multiple lines using \n

print("Hello\nWorld")

# Print with a function at the end

print("Hello", end="\n")  # Default end is \n
print("Hello", end=" | ")  # Now it will end with a |
print("World")  # Notice when you print their is now a | between them rather than \n
