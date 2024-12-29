# Write a program to understand various methods of array class mentioned: append, insert, remove, pop, index, tolist and count.

import array as arr

numbers = arr.array('i', [10, 20, 30, 40, 50])
print("Original Array:", numbers)

# 1. Append: Add an element to the end of the array
numbers.append(60)
print("After append(60):", numbers)

# 2. Insert: Add an element at a specific position
numbers.insert(2, 25)  # Insert 25 at index 2
print("After insert(2, 25):", numbers)

# 3. Remove: Remove the first occurrence of an element
numbers.remove(40)
print("After remove(40):", numbers)

# 4. Pop: Remove and return an element at a specific position 
popped_element = numbers.pop(3)  # Pop element at index 3
print(f"After pop(3): {numbers}, Popped Element: {popped_element}")

# 5. Index: Find the index of the first occurrence of an element
index_of_50 = numbers.index(50) #mistake
print("Index of 50:", index_of_50)

# 6. To List: Convert the array to a Python list
numbers_list = numbers.tolist() #mistake
print("Array as a list:", numbers_list)

# 7. Count: Count the occurrences of an element in the array
count_of_20 = numbers.count(20) #mistake
print("Count of 20:", count_of_20)

