""" 5. Escuela “Aprende Más” – Promedio de notas
Como profesor, quiero una función promedio_notas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, de lo contrario “Reprobado”.
Debe repetirse para varios estudiantes usando un while. """

def promedioDeNotas():
    while True:
        try:
            nota1 = float(input("Ingresa la primera nota: "))
            nota2 = float(input("Ingresa la segunda nota: "))
            nota3 = float(input("Ingresa la tercera nota: "))

            notas = [nota1, nota2, nota3]

            promedio = sum(notas) / len(notas)

            if promedio < 3.0:
                print(f"Tu promedio es: {promedio:.1f}, Reprobado...")
            else:
                print(f"Tu promedio es: {promedio:.1f}, aprobado!")

            continuar = input("¿Calcular otro promedio? (s/n): ").lower()
            if continuar != 's':
                break

        except ValueError:
            print("Error: Por favor, ingresa solo números válidos.")

promedioDeNotas()
