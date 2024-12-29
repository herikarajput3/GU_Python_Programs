# Write a program to convert the elements of two lists into key-value pairs of a dictionary. 

def lists_to_dict(keys, values):
    # Using zip to combine both lists into key-value pairs
    return dict(zip(keys, values)) # This function pairs elements from the keys list with elements from the values list, creating tuples.

# Main program
keys_list = input("Enter keys separated by spaces: ").split()  # e.g., "name age city"
values_list = input("Enter values separated by spaces: ").split()  # e.g., "Alice 30 NewYork"

# Convert the lists to a dictionary
result_dict = lists_to_dict(keys_list, values_list)

print("Resulting dictionary:")
print(result_dict)
