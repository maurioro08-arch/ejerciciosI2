import math
#Lectura de datos
def leerDatos():
  n = int(input("n: "))
  return n
#Proceso de datos
def calcularFn(n):
  aprox = math.sqrt(2*math.pi)*math.exp(-n)*n**(n+1/2)
  return aprox
#Mostrar resultados
def mostrarResultado(aprox):
  print("Aproximación de n!= ",aprox)

def ejercicio_2():
    #Llamada a las funciones
    n = leerDatos()
    aprox = calcularFn(n)
    mostrarResultado(aprox)