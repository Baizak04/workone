from tkinter import *




def b1(event):
    root.title("Левая кнопка")
    
def b3(event):
    root.title("правая кнопка")
    
def move(event):
    root.title("Движения")
    

root = Tk()
root.title("изначальный заголовок")
root.minsize(width=500, height=400)

root.bind('<Button-1>', b1)
root.bind('<Button-3>', b3)
root.bind('<Motion>', move)

root.mainloop()