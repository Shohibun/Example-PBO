import sqlite3

con = sqlite3.connect("Ini Diisi database nanti")
data = con.execute("SELECT * FROM Employee")

for item in data:
    print(item)