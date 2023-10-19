#Introducción a la programación Seccción 17
#Fecha de creación del programa: 19/10/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla las primeras tres letras de la cadena ingresada por el usuario
#Entrada: Soicitarle al usuario que ingrese una palabra
""""
Proceso principal
1. Solicitarle al usuario ingresar una palabra, de una en una
2. Ir almacenando las letras una a una en una variable nueva tipo cadena
3. Mostrar la nueva sub-cadena 
4. Solicitarle al usuario un nuevo texto
5. El texto será almacenado en una variabe tipo cadena
6. Recorrerá la variable tipo texto carácter a carácter
7. Sustituir las vocales "o" del texto por "x"
8. Mostrar en pantalla el nuevo texto que se formo
9. Investigar dos funciones con las que cuenta Pythin para el manejo de cadenas
"""
#Salida
Palabra = input("Ingrese una palabra: ")

Primerastresletras = Palabra[:3]
print("Las primeras tres letras de la palabra son:", Primerastresletras)

NuevaSubcadena = ""
for letra in Primerastresletras:
    NuevaSubcadena += letra
print("La nueva subcadena formada por las primeras tres letras es:", NuevaSubcadena)

texto = input("Ingrese un nuevo texto: ")

TextoModificado = ""
for letra in texto:
    if letra == 'O' or letra == 'o':
        TextoModificado += 'x'
    else:
        TextoModificado += letra

print("El nuevo texto con la vocal 'O' sustituidas por 'x' es:", TextoModificado)

# Funciones de manejo de cadenas en Python

# Función str.replace():
# Funcionamiento: Se utiliza para reemplazar todas las ocurrencias de una subcadena específica en una cadena con otra subcadena. Acepta dos argumentos, el primero es la subcadena que se va a reemplazar, y el segundo es la subcadena con la que se va a reemplazar.

# Función str.split():
# Funcionamiento: La función str.split() se utiliza para dividir una cadena en una lista de subcadenas utilizando un carácter o una secuencia de caracteres como separador. Puede tomar un argumento opcional para especificar el separador, y si no se proporciona, se utilizará el espacio en blanco como separador de forma predeterminada.