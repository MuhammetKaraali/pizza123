import sqlite3
dbase = sqlite3.connect('pizzares.db')
dbase.execute(''' CREATE TABLE reserve_user(
RESERVE_USERNAME TEXT  NOT NULL,
TABLE_NO INT NOT NULL,
PERSON_NUMBER INT NOT NULL)''')
dbase.commit()
dbase.close()