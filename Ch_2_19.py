# Create a program to sort tuple with nested tuples.

def sort_nested_tuples(nested_tuple):
    # Sorting the nested tuples based on the first element and then by the second element
    sorted_tuples = sorted(nested_tuple) #mistake sorted
    return sorted_tuples

# Sample nested tuple
nested_tuple = ((3, 2), (1, 5), (2, 4), (1, 2), (3, 1))

# Sorting the nested tuple
sorted_tuple = sort_nested_tuples(nested_tuple)

# Displaying the sorted result
print("Original tuple:", nested_tuple)
print("Sorted tuple:", sorted_tuple)
