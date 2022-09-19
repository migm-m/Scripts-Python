"""
6. La conjetura ULAM (en honor del matemático S. Ulam) dice lo siguiente: Se
comienza con un número entero positivo; si es par, se divide entre 2, si es impar
se multiplica por 3 y se le suma 1; el resultado si es par, se divide entre 2, si es
impar se multiplica por 3 y se le suma 1 y así sucesivamente hasta llegar a 1. Por
ejemplo si el entero inicial es 26, se obtiene la siguiente serie 26, 13, 40, 20, 10, 5,
16, 8, 4, 2, 1. Construya un programa que permita leer el entero, lo valide y lo
mande a una función que muestre la serie generada.
"""

# mensaje de bienvenida
print("Programa 6 para leer un entero, validarlo y generar una serie en base de la conjetura ULAM")
print("\n")

# se define la función
def listaulam(n):
    x = n
    lista.append(x)
    if n==1:
        return lista
    else:
        while n > 1:
            if n%2==0:            
                x = x/2
                n = x
                lista.append(x)
            else:
                x = (x*3)+1
                n = x
                lista.append(x)

# se declara el input para ingresar el número
n = int(input("Ingrese el número con el quiere realizar la conjetura: "))

# el número puede ser igual o mayor que uno
while n < 1:
    n = int(input("Error, valor no válido, inténtelo de nuevo con un número entero positivo"))
lista=[]
lu=lista
listaulam(n)
print(lu)

# fin del programa
#para que no se cierre automaticamente el programa después de la ejecución
input()