# Write a program to create a list using range functions and perform append, update and delete elements operations in it.

# Create a list using range function
my_list = list(range(1, 11)) #mistake # Creates a list with numbers from 1 to 10
print("Original List:", my_list)

my_list.append(11)  # Adding the number 11 to the end of the list
print("After Appending 11:", my_list)

my_list[4] = 50 #mistake  # Updating the 5th element (index 4) with the value 50
print("After Updating 5th Element to 50:", my_list)

del my_list[2] #mistake  # Deleting the 3rd element (index 2)
print("After Deleting the 3rd Element:", my_list)
