# Create a sample list of 7 elements and implement the List methods mentioned: append, insert, copy, extend, count, remove, pop, sort, reverse and clear. 

# Sample list with 7 elements
my_list = [10, 20, 30, 40, 50, 60, 70]
print("Original List:", my_list)

# 1. Append: Adds an element at the end of the list
my_list.append(80)
print("After Append (80):", my_list)

# 2. Insert: Inserts an element at a specific index
my_list.insert(3, 35)  # Inserts 35 at index 3
print("After Insert (35 at index 3):", my_list)

# 3. Copy: Creates a shallow copy of the list
copied_list = my_list.copy()
print("Copied List:", copied_list)

# 4. Extend: Extends the list by adding elements from another iterable (e.g., another list)
my_list.extend([90, 100]) #mistake
print("After Extend ([90, 100]):", my_list)

# 5. Count: Counts the occurrences of a specific element
count_of_30 = my_list.count(30)
print("Count of 30 in the List:", count_of_30)

# 6. Remove: Removes the first occurrence of a specific element
my_list.remove(50)
print("After Removing 50:", my_list)

# 7. Pop: Removes and returns the last element or element at a specific index
popped_element = my_list.pop()
print("After Pop (removes last element):", my_list)
print("Popped Element:", popped_element)

# 8. Sort: Sorts the list in ascending order
my_list.sort()
print("After Sort:", my_list)

# 9. Reverse: Reverses the order of the list
my_list.reverse()
print("After Reverse:", my_list)

# 10. Clear: Removes all elements from the list
my_list.clear()
print("After Clear:", my_list)
