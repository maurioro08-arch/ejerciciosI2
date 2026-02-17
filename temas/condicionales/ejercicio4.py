def leerDatos():
  a = int(input("a: ")) #entrada de datos o lectura de datos
  b = int(input("b: "))
  c = int(input("c: "))
  return a,b,c

def analizarDatos(a,b,c):
  d = b**2 - 4 * a * c
  if d > 0:
    mensaje="la gráfica es una hipérbola"
  if d == 0:
    if a == 0 and c == 0:
      mensaje="la gráfica es una recta"
    else:
      mensaje="la gráfica es una parábola"
  if d < 0:
    if a == c:
      mensaje="la gráfica es una cicunferencia"
    else:
      mensaje="la gráfica es una elipse"
  return mensaje
def mostrarMensaje(mensaje):
  print(mensaje)

def ejercicio_4():
    #LLamadas a las funciones
    a,b,c = leerDatos()
    mensaje = analizarDatos(a,b,c)
    mostrarMensaje(mensaje)