"""
4. Escribir un programa con una función que reciba como parámetro 
un número natural, y devuelva y muestre True si el número es una 
potencia de 2, y False en caso contrario.
"""

# mensaje de bienvenida
print("Programa 4 para saber si un número es potencia de 2 o no")
print("\n")

# función con condicional para validar si un número es potencia de 2 
def pwr2(n):
        return n > 0 and (n & (n - 1)) == 0
        
# código para pedir introducir el número a válidar
num = int(input("Ingrese el número a validar:  "))

# imprime resultado
print(pwr2(num))
print("El número",num, "si es potencia de 2")

#para que no se cierre automaticamente el programa después de la ejecución
input()

