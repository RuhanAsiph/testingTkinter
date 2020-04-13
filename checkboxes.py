from tkinter import *

main = Tk()
main.title("Testing")
main.geometry("400x400")

#defining show
def show():
    myLabel = Label(main, text=var.get()).pack()

#creating a variable
var = IntVar()

#creating a checkbox
c = Checkbutton(main, text="checkbox_testing", variable=var)
#displaying on the screen
c.pack()
#creating a button
myButton = Button(main, text="Show Selection", command=show)
myButton.pack()

main.mainloop()
