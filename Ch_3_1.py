# Write a program to create a Student class with name, age and marks as data members. Also create a method named display() to view the student details. Create an object to Student class and call the method using the object.

class Student:
    def __init__(self, name, age, marks):
        self.name = name   # Assign the name
        self.age = age     # Assign the age
        self.marks = marks # Assign the marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

# Creating an object of the Student class
student1 = Student("Alice", 20, 85)

# Calling the display method using the object
student1.display()


