import math
class Ejercicio1():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.x = 0
        
    def leerDatos(self):
        self.a = int(input("a: "))
        self.b = int(input("b: "))
        self.c = int(input("c: "))
    
    def calcularX(self):
        self.x = (math.sqrt(self.b-self.a**2)) / (self.c)

    def mostrarResultado(self):
        print("x= ",self.x)
    
    