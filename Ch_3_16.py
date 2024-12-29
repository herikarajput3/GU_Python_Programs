# Write a program to overload the addition operator (+) to make it act on the class objects.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self): # The __str__ method is overridden to provide a string representation of the Point object, making it easier to print.    
        return f"({self.x}, {self.y})"

# Create instances of the Point class
point1 = Point(1, 2)
point2 = Point(3, 4)

result = point1 + point2
print(result)  
