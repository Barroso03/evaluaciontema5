def suma(numero1, numero2):
        try:
            numero1 + numero2
        except TypeError:
            print("Tipo de dato no valido")
        else:
            return numero1 + numero2
def resta(numero1, numero2):
        try:
            numero1 - numero2
        except TypeError:
            print("Tipo de dato no valido")
        else:
            return numero1 - numero2
def multiplicacion(numero1, numero2):
        try:
            numero1 * numero2
        except TypeError:
            print("Tipo de dato no valido")
        else:
            return numero1 * numero2
def division(numero1, numero2):
        try:
            numero1 / numero2
        except TypeError:
            print("Tipo de dato no valido")
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
        else:
            return numero1 / numero2
       