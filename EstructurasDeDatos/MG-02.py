"""
2. Escribir un programa que pida al usuario un número entero positivo (asegúrese 
que sea entero positivo) y lo mande a una función para que muestre por pantalla un 
triángulo rectángulo como el ejemplo.
Ejemplo: Si se ingresa un 5, el resultado sería el siguiente:
1 
2 1
3 2 1
4 3 2 1 
5 4 3 2 1
"""

# mensaje de bienvenida
print("Programa 2 para imprimir una función que transforme un número en un triángulo rectángulo")
print("\n")

# input de número a trabajar
n = int(input("Ingresa el número: "))

# validar que el número sea mayor a 0, si es menor a 0 lo vuelve a pedir
while n <=0:
    n = int(input("Número no valido, intenta de nuevo ingresa un número mayor a 0: "))

# se crea una función para almacenar los datos
def tr(n):
    # se hace un ciclo para imprimir los valores en el triángulo rectángulo
    for i in range(1, n+1): 
        for j in range(i, 0, -1): 
            print(j, end=" ")   
        print("") 
tr(n)

#para que no se cierre automaticamente el programa después de la ejecución
input()