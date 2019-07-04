import sqlite3
connection = sqlite3.connect('collection.rb')

cursor = connection.cursor()

cursor.execute("SELECT * FROM record")
print("fetchall:")
result = cursor.fetchall()
for r in result:
        print(r)
cursor.execute("SELECT * FROM record")
print("\nfetchone:")
res = cursor.fetchone()
print(res)
