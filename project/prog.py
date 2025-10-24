import sqlite3 as sql3
import tkinter as tk
import os

#I СОЗДАНИЕ БД
db_file = "user_data.db"

# блок проверки бд
if not os.path.exists(db_file):
    database = sql3.connect(db_file)

    cursor = database.cursor()

    cursor.execute("""
    CREATE TABLE usersdata (
        login text,
        password text


    )""")

    database.commit()

else:
    database = sql3.connect(db_file)

    cursor = database.cursor()

    database.commit()


# II ФУНКЦИИ

# функция сохранения
def save():

    sql_zapros = "INSERT INTO usersdata (login, password) VALUES(?,?)"

    take_login = login.get()

    take_pass = passwords.get()

    cursor.execute(sql_zapros, (take_login, take_pass))
    print("work")

    database.commit()


# функция просмотра БД
def look_database():

    root_look = tk.Tk()
    root_look.geometry("300x300")
    
    but_to_close = tk.Button(root_look, text= "Закрыть окно", width=15, height=3, command=lambda close_root: root_look.destroy())
    but_to_close.pack(pady=10)
    
    key = "SELECT * FROM usersdata"

    cursor.execute(key)

    data = cursor.fetchall()

    data_from_db = tk.Entry(root_look)

    data_from_db.insert(0, str(data))

    data_from_db.pack(pady=10)

    database.commit()
    database.close()


    root_look.mainloop()


# III ОКНО
# главное окно
root = tk.Tk()

root.title("Регистрация")
root.geometry("600x600")

login = tk.Entry(root)
login.pack(pady=10)

passwords = tk.Entry(root)
passwords.pack(pady=10)


but_to_save = tk.Button(root, text= "сохранить в бд", width= 15, height=3, command=save)
but_to_save.pack(pady=10)


but_to_look = tk.Button(root, text = "просмотреть бд", width= 15, height= 3, command=look_database)
but_to_look.pack(pady=10)


login_label = tk.Label(root, text= "Логин:", width= 5, height=2)
login_label.place(x= 185, y = 2)

password_label = tk.Label(root, text= "Пароль:", width= 6, height=2)
password_label.place(x= 185, y = 40)

root.mainloop()


