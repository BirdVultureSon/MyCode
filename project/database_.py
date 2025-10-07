#создание базы данных


import sqlite3 as sql3 

database = sql3.connect("user_data.db")

cursor = database.cursor()

cursor.execute("""
CREATE TABLE usersdata (
    password text


)""")


database.commit()

database.close