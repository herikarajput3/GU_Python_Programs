# Asking the user to input a length in centimeters
length_cm = float(input("Enter the length in centimeters: "))

# Check if the length is negative
if length_cm < 0:
    print("Invalid input! Length cannot be negative.")
else:
    # Convert the length to inches (1 inch = 2.54 cm)
    length_inch = length_cm / 2.54
    print(f"{length_cm} cm is equal to {length_inch:.2f} inches.")
