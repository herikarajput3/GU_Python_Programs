# Write a program to demonstrate the use of Positional argument, keyword argument and default arguments.

# Function demonstrating positional, keyword, and default arguments
def student_info(name, age, course="Computer Science", grade="A"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Grade: {grade}")
    print()  

# Positional arguments: arguments are passed in the exact order defined in the function
print("Using Positional Arguments:")
student_info("Herika", 20,"Bca","A+")

# Keyword arguments: arguments are passed using the parameter names
print("Using Keyword Arguments:")
student_info(name="Bob", age=22, course="Mathematics", grade="B")

# Default arguments: if values are not provided, default values are used
print("Using Default Arguments:")
student_info(name="Charlie", age=18)  # No course or grade provided, so defaults will be used




