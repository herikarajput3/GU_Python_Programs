# Write a program to create a static method that counts the number of instances created for a class.

class Student:
    student_count = 0

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        Student.student_count += 1  # Increment the student count when a new instance is created

    @staticmethod
    def get_student_count():
        """Static method to get the total number of students"""
        return Student.student_count

    def display_info(self):
        """Instance method to display student information"""
        print(f"Name: {self.name}, Age: {self.age}")

# Creating instances of Student
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 19)

# Displaying information for each student
student1.display_info()
student2.display_info()
student3.display_info()

# Using static method to get the total number of students
print(f"Total number of students: {Student.get_student_count()}")
