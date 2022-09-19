"""
3. Escribir un programa con una función que reciba cuatro números 
enteros y devuelva el mayor producto de dos de ellos para que sea 
mostrado. Por ejemplo, si recibe los números 1, 5, -2, -4 debe 
devolver y mostrar 8, que es el producto más grande que se puede 
obtener entre ellos.
"""

# mensaje de bienvenida
print("Programa 3 para obtener el producto más grande dados los elementos de una lista")
print("\n")

# código para pedir el input para la lista
lista = [] # declara lista vacía
for i in range(0, 4): # loop para hacer la lista con 4 elementos
    l = int(input("Ingrese un número: "))
    lista.append(l)
  
# imprime la lista ingresada
print("Los números ingresados son: ",lista)
  
# hacer operaciones para obtener el producto mayor  
pm = max(int(x) * int(y) for x, y in zip(lista, lista[1:]))
  
# imprime resultado 
print("El producto mayor es: " + str(pm))

#para que no se cierre automaticamente el programa después de la ejecución
input()