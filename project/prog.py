import sqlite3 as sql3
import tkinter as tk
import os

''''
Проблемы:
1) кнопки по какой то причине прожимаются автоматически после запуска программы





'''


#I СОЗДАНИЕ БД


db_file = "user_data.db"

#блок проверки бд
if not os.path.exists(db_file):
    database = sql3.connect(db_file)

    cursor = database.cursor()

    cursor.execute("""
    CREATE TABLE usersdata (
        password text


    )""")

    database.commit()

else:
    database = sql3.connect(db_file)

    cursor = database.cursor()

    database.commit()


#II ФУНКЦИИ

#функция сохранения
def save():

    sql_zapros = "INSERT INTO usersdata (password) VALUES(?)"

    take_text = text.get()

    cursor.execute(sql_zapros, (take_text, ))
    print("work")

    database.commit()

#функция просмотра
def look_database():

    root_look = tk.Tk()
    root_look.geometry("300x300")

    key = "SELECT * FROM usersdata"

    cursor.execute(key)

    data = cursor.fetchall()

    data_from_db = tk.Entry(root_look)

    data_from_db.insert(0, str(data))

    data_from_db.pack(padx= 150, pady= 150)

    database.commit()
    database.close()


    root_look.mainloop()


#III ОКНО
root = tk.Tk()

root.title("Регистрация")
root.geometry("600x600")
text = tk.Entry(root)
text.pack(padx = 150, pady = 150)
but_to_save = tk.Button(root, text= "сохранить в бд", width= 15, height=3, command=save())
but_to_save.pack(padx = 3, pady= 3)


but_to_look = tk.Button(root, text = "просмотреть бд", width= 15, height= 3, command=look_database())
but_to_look.pack(padx = 80, pady = 80)


root.mainloop()

