# Escribir un programa que lea una lista de tuplas y que devuelva un diccionario en donde 
# las claves sean los primeros elementos de las tuplas, y los valores una lista con los 
# segundos.
# Por ejemplo:
# Lista = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
# Deberá mostrar: { 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

lista_tuplas = [('Hola', 'don Pepe'), ('Hola', 'don Jose'), ('Buenas', 'tardes')]

diccionario = {}

for x, y in lista_tuplas:
    diccionario.setdefault(x, []).append(y)

print(lista_tuplas)
print(diccionario)
input()