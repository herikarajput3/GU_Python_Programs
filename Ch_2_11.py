# Write a lambda/Anonymous function to find bigger number in two given numbers. 

bigger_number = lambda a, b: a if a > b else b  #mistake spelling of lambda

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find and print the bigger number
print("The bigger number is:", bigger_number(num1, num2))

