import mysql.connector

def create_database():
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="Herika",  # Replace with your MySQL username
            password="Herika1234"  # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Connection to MySQL server established successfully.")
            cursor = connection.cursor()

            # Check if the database already exists
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()

            if any(db[0] == "Sample_DB" for db in databases):
                print("Database 'Sample_DB' already exists.")
            else:
                # Create the database
                cursor.execute("CREATE DATABASE Sample_DB")
                print("Database 'Sample_DB' created successfully.")
            
            # Close the cursor
            cursor.close()
        else:
            print("Failed to connect to MySQL server.")
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

# Call the function
create_database()
