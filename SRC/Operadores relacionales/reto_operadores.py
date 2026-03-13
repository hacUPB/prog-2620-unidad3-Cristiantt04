edad_usuario = int(input("¿Cuál es tu edad?: "))
saldo_billetera = float(input("¿Cuál es tu saldo en cartera? "))
tiene_suscripción_premium = bool(input("¿Tienes suscripción premium? "))

edad_requerida = 17
Saldo_requerido = 60.0
Descuento = 0.1

Descuento_10 = edad_usuario > 17 and tiene_suscripción_premium 
print("Tienes un descuento especial?", Descuento_10)

Compra_completada_sindescuento = (saldo_billetera >= Saldo_requerido) and (edad_usuario >= edad_requerida)

Compra_completa_condescuento = (saldo_billetera >= Saldo_requerido) and Descuento_10

print("Compra exitosa?", Compra_completada_sindescuento)
print("Compra exitosa?", Compra_completa_condescuento)