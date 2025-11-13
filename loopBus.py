""" 6. Estación “LoopBus” – Simulador de pasajeros
Como conductor, quiero una función simular_viaje(pasajeros) que recorra con un 
for cada pasajero y muestre “Pasajero X a bordo”.
Si llega a 10 pasajeros, mostrar “Bus lleno” y detener el bucle. """


def simularViaje():
    for pasajero in range(0, 10):
        pasajero +=1
        print(f"Pasajero {pasajero} a bordo!")
        if pasajero == 10:
            print("Bus lleno")

simularViaje()