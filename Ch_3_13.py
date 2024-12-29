# Write a program to implement multiple inheritance using two base classes.

class BaseClass1:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name from BaseClass1: {self.name}")

class BaseClass2:
    def __init__(self, age):
        self.age = age

    def show_age(self):
        print(f"Age from BaseClass2: {self.age}")

class DerivedClass(BaseClass1, BaseClass2):
    def __init__(self, name, age, city):
        BaseClass1.__init__(self, name)  
        BaseClass2.__init__(self, age)   
        self.city = city

    def show_info(self):
        self.show_name()  
        self.show_age()   
        print(f"City from DerivedClass: {self.city}")

derived = DerivedClass("Alice", 25, "New York")
derived.show_info()
