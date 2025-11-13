""" 7. Panadería “Don Pancho” – Control de producción diaria
Como panadero, quiero una función hornear_pan(lotes) que use un for
para indicar qué lote se está horneando.
Si el lote es divisible por 3, mostrar “Verificación de calidad”.
Al final, mostrar “Producción terminada”. """

def hornearPan():
    panadero = int(input("Ingrese el lote: "))
    for panes in range (1, panadero):
        panes +=1
        print(f"numero de panes: {panes}")
        if panes % 3 == 0:
            print("Verificacion de calidad")
   
        elif panes == panadero:
            print("Producción terminada")
hornearPan()