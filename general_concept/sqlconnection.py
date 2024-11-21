import mysql.connector

# Replace these with your actual database credentials
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'your_databas'
}

# Establish the connection
cnx = mysql.connector.connect(**config)

# Create a cursor object
cursor = cnx.cursor()

# Sample query to show databases
cursor.execute("SHOW DATABASES")

# Fetch and print all databases
for (database,) in cursor:
    print(database)

# Close the cursor and connection
cursor.close