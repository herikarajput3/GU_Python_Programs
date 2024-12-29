# Write a program to understand the order of execution of methods in several base classes according to method resolution order (MRO).

class A:
    def method(self):
        print("Method from Class A")

class B(A):
    def method(self):
        print("Method from Class B")
        super().method()  # Calls method from Class A

class C(A):
    def method(self):
        print("Method from Class C")
        super().method()  # Calls method from Class A

class D(B, C):
    def method(self):
        print("Method from Class D")
        super().method()  # Calls method from Class B

d = D()
d.method()

print("\nMethod Resolution Order (MRO):")
print(D.__mro__) #tuple
print()
print(D.mro()) #list
