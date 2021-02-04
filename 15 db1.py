#py4e
#Chapter 15 - Using Databases and SQL
#db1

import sqlite3

conn = sqlite3.connect('databases\emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()
