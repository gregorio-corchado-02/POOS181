from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:

    def _init_(self):
        pass

    # Metodo para crear conexiones
    def conexionBD(self):

        try:
            conexion = sqlite3.connect("C:\Users\Antonio Gutierrez V\Documents\GitHub\POOS181\actividad 29\BaseDeDatos.db")
            print("Conectado a la Base de Datos")
            return conexion
        except sqlite3.OperationalError:
            print("No se puede conectar")

    #Metodo para guardar usuarios
    def guardarUsuario(self,nom,cor,con):

        # paso 1: usamos una conexion
        conx = self.conexionBD()

        # paso 2: validar parametros que esten vacios
        if(nom=="" or cor=="" or con ==""):
            messagebox.showwarning("Formulario Incompleto")
        else:
        # paso 3: preparamos el cursor, datos y QuerySQL
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos = (nom,cor,conH)
            qrInsert = "insert into TBRegistrados(nombre,correo,contraseña) values(?,?,?)"

        # paso 4: ejecutar Insert y cerramos conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario Guardado")

    def encriptarCon(self,con):
        conPlana = con
        conPlana = conPlana.encode() #convertimos con a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)

        #enviamos la contraseña encryptada
        return conHa