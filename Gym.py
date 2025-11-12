""" 2. Gimnasio “Level Up” – Control de repeticiones
Como entrenador, quiero una función repeticiones(n) que use un bucle for para mostrar las repeticiones 
del 1 al número indicado.
Si el número actual es par, mostrar “Excelente forma”, si no, “Mantén el ritmo”.

 """

def repeticiones(n):
    for n in range(1, usuario):
        if n % 2 == 0:
            print(f"{n} Excelente forma")
        else:
            print(f"{n} Manten el ritmo")



usuario = int(input("Ingrese sus repeticiones: "))
repeticiones(usuario)

