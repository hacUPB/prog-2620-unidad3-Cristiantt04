# Genere una constante de texto que sera la contraseña. Luego pida al usuario que ingrese la contraseña. Mientras no sea la correcta, se deja continuar al resto del programa. 

password = "saxce8"

pasword_usuario = input("Ingresa la contraseña: ")

while pasword_usuario != password:
    print("Contraseña incorrecta")
    pasword_usuario = input("Ingresa la contraseña: ")

print("Acceso concedido!")
