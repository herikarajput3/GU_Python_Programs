import mysql.connector

# Connect to MySQL server and the Sample_DB database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="Herika",
        password="Herika1234",  # Replace with your MySQL root password
        database="Sample_DB"
    )
    
    cursor = conn.cursor()

    # SQL query to create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS new_employee_tbl (
        eno INT PRIMARY KEY,
        ename CHAR(30),
        gender CHAR(1),
        salary FLOAT
    )
    """

    # Execute the query
    cursor.execute(create_table_query)
    print("Table 'new_employee_tbl' created successfully (or already exists).")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")
