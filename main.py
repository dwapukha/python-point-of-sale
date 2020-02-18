from tkinter import *
#from Tkinter import  *
import  random
import time
import datetime
from tkinter import messagebox
import sqlite3

root =Tk()
#root.geometry("1280x920+0+0")
root.title("Poa Point of Sale")
root.configure(bg="grey")
root.resizable(True, False)
#------creating database or connecting to database-------
conn=sqlite3.connect('POS.db')
#create cursor------
c= conn.cursor()


#---effect data base changes -----
conn.commit()

#----close database-------

def popinfo():
   # top= Toplevel()
   # global mess
  #  mess=top
  #  top =  lunchmenu()
  #  mylabelinfo= Label(top, text=mess)
  #  mylabelinfo.pack()
  return



def reset_button():
    mylist.delete()

def pay_button():
    return
def total_button():
    return
def breakfast_menu():
    myteabtn = Listbox(f1ab, font=('arieal',16) )
    myteabtn.insert(0, "White Tea")
    myteabtn.insert(1, "Special Tea")
    myteabtn.insert(2, "Hot Coffee")
    myteabtn.insert(3,"Black Tea")
    myteabtn.insert(4, "Black Tea")
    myteabtn.insert(5, "Black Tea")
    myteabtn.insert(6,"Black Tea")
    myteabtn.pack()
def lunchmenu():

    conn=sqlite3.connect('POS.db')
    c= conn.cursor()
    c.execute("SELECT * FROM menuitems ")
    results_print = ''
    results= c.fetchall()
    for result in results:
        results_print += str(result) + "\n"
    labelresults= Label(f1ab, text= results_print)
    labelresults.pack()
    conn.commit()
    conn.close()


def dinner_button():

    din= Listbox(f1ab, font=('arieal', 16))
    din.insert(0, "1/4 Kuku Chip------ $12")
    din.insert(1, "1/2 Chip")
    din.insert(2, "Full Chip")
    din.insert(3, "Full Kuku Chip")
    din.insert(4, "1/2Kuku Chip")
    din.insert(5, "Wet fry Chips")
    din.insert(6, "Chapati")
    din.insert(7, "Ugali plain")
    din.insert(8, "Beans Rice")
    #din.delete(0, END)
    din.pack()
    #breakfastItems= [f1b, "Black Tea", "White Tea", "Expresso", "Chocolate Tea"]
   # print(breakfastItems)
#Top part of the POS
Tops = Frame (root, width=1350, height=100, bd=14, relief="ridge")
#OrganizationName= Label(root, text="POA Resturuant Management System", font="Times, 32")
#OrganizationName.pack()
Tops.pack(side=TOP)
# Total main frame starts here
#-------------left main frame defined-------
f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
#----------another top frame------
f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

#------------TOP LEFT FRAME--------------
f1b = Frame(f1a, width=450, height=330, bd=16, relief="raise")
f1b.pack(side=LEFT)
#-----------Top Right frame----------
f1ab = Frame(f1a, width=450, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)
#----LEFT bottom frame--------
f2= Frame(f1, width=900, height=320, bd=6, relief="raise")
f2.pack(side=BOTTOM)

# ---------LEFT bottom LEFT framework -----------
f2ab= Frame(f2, width=450, height=330, bd=14, relief="raised")
f2ab.pack(side=LEFT)
# ---------LEFT bottom RIGHT framework -----------
f2abe= Frame(f2, width=450, height=330, bd=14, relief="raised")
f2abe.pack(side=RIGHT)
#----------Right frame ------------------
f3= Frame(root, width=450, height=650, bd=8, relief="raised")
f3.pack(side=RIGHT)
#----------Right frame TOP ------------------
f3a = Frame(f3, width=450, height= 330, bd=16, relief="raised")
f3a.pack(side=TOP)
#-----------------Right Frame Bottom--------------
f3b= Frame(f3, width=450, height=330, bd=16, relief="groove")
f3b.pack(side=BOTTOM)
#------POS Organizatio name at Tops--------
infoLabel= Label(Tops,  text=" Poa Restuarant Point of Sale ", bd=10, font=("Times", 72, "bold"))
infoLabel.grid()
#------------------List of Food Items------------
#Tea = Checkbutton(f1a, text="Tea \t", variable=var1, onvalue=1, offvalue=0, fot=("aerial", 18, "bold"), command=chkButton )

#---------List of Items
mylist= Listbox(f3a, bd=3)
mylist.insert(0,"1/4 Kuku Chips")
mylist.pack()

#-----------Getting values from the lists--------
def getlistvalues():
    return
#--------------quit message----------
def popup():
    response= messagebox.askyesno("Your are bout to close POS", "Are you sure you want to close POS?")
    if response == 1:
        root.quit()
    if response == 0:
        root.option_clear()

