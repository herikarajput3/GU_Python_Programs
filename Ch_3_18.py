# Write a program to override the super class method in subclass.

class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

generic_animal = Animal()
dog = Dog()

print(generic_animal.make_sound())  
print(dog.make_sound())             
