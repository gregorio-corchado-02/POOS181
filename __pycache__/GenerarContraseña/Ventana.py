
from tkinter import *
from tkinter import ttk, font
from Logica import *


Pestaña = Tk()
Pestaña.title("GENERADOR DE CONTRASEÑAS")
Pestaña.geometry("600x200")

Entry = ttk.Entry(font=font.Font(family="Arial", size=14))
Entry.place(x=250, y=20)

Entry = ttk.Entry(font=font.Font(family="Arial", size=14))
Entry.place(x=250, y=80)

Pestaña.mainloop()