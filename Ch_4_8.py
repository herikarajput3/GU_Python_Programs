import mysql.connector

# Connect to MySQL server and the Sample_DB database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="Herika",
        password="Herika1234",  # Replace with your root password
        database="Sample_DB"
    )
    
    cursor = conn.cursor()

    # Function to insert multiple rows into the employee table
    def insert_employees():
        print("Enter employee details (ID, Name, Salary). Type 'exit' to stop.")
        
        while True:
            # Take input from the user
            user_input = input("Enter Employee (ID Name Salary): ")
            
            # Check if the user wants to exit
            if user_input.lower() == 'exit':
                print("Exiting input mode.")
                break
            
            # Split the input and validate it
            try:
                eid, name, sal = user_input.split()
                eid = int(eid)
                sal = float(sal)
                
                # Insert the record into the employee table
                cursor.execute(
                    "INSERT INTO employee (eid, name, sal) VALUES (%s, %s, %s)",
                    (eid, name, sal)
                )
                conn.commit()
                print(f"Record inserted: {eid}, {name}, {sal}")
            
            except ValueError:
                print("Invalid input. Please enter data in the format: ID Name Salary")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
    
    # Call the function to insert employee data
    insert_employees()

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")
