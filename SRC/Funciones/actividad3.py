# Funcion menu: imprime un menú de opciones y retorna la opcion elegida por el usuario

def menu():
    opcion = 0
    while opcion < 1 or opcion > 4:
        print("1. suma\n2. Resta\n3. Multiplicacion\n4. División")
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 4:
            print("opcion no valida, seleccione una opcon correcta")
    return opcion

operacion = menu()
print(f"El usuario eligio la opción {operacion}")

if operacion == 1:
    pass
elif operacion ==2:
    pass
elif operacion == 3:
    pass