import sys

def sum_of_even_numbers(args):
    # Initialize the sum of even numbers to 0
    total_sum = 0
    
    # Loop through the arguments (starting from index 1 to skip the script name)
    for arg in args[1:]:
            # Convert argument to integer
            num = int(arg)
            # Check if the number is even
            if num % 2 == 0:
                total_sum += num    
    return total_sum

# Get the command-line arguments
args = sys.argv

# Call the function and display the result
result = sum_of_even_numbers(args)
print("Sum of even numbers:", result)
