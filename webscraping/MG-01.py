"""
1. Escriba un programa con las expresiones regulares necesarias 
para dar entrada a: una dirección IP con el formato 99.99.999.999 y muestre 
un mensaje de que es válida o no

"""
# reglas para validar una dirección ip IPv4
# debe contener 4 enteros de 0 a 255
# una dirección con más de 3 puntos (.) no es valida
# cualquier dirección con un numero mayor que 255 es inválida 
# cualquier dirección con un valor no númerico es inválida 


# importar libreria regex
import re

# pedir input para validar dirección ip
ip =input("Por favor ingrese la dirección IP a validar: ")

# regex en formato ipv4 999.999.99.99
validip = re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",ip)

# condicional para validar si la ip ingresada es valida o no e imprimir resultado
if validip:

    print("La dirección ip " + validip.group() + " es válida")

else: 
    print("Los datos ingresados no son válidos")

input()
# probando con direccion ip 187.189.69.37 
# output valido