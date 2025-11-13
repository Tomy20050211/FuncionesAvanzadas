""" 8. Cine “MovieLoop” – Calculadora de entradas
Como cajero, quiero una función calcular_entradas() que pida edades de 
los clientes hasta que se ingrese 0.
Aplicar precio:

    Menores de 12 → $5.000
    De 12 a 59 → $8.000
    Mayores de 60 → $4.000
    Usar un while y condiciones.

 """

def calcularEntradas():
    while True:
        edad = int(input("Ingrese su edad:"))
        if  0< edad < 12:
            print("Paga 5 lukas")
        elif 12 <= edad <= 59:
            print("Paga 8 lukitas")
        elif edad > 60:
            print("paga 4 lukititas")
        elif edad == 0:
            print("Saliendo del programa")
            break
            
calcularEntradas()
