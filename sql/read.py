import sqlite3

conn = sqlite3.connect("Zoo.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM Animal")
animals = cursor.fetchall()

print("Animals in the Zoo:")
for animal in animals:
    print(animal[1])

conn.close()
