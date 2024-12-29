def handle_exceptions():
    try:
        # Simulating a TypeError: Attempting an invalid operation
        print("Attempting a TypeError operation...")
        "string" + 5  # This will raise TypeError
    except TypeError as te:
        # Handle TypeError
        print(f"TypeError caught: {te}")
    print()

    try:
        # Simulating SyntaxError: Using eval with invalid syntax
        print("Simulating a SyntaxError operation...")
        eval("x === 5")  # Triple equals is invalid syntax in Python
    except SyntaxError as se:
        # Handle SyntaxError
        print(f"SyntaxError caught: {se}")

# Call the function to demonstrate exception handling
handle_exceptions()
