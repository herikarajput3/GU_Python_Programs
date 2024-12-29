# Define two lists
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

# Find common elements
common_elements = [element for element in list1 if element in list2]

# Find non-common elements (elements that are only in list1 or list2, but not both)
non_common_elements = [element for element in list1 + list2 if element not in common_elements]

# Display the results
print("Common elements:", common_elements)
print("Non-common elements:", non_common_elements)
