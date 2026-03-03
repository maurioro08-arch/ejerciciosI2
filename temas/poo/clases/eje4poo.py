class Ejercicio4():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.mensaje = 0
    def leerDatos(self):
        self.a = int(input("a: ")) #entrada de datos o lectura de datos
        self.b = int(input("b: "))
        self.c = int(input("c: "))
    
    def analizarDatos(self):
        self.d = self.b**2 - 4 * self.a * self.c
        if self.d > 0:
            self.mensaje="la gráfica es una hipérbola"
        if self.d == 0:
            if self.a == 0 and self.c == 0:
                self.mensaje="la gráfica es una recta"
        else:
            self.mensaje="la gráfica es una parábola"
        if self.d < 0:
            if self.a == self.c:
                self.mensaje="la gráfica es una cicunferencia"
        else:
            self.mensaje="la gráfica es una elipse"
    
    def mostrarMensaje(self):
        print(self.mensaje)
