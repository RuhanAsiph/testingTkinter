from tkinter import *
main = Tk()
#Window title
main.title("Calculator")
#Space required for inserting numbers
e = Entry(main, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#function for adding two numbers
def clickk(number):
    #clearing the window
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) +str(number))#inserting the number that we hit on the num pad
def clrr():
    e.delete(0, END)
def addd():
    first_number= e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
def equall():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    
#more functions
def subtractt():
    first_number= e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
def multt():
    first_number= e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
def divv():
    first_number= e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    
#creating buttons
button1 = Button(main, text="1", padx=40, pady=20, command=lambda: clickk(1))
button2 = Button(main, text="2", padx=40, pady=20, command=lambda: clickk(2))
button3 = Button(main, text="3", padx=40, pady=20, command=lambda: clickk(3))
button4 = Button(main, text="4", padx=40, pady=20, command=lambda: clickk(4))
button5 = Button(main, text="5", padx=40, pady=20, command=lambda: clickk(5))
button6 = Button(main, text="6", padx=40, pady=20, command=lambda: clickk(6))
button7 = Button(main, text="7", padx=40, pady=20, command=lambda: clickk(7))
button8 = Button(main, text="8", padx=40, pady=20, command=lambda: clickk(8))
button9 = Button(main, text="9", padx=40, pady=20, command=lambda: clickk(9))
button0 = Button(main, text="0", padx=40, pady=20, command=lambda: clickk(0))
buttonAdd = Button(main, text="+", padx=39, pady=20, command=addd)
buttonEqual = Button(main, text="=", padx=91, pady=20, command=equall)
buttonClr = Button(main, text="clr", padx=88, pady=20, command=clrr)
#creating more buttons
buttonSubtract = Button(main, text="-", padx=41, pady=10, command=subtractt)
buttonMult = Button(main, text="*", padx=41, pady=10, command=multt)
buttonDiv = Button(main, text="/", padx=41, pady=10, command=divv)
#putting buttons on the screen
button1.grid(row=3,column=1)
button2.grid(row=3,column=2)
button3.grid(row=3,column=0)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=0)
button7.grid(row=1,column=1)
button8.grid(row=1,column=2)
button9.grid(row=1,column=0)
button0.grid(row=4,column=0)
buttonClr.grid(row=4,column=1, columnspan=2)
buttonAdd.grid(row=5,column=0)
buttonEqual.grid(row=5,column=1, columnspan=2)

buttonSubtract.grid(row=6, column=0)
buttonMult.grid(row=6, column=1)
buttonDiv.grid(row=6, column=2)
