import sqlite3
dbase = sqlite3.connect('pizzares.db')
dbase.execute(''' CREATE TABLE pizza_user(
USER_NAME TEXT  NOT NULL,
PIZZA_PRICE INT NOT NULL)''')
dbase.commit()
dbase.close()