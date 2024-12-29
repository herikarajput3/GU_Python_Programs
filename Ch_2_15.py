# Write a program to combine two List, perform repetition of lists and create cloning of lists.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 1. Combine two lists
combined_list = list1 + list2
print("Combined List:", combined_list)

# 2. Perform repetition of lists (repeat list1 3 times)
repeated_list = list1 * 3
print("Repeated List (list1 repeated 3 times):", repeated_list)

# 3. Create a clone (copy) of a list
cloned_list = list1[:]  # Cloning list1
# cloned_list = list1.copy()

print("Cloned List:", cloned_list)

# Modify the original list to show that the cloned list is independent
list1.append(7)
print("Original List after modification:", list1)
print("Cloned List after original list modification:", cloned_list)
