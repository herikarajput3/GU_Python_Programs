# Create a python function to accept python function as a dictionary and display its elements.

# The program allows us to define some functions and then puts these functions into a dictionary. It then runs each function from the dictionary and shows us the results. 

# Sample functions
def greet():
    return "Hello, World!"

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def display_function_results(func_dict):
    for func_name, func in func_dict.items():
        # The items() method in Python is used with dictionaries to return a view object that displays a list of a dictionary’s key-value tuple pairs. This is particularly useful when you want to iterate over both the keys and values in a dictionary.
        if func_name in ['add', 'multiply']:
            result = func(5, 3)  # Call with sample arguments
        else:
            result = func()  # Call without arguments
        print(f"{func_name}: {result}")

# Dictionary with function names and their corresponding function objects
functions_dict = {
    'greet': greet,
    'add': add,
    'multiply': multiply
}

# Display results
display_function_results(functions_dict)
