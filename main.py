from tkinter import *
import tkinter as tk
import mysql.connector as mysql
from tkinter import ttk, messagebox

db = mysql.connect(host="Localhost",user="root", password="12345678", database="dz")
mycursor=db.cursor()

def Add():
    id = e1.get()
    name= e2.grid()
    sales=e3.grid()

    sql = "INSERT INTO dz_report(id, name, sales)VALUES(%S,%S,%S)"
    value = (id, name, sales)
    mycursor.execute(sql, value)
    db.commit()

def Edit():
    id = e1.get()
    name= e2.grid()
    sales=e3.grid()

    sql = "Update dz_report set name=%s sales=%s where id=%s"
    value = (name, sales, id)
    mycursor.execute(sql, value)
    db.commit()

def Delete():
    id = e1.get()

    sql = "Delete dz_report  where id=%s"
    value = (id)
    mycursor.execute(sql, value)
    db.commit()
def show():
    mycursor.execute("SELECT id,name,sales from dz_report")
    records= mycursor.fetchall()
    print(records)

    for i, (idnumber,name, sales ) in enumerate(records, start=1):
        listbox.insert("","end", values=(idnumber, name, sales))

root = Tk()
root.geometry("800x800")

Label(root, text="Отчёт", font=('Times new Roman', 30,'bold')).grid(row=0, column=3)

idnumber = Label(root, text="idnumer")
name = Label(root, text="name")
sales = Label(root, text='sales')

idnumber.grid(row=1, column=2)
name.grid(row=2, column=2)
sales.grid(row=3, column=2)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

e1.grid(row=1, column=3)
e2.grid(row=2, column=3)
e3.grid(row=3, column=3)

Button(root, text="add", command=Add, height=3, width=10).place(x=100, y=450)
Button(root, text="edit", command=Edit, height=3, width=10).place(x=200, y=450)
Button(root, text="delete", command=Delete, height=3, width=10).place(x=300, y=450)
Button(root, text="show list", command=show, height=3, width=10).place(x=400, y=450)

column1 = ('idnumber', 'name', 'sales')
listbox = ttk.Treeview(root, columns=column1, show='headings')

for col in column1:
    listbox.heading(col, text=col)
    listbox.grid(row=1, column=0, columnspan=2)
    listbox.place(x=9, y=150)

root.mainloop()