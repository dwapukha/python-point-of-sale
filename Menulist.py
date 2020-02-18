from tkinter import *
import sqlite3
from tkinter import messagebox

menulist = Tk()
menulist.title("List of Menu Items")
menulist.configure(bg='lightgreen')

def showlist():
    conn=sqlite3.connect('POS.db')
    c= conn.cursor()
    c.execute("SELECT *, oid FROM menuitems")
    records= c.fetchall()

    print_records= ''
    for record in records:
        print_records += str(record) + "\n"
    labelitem= Label(menulist, text= print_records).grid()
    #print(records)

    conn.commit()
    conn.close()
btnquery= Button(menulist, text="Click to Show list", command=showlist)
btnquery.grid(row=1, column=1)









menulist.mainloop()