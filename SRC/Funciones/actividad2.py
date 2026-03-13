# Crear una fincion que calcule el factorial de un número y los retorne. 

def factorial(numero:int):
    # si numero es 0 el factorial es 1. 
    #si el numero es negativo,-1
    if numero < 0:
        print("El numero no es valido")
        return -1

    # multiplicar desde el 1 hasta número y acumular el resultado.  
    acumulador = 1
    for factor in range (1,numero+1): #hay que remplazar un pass por el codigo
        acumulador = acumulador * factor #acumulador *= factor
    return acumulador 


resultado = factorial(-5)
print(resultado)