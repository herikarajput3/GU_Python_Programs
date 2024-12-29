# Define two variables
a = 10
b = 10

# Display the memory locations of both variables using id()
print("Memory location of a:", id(a))
print("Memory location of b:", id(b))

# Compare if both variables point to the same object using identity operators
if a is b:
    print("a and b refer to the same memory location (same object).")
else:
    print("a and b do not refer to the same memory location (different objects).")

# Now, let's try with variables that are definitely different objects
x = [1, 2, 3]
y = [1, 2, 3]

# Display the memory locations of x and y
print("\nMemory location of x:", id(x))
print("Memory location of y:", id(y))

# Compare if both variables point to the same object using identity operators
if x is y:
    print("x and y refer to the same memory location (same object).")
else:
    print("x and y do not refer to the same memory location (different objects).")
