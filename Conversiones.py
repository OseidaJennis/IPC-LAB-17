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

#Convertir de cm a m
def centimetrosAmetros(centimetros):
    metros = centimetros / 100
    return metros

#Convertir de cm a km
def centimetrosAkilometros(centimetros):
    kilometros = centimetros / 100000
    return kilometros

#Convertir de cm a pulg
def centimetrosApulgadas(centimetros):
    pulgadas = centimetros *0.393701
    return pulgadas

#Convertir de cm a ft
def centimetrosApies(centimetros):
    pies = centimetros *0.0328084
    return pies