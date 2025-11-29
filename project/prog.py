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
        password text,
        email text,
        phone text


    )""")

    database.commit()

else:
    database = sql3.connect(db_file)

    cursor = database.cursor()

    database.commit()


# II ФУНКЦИИ

# функция сохранения
def save():

    sql_zapros = "INSERT INTO usersdata (login, password, email, phone) VALUES(?,?,?,?)"

    take_login = login.get()

    take_pass = passwords.get()

    take_email = email.get()

    take_phone = phone_number.get()

    cursor.execute(sql_zapros, (take_login, take_pass, take_email, take_phone))
    print("work")

    database.commit()


# III ОКНО
# главное окно
root = tk.Tk()

root.title("Регистрация")
root.geometry("600x600")

login = tk.Entry(root)
login.place(x = 250, y = 10)

passwords = tk.Entry(root)
passwords.place(x = 250, y = 50)


email = tk.Entry(root)
email.place(x = 250, y = 90)

phone_number = tk.Entry(root)
phone_number.place(x = 250, y = 130)


but_to_save = tk.Button(root, text= "Зарегистрироваться", width= 17, height=2, command=save)
but_to_save.place(x = 250, y = 180)



login_label = tk.Label(root, text= "Логин:", width= 5, height=2)
login_label.place(x= 185, y = 2)

password_label = tk.Label(root, text= "Пароль:", width= 6, height=2)
password_label.place(x= 185, y = 40)

email_label = tk.Label(root, text = "Э.Почта:", width= 7, height= 2)
email_label.place(x = 185, y = 80)

phone_number_label = tk.Label(root, text = "Телефон:", width=8, height=2)
phone_number_label.place(x = 185, y = 120)

root.mainloop()