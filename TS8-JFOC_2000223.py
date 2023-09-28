#Introducción a la programación Seccción 17
#Fecha de creación del programa: 28/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Utilizando FOR Y WHILE mostrar la secuencia de ciertos rangos establecidos
#Entrada: Mostrar la secuencia de numeros en distinto orden
""""
Proceso principal
1. Solicitiar al usuario que ingrese un número del apartado menú 
2. Ejecutar el programa
    Si selecciona opción 1 mostrará una solución factorial
    Si selecciona opción 2 mostrará la secuencia de fibonacci del número ingresado
3. Mostrar el resultado en pantalla
4. Si selecciona opción 3 saldrá del programa
"""
print("Uso ciclos FOR Y WHILE")
#Salida
print("Secuencia de numeros en un rango de 1- 25, incrementando de 1 en 1 utilizando FOR")
for i in range(1, 26):
    print(i)
i = 1

print("Secuencia de numeros en un rango de 1 - 25, incrementando de 1 en 1 utilizando WHILE")
while i <= 25:
    print(i)
    i += 1

print("Secuencia de numeros en un rango de 5 - 50, incrementando de 5 en 5 utilizando FOR")
for i in range(5, 51, 5):
    print(i)

print("Secuencia de numeros en un rango de 5 - 50, incrementando de 5 en 5 utilizando WHILW")
i = 5
while i <= 50:
    print(i)
    i += 5

print("Secuencia de numeros en un rango de 20 - 0, decrementando de 2 en 2 utilizando FOR")
for i in range(20, -2, -2):
    print(i)
i = 20

print("Secuencia de numeros en un rango de 20 - 0, decrementando de 2 en 2 utilizando WHILE")
while i >= 0:
    print(i)
    i -= 2