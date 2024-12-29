# Write a program to implement single inheritance in which two sub classes are derived from a single base class.

class BaseClass:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name from BaseClass: {self.name}")

class SubClass1(BaseClass):
    def __init__(self, name, age):
        super().__init__(name)  # Call the base class constructor
        self.age = age

    def show_info(self):
        self.show_name()  # Call method from BaseClass
        print(f"Age from SubClass1: {self.age}")

class SubClass2(BaseClass):
    def __init__(self, name, city):
        super().__init__(name)  # Call the base class constructor
        self.city = city

    def show_info(self):
        self.show_name()  # Call method from BaseClass
        print(f"City from SubClass2: {self.city}")

sub1 = SubClass1("Alice", 25)
sub2 = SubClass2("Bob", "New York")

# Calling show_info method for both subclasses
sub1.show_info()
print()  
sub2.show_info()
