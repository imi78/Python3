import pandas as pd
import sqlite3

conn = sqlite3.connect('/home/ivo/Python3/SQL/db.sqlite')
curr = conn.cursor()
curr.execute('SELECT player_name, height FROM Player')
res = curr.fetchall()

df = pd.DataFrame(res, columns=['Player name',  'Height'])
print(df)


