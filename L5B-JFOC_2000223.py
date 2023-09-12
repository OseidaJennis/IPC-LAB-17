#Introducción a la programación Seccción 17
#Fecha de creación del programa: 12/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla el día de la semana que coresponde al número ingresado
#Entrada: Ingresar un numero entre 1 y 7
""""
Proceso principal
1. Solicitarle al usuario ingresar un número
2. Establecer variable que evalue si el número es menor que cero o es mayor que siete
3. Si el número esta entre uno y siete la variable evaluará que día le corresponde
4. Mostrar en pantalla el resultado
"""
#Salida
print("Ejercicio 2")
#Solicitar valor numerico
Numero=int(input("Ingrese un número entre 1 y 7:"))
#Evaluar variable
if (Numero == 1):
    print(Numero, "Día:el día de hoy es lunes")
elif (Numero == 2):
    print(Numero, "Día: el día de hoy es martes")
elif (Numero == 3):
    print(Numero, "Día: el día de hoy es miércoles")
elif (Numero == 4):
    print(Numero, "Día:el día de hoy es jueves")
elif (Numero == 5):
    print(Numero, "Día:el día de hoy es viernes")
elif (Numero == 6):
    print(Numero, "Día:el día de hoy es sábado")
elif (Numero == 7):
    print(Numero, "Día:el día de hoy es domingo")

else:
    print(Numero, "Error, el número a ingresar debe estar contenido entre 1 y 7")