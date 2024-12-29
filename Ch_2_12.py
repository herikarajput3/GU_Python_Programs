# Create a decorator function to increase the value of a function by 3.
def add_three(func):  # func is a function passed to add_three
    def wrapper():
        result = func()  # Call the passed function and store its result
        return result + 3  # Add 3 to the result
    return wrapper  # Return the wrapper function

@add_three  # This passes get_number to add_three
def get_number():  # get_number is the function being decorated
    return 5  # It simply returns 5

print("Result:", get_number())  # Calls the decorated get_number


'''
The program starts with the print statement:

print("Result:", get_number())
The print statement tries to output the result of calling the get_number() function.

Decorator (@add_three) is applied to get_number: When the @add_three decorator is used, it means that get_number is passed to the add_three function. This happens when the function is defined, not when it is called. So, the add_three function receives get_number as its argument (func).

The add_three function returns the wrapper function.
Now, instead of calling get_number directly, what actually gets called is the wrapper function created inside the add_three function.
get_number() is replaced with wrapper(): When you call get_number(), it now executes the wrapper function that was returned by add_three. So the next step is calling wrapper.

Inside the wrapper function: The wrapper function executes the following steps:

result = func()  # Calls the original get_number function
return result + 3  # Adds 3 to the result and returns it

func() refers to the original get_number function, which returns 5.
The result of func() is 5, and then 3 is added to it.
wrapper() returns 8.
Back to the print statement: The value returned by get_number() (which is now 8 because of the decorator) is passed to the print statement, resulting in:
'''