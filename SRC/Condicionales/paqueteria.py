# ´´´

# Una compañía de paquetería internacional tiene servicio en algunos países según su zona. El costo por el servicio de paquetería se basa en el peso del paquete y la zona a la que va dirigido. Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados por seguridad. Usa la siguiente tabla para resolver el problema:

# ´´´

Peso_limite = 5 
Peso = float(input("Ingresa el peso de tu paquete: "))
Zona = input("Ingresa la zona a la que quieres enviar tu paquete: ")

if Peso <= 5.0:
    if  Zona == "América del Norte":
        Precio_envio = Peso * 11
    elif Zona == "América Central":
        Precio_envio = Peso * 10
    elif Zona == "América del Sur":
        Precio_envio = Peso * 12
    elif Zona == "Europa":
        Precio_envio = Peso * 24
    else:
        Precio_envio = Peso * 27
    print(f"El paquete enviado a {Zona}, el cual cuenta con un peso de {Peso}. Tendra un costo de envio igual a {Precio_envio}.")
else: 
    print("El paquete no puede ser transportado por nosotros") 
