from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from logica import logica

 
controlador = logica()
 
def ejecutaInsert():
    controlador.guardarmercancia(Idm.get(), mercancia.get(), pais.get())


ventana = tk.Tk()
ventana.title("Crud de Mercancia")
ventana.geometry("500x300")
 
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')
 
pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)
pestaña5 = ttk.Frame(panel)
 
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

panel.add(pestaña1, text='Insertar una mercancia')
ventana.mainloop()
