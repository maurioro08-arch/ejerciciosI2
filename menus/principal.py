from temas.basicos.ejercicio1 import ejercicio_1
from temas.basicos.ejercicio2 import ejercicio_2
from temas.listas.ejercicio3 import ejercicio_3
from temas.condicionales.ejercicio4 import ejercicio_4
from temas.ciclos.ejercicio5 import ejercicio_5
#   carpeta.carpeta.archivo          función
from temas.poo.clases.ejer1poo import Ejercicio1
#            carpetas archivo          clase

def menuPrincipal():
    while True:
        print(" \n\n :: Menú principal :: ")
        print("1.- Ejercicio 1")
        print("2.- Ejercicio 2")
        print("3.- Ejercicio 3")
        print("4.- Ejercicio 4")
        print("5.- Ejercicio 5")
        print("6.- Salir")
        
        op = int(input("Elija la opción deseada: "))
        print()
        match(op):
            case 1:
                #ejercicio_1()
                #crear el objeto de la clase
                e1 = Ejercicio1()
                #llamar al método a través del objeto
                e1.leerDatos()
                e1.calcularX()
                e1.mostrarResultado()
                print()
            case 2:
                ejercicio_2()
            case 3:
                ejercicio_3()
            case 4:
                ejercicio_4
            case 5:
                ejercicio_5
            case 6:
                print("Hasta pronto")
                break
            case _:
                print("opción no válida")
            
        