# List of elements
my_list = [10, 20, 30, 40, 50]

# Element to search for
search_element = int(input("Enter the element to search for: "))

# For loop to search for the element
for element in my_list:
    if element == search_element:
        print(f"Element {search_element} found in the list!")
        break
else:
    print(f"Element {search_element} not found in the list.")
