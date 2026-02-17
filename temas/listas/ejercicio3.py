def mostrarIndices():
    lista = [1,2,3,[9,8,7,[6,5,4]]]
    #Para recuperar el valor 2
    print(lista[1])
    print(lista[3][1])
    print(lista[3][3][2])
    print(lista[-1][-1][-1]) # índices negativos
    
def ejercicio_3():
    #Llamada a la funcion
    mostrarIndices()