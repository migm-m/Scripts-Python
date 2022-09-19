# PROBLEMA 3
# Implementar en un programa en Python el algoritmo de Euclides para calcular el máximo 
# común divisor de dos números a y b

#INICIO DEL PROGRAMA
a = int(input("Ingresa el primer número "))
if a > 0:
    b = int(input("Ingresa el segundo número "))
    if b > 0:
        while b > 0:
            temp = b
            b = a % b
            a = temp
        print("El máximo común divisor de los números es {}" .format(a))
    else:
        print("Valores inválidos, ejecute de nuevo e ingrese un número mayor a 0.")
else:
    print("Valores inválidos, ejecute de nuevo e ingrese un número mayor a 0.")
input()
#FIN DEL PROGRAMA