# Write a program to store data into instances using mutator methods and to retrieve data from the instances using accessor methods.

class Student:
    # def __init__(self, name="", age=0):
    #     self._name = name 
    #     self._age = age

    # Mutator method for name
    def set_name(self, name):
        self._name = name

    # Mutator method for age
    def set_age(self, age):
        self._age = age

    # Accessor method for name
    def get_name(self):
        return self._name

    # Accessor method for age
    def get_age(self):
        return self._age

# Creating an instance of Student
student1 = Student()

# Using mutator methods to set data
student1.set_name("Alice")
student1.set_age(20)

# Using accessor methods to retrieve and print data
print(f"Student Name: {student1.get_name()}")
print(f"Student Age: {student1.get_age()}")

# Creating another instance of Student
# student2 = Student("Bob", 22)
student2 = Student()

# Using mutator methods to change data
student2.set_name("Charlie")
student2.set_age(23)

# Using accessor methods to retrieve and print data
print(f"\nStudent Name: {student2.get_name()}")
print(f"Student Age: {student2.get_age()}")
