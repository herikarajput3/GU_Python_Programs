import mysql.connector

# Connect to MySQL server and the Sample_DB database
try:
    # Establish connection
    conn = mysql.connector.connect(
        host="localhost",
        user="Herika",
        password="Herika1234",  # Replace with your root password
        database="Sample_DB"
    )
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Step 1: Create the employee table (if it doesn't exist)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            eid INT PRIMARY KEY,
            name VARCHAR(100),
            sal DECIMAL(10, 2)
        )
    """)
    print("Employee table created or already exists.")
    
    # Step 2: Insert sample records into the table
    sample_data = [
        (1, "Alice", 50000.00),
        (2, "Bob", 60000.00),
        (3, "Charlie", 70000.00)
    ]
    
    cursor.executemany("""
        INSERT IGNORE INTO employee (eid, name, sal) 
        VALUES (%s, %s, %s)
    """, sample_data)
    conn.commit()
    print("Sample records inserted (if not already present).")
    
    # Step 3: Retrieve and display all rows from the employee table
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    
    print("\nEmployee Table Data:")
    print("EID\tName\t\tSalary")
    print("-" * 30)
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")
