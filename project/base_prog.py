import sqlite3 as sql3
import tkinter as tk
from database_ import database
from database_ import cursor

root = tk.Tk()

root.title("Регистрация")
root.geometry("600x600")
text = tk.Entry(root)
text.pack(padx = 150, pady = 150)
but = tk.Button(root, text= "сохранить в бд", width= 15, height=3)
but.pack(padx = 100, pady= 100)

def save():
    database = sql3.connect()
    user_password = text.get()
    cursor.execute("""
INSERT INTO user_data VALUES ({user_password})


""")
    database.commit()
    database.close()

root.mainloop()