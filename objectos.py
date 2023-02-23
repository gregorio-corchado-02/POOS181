#1.- Importar la clase
from personaje import *

#2.- Solicitar atributos del objecto
print("")
print("Solicitar de datos heroe")
espH= input("Escribe la especie")
nomH= input("Escribe el nombre")
altH= input("Escribe la altura")
cargaH= input("Cuntas balas recarga el heroe")

print("")
print("Solicitar de datos villano")
espV= input("Escribe la villano")
nomV= input("Escribe el villano")
altV= input("Escribe la villano")
cargaV= input("Cuntas balas recarga el villano")

Heroe = Personaje(espH, nomH, altH)
Villano= Personaje(espV, nomV, altV)

#3.- Accerder a sus atributos

print("El personaje pertenece a la raza:"+ Heroe.especie)
print("El personaje se llama:"+ Heroe.nombre)
print("El personaje mide:"+ str(Heroe.altura) + "Metros")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(68)

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma

print("El personaje pertenece a la raza:"+ Heroe.especie)
print("El personaje se llama:"+ Heroe.nombre)
print("El personaje mide:"+ str(Heroe.altura) + "Metros")

print("El personaje pertenece a la raza:"+ Villano.especie)
print("El personaje se llama:"+ Villano.nombre)
print("El personaje mide:"+ str(Villano.altura) + "Metros")

Villano.correr(True)
Villano.lanzarGranada()
Villano.recargarArma