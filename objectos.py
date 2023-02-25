from personaje import *

print("")
print("Solicitar de datos heroe ")
espH= input("Escribe la especie ")
nomH= input("Escribe el nombre ")
altH= input("Escribe la altura ")
cargaH=int( input("Cuntas balas recarga el heroe "))

print("")
print("Solicitar de datos villano")
espV= input("Escribe la epecie villano ")
nomV= input("Escribe el nombre villano ")
altV= input("Escribe la altura villano ")
cargaV= int(input("Cuntas balas recarga el villano "))

Heroe = Personaje(espH, nomH, altH)
Villano= Personaje(espV, nomV, altV)

Heroe.setNombre("Pepe pecas")

print("El personaje pertenece a la raza: "+ Heroe.getEspecie())
print("El personaje se llama: "+ Heroe.getNombre())
print("El personaje mide: "+ str(Heroe.getAltura()) + "Metros")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)
#Heroe.__pensar()


print("El personaje pertenece a la raza: "+ Villano.getEspecie())
print("El personaje se llama: "+ Villano.getNombre())
print("El personaje mide: "+ str(Villano.getAltura()) + "Metros")

Villano.correr(True)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)