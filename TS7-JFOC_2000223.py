#Introducción a la programación Seccción 17
#Fecha de creación del programa: 21/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla la tabla de multiplicar del número indicado por el usuario
#Entrada: Ingresar un número entre 1 a 10
""""
Proceso principal
1. Solicitar al usuario que ingrese su nombre completo
2. Pedirle al usuario que ingrese un número entre 1 a 10
3. Verificar que este dentro del rango correcto
4. Mostrar en pantalla la tabla de multiplicar del número ingresado
5. Preguntar al usuario si desea reiniciar el programa
6. Opcion salir 
"""
print("Ejercicio Tablas de multiplicar")

#Salida
sNombre=str(input("Ingrese su nombre: "))

while True:
    N1 = int(input("Ingresa un número entre 1 y 10: "))
    if 1 <= N1 <= 10:
        for i in range(1, 11):
            resultado = N1 * i
            print(f"{N1} X {i} = {resultado}")
        
        Solución = input("¿Deseas generar la tabla de multiplicar de otro número?")
        Solución = input ("Escriba: SALIR para salir del programa): ")
        if Solución.upper() == "SALIR":
            break
    else:
        print("El número ingresado no está dentro del rango, ingrese otro número.")
