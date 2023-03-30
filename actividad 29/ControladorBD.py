from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorBD import controladorBD

# Creamos un objeto de la clase controladorBD
controlador = controladorBD()

# Función para disparar el botón
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)

# Pestaña1: Formulario de usuarios

Label(pestaña1, text='Registro de usuarios', fg='blue', font=('Modern', 18)).pack()

varNom = StringVar()
Label(pestaña1, text="Nombre: ").pack()
Entry(pestaña1, textvariable=varNom).pack()

varCor = StringVar()
Label(pestaña1, text="Correo: ").pack()
Entry(pestaña1, textvariable=varCor).pack()

varCon = StringVar()
Label(pestaña1, text="Contraseña: ").pack()
Entry(pestaña1, textvariable=varCon).pack()

btnGuardar = Button(pestaña1, text="Guardar Usuario", command=ejecutaInsert)
btnGuardar.pack()

#Pestaña 2: Buscar Usuarios

titulo2 = Label(pestaña2,text="Buscar Usuario", fg='green', font=("Modern",18)).pack()

varBus = tk.StringVar()
lblid = Label(pestaña2,text= "Identificador de usuarios: ").pack()
txtid = Entry(pestaña2,textvariable=varBus).pack()
btnBus = Button(pestaña2, text="Buscar").pack()

subBus = Label(pestaña2,text="Encontrado: ", fg='blue', font=("Modern",15)).pack()
textEnc = tk.Text(pestaña2,height=5,width=52).pack()


panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar usuario')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar usuario')

ventana.mainloop()