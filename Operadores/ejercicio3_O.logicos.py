promedio = float(input("¿Cuál es tu promedio acádemico?: "))
Nivel_economico = int(input("¿Cuál es tu nivel economico?: "))
Beca = promedio >= 9.0 or (Nivel_economico == 1 and promedio > 8.0)
print("¿Tienes la beca?" ,Beca)
