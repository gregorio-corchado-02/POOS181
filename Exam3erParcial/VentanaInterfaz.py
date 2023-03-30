from tkinter import Entry, Tk, Label, Button
from ParteLogica import ParteLogica


axc=ParteLogica()

def juntar():
        axc.GenerarMatri(txt1.get(),txt2.get(),txt3.get(),txt4.get(),txt5.get(),txt6.get())



ventana = Tk()
ventana.geometry("400x250")
ventana.title("Mi primera ventana")
ventana.config(bg="black")

lbl1 = Label(ventana,text="Nombre",bg="white")
lbl1.place(x=10,y=10,width=100,height=30)
txt1 = Entry(ventana,bg="white")
txt1.place(x=120,y=10,width=100,height=30)

lbl2= Label(ventana,text="Apellido Paterno",bg="white")
lbl2.place(x=10,y=50,width=100,height=30)
txt2 = Entry(ventana,bg="white")
txt2.place(x=120,y=50,width=100,height=30)
btn = Button(ventana,text="Matricula",command=juntar)
btn.place(x=230,y=50,width=100,height=30)

lbl3= Label(ventana,text="Apellido Materno",bg="white")
lbl3.place(x=10,y=90,width=100,height=30)
txt3 = Entry(ventana,bg="white")
txt3.place(x=120,y=90,width=100,height=30)

lbl4= Label(ventana,text="Año",bg="white")
lbl4.place(x=10,y=130,width=100,height=30)
txt4 = Entry(ventana,bg="white")
txt4.place(x=120,y=130,width=100,height=30)

lbl5= Label(ventana,text="Año en Curso",bg="white")
lbl5.place(x=10,y=170,width=100,height=30)
txt5 = Entry(ventana,bg="white")
txt5.place(x=120,y=170,width=100,height=30)

lbl6= Label(ventana,text="Carrera",bg="white")
lbl6.place(x=10,y=210,width=100,height=30)
txt6 = Entry(ventana,bg="white")
txt6.place(x=120,y=210,width=100,height=30)

ventana.mainloop()