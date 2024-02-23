import sqlite3

conn = sqlite3.connect("Zoo.db")

cursor = conn.cursor()

animals = [("Lion",), ("Elephant",), ("Giraffe",)]
cursor.executemany("INSERT INTO Animal (name) VALUES (?)", animals)

conn.commit()
conn.close()
