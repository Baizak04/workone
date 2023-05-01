from tkinter import *

root = Tk()
root.title("кнопки")      # Заголовок окна
root.geometry("800x400")     # начальные размеры окна


# Button tkinter

# r = ['Python', 'C#', 'C++', 'java', 'C+']
# lis = Listbox(root, selectmode=SINGLE, height=5)
# for i in r:
#     lis.insert(END, i)
    
# lis.pack()

# widget text 

fra1 = Frame(root, width=400, height=150, bg="darkred")
fra2 = Frame(root, width=250, height=100, bg="green", bd=20)
fra3 = Frame(root, width=100, height=50, bg="darkblue")

ent1 = Entry(fra1, width=20,)

fra1.pack()
fra2.pack()
fra3.pack()
ent1.pack()

root.mainloop()