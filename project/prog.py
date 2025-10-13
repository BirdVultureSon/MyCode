import sqlite3 as sql3
import tkinter as tk
import os

#блок создания базы данных

db_file = "user_data.db"

if not os.path.exists(db_file):
    database = sql3.connect(db_file)

    cursor = database.cursor()

    cursor.execute("""
    CREATE TABLE usersdata (
        password text


    )""")


else:
    database = sql3.connect(db_file)



database.commit()

database.close()



#блок программы
root = tk.Tk()

root.title("Регистрация")
root.geometry("600x600")
text = tk.Entry(root)
text.pack(padx = 150, pady = 150)
but_to_save = tk.Button(root, text= "сохранить в бд", width= 15, height=3)
but_to_save.pack(padx = 100, pady= 100)

but_to_get = tk.Button(root, text = "войти в бд", width= 15, height= 3)
but_to_get.pack(padx = 80 , pady= 80)

def save():
    data = text.get
    sql_work = "INSERT INTO userdata (password) VALUES(?,?)"
    cursor.execute(sql_work, (data))

    database.commit()
    database.close()

    root.destroy()

root.mainloop()