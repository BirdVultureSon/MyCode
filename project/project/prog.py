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
        login TEXT,
        password TEXT,
        email TEXT,
        number INT

    )""")

    database.commit()

else:
    database = sql3.connect(db_file)

    cursor = database.cursor()

    database.commit()


# II ФУНКЦИИ

# функция сохранения
def save():

    sql_zapros = "INSERT INTO usersdata (login, password, email, number) VALUES(?,?,?,?)"

    take_login = login.get()

    take_pass = passwords.get()

    take_email = email.get()

    take_num = phone_number.get()

    cursor.execute(sql_zapros, (take_login, take_pass, take_email, take_num, ))
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
login.place(x = 238, y = 55)

passwords = tk.Entry(root)
passwords.pack(pady=10)


email = tk.Entry(root)
email.place(x = 238, y = 100)


phone_number = tk.Entry(root)
phone_number.place(x = 238, y = 150)


but_to_save = tk.Button(root, text= "Зарегистрироваться", width= 20, height=3, command=save)
but_to_save.place(x = 229, y = 200)



login_label = tk.Label(root, text= "Логин:", width = 5, height = 2)
login_label.place(x= 185, y = 2)

password_label = tk.Label(root, text= "Пароль:", width= 6, height = 2)
password_label.place(x= 185, y = 40)


email_label = tk.Label(root, text = "Э.Почта: ", width = 7, height = 2)
email_label.place(x = 180, y = 90)

phone_number_label = tk.Label(root, text = "Номер телефона: ", width= 14, height= 2)
phone_number_label.place(x = 130, y = 140)

dop_label = tk.Label(root, text = "(Без +)", width= 5, height= 2)
dop_label.place(x = 380, y = 141)

root.mainloop()
