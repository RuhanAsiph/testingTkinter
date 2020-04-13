#Frames
from tkinter import *
main = Tk()
main.title('Frames')
#creating frames 
frame = LabelFrame(main, text="Testing", padx=50, pady=50)
frame.pack(padx=10, pady=10)

#Displaying frames

b = Button(frame, text="Testing")
b.grid(row=0, column=0)
