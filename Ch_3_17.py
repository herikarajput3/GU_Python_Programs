# Write a program to show method overloading to find sum of two or three numbers.

class Calculator:
    def sum(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

calc = Calculator()
print(calc.sum(10, 20))  
print(calc.sum(10, 20, 30))  