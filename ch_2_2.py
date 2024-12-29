# Create a program to retrieve, display and update only a range of elements from an array using indexing and slicing in arrays. 

import array as arr

a = arr.array('i',[1,2,3,4,5,6,7,8,9])
print(a)
# Retrieve a range of elements using slicing
sliced_arr = a[2:5]
print("Elements from index 2 to 4:", sliced_arr)
# Update a range of elements using indexing and slicing
a[2:5] = arr.array('i',[10,11,12])
# Display the updated array
print("Updated Array:", a)