# Write a program to create Student class with a constructor having more than one parameter.

class Student:
    def __init__(self, name, age, marks, course):
        self.name = name      # Assign the name
        self.age = age        # Assign the age
        self.marks = marks    # Assign the marks
        self.course = course  # Assign the course

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Course: {self.course}")

student1 = Student("Bob", 22, 90, "Computer Science")
student1.display()
