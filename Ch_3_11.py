# Write a program to override super class constructor and method in sub class. 

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Bark"

# Create an instance of the subclass
dog = Dog("Buddy", "Golden Retriever")

# Access the overridden methods
print(f"Name: {dog.name}")  
print(f"Breed: {dog.breed}")  
print(f"Sound: {dog.make_sound()}")  

