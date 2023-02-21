#1.- Importar la clase
from personaje import *

#2.- Instaciar un objecto
Heroe = Personaje()

#3.- Accerder a sus atributos

print("El personaje pertenece a la raza:"+ Heroe.especie)
print("El personaje se llama:"+ Heroe.nombre)
print("El personaje mide:"+ str(Heroe.altura) + "Metros")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(68)