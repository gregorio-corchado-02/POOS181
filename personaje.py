
class Personaje:
    #atributos de personaje
    especie = "humano"
    nombre = "Gregorio"
    altura = 1.78
    
    #Metodos del personaje
    def correr(self,status):
        if(status):
            print("El personaje" + self.nombre+"esta corriendo")
        else:
            print("El personaje" + self.nombre+"se detuvo")
            
    def lanzarGranada(self):
        print("Se lanzo granada")
        
    def recargarArma (self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("El arma tiene: "+ str(cargador) +"balas")