#Introducción a la programación Seccción 17
#Fecha de creación del programa: 24/10/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Mostrar en pantalla la administración de una lista de contactos
#Entrada: Ingresar el nombre y numero telefonico de los contactos deseados por el usuario
""""
Proceso principal
1. Declarar una variable tipo lista
2. El usuario ingresara la cantidad de contactos que desea agregar a la lista
3. El usuario ingresara el nombre y numero telefonico de cada contacto
4. Mostrar en pantalla la lista de contactos final
5. Brindarle la opcion al usuario de poder eliminar cualquier contacto de la lista
6. Ordenar la lista de conctactos alfabeticamente
7. Tener la opcion de agregar un contacto, en el cual se almacene el nombre en mayusculas
8. Mostrar la lista de conctactos actualizada
9. Crear una copua de la lista de contactos original ordenada alfabeticamente de forma descendente 
10. Mostrar en pantalla la lista de contactos original y la ordenada
"""
#Salida
ListaContactos = []
n = int(input("Ingrese la cantidad de contactos que va a agregar: "))

for i in range(n):
    Nombre = input("Ingrese el nombre del contacto: ")
    Numero = input("Ingrese el número de teléfono del contacto: ")
    Contacto = [Nombre, Numero]
    ListaContactos.append(Contacto)

print("Lista de contactos completa:")
for contacto in ListaContactos:
    print(contacto)

nombre_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
for contacto in ListaContactos:
    if contacto[0] == nombre_eliminar:
        ListaContactos.remove(contacto)
        break

print("Lista de contactos actualizada:")
for contacto in ListaContactos:
    print(contacto)

ListaContactos.sort()

nombre_nuevo = input("Ingrese el nombre del nuevo contacto en mayúsculas: ")
numero_nuevo = input("Ingrese el número de teléfono del nuevo contacto: ")
nuevo_contacto = [nombre_nuevo.upper(), numero_nuevo]
ListaContactos.append(nuevo_contacto)

print("Lista de contactos ordenada alfabéticamente:")
for contacto in ListaContactos:
    print(contacto)

posicion = int(input("Ingrese la posición donde desea agregar un nuevo contacto: "))
nombre_nuevo = input("Ingrese el nombre del nuevo contacto: ")
numero_nuevo = input("Ingrese el número de teléfono del nuevo contacto: ")
nuevo_contacto = [nombre_nuevo, numero_nuevo]
ListaContactos.insert(posicion, nuevo_contacto)

print("Lista de contactos completa:")
for contacto in ListaContactos:
    print(contacto)

copia_lista = ListaContactos.copy()
copia_lista.sort(reverse=True)

print("Lista ordenada de forma descendente:")
for contacto in copia_lista:
    print(contacto)

print("Lista original:")
for contacto in ListaContactos:
    print(contacto)