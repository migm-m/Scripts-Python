# PROGRAMA 6
# Escribir un programa que, permita leer los elementos de una lista, devuelva una nueva lista 
#cuyo contenido sea igual a la original pero invertida. 


# INICIO DEL PROGRAMA 

# INPUT DE LA LISTA
lista = [] 
lista = [item for item in input("Ingresa los elementos de la lista separados por un espacio: ").split()]
print("La lista es: {}" .format(lista))
# FUNCIÓN PARA IMPRIMIR LA LISTA EN REVERSA
def Reverse(lista):
    new_lst = lista[::-1]
    return new_lst
print("La lista invertida es: {}" .format(Reverse(lista)))
input()
# FIN DEL PROGRAMA

