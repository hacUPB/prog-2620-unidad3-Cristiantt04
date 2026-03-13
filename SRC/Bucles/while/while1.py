# Solicitar dos números al usuario e imprimir los valores pares que hay entre dichos números. 

N1 = int(input("ingresa el primer número: "))
N2 = int(input("Ingresa el segundo número: "))

# Identificar al menor y al mayor entre los dos 

if N1 > N2: 
    Mayor = N1
    Menor = N2
else: 
    Mayor = N2
    Menor = N1

while Mayor >= Menor:
    Residuo = Mayor % 2 
    if Residuo == 0:
        print(Mayor)
    Mayor -= 1



