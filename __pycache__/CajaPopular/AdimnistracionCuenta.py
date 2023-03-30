from tkinter import *
from warnings import showwarning 
ventana = Tk() 
ventana.title("Administración de cuenta") 
ventana.geometry("520x480")



def datos():
    E

seccion1=Frame(ventana,bg="#000000")
seccion1.pack(expand=True,fill='both')

lblCuenta= Label(seccion1, text="No. Cuenta: ", font=("Arial", 14)).pack()
txtCuenta= Entry(seccion1, textvariable=int,takefocus=True).pack()

lblTitular= Label(seccion1, text="Titular: ", font=("Arial", 14)).pack()
txtTitular= Entry(seccion1, textvariable=int).pack()

lblEdad= Label(seccion1, text="Edad: ", font=("Arial", 14)).pack()
txtEdad= Entry(seccion1, textvariable=int).pack()

lblSaldo= Label(seccion1, text="Saldo: ", font=("Arial", 14)).pack()
txtSaldo= Entry(seccion1, textvariable=int).pack()

ventana.mainloop() 