#---------Input for amount paid-----
taxLabel= Label(f2ab, text="Enter tax %: ", font=("Times", 15))
taxLabel.pack()
taxvalue= Entry(f2ab, width=8, bd=6)
taxvalue.pack(side=RIGHT)
#----------Control Buttons-----------
Totalbtn= Button(f3b, text="Total", command='',width=15)
Totalbtn.pack(side=TOP)
Totalbtn1= Button(f3b, text="Pay", command=popinfo, width=15)
Totalbtn1.pack(side=RIGHT)
Totalbtn2= Button(f3b, text="Reset", command= reset_button,width=15)
Totalbtn2.pack(side=LEFT)
Totalbtn3= Button(f3b, text="Quit", command= popup, width=25)
Totalbtn3.pack(side=BOTTOM)

#------top left frame buttons main menu items-----
btnBreakfast= Button(f1b, text="BreakFast", padx=19, pady=15, bd=5, font=('times',18, 'bold'), command= lambda: breakfast_menu() )
btnLunch= Button(f1b, text="Lunch", padx=39, pady=15, bd=5, font=('times',18, 'bold'), command=lunchmenu )
btnDinner= Button(f1b, text="Dinner", padx=39, pady=15, bd=5, font=('times',18, 'bold'), command=lambda: dinner_button() )
btnAddons= Button(f1b, text="Addons", padx=39, pady=15, bd=5, font=('times',18, 'bold'))

btnBreakfast.pack()
btnLunch.pack()
btnDinner.pack()
btnAddons.pack()
#----function to get the values of the radio button-----
def optioned(value):
    myLabel = Label(f3a, text= value)
    myLabel.pack()

#----------Bottom Left buttons f2---------
r= StringVar()
r.set("Cash Payment")
r.get()
mypayment= Label(f2, text="Customer Payment Method", font=('times', 14, 'bold')).pack()
Radiobutton(f2, text="Cash Payment", variable= r, value="Cash Payment", command=lambda: optioned(r.get())).pack()
Radiobutton(f2, text="Mpesa Payment", variable= r, value="Mpesa Payment", command=lambda: optioned(r.get())).pack()
Radiobutton(f2, text="Card Payment", variable= r, value="Card Payment", command=lambda: optioned(r.get())).pack()
myLabel= Label(f3a, text= r.get())
myLabel.pack(anchor=E)
#----------------Middle bottom frame-------------
def orderoption(value1):
    myLabel1= Label(f3a, text=value1)
    myLabel1.pack(anchor=W)
ort= StringVar()
ort.set("Take in order")
Typeoforder= Label(f2abe, text="Customer Order Type",font=('times', 14, 'bold')).pack()
Radiobutton(f2abe, text="Take in order", variable= ort, value="Take in order" , command=lambda: orderoption(ort.get())).pack()
Radiobutton(f2abe, text="Packed Take Away", variable= ort, value="Packed take away" , command=lambda: orderoption(ort.get())).pack()
Radiobutton(f2abe, text="Pre-booking", variable= ort, value="Pre-Booking", command=lambda: orderoption(ort.get())).pack()
myLabel1= Label(f3a, text= ort.get())
myLabel1.pack()
#------------creating option button using different option------------
Accampaniments=[
    ("Sourceage", "Sourceage"),
    ("Sugerless", "Sugerless"),
    ("TotamoSource", "TotamoSource"),
    ("Salads", "Salads"),
    ("Maredd", "Mareed"),
]
extras= StringVar()
extras.set("Sourceage")
for text, accampaniment in Accampaniments:
    Radiobutton(f2ab, text=text, variable= extras, value= accampaniment).pack()
def clicked(value3):
    myLabel2= Label(f3a, text= value3)
    myLabel2.pack()

myLabel2= Label(f3a, text=extras.get())
myLabel2.pack()
myLabel1.forget()

var = StringVar()
def show():
    mylabel=Label(f3a, text=var.get()).pack()
def optionsprint():
    mylabelm = Label(f3a, text=options.get()).pack()
    mylabelty = Label(f3a, text= option.get()).pack()
checkbox1= Checkbutton(f1ab, text="Check me now", variable= var, onvalue="Yes", offvalue="No")
checkbox1.pack()
mybutton= Button(f1ab, text="view selection", command= show).pack()
checkbox1.deselect()
option= StringVar()
option.set("Take away")
options = StringVar()
options1 = [1,2,4,5,6,7,8,9,0,10]

optionmn= OptionMenu(f1a, option, "Take Away", "Seat in", "Pre-order").pack()
options.set([2])
optionsbox= OptionMenu(f1a, options, *options1).pack()

buttonoption= Button(f1a, text="Set order Options", command=optionsprint).pack()

root.mainloop()
