import sqlite3

# Connect to the DB
conn = sqlite3.connect('/home/ivo/Python3/SQL/db.sqlite')

# Cursor
curr = conn.cursor()

#List with SQL queries to be executed. Just add input to the list
commands = [
"SELECT * FROM Player",
"SELECT id, player_name as name, birthday, height, weight FROM Player WHERE height>150",
"INSERT INTO Country(id, Name) VALUES (2, 'Bulgaria')",
"SELECT name,id FROM Country ORDER BY id",
"SELECT ROUND(AVG (height), 3) AS 'Rounded' FROM Player",
"SELECT ROUND(AVG(weight), 3) FROM Player"
]

# Execute the commands one by one
for command in commands:
    curr.execute(command)
    res = curr.fetchall() # Fetch all entries
    for i in res[:10]: # Only first ten will be printed
        print(i)
    
    # adds space between results for readability
    print() 

