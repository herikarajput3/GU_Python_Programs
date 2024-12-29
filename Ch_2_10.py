# Write a program to show variable length argument and its use.

# Function to demonstrate variable-length positional arguments
def print_numbers(*args):
    print("The numbers are:")
    for num in args:
        print(num)

# Function to demonstrate variable-length keyword arguments
def print_person_info(**kwargs):
    print("Person Information:")
    for key, value in kwargs.items(): #This method returns a view object that displays a list of a dictionary's key-value tuple pairs.
        print(f"{key}: {value}")

# Using the functions
print("Using *args:")
print_numbers(1, 2, 3, 4, 5)  # Passing variable number of positional arguments

print("\nUsing **kwargs:")
print_person_info(name="Alice", age=30, city="New York")  # Passing variable number of keyword arguments


    