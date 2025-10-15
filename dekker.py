def Hilo1():
    hacerMientras = False
    while (completado == False or not hacerMientras):
        hacerMientras = True
        hilo1QuiereEntrar = True

        while (hilo2QuiereEntrar == True):
            # da acceso al otro hilo
            # espera una cantidad aleatoria de tiempo
            hilo1QuiereEntrar = False

            hilo1QuiereEntrar = True
        
        # sección de entrada
        # espera hasta que el hilo2 quiera entrar
        # en su sección crítica

        # sección crítica

        # sección de salida
        # indica que el hilo1 ha completado
        # su sección crítica
        hilo1QuiereEntrar = False

        # sección de resto


def Hilo2():
    hacerMientras = False
    while (completado == False or not hacerMientras):
        hacerMientras = True
        hilo2QuiereEntrar = True

        while (hilo1QuiereEntrar == True):
            # da acceso al otro hilo
            # espera una cantidad aleatoria de tiempo
            hilo2QuiereEntrar = False

            hilo2QuiereEntrar = True
        
        # sección de entrada
        # espera hasta que el hilo1 quiera entrar
        # en su sección crítica

        # sección crítica

        # sección de salida
        # indica que el hilo2 ha completado
        # su sección crítica
        hilo2QuiereEntrar = False
