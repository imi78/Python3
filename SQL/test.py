import sqlite3

conn = sqlite3.connect('/home/ivo/Python/Python3/SQL/db.sqlite')

curr = conn.cursor()

command = "SELECT * FROM Player"

curr.execute(command)

res = curr.fetchall()
for i in res[:10]:
    print(i)