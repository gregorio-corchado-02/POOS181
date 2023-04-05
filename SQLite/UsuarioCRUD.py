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
        txtenc.insert(tk.INSERT,cadena)
    else:
        messagebox.showinfo("usuario no encontrado","usuario no existe en la BD")

def ejecutaconsult():
    personas= controlador.consultarBase()
    for i in personas:
        elemets = personas
        if(personas):
            tree.insert('', tk.END, text=i)
        else:
            messagebox.showinfo("usuarios no encontrados","no hay registros")

def ejecutaEdit():
    controlador.editasrUsuario(idBuscada.get(), nombre2.get(), correo2.get(), contrasena2.get())

def ejecutaEliminar():
    controlador.eliminarUsuario(id3.get())


ventana = tk.Tk()
ventana.title("Crud de usuarios")
ventana.geometry("500x300")
 
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')
 
pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)
pestaña5 = ttk.Frame(panel)
 
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
txtenc=tk.Text(pestaña2,height=5,width=52)
txtenc.pack()

titulo3 = tk.Label(pestaña3, text='Consultar Usuarios', fg='blue', font=('modern',18))
titulo.pack()

tap=tk.StringVar()
txtconsul = tk.Label(pestaña3, text="Mostrar todos los usuarios de la base de datos")
txtconsul.pack()
btnConsult = tk.Button(pestaña3, text="Mostrar", command=ejecutaconsult).pack()
tree=ttk.Treeview(pestaña3)
tree.pack()

titulo4 = tk.Label(pestaña4, text='Editar Usuario', fg='blue', font=('modern',18))
titulo4.pack()

idBuscada = tk.StringVar()
lblid2 = tk.Label(pestaña4, text="Ingrese la id del usuario que desee modificar")
lblid2.pack()
txtid2 = tk.Entry(pestaña4, textvariable=idBuscada)
txtid2.pack()

nombre2 = tk.StringVar()
lblNom2 = tk.Label(pestaña4, text="Nuevo Nombre")
lblNom2.pack()
txtNom2 = tk.Entry(pestaña4, textvariable=nombre2)
txtNom2.pack()
 
correo2 = tk.StringVar()
lblCor2 = tk.Label(pestaña4, text="Nuevo Correo")
lblCor2.pack()
txtCor2 = tk.Entry(pestaña4, textvariable=correo2)
txtCor2.pack()
 
contrasena2 = tk.StringVar()
lblCon2 = tk.Label(pestaña4, text="Nueva Contraseña")
lblCon2.pack()
txtCon2 = tk.Entry(pestaña4, textvariable=contrasena2)
txtCon2.pack()
 
btnGuardar2 = tk.Button(pestaña4, text="Agregar nuevos datos", command=ejecutaEdit)
btnGuardar2.pack()

titulo5 = tk.Label(pestaña5, text='Elimina usuario', fg='blue', font=('modern',18))
titulo5.pack()
id3 = tk.StringVar()
lblNom2 = tk.Label(pestaña5, text="Ingresa ID del usuario a Eliminar")
lblNom2.pack()
txtCor2 = tk.Entry(pestaña5, textvariable=id3)
txtCor2.pack()
btnGuardar2 = tk.Button(pestaña5, text="Eliminar Usuario", command=ejecutaEliminar)
btnGuardar2.pack()

panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar Usuarios')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar Usuarios')
panel.add(pestaña5, text='Eliminar Usuario')

 
ventana.mainloop()




