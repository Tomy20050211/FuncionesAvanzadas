""" 3. Tienda “LoopShop” – Descuentos acumulados
Como vendedor, quiero una función aplicar_descuentos() que pida varios precios hasta que el usuario escriba 0.
Si el precio supera 50.000, aplicar 10% de descuento.
Al final, mostrar la suma total de las compras con descuento. """

def aplicar_descuentos():
    total_con_descuento = 0  
    descuento = 0.10

    while True:
        precio = float(input("Ingrese el precio del producto (0 para terminar): "))

        if precio == 0:
            break  

        if precio > 50000:
            precio_final = precio - (precio * descuento)
            print(f"Se aplicó un 10% de descuento. Precio final: ${precio_final:.2f}")
        else:
            precio_final = precio
            print(f"No se aplicó descuento. Precio final: ${precio_final:.2f}")

        # acumular el precio con descuento
        total_con_descuento += precio_final

    print(f"Total a pagar por todas las compras: ${total_con_descuento:.2f}")



aplicar_descuentos()
