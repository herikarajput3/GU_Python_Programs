# Write a program to check the object type to know whether the method exists in the object or not. 

class Bird:
    def sing(self):
        print("Tweet! Tweet!")

class Fish:
    def swim(self):
        print("Swim, Swim!")

# Function to check if an object has a specific method
def check_method(obj, method_name):
    if hasattr(obj, method_name): #hasattr() is a built-in Python function that returns True if the object has the method, and False if it doesn't.
        print(f"The object of type '{type(obj).__name__}' has the method '{method_name}'.") #type(obj).__name__ gets the name of the object's class (like Bird or Fish).
    else:
        print(f"The object of type '{type(obj).__name__}' does NOT have the method '{method_name}'.")

bird = Bird()
fish = Fish()
check_method(bird, 'sing')  
check_method(bird, 'swim')   
check_method(fish, 'swim')   
check_method(fish, 'sing')    


