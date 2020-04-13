#Frames
from tkinter import *
from tkinter import messagebox
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

main = Tk()
main.title('Message')

#defining functions 
def popup():
    response = messagebox.askquestion("Pop up", "testing")
    Label(main, text=response).pack()
    if response == "yes":
        Label(main, text="You clicked yes").pack()
    else:
        Label(main, text="you clicked no").pack()
        

#creating a button
Button(main, text="Pop up", command=popup).pack()


mainloop()
