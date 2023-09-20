#Introducción a la programación Seccción 17
#Fecha de creación del programa: 19/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla el resultado de distintas operaciones aritméticas
#Entrada: Ingresar dos numeros, N1, N2
""""
Proceso principal
1. Solicitar al usuario que ingrese 3 números
2. Con los valores ingresados calcular el resultado de ellos utilizando la formúla cuadrática
3. Mostrar el resultado en pantalla
"""
print("Ejercicio 3 Jerarquía de operaciones")

#Salida

import math
import os
while True:
    os.system('cls')
    N1= int(input("Ingrese (A) número:"))
    N2= int(input("Ingrese (B) número:"))
    N3= int(input("Ingrese (C) número:"))

    User=int(input("\n1. a*b+c\n2. a*(b+c)\n3. a/(b*c)\n4. (3a + 2b)/c^2\n5. Formúla cuadrática\n6. Salir\nSeleccione una opción del menú:"))
    try:
        if(User==1):
            print("Primera operación: ", N1*N2+N3)
        elif(User==2):
            print("Segunda operación: ", N1*(N2+N3))
        elif(User==3):
            print("Tercera operación: ", (N1)/(N2*N3))
        elif(User==4):
            try:
                print("Cuarta operación: ", (3*N1+2*N2)/(N3**2))
            except ZeroDivisionError:
                print("Error")
        elif(User==5):
            try:
                print("Por formúla cuadrática")
                discriminante =  N1**2 - 4 * N1 * N3
                if discriminante < 0:
                    print("No tiene solución")
                else:    
                    Solución1 = (-N1 + math.sqrt(discriminante)) / (2 * N1)
                    if(discriminante != 0):
                        Solución2 = (-N1 - math.sqrt(discriminante)) / (2 * N1)
                        print("\nSolución 1: ", Solución1)
                        print("Solución 2: ", Solución2)
                    else:
                        print("\nSolución unica: ", Solución1)
            except ZeroDivisionError:
                print("Error")
        elif(User==6):
            break
        else:
            print("El número ingresado no esta dentro del rango")
    except ValueError:
        print("Error, el número ingresado no es valor numerico")
    bucle=input("\n\n¿Desea realizar otra operacion? S/N:  ")
    if bucle.upper() != "S":
        exit()