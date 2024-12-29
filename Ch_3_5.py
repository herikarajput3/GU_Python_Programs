# Write a program to use class method to handle the common features of all the instance of Student class.

class Student:
    student_count = 0

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        Student.student_count += 1  

    @classmethod
    def get_student_count(cls):
        """Class method to get the total number of students"""
        return cls.student_count

    def display_info(self):
        """Instance method to display student information"""
        print(f"Name: {self.name}, Age: {self.age}")

# Creating instances of Student
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Displaying information for each student
student1.display_info()
student2.display_info()

# Using class method to get the total number of students
print(f"Total number of students: {Student.get_student_count()}") #mistake
