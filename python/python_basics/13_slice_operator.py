# Slice Operators

""" In Python, the slice operator is a feature that allows you to extract a portion (or slice) of a sequence, such as a string, list, or tuple. The slice operator uses the colon (`:`) to indicate the start, stop, and step values for the slice.

The syntax for the slice operator is as follows:

sequence[start:stop:step]

Here's a breakdown of the components:

- `start` (optional): It specifies the index where the slice starts. If not provided, it defaults to the beginning of the sequence (index 0).
- `stop` (required): It specifies the index where the slice ends. The slice includes all elements up to, but not including, the element at the stop index.
- `step` (optional): It determines the increment between indices while slicing. If not provided, it defaults to 1, meaning consecutive elements will be included in the slice. A negative step value allows you to traverse the sequence in reverse.

Here are a few examples to illustrate the usage of the slice operator: """

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract a slice from index 2 to index 5 (exclusive)
slice1 = my_list[2:5]
print(slice1)  # Output: [2, 3, 4]

# Extract a slice from index 1 to the end
slice2 = my_list[1:]
print(slice2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract a slice from the beginning to index 6 (exclusive), with a step of 2
slice3 = my_list[:6:2]
print(slice3)  # Output: [0, 2, 4]

# Reverse the list using a negative step
reverse_slice = my_list[::-1]
print(reverse_slice)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

""" The slice operator is a powerful tool in Python for manipulating sequences and extracting subsets of data efficiently. """

x = [0,1,2,3,4,5,6,7,8,9]
y = ["hi", "hello", "world", "cya", "sure"]
s = "hello"

# slice = y[start,stop,step]

slice = y[0:4:2]
print(slice) 

slice = y[0:4]
print(slice)

slice = y[::2] # Will print all but step by 2
print(slice)

slice = y[::-1] # Will print in reverse order
print(slice)