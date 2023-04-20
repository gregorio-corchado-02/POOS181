from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from logica import logica

 
controlador = logica()
 
def ejecutaInsert():
    controlador.guardarmercancia(Idm.get(), mercancia.get(), pais.get())

def ejecutaEliminar():
    controlador.eliminarmercancia(id2.get())

def ejecutaconsult():
    personas= controlador.consultarBase(paism.get())
    for i in personas:
        elemets = personas
        if(personas):
            tree.insert('', tk.END, text=i)
        else:
            messagebox.showinfo("mercancia no encontrados","no existe")


ventana = tk.Tk()
ventana.title("Crud de Mercancia")
ventana.geometry("500x300")
 
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')
 
pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
 
titulo = tk.Label(pestaña1, text='Insertar una mercancia', fg='blue', font=('modern',18))
titulo.pack()
 
Idm = tk.StringVar()
lblidm = tk.Label(pestaña1, text="ID")
lblidm.pack()
txtIdm = tk.Entry(pestaña1, textvariable=Idm)
txtIdm.pack()
 
mercancia = tk.StringVar()
lblMER = tk.Label(pestaña1, text="Nombre de mercancia")
lblMER.pack()
txtMER = tk.Entry(pestaña1, textvariable=mercancia)
txtMER.pack()
 
pais = tk.StringVar()
lblpa = tk.Label(pestaña1, text="Ingrese el Pais")
lblpa.pack()
txtpa = tk.Entry(pestaña1, textvariable=pais)
txtpa.pack()
 
btnGuardar = tk.Button(pestaña1, text="Registrar Usuario", command=ejecutaInsert)
btnGuardar.pack()

titulo2 = tk.Label(pestaña2, text='Elimina mercancia', fg='blue', font=('modern',18))
titulo2.pack()
id2 = tk.StringVar()
lblNom2 = tk.Label(pestaña2, text="Ingresa ID de la mercancia a Eliminar")
lblNom2.pack()
txtCor2 = tk.Entry(pestaña2, textvariable=id2)
txtCor2.pack()
btnGuardar2 = tk.Button(pestaña2, text="Eliminar mercancia", command=ejecutaEliminar)
btnGuardar2.pack()

titulo3 = tk.Label(pestaña3, text='Consultar nercancia', fg='blue', font=('modern',18))
titulo.pack()

paism=tk.StringVar()
lblconsul = tk.Label(pestaña3, text="Ingrese la id de la mercancia a buscar")
lblconsul.pack()
txtbus = tk.Entry(pestaña3, textvariable=paism)
txtbus.pack()
btnConsult = tk.Button(pestaña3, text="Mostrar", command=ejecutaconsult).pack()
tree=ttk.Treeview(pestaña3)
tree.pack()

panel.add(pestaña1, text='Insertar una mercancia')
panel.add(pestaña2, text='Eliminar mercancia')
panel.add(pestaña3, text='Buscar mercancia')
ventana.mainloop()
