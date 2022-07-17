import pandas as pd
import sqlite3

# first connect to SQL DB
conn = sqlite3.connect('/home/ivo/Python3/SQL/db.sqlite')

# Now make a dataframe with selected SQL command and pass the connection as a second parameter of 'sql_read' function
df = pd.read_sql('SELECT player_name, birthday FROM Player', conn)

if __name__ == '__main__':
    print(df)

