import sqlite3

conn = sqlite3.connect("Zoo.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Animal (
                id INTEGER PRIMARY KEY,
                name TEXT
                )''')

conn.commit()
conn.close()
