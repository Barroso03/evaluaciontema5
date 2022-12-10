import pickle

class Gestor:
    def __init__(self):
        self.personajes = []
        self.cargar()
    def __str__(self):
        return "Personajes: {}".format(self.personajes)
    def cargar(self):
        try:
            with open("ejercicio3/personajes.pckl", "rb") as f:
                self.personajes = pickle.load(f)
        except FileNotFoundError:
            print("No existe el fichero")
    def guardar(self):
        with open("ejercicio3/personajes.pckl", "wb") as f:
            pickle.dump(self.personajes, f)
    def añadir(self, personaje):
        self.personajes.append(personaje)
        self.guardar()
    def mostrar(self):
        for personaje in self.personajes:
            print(personaje)
    def borrar(self, nombre):
        for personaje in self.personajes:
            if personaje.nombre == nombre:
                self.personajes.remove(personaje)
                self.guardar()
                return
        print("No existe el personaje")