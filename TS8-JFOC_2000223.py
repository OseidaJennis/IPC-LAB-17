#Introducción a la programación Seccción 17
#Fecha de creación del programa: 28/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Utilizando FOR Y WHILE mostrar la secuencia de ciertos rangos establecidos
#Entrada: Mostrar la secuencia de numeros en distinto orden
""""
Proceso principal
1. Secuencia de numeros en un rango de 1- 25, incrementando de 1 en 1 utilizando FOR
2. Secuencia de numeros en un rango de 1 - 25, incrementando de 1 en 1 utilizando WHILE
3. Secuencia de numeros en un rango de 5 - 50, incrementando de 5 en 5 utilizando FOR
4. Secuencia de numeros en un rango de 5 - 50, incrementando de 5 en 5 utilizando WHILW
5. Secuencia de numeros en un rango de 20 - 0, decrementando de 2 en 2 utilizando FOR
6. Secuencia de numeros en un rango de 20 - 0, decrementando de 2 en 2 utilizando WHILE
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
