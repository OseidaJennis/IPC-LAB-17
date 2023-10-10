#Introducción a la programación Seccción 17
#Fecha de creación del programa: 10/10/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Crear un módulo para convertir una cantidad expresada en centímetros a metros, kilómetros, pulgadas y pies.
#Entrada: Unidades de medida en cm
""""
Proceso principal
1. Solicitiar al usuario que seleccione la unidad de medida a convertir 
2. Ingresar la cantidad de centimetros a convertir 
    Si selecciona opción 1 convertirá de centimetros a metros
    Si selecciona opción 2 convertirá de centimetros a kilometros
    Si selecciona opción 2 convertirá de centimetros a pulgadas
    Si selecciona opción 2 convertirá de centimetros a pies
3. Mostrar el resultado en pantalla
4. Si selecciona opción 5 saldrá del programa
"""
print("Pensamiento computacional, S10 - Módulo de conversión de centímetros")
#Salida
#Importar el código fuente del módulo indicado
import Conversiones

while True:
    print("1.Centímetros a metros")
    print("2.Centímetros a kilómetros")
    print("3.Centímetros a pulgadas")
    print("4.Centímetros a pies")
    print("5.Salir")
    
    menu = input("Selecciona una opción: ")
    
    if menu == "1":
        cm= float(input("Ingresar la cantidad de centimetros a convertir: "))
        m= round(Conversiones.centimetrosAmetros(cm),2)
        print(cm, "centímetros equivalen a", m,  "metros")
    elif menu == "2":
        cm= float(input("Ingresar la cantidad de centimetros a convertir: "))
        km= round(Conversiones.centimetrosAkilometros(cm),2)
        print(cm,"centímetros equivalen a", km, "kilometros")
    elif menu == "3":
        cm= float(input("Ingresar la cantidad de centimetros a convertir: "))
        pulg= round(Conversiones.centimetrosApulgadas(cm),2) 
        print(cm, "centímetros equivalen a", pulg, "pulgadas")
    elif menu == "4":
        cm= float(input("Ingresar la cantidad de centimetros a convertir: "))
        ft = round(Conversiones.centimetrosApies(cm),2)
        print(cm, "centímetros equivalen a", ft, "pies")
    elif menu == "5":
        break
    else:
        print("Error, ingrese una cantidad numerica valida")
        