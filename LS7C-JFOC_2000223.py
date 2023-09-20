#Introducción a la programación Seccción 17
#Fecha de creación del programa: 19/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla el resultado de distintas operaciones aritméticas
#Entrada: Ingresar dos numeros, N1, N2
""""
Proceso principal
1. Solicitar al usuario que ingrese 3 números
2. Con los valores ingresados mostrar el resultado de las expresiones en pantalla
"""
print("Ejercicio 3 Jerarquía de operaciones")

#Salida
N1= int(input("Ingrese el primer número:"))
N2= int(input("Ingrese el segundo número:"))
N3= int(input("Ingrese el tercer número:"))

print("A.""\n", N1*N2+N3)
print("B.""\n", N1*(N2+N3))
print("C.""\n", (N1)/(N2*N3))
print("D.""\n", (3*N1+2*N2)/(N3**2))

SystemExit