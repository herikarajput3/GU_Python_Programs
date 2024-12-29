# Write a program to create nested list and display its elements.

# Creating a nested list (a list within another list)
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Display the entire nested list
print("Nested List:", nested_list)

# Displaying each sublist in the nested list
for sublist in nested_list:
    print("Sublist:", sublist)

# Displaying each element in the nested list individually
print("\nElements in the nested list:")
for sublist in nested_list: #mistake
    for item in sublist:
        print(item, end=" ")
