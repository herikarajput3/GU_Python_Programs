# Write a program to create a Emp class and make all the members of the Emp class available to another class (Myclass). [By passing members of one class to another] 

class Emp:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

class MyClass:
    def __init__(self, emp):
        """Constructor to accept an Emp object and make its members available."""
        self.emp_name = emp.name
        self.emp_age = emp.age
        self.emp_position = emp.position

    def display_emp_details(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Age: {self.emp_age}")
        print(f"Employee Position: {self.emp_position}")

# Create an instance of Emp
employee = Emp("John Doe", 30, "Software Engineer")

# Pass the Emp instance to MyClass
my_class_instance = MyClass(employee)

# Display the employee details using MyClass
my_class_instance.display_emp_details()
