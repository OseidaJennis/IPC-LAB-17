#Introducción a la programación Seccción 17
#Fecha de creación del programa: 07/11/2023
#Autor: Jennifer Oseida Castillo
#Objetivo: Definir un método constructor donde se establezcan los atributos con valores por defecto 
#Entrada: Crear clase que contenga atributos y metodos 
""""
Proceso principal
1. Crear una clase que contenga los atributos solicitados 
2. Definir un método constructor 
3. Definir los metodos solicitados
"""
print("Pensamiento computacional, S14")
#Salida
class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = True
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 5

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Si se encuentra disponible"
        else:
            return "En este momento no se encunetra disponible"

    def MostrarInformacion(self):
        PrecioEnDolares = self.precio / self.tipoCambioDolar
        return f"Marca del auto: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares: ${PrecioEnDolares}. Disponiblidad {self.MostrarDisponibilidad()}"

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        self.precio -= miDescuento
        self.DefinirPrecio(self.precio)

auto = Automovil()
auto.DefinirModelo(2020)
auto.DefinirPrecio(35000.0)
auto.DefinirMarca("BMW")
auto.DefinirTipoCambio(7.94)
print(auto.MostrarInformacion())
auto.CambiarDisponibilidad()
print(auto.MostrarInformacion())
auto.AplicarDescuento(1000.0)
print(auto.MostrarInformacion())