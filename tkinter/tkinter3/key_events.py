from tkinter import *


def dosomething(event):
    print("Что то " + event.keysym)
    label.config(text=event.keysym)
    

window = Tk()

window.bind("<Key>", dosomething)

label = Label(window, font=("Hello", 100))

window.mainloop()