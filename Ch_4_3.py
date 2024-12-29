# Importing the os module
import os

# Print the current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

# Get a list of all functions and attributes in the os module
os_functions = dir(os)
print("\nList of all functions and attributes in the 'os' module:")
print(os_functions)
