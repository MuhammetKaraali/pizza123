import sqlite3
dbase = sqlite3.connect('pizzares.db')
dbase.execute(''' CREATE TABLE signbc_user(
USER_NAME TEXT NOT NULL,
PASSWORD INT NOT NULL,
EMAIL TEXT NOT NULL)''')
dbase.commit()
dbase.close()