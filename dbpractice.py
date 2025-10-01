# Databse Practice :)
import sqlite3
# Connection allows us to connect Python to a SQL database :)
connection = sqlite3.connect("./database.db") 
# cursor allows us to interact with SQL DB
cursor = connection.cursor() # always create a cursor from connection
query = """ 
SELECT product_name, price FROM Products;
""" # SQL string
result = cursor.execute(query).fetchall()
print(f"OUR SQL RESULT: {result}")

# BOTTOM/END OF OUT CODE
connection.commit() # this commits our changes
connection.close() # this disconnects our connection