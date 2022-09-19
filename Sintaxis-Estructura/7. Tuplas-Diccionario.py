print("Problema 7")
print("Devuelva un diccionario conformado por los elementos y valores de la lista de tuplas dada")

lista_tuplas = [('Estructuras de datos','cadenas'), ('Estructuras de datos','listas'), ('Estructuras de datos','tuplas'), ('Estructuras de datos','python sets'), ('Estructuras de datos','dicionarios')]

print(lista_tuplas)
d = {}

for x, y in lista_tuplas:
  d.setdefault(x,[]).append(y)

print(d)
input()