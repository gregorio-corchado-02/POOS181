from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

controlador=controladorBD()

def ejecutaInsert():
    controlador.guardarusuario(varNom.get(),varCor.get(),varCon.get())

ventana = Tk ()
ventana.title("Crude de usuarios")
ventana.geometry("500x300")


panel= ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestaña1= ttk.Frame(panel)
pestaña2= ttk.Frame(panel)
pestaña3= ttk.Frame(panel)
pestaña4= ttk.Frame(panel)

#pestaña1: Formulario de ususarios
titulo= Label(pestaña1,text='Registro de usuarios',fg='blue',font=('modern',18)).pack()

varNom= tk.StringVar()
lblNom= Label(pestaña1,text= "Nombre").pack()
txtNom=Entry(pestaña1,textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(pestaña1,text= "correo").pack()
txtCor=Entry(pestaña1,textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(pestaña1,text= "Contraseña").pack()
txtCon=Entry(pestaña1,textvariable=varCon).pack()

btmGuardar= tk.Button(pestaña1 ,text= "Registrar: ",command=ejecutaInsert).pack()




panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar Usuarios')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar Usuarios')

ventana.mainloop()




