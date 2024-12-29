def is_palindrome(s):
    # Remove any spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Input from the user
string = input("Enter a string to check if it is a palindrome: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")
