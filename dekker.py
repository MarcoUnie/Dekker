import threading
import time
import random

# Variables compartidas (globales)
hilo1QuiereEntrar = False
hilo2QuiereEntrar = False
completado = False

# Variable compartida simulando un recurso crítico
contador_compartido = 0

def Hilo1():
    global hilo1QuiereEntrar, hilo2QuiereEntrar, completado, contador_compartido
    hacerMientras = False

    while (not completado or not hacerMientras):
        hacerMientras = True
        hilo1QuiereEntrar = True

        while hilo2QuiereEntrar:
            hilo1QuiereEntrar = False
            time.sleep(random.uniform(0.1, 0.3))
            hilo1QuiereEntrar = True

        # Sección crítica
        print(" Hilo 1 entra a la sección crítica")
        valor = contador_compartido
        time.sleep(random.uniform(0.1, 0.2))  # Simula trabajo
        contador_compartido = valor + 1
        print(" Hilo 1 sale de la sección crítica. Contador =", contador_compartido)

        # Sección de salida
        hilo1QuiereEntrar = False

        # Sección de resto
        time.sleep(random.uniform(0.2, 0.4))

        if contador_compartido >= 10:
            completado = True
            break


def Hilo2():
    global hilo1QuiereEntrar, hilo2QuiereEntrar, completado, contador_compartido
    hacerMientras = False

    while (not completado or not hacerMientras):
        hacerMientras = True
        hilo2QuiereEntrar = True

        while hilo1QuiereEntrar:
            hilo2QuiereEntrar = False
            time.sleep(random.uniform(0.1, 0.3))
            hilo2QuiereEntrar = True

        # Sección crítica
        print(" Hilo 2 entra a la sección crítica")
        valor = contador_compartido
        time.sleep(random.uniform(0.1, 0.2))
        contador_compartido = valor + 1
        print(" Hilo 2 sale de la sección crítica. Contador =", contador_compartido)

        # Sección de salida
        hilo2QuiereEntrar = False

        # Sección de resto
        time.sleep(random.uniform(0.2, 0.4))

        if contador_compartido >= 10:
            completado = True
            break


# Crear los hilos
t1 = threading.Thread(target=Hilo1)
t2 = threading.Thread(target=Hilo2)

# Iniciar los hilos
t1.start()
t2.start()

# Esperar a que terminen
t1.join()
t2.join()

