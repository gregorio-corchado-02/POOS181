from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBD import controladorBD
 
controlador = controladorBD()
 
def ejecutaInsert():
    controlador.guardarusuario(nombre.get(), correo.get(), contrasena.get())

def ejecutaselectu():
    usuario= controlador.consultarUsuario(varBus.get())
    for usu in usuario:
        cadena=str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+ str(usu[3])
    if(usuario):
        print(cadena)
    else:
        messagebox.showinfo("usuario no encontrado","usuario no existe en la BD")
    textenc.insert(tk.INSERT,cadena)
 
ventana = tk.Tk()
ventana.title("Crud de usuarios")
ventana.geometry("500x300")
 
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')
 
pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)
 
titulo = tk.Label(pestaña1, text='Registro de usuarios', fg='blue', font=('modern',18))
titulo.pack()
 
nombre = tk.StringVar()
lblNom = tk.Label(pestaña1, text="Nombre")
lblNom.pack()
txtNom = tk.Entry(pestaña1, textvariable=nombre)
txtNom.pack()
 
correo = tk.StringVar()
lblCor = tk.Label(pestaña1, text="Correo")
lblCor.pack()
txtCor = tk.Entry(pestaña1, textvariable=correo)
txtCor.pack()
 
contrasena = tk.StringVar()
lblCon = tk.Label(pestaña1, text="Contraseña")
lblCon.pack()
txtCon = tk.Entry(pestaña1, textvariable=contrasena)
txtCon.pack()
 
btnGuardar = tk.Button(pestaña1, text="Registrar Usuario", command=ejecutaInsert)
btnGuardar.pack()

titulo2 = tk.Label(pestaña2, text='Buscar usuarios', fg='blue', font=('modern',18))
titulo.pack()

varBus=tk.StringVar()
lblid = tk.Label(pestaña2, text="Identificador de susarios")
lblid.pack()
txtid = tk.Entry(pestaña2, textvariable=varBus)
txtid.pack()

btnBus = tk.Button(pestaña2, text="Buscar", command=ejecutaselectu).pack()

subBus = tk.Label(pestaña2, text="Encontrado",fg="blue",font=("Modern",15)).pack()
textenc=tk.Text(pestaña2,height=5,width=52)
textenc.pack()

panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar Usuarios')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar Usuarios')
 
ventana.mainloop()




