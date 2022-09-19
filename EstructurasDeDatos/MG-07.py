"""
7. Escribir una función recursiva para replicar los elementos de una lista una 
cantidad n de veces. Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])

"""

# mensaje de bienvenida
print("Programa 7 para replicar los elementos de una lista una cierta cantidad de veces")
print("\n")

# se define la función que replica los elementos de la lista un numero r de veces
def numrep (x,y):  # x = lista, y = r (numero de veces que se repiten los elementos)
    listarep = []
    for i in range (len(x)): # len checa la longitud de la lista "lista"
        for j in range (y):
            listarep.append(x[i])
    return listarep

# declaramos la lista vacía
lista = []

# declaramos el número de elementos que va a contener nuestra lista
n = int(input("Ingresa cuantos elementos tene la lista: "))  

# usamos un ciclo for para pedir cada valor de la lista
for i in range(0, n):
    print("Ingresa valor:", i+1) 
    e = input()
    lista.append(e)
# se imprime la lista resultante de los elementos que el usuario ingresó
print("La lista es: {}" .format(lista))


# pedimos el numero de veces que los elementos se repiten en la lita
r = int(input("Ingresa el número de veces que se repiten los elementos de la lista: ")) 

# se imprimen los resultados en una lista final
print("La nueva lista es:")
print(numrep(lista,r))

# fin del programa
# para que no se cierre automaticamente el programa después de la ejecución ponemos input()
input()