import tkinter as tk
from tkinter import ttk
from controladorBD import controladorBD
 
controlador = controladorBD()
 
def ejecutaInsert():
    controlador.guardarusuario(nombre.get(), correo.get(), contrasena.get())
 
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
 
panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar Usuarios')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar Usuarios')
 
ventana.mainloop()




