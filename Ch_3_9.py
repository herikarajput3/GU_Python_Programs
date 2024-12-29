# Create a Student class to with the methods set_id, get_id, set_name, get_name, set_marks and get_marks where the method name starting with set are used to assign the values and method name starting with get are returning the values. Save the program by student.py. Create another program to use the Student class which is already available in student.py.

from student import Student  # Importing the Student class from student.py

def main():
    student = Student()

    # Set student details
    student.set_id(1)
    student.set_name("Alice")
    student.set_marks(88.5)

    # Get and display student details
    print("Student ID:", student.get_id())
    print("Student Name:", student.get_name())
    print("Student Marks:", student.get_marks())

main()

