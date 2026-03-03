import math
class Ejercicio2():
    def __init__(self):
        self.n = 0
        self.aprox = 0
    
    def leerDatos(self):
        self.n = int(input("n: "))
    
    def calcularFn(self):
        self.aprox = math.sqrt(2*math.pi)*math.exp(-self.n)*self.n**(self.n+1/2)
    
    #Mostrar resultados
    def mostrarResultado(self):
        print("Aproximación de n!= ",self.aprox)
