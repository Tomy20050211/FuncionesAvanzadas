""" 9. Tienda “EnergyStore” – Simulador de puntos
Como cliente, quiero una función calcular_puntos(compras) que use un for para recorrer 
la cantidad de compras (ingresada por el usuario).
Si el número de compra es múltiplo de 3, agregar 10 puntos; en caso contrario, agregar 5.
Al final, mostrar los puntos totales. """


def calcular_puntos():
    conpras = int(input("Ingrese la cantidad de compras realizadas: "))
    suma = 0
    for i in range(1, conpras + 1 ):
        if i % 3 == 0:
            suma += 10
            print(f"Agregar 10 puntos, compra numero {i} ")
            suma
        else:
            suma += 5
            print(f"Agregar 5 puntos, compra numero {i} ")
    print(f"La cantidad de punto totales fueron: {suma}")

calcular_puntos()