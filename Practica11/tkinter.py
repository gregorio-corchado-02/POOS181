from tkinter import Tk, Frame, Button

from tkinter import Tk, Frame, Button, messagebox

#4. Función de mensajes
def mostrarMensaje() :
    messagebox.showinfo("Aviso", "Este mensaje es para informar algo")
    messagebox.showerror("Error", "Este mensaje fallo con exito")
    messagebox.askokcancel("Pregunta", "¿El o ella jugo con tu corazon?")
    print(messagebox.askokcancel("Pregunta", "¿El o ella jugo con tu corazon?"))
    
    
#5Funcion para declarar funciones
def agregarBoton() :
    botonVerde.config(text="+", bg= "green", fg="white")    
    botonNuevo= Button(seccion3, text="Boton Nuevo")
    botonNuevo.pack()
    
    
    
    
    

#1. Creración ventana
ventana= Tk()
ventana.title(' Practica 11:3 Frames')
ventana.geometry('600x400')

#2. Definimos las secciones de la ventana
seccion1=Frame(ventana,bg="RED")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="WHITE")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="BLUE")
seccion3.pack(expand=True,fill='both')

#3. Botones
botonAzul= Button(seccion1, text="Boton Azul", fg="blue", command= mostrarMensaje)
botonAzul.place(x=60, y=60)

botonAmarillo= Button(seccion2, text="Boton Amarillo", bg="#ffff1a")
botonAmarillo.grid(row=0, column=0)

botonNegro= Button(seccion2, text="Boton Negro", fg="black")
botonNegro.grid(row=0, column=1)

botonVerde= Button(seccion3, text="Boton Verde", bg="green", command= agregarBoton)
botonVerde.pack()




#Main de ejecucion de la ventana
ventana.mainloop()