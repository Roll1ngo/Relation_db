import sqlite3

with open('select_1.sql', 'r') as sql_file:
    sql_script = sql_file.read()


db = sqlite3.connect('hw_db.sqlite')
cursor = db.cursor()
cursor.executescript(sql_script)
print(cursor.fetchall())
db.commit()
db.close()