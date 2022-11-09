create table
import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS mahasiswa")

query = "CREATE TABLE mahasiswa(id INTEGER PRIMARY KEY NOT NULL,nama TEXT NOT NULL)"

cursor.execute(query)

conn.commit()
conn.close()

#insert 
import sqlite3
conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

query = "INSERT INTO mahasiswa(nama) VALUES('john lennon')"

cursor.execute(query)

conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

query = "INSERT INTO mahasiswa(id,nama) VALUES(?,?)"

data = [
    ('',"abc"),
    ('',"abcde"),
]
cursor.executemany(query,data)

conn.commit()
conn.close() 

#read
import sqlite3
conn = sqlite3.connect('mydatabase.db')

query = "SELECT nama FROM mahasiswa"
cursor = conn.execute(query)

data = cursor.fetchall()


for item in data:
    print(item)

conn.close() 

#update
 import sqlite3
conn = sqlite3.connect('mydatabase.db')

query = "UPDATE mahasiswa SET nama='jhonson mobil' WHERE id=1"

conn.execute(query)

cursor = conn.execute("SELECT nama FROM mahasiswa")

data = cursor.fetchall()

print(data)

conn.commit()
conn.close() 

#delete
 import sqlite3
conn = sqlite3.connect('mydatabase.db')

query = "DELETE from mahasiswa WHERE nama = 'jhonson mobil' "
conn.execute(query)
conn.commit()

cursor = conn.execute("SELECT nama FROM mahasiswa")

data = cursor.fetchall()

print(data)

conn.close() 

#count aggregate func
 import sqlite3
conn = sqlite3.connect('mydatabase.db')

query = "SELECT SUM(id) FROM mahasiswa"
cursor = conn.execute(query)

data = cursor.fetchone()

print(data)

conn.close() 

 import sqlite3
conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

query = "INSERT INTO coba(nama) VALUES('kaka')"

cursor.execute(query)

conn.commit()
conn.close() 