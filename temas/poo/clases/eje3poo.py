class Ejercicio3():
    def __init__(self):
        self.lista = 0
    def mostrarIndices(self):
        self.lista = [1,2,3,[9,8,7,[6,5,4]]]
        #Para recuperar el valor 2
        print(self.lista[1])
        print(self.lista[3][1])
        print(self.lista[3][3][2])
        print(self.lista[-1][-1][-1]) # índices negativos
    
