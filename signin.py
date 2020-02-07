from tkinter import *
mysignup = Tk()
mysignup.title("PoappsPOS")

def myClick():
    myLabel = Label(mysignup, text=username.get())
    myLabel.grid()

mysignup.configure(width=350, height=200, bg="grey")
myLabel1 = Label(mysignup, text="Username")
username = Entry(mysignup, bg='brown', width=30)
myLabel2 = Label(mysignup, text="Password",)
myPass = Entry(mysignup,bg='brown', width=30)
mybutton = Button(mysignup, text='Login', command=myClick, padx=50, pady=10, bg="green")
mybutton2 = Button(mysignup, text="Cancel", padx=50, pady=15)
myLabel1.grid(row=0, column=0)
username.grid(row=0, column=1)
myLabel2.grid(row=1, column=0)
myPass.grid(row=1,column=1)
mybutton.grid(row=2, column=1)
mybutton2.grid(row=2, column=2)

mainloop()

