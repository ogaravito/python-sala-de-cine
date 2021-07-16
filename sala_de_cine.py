"""
Programa que permite reservar asientos de una sala de cine (8 filas x 10 columnas). 
La posición de cada asiento se definirá con una letra (A-H) para la fila y un número (1-10) para la columna. 
El program muestra qué sitios están disponibles para que el cliente pueda decidir dónde sentarse. 
Antes de hacer la reserva, el programa comprueba que el asiento está libre, en caso contrario devolverá un mensaje.
"""
import cine
import time

opcion = ''
sillas = cine.iniciar_sala()
cine.limpiar_pantalla()
sillas_reservadas=[]

with open('data.txt', 'r') as f:
    sillas_reservadas = [ silla_reservada.strip('\n') for silla_reservada in f ]

while opcion != 'N':

    opcion = input("Desea reservar (s/n) ").upper()

    if opcion == 'S':

        cine.mostrar_sillas(sillas, sillas_reservadas)
        silla_deseada=input('Ingrese la silla que desea reservar: ').upper()
        existe = False

        for i in range(len(sillas)):
            for j in range(len(sillas[i])):
                if silla_deseada in sillas_reservadas:
                    existe = True
                    print("La silla está reservada")
                    time.sleep(2)               
                    break
                elif sillas[i][j] == silla_deseada:
                    existe = True
                    sillas_reservadas.append(silla_deseada)
                    with open("data.txt", "a+") as f:
                        f.write(silla_deseada+'\n')
                    print("Reserva exitosa")
                    time.sleep(2)
                    break
            if existe==True:
                break

        if existe==False:
            print('La silla NO existe')
            time.sleep(2)

        cine.mostrar_sillas(sillas, sillas_reservadas)

    elif  opcion == 'N':
        print('GRACIAS')
    else:
        print('Opción no encontrada')
