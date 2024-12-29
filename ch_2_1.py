import array

# Original array
og_arr = array.array('i', [1, 2, 3, 4, 5, 6])

# Creating a copy of the original array
new_arr = og_arr[:]

print("Original array:", og_arr)
print("New array:", new_arr)

print(id(og_arr))
print(id(new_arr))

