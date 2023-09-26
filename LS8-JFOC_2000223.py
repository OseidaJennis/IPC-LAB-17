#Introducción a la programación Seccción 17
#Fecha de creación del programa: 26/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla el resultado factorial y la secuencia de ficonacci de cualquier número
#Entrada: Seleccionar una opción del menú
""""
Proceso principal
1. Solicitiar al usuario que ingrese un número del apartado menú 
2. Ejecutar el programa
    Si selecciona opción 1 mostrará una solución factorial
    Si selecciona opción 2 mostrará la secuencia de fibonacci del número ingresado
3. Mostrar el resultado en pantalla
4. Si selecciona opción 3 saldrá del programa
"""
print("Pensamiento computacional, S8")
#Salida

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

def fibonacci(numero):
    if numero <= 0:
        return []
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, numero):
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence

while True:
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    opcion = int(input("Ingrese el número del menú que quiere ejecutar: "))

    if opcion == 1:
        numero = int(input("Ingrese un número para calcular su factorial: "))
        resultado = factorial(numero)
        print(f"{numero}! = {resultado}")
    elif opcion == 2:
        numero = int(input("Ingrese un número para mostrar la secuencia de Fibonacci: "))
        secuencia = fibonacci(numero)
        print(",".join(map(str, secuencia)), f"... Fibonacci ({numero})")
    elif opcion == 3:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")

    input("Presione Enter para continuar")
