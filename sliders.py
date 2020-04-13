#Frames
from tkinter import *

main = Tk()
main.title('Slider')
#Adjusting the main screen
main.geometry("400x400")

#creating sliders
vertical = Scale(main, from_=0, to=200)
vertical.pack()

#defining scale(function)
def scale(var):
    myLabel = Label(main, text=horizontal.get()).pack()

#slider
horizontal = Scale(main, from_=0, to=200, orient=HORIZONTAL, command=scale)
horizontal.pack()

#displaying sliders position
myLabel = Label(main, text=horizontal.get()).pack()
myLabel2 = Label(main, text=vertical.get()).pack()

#defining scale(function)
def scale():
    myLabel = Label(main, text=horizontal.get()).pack()
#defining scale_2
def scale2():
    myLabel2 = Label(main, text=vertical.get()).pack()
    
    

#creating a button
myButton = Button(main, text="testing", command=scale).pack()
secondBtn = Button(main, text="testing_2", command=scale2).pack()
main.mainloop()

