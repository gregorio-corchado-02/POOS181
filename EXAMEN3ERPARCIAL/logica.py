from tkinter import *
import sqlite3
import bcrypt
from tkinter import messagebox

class logica:

    def __init__(self):
        pass

   
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/Gregorio/Documents/GitHub/POOS181/EXAMEN3ERPARCIAL/BDImportaciones.db")
            print("Conectado a la base de datos")
            return conexion
        except sqlite3.OperationalError:
             print("Conectado a la base de datos")

    
    def guardarmercancia(self,id,mer,pais):

        conx= self.conexionBD()

        if(id=="" or  mer=="" or pais==""):
            messagebox.showwarning("Formulario incompleto")
        else:
            cursor=conx.cursor()
            datos=(id,mer,pais)
            qrInsert = "insert into TB_Europa(ID,Mercancia,Pais)  values(?,?,?)"

            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showwarning("Mercancia guardada")