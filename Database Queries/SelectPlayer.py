import sqlite3 as sql

# connect to the database
conn = sql.connect('C:\Projects\Elliotte\Model\Database\model.db')
cursor = conn.cursor()

# get player to select
player_name = input("Player Name: ")
first_name = player_name.split()[0]
last_name = player_name.split()[1]

# create query
query = "SELECT * FROM players WHERE last_name='"+last_name+"' and first_name='"+first_name+"';"

# display query
print(query)

# execute query
cursor.execute(query)

# display results
print(cursor.fetchall())

# close connection
cursor.close()
conn.close()


