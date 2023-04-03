from tkinter import *
import sqlite3
import bcrypt
from tkinter import messagebox

class controladorBD:

    def __init__(self):
        pass

   #Metodo oara crear conexion
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/Gregorio/Documents/GitHub/POOS181/SQLite/BaseDeDatos.db")
            print("Conectado a la base de datos")
            return conexion
        except sqlite3.OperationalError:
             print("Conectado a la base de datos")

    #Metodo oara guardar usuarios
    def guardarusuario(self,nom,cor,con):

        #usamos una conexion
        conx= self.conexionBD()

        #validar paratros vacios
        if(nom=="" or  cor=="" or con==""):
            messagebox.showwarning("Formulario incompleto")
        else:
            cursor=conx.cursor()
            datos=(nom,cor,con)
            qrInsert = "insert into TBRegistrados(Nombre,Correo,Contraseña)  values(?,?,?)"

            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showwarning("Usuario guardado")
    
    def encriptarCon(self,con):
        conPlana= con
        conPlana= conPlana.encode()
        sal= bcrypt.gensalt()
        conHa= bcrypt.hashpw(conPlana,sal)
        return conHa
    
    def consultarUsuario(self,id):
        conx=self.conexionBD()
        
        if (id==""):
            messagebox.showwarning("Cuidad","ID vacia")
        else:
            try:

                cursor=conx.cursor()
                selectQry="Select * from TBRegistrados where id="+id

                cursor.execute(selectQry)
                rsUsuario= cursor.fetchall()
                conx.close()
                return rsUsuario

            except sqlite3.OperationalError:
                print("Error Consulta")

    def consultarBase(self):
        conx=self.conexionBD()
        cursor=conx.cursor()
        selectQry="Select * from TBRegistrados"
        cursor.execute(selectQry)

        return cursor.fetchall()

            





    