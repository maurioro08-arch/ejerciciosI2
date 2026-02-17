import math
#Lectura de datos
def leerDatos():
  a = int(input("a: "))
  b = int(input("b: "))
  c = int(input("c: "))
  return a,b,c
#Proceso de datos
def calcularX(a,b,c):
  x = (math.sqrt(b-a**2)) / (c)
  return x
#Mostrar resultados
def mostrarResultado(x):
  print("x= ",x)

def ejercicio_1():
    #Llamada a las funciones
    a,b,c = leerDatos()
    x = calcularX(a,b,c)
    mostrarResultado(x)