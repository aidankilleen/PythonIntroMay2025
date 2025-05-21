# tk_investigation.py

import sqlite3
import tkinter as tk
from tkinter import messagebox

DATABASE_FILE_NAME = r"C:\work\training\python\testdb.db"

conn = sqlite3.connect(DATABASE_FILE_NAME)

def on_exit():
    conn.close()
    root.destroy()

def get_records():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(tk.END, row[1])

def on_save_click():
    name = txt_name.get()
    email = txt_email.get()
    cursor = conn.cursor()
    sql = "INSERT INTO members (name, email, active) VALUES(?,?,?)"
    cursor.execute(sql, (name, email, 1))
    conn.commit()
    listbox.insert(tk.END, name)

root = tk.Tk()
root.title("TKInter Hello World")
root.geometry("600x400")
root.protocol("WM_DELETE_WINDOW", on_exit)

def on_button_click():
    messagebox.showinfo("Information", "You clicked the button")
    print ("You pressed the button")

button = tk.Button(root, text="Press Me", command=on_button_click)
#button.pack()
button.place(x=10, y=10)

listbox = tk.Listbox(root, height=10)
listbox.place(x=10, y=40)
get_records()

lbl_name = tk.Label(root, text="Name")
lbl_name.place(x=10, y=230)
txt_name = tk.Entry(root)
txt_name.place(x=10, y=250)

lbl_email = tk.Label(root, text="Email")
lbl_email.place(x=10, y=270)
txt_email = tk.Entry(root)
txt_email.place(x=10, y=290)

btn_save = tk.Button(root, text="Save", command=on_save_click)
btn_save.place(x=10, y=320)

root.mainloop()