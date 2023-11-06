import sqlite3 as sql

# connect(filePathToDatabase)
conn = sql.connect("filmflix.db")

cursor = conn.cursor()


