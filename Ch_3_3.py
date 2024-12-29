# Write a program to demonstrate the use of instance and class/static variables.

class Student:
    # Class variable
    school_name = "ABC High School" 

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {Student.school_name}")  # Accessing class variable

# Creating instances of the Student class
student1 = Student("Alice", 16)
student2 = Student("Bob", 17)

# Displaying information for each student
student1.display_info()
print() 
student2.display_info()

# Changing the class variable
Student.school_name = "XYZ Academy"

print("\nAfter changing the school name:")
student1.display_info()
print()  
student2.display_info()
