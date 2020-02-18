from tkinter import *
#from Tkinter import  *
import  random
import time
import datetime
from tkinter import messagebox
import sqlite3

addmenu =Tk()
root.geometry("1280x920+0+0")
addmenu.title("Poa Point of Sale")
addmenu.configure(bg="grey")
addmenu.resizable(True, False)
#------creating database or connecting to database-------
conn=sqlite3.connect('POS.db')
#create cursor------
c= conn.cursor()

#--------create table--------
''' 
c.execute("""CREATE TABLE users(
    userid number
    F_name text,
    L_name text,
    role text
)""") 
'''

def extmenumsg():
    mess2=messagebox.askyesno("About to Exit", "Are you sure you want to exit")
    if mess2== 1:
        addmenu.quit()
    if mess2== 0:
        addmenu.option_clear()

def additem1():
    conn=sqlite3.connect('POS.db')
    c= conn.cursor()

    #-----insert sqlite command-----
    c.execute("INSERT INTO menuitems VALUES(:item_code, :menu_name, :menu_category, :menu_price )",
              {
                  'item_code': item_code.get(),
                  'menu_name': menu_name.get(),
                  'menu_category':menu_category.get(),
                  'menu_price': menu_price.get()
              }
              )

    conn.commit()
    conn.close()
    #-----------CLEAR TEXTBOX-----------
    item_code.delete(0, END)
    menu_name.delete(0, END)
    menu_category.delete(0, END)
    menu_price.delete(0, END)

#--------------creating Labels form the form inputs------------
itemcode= Label(addmenu, text="Menu code: ", font= ('times', 13), width=15)
itemname= Label(addmenu, text="Item Name: ", font= ('times', 13), width=15)
itemcat= Label(addmenu, text="Item Category: ", font= ('times', 13), width=15)
itemprice= Label(addmenu, text="Item price: ", font= ('times', 13), width=15)

itemcode.grid(row=0, column=0)
itemname.grid(row=1, column=0)
itemcat.grid(row=2, column=0)
itemprice.grid(row=3, column=0)
#-------------textbox-------------
item_code = Entry(addmenu, width=25)
menu_name= Entry(addmenu, width=25)
menu_category=Entry(addmenu, width=25)
menu_price=Entry(addmenu, width=25)

item_code.grid(row=0, column=2)
menu_name.grid(row=1, column=2)
menu_category.grid(row=2, column=2)
menu_price.grid(row=3, column=2)
#--------------buttons for action--------
addbutton= Button(addmenu, text="Add new Item", bg="lightblue", command= additem1)
addbutton.grid(row=4, column=1, columnspan=2, ipady=10, pady=20, ipadx=10,padx=20)
cancelbutton= Button(addmenu, text="Cancel", command=extmenumsg)
cancelbutton.grid(column=3, row=4, ipady=10, pady=20, ipadx=10,padx=20)

#---------effect data base changes -----------
conn.commit()

#----close database-------
conn.close()

addmenu.mainloop()