import sqlite3
import requests
from flask import Flask

app = Flask(__name__)

# Connect to an in-memory database
connection = sqlite3.connect(':memory:', check_same_thread=False)
cursor = connection.cursor()

# Create a table to store API data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_lugar (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        endereco TEXT,
        horarioAbre TEXT,
        horarioFecha TEXT
    )
''')

cursor.execute('INSERT INTO tb_lugar (nome, endereco, horarioAbre, horarioFecha) \
               VALUES (?, ?, ?, ?)', [('biblioteca'), ('endereco'), ('08:00'), ('22:00')])
connection.commit()

# Query the stored data
cursor.execute('SELECT * FROM tb_lugar')
rows = cursor.fetchall()

# Print the results
print("\nData in the in-memory database:")
for row in rows:
    print(row)


@app.route("/")
def hello_world():

    cursor.execute('SELECT * FROM tb_lugar')
    rows = cursor.fetchall()

    return rows



# Close the connection
# connection.close()