from clases.gestor import *
from clases.personaje import *

gestor = Gestor()
print("Añadiendo personajes")
gestor.añadir(Personaje("Caballero", 4,2,4,5))
gestor.añadir(Personaje("Guerrero",2,4,2,3))
gestor.añadir(Personaje("Arquero",2,4,1,1))
gestor.mostrar()
print("Borrando Arquero")
gestor.borrar("Arquero")
gestor.mostrar()


    