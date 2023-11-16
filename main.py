import sqlite3
import requests
from flask import Flask

app = Flask(__name__)

# Connect to an in-memory database
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

# Create a table to store API data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS api_data (
        id INTEGER PRIMARY KEY,
        name TEXT,
        value TEXT
    )
''')

cursor.execute('INSERT INTO api_data (name, value) VALUES (?, ?)', [('name'), ('value')])
connection.commit()

# Query the stored data
cursor.execute('SELECT * FROM api_data')
rows = cursor.fetchall()

# Print the results
print("\nData in the in-memory database:")
for row in rows:
    print(row)

# Close the connection
connection.close()
