import pyodbc
import pandas as pd

# Set up the connection to the SQL Server database
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
connection = pyodbc.connect(connection_string)

# SQL query to retrieve data from a specific table
query = "SELECT * FROM your_table_name"

# Fetch data from the database and store it in a Pandas DataFrame
dataframe = pd.read_sql(query, connection)

# Close the database connection
connection.close()

# Print the first few rows of the DataFrame
print(dataframe.head())
