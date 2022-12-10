import os

def contador():
   # si el fichero no existe, se crea
    if not os.path.exists("ejercicio2/contador.txt"):
        with open("ejercicio2/contador.txt", "w") as f:
            f.write("0")
    # si el fichero existe, se abre y se lee
    with open("ejercicio2/contador.txt", "r") as f:
        contador = int(f.read())
    # si escribes inc o dec, se incrementa o decrementa
    if input("inc o dec? ") == "inc":
        contador += 1
    elif input("inc o dec? ") == "dec":
        contador -= 1
    else:
        return contador
    # se escribe el nuevo valor en el fichero
    with open("ejercicio2/contador.txt", "w") as f:
        f.write(str(contador))
    print(contador)
    # se muestra el valor del contador
   
contador()


