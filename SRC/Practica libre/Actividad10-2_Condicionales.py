Nota = float(input("Ingeresa tu nota: "))

if Nota >= 0 and Nota <= 5:
    if Nota < 2:
        Clasificación = "Terrible"
    elif Nota < 3:
        Clasificación = "Baja"
    elif Nota < 4:
        Clasificación = "Media"
    else:
        Clasificación = "Alta"
    print(f"Tu nota esta clasificada como {Clasificación}")
else:
    print("La nota es incorrecta")
