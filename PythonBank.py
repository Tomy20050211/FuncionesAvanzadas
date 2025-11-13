""" Como asesor financiero, quiero una función evaluar_credito(ingresos, edad) que:
pruebe el crédito si los ingresos son mayores de 2 millones y la edad está entre 25 y 60.
Si no cumple, mostrar “Crédito rechazado”.
Usar condicionales dentro de la función.
 """
def evaluarCredito():
    ingresos = float(input("Ingresos: "))
    edad = int(input("Edad: "))
    if ingresos > 2000000 and 25 <= edad <= 60:
        print("Prestamo exitoso")
    else:
        print("Credito rechazado...")

evaluarCredito()