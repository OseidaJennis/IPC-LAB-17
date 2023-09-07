#Introducción a la programación Seccción 17
#Fecha de creación del programa: 7/09/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla los datos que le son solicitados ingresar al usuario
#Entrada: Ingresar datos personales
""""
Proceso principal
1. Solicitarle al usuario su nombre
2. Solicitarle su edad
3. Solicitar la carrera que estudia
4. Solicitar su número de carnet
"""
print("Mi segundo programa")
#Salida
sNombre=str(input("Ingrese su nombre: "))
sEdad=str(input("Ingrese su edad: "))
sCarrera=str(input("Ingrese la carrera que estudia: "))
sCarne=str(input("Ingrese su número de carnet: "))

print("Datos personales:")
print("Nombre: ", sNombre)
print("Edad: ", sEdad)
print("Carrera: ", sCarrera)
print("Carne: ", sCarne)
print("Soy",sNombre,",tengo", sEdad, "y estudio la carrera de", sCarrera,". Mi número de carnpe es;",sCarne)