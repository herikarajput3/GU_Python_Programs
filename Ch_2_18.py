# Write a program to accept elements in the form of a tuple and display its minimum, maximum, sum and average. 

def tuple_statistics(numbers):
    minimum = min(numbers)  # Finding the minimum value
    maximum = max(numbers)  # Finding the maximum value
    total_sum = sum(numbers)  # Finding the sum of all elements
    average = total_sum / len(numbers)  # Calculating the average

    print(f"Tuple: {numbers}")
    print(f"Minimum value: {minimum}")
    print(f"Maximum value: {maximum}")
    print(f"Sum of values: {total_sum}")
    print(f"Average value: {average}")

# Accepting elements from the user and converting them into a tuple
elements = input("Enter numbers separated by spaces: ").split() #mistake  

numbers_tuple = tuple(map(int, elements))  
# The map() function is used to apply a specific function to each item in an iterable (such as a list, tuple, etc.). It returns a map object, which is an iterator that can be converted into other data types like lists or tuples.

tuple_statistics(numbers_tuple)

