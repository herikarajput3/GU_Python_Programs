# Create a program to search the position of an element in an array using index() method of array class.

import array

# Create an array of integers
arr = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(arr)

# Element to search for
element_to_find = int(input("Enter element from above list: "))

position = arr.index(element_to_find)
print(f"Element {element_to_find} found at position: {position}")


