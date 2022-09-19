"""
9. Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia 
de b. Ejemplos:

"""

# mensaje de bienvenida
print("Programa 9 para saber valide si dados 2 números ingresados el primero es potencia del segundo")
print("\n")

# se define la función con la cual se harán las operaciones
def pwrn(n, b):
  while n % b == 0: 
    n = n / b
  if n == 1:
    return True
  return False

# input para pedir los números que se van a validar
n = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
print(pwrn(n,b))
print("El número",n, "si es potencia de ", b)

#para que no se cierre automaticamente el programa después de la ejecución
input()

