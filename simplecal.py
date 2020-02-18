from tkinter import *
cal= Tk()
cal.title("Simple Calculator")
#global f_num
#global operand
def button_click(number):
    current= data.get()
    data.delete(0, END)
    data.insert(0, str(current) + str(number))
def clearbtn():
    data.delete(0, END)
def button_add():
    first_number = data.get()
    global f_num
    global math
    math= "addition"
    f_num = int(first_number)
    data.delete(0, END)

def button_substrat():
    first_number = data.get()
    global f_num
    global math
    math = "substration"
    f_num = int(first_number)
    data.delete(0, END)
def button_multiply():
    first_number = data.get()
    global f_num
    global math
    math= "multiplication"
    f_num = int(first_number)
    data.delete(0, END)

def button_divide():
    first_number = data.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    data.delete(0, END)
def button_equal():
    second_number= data.get()
    data.delete(0, END)
    if math == "addition":
        data.insert(0, f_num + int(second_number))
    if math == "substration":
        data.insert(0, f_num - int(second_number))
    if math == "multiplication":
        data.insert(0, f_num * int(second_number))
    if math == "division":
        data.insert(0, f_num / int(second_number))




data = Entry(cal, width=35, bd=8, font=('times',  20), bg="grey", relief="sunken")
data.grid(row=0, column=0, columnspan=3)

calbtn1= Button(cal, text=4, padx=40, pady=40, command=lambda: button_click(4))
calbtn1.grid(row=2, column=0)
calbtn2= Button(cal, text=5, padx=40, pady=40,command=lambda: button_click(5))
calbtn2.grid(row=2, column=1)
calbtn3= Button(cal, text=6, padx=40, pady=40, command=lambda: button_click(6))
calbtn3.grid(row=2, column=2)
calbtnmult= Button(cal, text="x", font=('aerial', 16, 'bold'), padx=25, pady=35, command= button_multiply)
calbtnmult.grid(row=2, column=3)

calbtn4= Button(cal, text=7, padx=40, pady=40, command=lambda: button_click(7))
calbtn4.grid(row=1, column=0)
calbtn5= Button(cal, text=8, padx=40, pady=40, command=lambda: button_click(8))
calbtn5.grid(row=1, column=1)
calbtn6= Button(cal, text=9, padx=40, pady=40, command=lambda: button_click(9))
calbtn6.grid(row=1, column=2)
calbtndiv= Button(cal, text="/", font=('aerial', 16, 'bold'), padx=25, pady=35, command= button_divide)
calbtndiv.grid(row=1, column=3)

calbtn7= Button(cal, text=0, padx=40, pady=40, command=lambda: button_click(0))
calbtn7.grid(row=4, column=0)
calbtn8= Button(cal, text=".", padx=40, pady=40)
calbtn8.grid(row=4, column=1)
calbtn9= Button(cal, text='+', font=('aerial', 16, 'bold'), padx=40, pady=40, command=button_add)
calbtn9.grid(row=4, column=2)

calbtn01= Button(cal, text=1, padx=40, pady=40, command=lambda: button_click(1))
calbtn01.grid(row=3, column=0)
calbtn02= Button(cal, text=2, padx=40, pady=40, command=lambda: button_click(2))
calbtn02.grid(row=3, column=1)
calbtn03= Button(cal, text=3, padx=40, pady=40, command=lambda: button_click(3))
calbtn03.grid(row=3, column=2)
calbtnmult= Button(cal, text="-", font=('aerial', 16, 'bold'), padx=25, pady=35, command= button_substrat)
calbtnmult.grid(row=3, column=3)

calbtn04= Button(cal, text="Clear", font=('aerial', 17, 'bold'), padx=40, pady=40, command=lambda: clearbtn ())
calbtn04.grid(row=5, column=0)
calbtn04= Button(cal, text="=", font=('aerial', 16, 'bold'),padx=40, pady=40, command= lambda: button_equal())
calbtn04.grid(row=5, column=1)





cal.mainloop()
