# El Ministerio de Salud clasifica las personas según las etapas del ciclo de vida, con el fin de tener una idea sobre su vulnerabilidad. Diseñe un algoritmo que pida al usuario su edad y la clasifique según la etapa del ciclo de vida que le corresponda. Verifique que el usuario no ingrese valores menores a cero. Clasificación etaria de la población colombiana:

Edad = int(input("Ingresa tu edad: "))

if Edad >= 0 and Edad <= 130:
    if Edad < 6:
        Etapa = "Infancia"
    elif Edad < 12:
        Etapa = "Niñez"
    elif Edad < 20:
        Etapa = "Adolescencia"
    elif Edad < 25:
        Etapa = "Juventud"
    elif Edad < 60:
        Etapa = "Adultez"
    else:
        Etapa = "Ancianidad"
    print(f"A sus {Edad} años, Usted está en la {Etapa}")
else:
    print("La edad ingresa no es valida, o es un números incorrecto")
