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

    # Function to delete a row based on employee ID (eid)
    def delete_employee():
        eid = input("Enter the Employee ID (eid) to delete: ")
        
        try:
            eid = int(eid)  # Ensure eid is an integer
            
            # Check if the employee exists
            cursor.execute("SELECT * FROM employee WHERE eid = %s", (eid,))
            result = cursor.fetchone()
            
            if result:
                # Delete the employee record
                cursor.execute("DELETE FROM employee WHERE eid = %s", (eid,))
                conn.commit()
                print(f"Employee with ID {eid} deleted successfully.")
            else:
                print(f"No employee found with ID {eid}.")
        
        except ValueError:
            print("Invalid input. Employee ID must be an integer.")
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
    
    # Call the function to delete an employee
    delete_employee()

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")
