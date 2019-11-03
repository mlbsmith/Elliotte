import sqlite3 as sql

conn = sql.connect('C:\Projects\Elliotte\Model\Database\model.db')

cursor = conn.cursor()

cursor.execute('ALTER TABLE players RENAME COLUMN "Last Name" TO last_name;')
cursor.execute('ALTER TABLE players RENAME COLUMN "First Name" TO first_name;')

cursor.close()
conn.close()
