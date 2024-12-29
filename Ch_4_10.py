import mysql.connector
from decimal import Decimal  # Import Decimal for handling MySQL DECIMAL type

# Connect to MySQL server and the Sample_DB database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="Herika",
        password="Herika1234",  # Replace with your MySQL root password
        database="Sample_DB"
    )
    
    cursor = conn.cursor()

    # Function to increase the salary of an employee
    def increase_salary():
        try:
            eid = int(input("Enter the Employee ID (eid) to increase salary: "))
            increment = float(input("Enter the amount to increase salary: "))
            
            # Check if the employee exists
            cursor.execute("SELECT sal FROM employee WHERE eid = %s", (eid,))
            result = cursor.fetchone()
            
            if result:
                current_salary = result[0]  # This will be of type decimal.Decimal
                
                # Convert increment to Decimal to match the current_salary type
                increment = Decimal(increment)
                
                # Calculate the new salary
                new_salary = current_salary + increment
                
                # Update the salary in the table
                cursor.execute(
                    "UPDATE employee SET sal = %s WHERE eid = %s",
                    (new_salary, eid)
                )
                conn.commit()
                print(f"Salary of Employee ID {eid} increased by {increment}. New salary: {new_salary:.2f}")
            else:
                print(f"No employee found with ID {eid}.")
        
        except ValueError:
            print("Invalid input. Employee ID must be an integer and increment must be a number.")
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")

    # Call the function to increase the salary
    increase_salary()

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")
