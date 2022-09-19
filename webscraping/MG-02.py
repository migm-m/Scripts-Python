"""
2. Escriba un programa con las expresiones regulares necesarias 
para dar entrada a :
Una fecha con el formato dd/mm/aaaa es válida o no, 
donde dd puede tener valores entre 1 y 30, 1 y 31, 1 y 28 o 
1 y 29 dependiendo del valor del mes que se da en mm y 
del año que se da en aaaa

"""

# importar libreria regex
import re

# pedir input para validar fecha
fecha = input("Ingresa la fecha a validar, con formato de dd/mm/aaaa pls: ")

# patrón de regex para validar fecha
patrón = re.compile(r"([0-2]\d|3[01])/(0\d|1[0-2])/([12]\d{3})")
match = patrón.search(fecha)

# condicional para validar fecha e imprimir resultados
if match:
    día = int(match.group(1))
    mes = int(match.group(2))
    año = int(match.group(3))
    print("La fecha: " + str(día)," /"+ str(mes),"/ "+str(año)," es válida")

else:
    print("La fecha ingresada no es válida, ejecute de nuevo el programa e intentelo de nuevo")

input()