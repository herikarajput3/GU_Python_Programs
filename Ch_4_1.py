# Python program to handle ZeroDivisionError

# Function to divide two numbers
def divide_numbers(a, b):
    try:
        # Attempt to perform division
        result = a / b
        print(f"The result of division is: {result}")
    except ZeroDivisionError:
        # Handle the ZeroDivisionError
        print("Error: Division by zero is not allowed!")

# Input from the user
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

# Call the function
divide_numbers(num1, num2)
