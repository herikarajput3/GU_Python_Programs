# Write a program to access the base class constructor from a sub class by using super() method and also without using super() method.

class baseclass:
    def __init__(self):
        print(f"BaseClass constructor")
class subclass(baseclass):
    def __init__(self):
        super().__init__()
        print("SubClass constructor called using super().")
class subclassWithoutSuper(baseclass):
    def __init__(self):
        baseclass.__init__(self)
        print("SubClass constructor called without using super().")
        
# b = baseclass()
s = subclass()
sw = subclassWithoutSuper()
        
