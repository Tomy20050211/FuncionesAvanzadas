""" 1. Restaurante “Buen Sabor” – Cálculo de propina
Como mesero, quiero una función calcular_propina(total_cuenta) 
que reciba el valor total de la cuenta y calcule la propina del 10%.
Si el total es mayor de $100.000, aplicar el 15%.
El programa debe mostrar el total final a pagar. """

def calcular_propina(total_cuenta):
    if total_cuenta >= 100000:
        propina = total_cuenta * 0.15
    else:
        propina = total_cuenta * 0.10

    total_final = total_cuenta + propina
    print(f"Propina: ${propina}")
    print(f"Total a pagar: ${total_final}")

mesero = float(input("Ingresa el precio: "))
calcular_propina(mesero)

