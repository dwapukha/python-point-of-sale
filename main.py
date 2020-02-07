from tkinter import *
#from Tkinter import  *
import  random
import time
import datetime
#import tkMessageBox

root =Tk()
root.geometry("1280x920+0+0")
root.title("Poa Point of Sale")
root.configure(bg="grey")
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
mylist.pack()
#---------Input for amount paid-----
taxLabel= Label(f2ab, text="Enter tax %: ", font=("Times", 15))
taxLabel.pack()
taxvalue= Entry(f2ab, width=8, bd=6)
taxvalue.pack(side=RIGHT)
#----------Control Buttons-----------
Totalbtn= Button(f3b, text="Total", command='',width=15)
Totalbtn.pack(side=TOP)
Totalbtn1= Button(f3b, text="Pay", command='', width=15)
Totalbtn1.pack(side=RIGHT)
Totalbtn2= Button(f3b, text="Reset", command='',width=15)
Totalbtn2.pack(side=LEFT)
Totalbtn3= Button(f3b, text="Quit", command='', width=25)
Totalbtn3.pack(side=BOTTOM)
root.mainloop()
