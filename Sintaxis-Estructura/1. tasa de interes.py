# PROBLEMA 1
# Escribir un programa que le pregunte al usuario una cantidad de dinero en pesos
# (asegurarse que sea válido), una tasa de interés (asegurarse que sea válido) y un número 
# de años (asegurarse que sea válido) y muestre como resultado el monto final a obtener. 
# Utilice la siguiente fórmula:
# Cn = C * (1 + x/100) ^ n
# Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

# INICIO DEL PROGRAMA
c = int(input("Ingresa la cantidad de dinero "))
if c > 0:
    tasa = int(input("Ingresa la tasa de interés "))
    if tasa > 0:
        años = int(input("Ingresa la cantidad de años a calcular "))
        if años > 0:
            cn = c * (1 + float(tasa) / 100) ** años
            print(cn)
        else:
            print("valor inválido, ejecuta de nuevo el programa e inténtalo de nuevo")
    else:
        print("valor inválido, ejecuta de nuevo el programa e inténtalo de nuevo")
else:
    print("valor inválido, ejecuta de nuevo el programa e inténtalo de nuevo")
input()    
# FIN DEL PROGRAMA