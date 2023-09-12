#Introducción a la programación Seccción 17
#Fecha de creación del programa: 12/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla si una variable es positiva, negativa o si es cero
#Entrada: Ingresar un numero entero
""""
Proceso principal
1. Solicitarle al usuario ingresar un número entero
2. Almacenar el dato ingresado dentro de una variable
3. Agregar código para evaluar la variable
4. Mostrar en pantalla el resultado
"""
#Salida
print("Ejercicio 1")
#Solicitar valor numerico
try:
    Numero=int(input("Ingrese un número entero:"))

    #Evaluar variable
    if (Numero > 0):
        print(Numero, "Es un número positivo")
    elif (Numero < 0):
        print(Numero, "Es un número negativo")
    else:
        print(Numero, "El número es 0")

except ValueError:
    print("Eroror, el valor ingresado no es un número")