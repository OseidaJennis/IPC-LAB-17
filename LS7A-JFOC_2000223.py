#Introducción a la programación Seccción 17
#Fecha de creación del programa: 19/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla el resultado de distintas operaciones aritméticas
#Entrada: Ingresar dos numeros, N1, N2
""""
Proceso principal
1. Solicitar al usuario que ingrese 2 números
2. Con los valores ingresados realizar todas las operaciones básicas
3. Mostrar el resultado en pantalla
"""
print("Ejercicio 1 operaciones aritméticas")
#Salida
N1= int(input("Ingrese el primer número:"))
N2= int(input("Ingrese el segundo número:"))

#Operaciones y resultados
print("Operación suma:")
print(N1,"+",N2,"=",N1+N2)

print("Operación resta:")
print(N1,"-",N2,"=",N1-N2)

print("Operación multiplicación:")
print(N1,"*",N2,"=",N1*N2)

print("Operación división:")
print(N1,"/",N2,"=",N1/N2)

print("Operación módulo:")
print(N1,"%",N2,"=",N1%N2)

print("Operación exponenciación:")
print(N1,"**",N2,"=",N1**N2)

print("Operación cociente:")
print(N1,"//",N2,"=",N1//N2)

SystemExit