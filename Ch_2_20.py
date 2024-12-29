# Write a program to create a dictionary from the user and display the elements.

def create_dictionary():
    user_dict = {}   # Initialize an empty dictionary

    # Loop to get key-value pairs from the user
    while True:
        key = input("Enter a key (or type 'exit' to finish): ")
        if key.lower() == 'exit': #The lower() part makes sure it doesn't matter if the user types 'exit', 'Exit', or 'EXIT'; it will still recognize it as 'exit'.
            break  # Exit the loop if the user types 'exit'
        value = input(f"Enter a value for {key}: ") 
        user_dict[key] = value  # Add key-value pair to the dictionary

    return user_dict

created_dict = create_dictionary()  # Create the dictionary

print("\nCreated Dictionary:")
for key, value in created_dict.items(): #mistake create_dictionary() instead of created_dict
    print(f"{key}: {value}")

