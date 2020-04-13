#Frames
from tkinter import *
main = Tk()
main.title('Radio Buttons')
#creating a list embedded with tuples
#first value = text
#second value = mode

toppings = [
    ("Mushroom","Mushroom"),
    ("Jalapeno","Jalapeno"),
    ("Onion","Onion"),
    ("Chicken","Chicken"),
    ]

#defining the variable
menu = StringVar()
menu.set("Mushroom")

#looping through the list
for text, mode in toppings:
    Radiobutton(main, text=text, variable=menu, value=mode).pack(anchor=W)

#defining the variable
def clicked(value):
    myLabel = Label(main, text=value)
    myLabel.pack()

#Displaying labels and buttons on the screen
'''myLabel = Label(main, text=menu.get())
myLabel.pack() '''
myButton = Button(main, text="Testing", command=lambda: clicked(menu.get()))
myButton.pack()
mainloop()
