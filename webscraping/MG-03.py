"""
3. Escriba un programa con las expresiones regulares necesarias 
para dar entrada a 
• Una URL https://xxxxxxx.com.mx donde xxxxxxx debe tener 
máximo 15 caracteres

"""

# importar libreria regex
import re

# pedir input para validar dirección ip
url =input("Por favor ingrese la ur a validar: ")

# regex en formato ipv4 999.999.99.99
validurl = re.compile(r"^(https://)([A-z0-9\-]+)(.com.mx)$")
match = validurl.search(url)

# condicional para validar si la url ingresada es valida o no e imprimir resultado
if match:

    match.group(1)
    match.group(2)
    match.group(3)

    print("La url: " + url, " es válida")

else: 
    print("La url ingresada no es válida")

input()
