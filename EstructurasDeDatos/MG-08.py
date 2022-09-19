"""
8. Escribir una función recursiva que reciba como parámetros dos strings a y b, y 
devuelva una lista con las posiciones en donde se encuentra b dentro de a. 

"""

# mensaje de bienvenida
print("Programa 8 para encontrar las posiciones donde podemos encontrar una cadena dentro de otra")
print("\n")

# declaramos función de búsqueda
def rstring(stra,strb,pos):
    import string
    result=str.rfind(stra, strb) #rfind encuentra las incidencias leyendo una lista de atrás hacia adelante
    if result !=-1:

        stra=stra[:(result+len(strb)-1)]
        pos.append(result) # agregar incidencia al final de la lista 
        return rstring(stra,strb,pos) 
    else:
        return pos

# imprime las incidencias encontradas en una lista
cadena1 = str(input("ingresa aquí tu cadena: "))
cadena2 = str(input("ingresa la cadena 2 que se buscará en la cadena 1: "))
# se declara la lista donde se almacenaran las coincidencias de las cadenas
poslista = rstring(cadena1, cadena2,[])
poslista.reverse() # como rfind busca de atrás hacia adelante se le da un reverse a la lista para imprimirse en orden

# se imprimen los resultados en la lista final
print(poslista)


# fin del programa
#para que no se cierre automaticamente el programa después de la ejecución
input()