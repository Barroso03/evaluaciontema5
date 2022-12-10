import pickle

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa,alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
        # la vida el ataque y la defensa tiene que ser un numero entero positivo
        if not isinstance(self.vida, int) or not isinstance(self.ataque, int) or not isinstance(self.defensa, int) or not isinstance(self.alcance, int):
            raise ValueError("La vida, el ataque y la defensa tienen que ser numeros enteros")
        if self.vida < 0 or self.ataque < 0 or self.defensa < 0 or self.alcance < 0:
            raise ValueError("La vida, el ataque y la defensa tienen que ser numeros positivos")
    def __str__(self):
        return "Nombre: {} Vida: {} Ataque: {} Defensa: {} Alcance: {}".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)
    
    






        

    