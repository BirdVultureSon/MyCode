import sqlite3 as sql3
import tkinter as tk
import os

#блок создания базы данных


    



#создание бд




db_file = "user_data.db" #название бд

#проверка бд
if not os.path.exists(db_file):
    database = sql3.connect(db_file)

    cursor = database.cursor()

    cursor.execute("""
    CREATE TABLE usersdata (
        password text


    )""")


else:
    database = sql3.connect(db_file)

    cursor = database.cursor()



database.commit()



def look_database():
    taked_data = cursor.execute("SELECT * FROM usersdata")
    print(taked_data)



def take_data_from_text():
    return text.get()


def save():
    sql_work = "INSERT INTO usersdata (password) VALUES(?)"
    cursor.execute(sql_work, (take_data_from_text()))

    print("work")

    database.commit()
    database.close()

    root.destroy()




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