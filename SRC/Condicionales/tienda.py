'''
Una tienda ofrece una promoción, por la compra de 3 articulos, el costo del elemento de menor valor tiene un descuento del 50%
'''
articulo1 = int(input("ingrese el precio del articulo 1: "))
articulo2 = int(input("ingrese el precio del articulo 2: "))
articulo3 = int(input("ingrese el precio del articulo 3: "))

if articulo1 < articulo2:
    menor = articulo1
else:
    menor = articulo2

if menor < articulo3:
    menor_definitivo = menor
else:
    menor_definitivo = articulo3 

