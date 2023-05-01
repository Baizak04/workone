from tkinter import *

root = Tk()
root.title("Программа")      # Заголовок окна
root.geometry("800x400")     # начальные размеры окна

but = Button(root,
             text="нажми",
             width=20, height=2,
             bg="white", fg="blue")

lab = Label(root, text="что-то", font="Arial 16")

ent = Entry(root, width=15, bd=2)

text = Text(root, width=15, font="Oswald 16", wrap=WORD)

r1 = Radiobutton(text="Windows")
r2 = Radiobutton(text="Linux")


but.pack()
ent.pack()
lab.pack()
text.pack()
r1.pack()
r2.pack()

root.mainloop()