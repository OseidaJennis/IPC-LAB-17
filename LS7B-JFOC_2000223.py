#Introducción a la programación Seccción 17
#Fecha de creación del programa: 19/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla el resultado de distintas operaciones aritméticas
#Entrada: Ingresar dos numeros, N1, N2
""""
Proceso principal
1. Solicitar al usuario que ingrese 2 números
2. Mostrar en pantalla las opciones aritméticas
2. Con los valores ingresados realizar la operación aritmética seleccionada
3. Mostrar el resultado en pantalla
"""
print("Ejercicio 2 operaciones aritméticas")
#Salida
""""
1. Suma
2. Resta
3. Multiplicación
4. División
5. Módulo
6. Exponenciación
7. Cociente
"""""
N1= int(input("Ingrese el primer número:"))
N2= int(input("Ingrese el segundo número:"))

while True:
    User=int(input("\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n5.Módulo\n6.Exponenciación\n7.Cociente\n8.Salir\nSeleccione una opción del menú: "))
    try:
        if(User==1):
            print("Operación suma:")
            print(N1,"+",N2,"=",N1+N2)
        elif(User==2):
            print("Operación resta:")
            print(N1,"-",N2,"=",N1-N2)
        elif(User==3):
            print("Operación multiplicación:")
            print(N1,"*",N2,"=",N1*N2)
        elif(User==4):
            print("Operación división:")
            print(N1,"/",N2,"=",N1/N2)
        elif(User==5):
            print("Operación módulo:")
            print(N1,"%",N2,"=",N1%N2)
        elif(User==6):
            print("Operación exponenciación:")
            print(N1,"**",N2,"=",N1**N2)
        elif(User==7):
            print("Operación cociente:")
            print(N1,"//",N2,"=",N1//N2)
        else:
            print("El número ingresado no se encuentra dentro del rango")

    except ValueError:
        print("Seleccione nuevamente un número del menú")
    accion=(input("¿Quiere seleccionar otra opción del menú? S/N:  "))
    if accion.upper() != "S":
        break
SystemExit