"""
5. Escribir un programa que reciba una expresión y un archivo de 
texto e imprima las líneas del archivo que contienen la expresión 
recibida


"""


# importar libreria para abrir archivos de texto
from io import open

# importar librería de regex
import re

# abrir el archivo en modo read 
archivo = open(r'hopeurok.txt','r', encoding= "utf-8")

# variable donde se van a guardar los datos del archivo cuando se lean
archivo_txt = archivo.read()

# imprimir en pantalla el contenido del archivo
print(archivo_txt)

# abrir el archivo en modo read 
archivo = open(r'hopeurok.txt','r', encoding= "utf-8")

# ingresar expresión a buscar en el texto
expresion=input("Ingresa el texto a buscar en el archivo: ")

# buscar la expresión ingresada en el contenido del archivo de texto 
match = 0
match_texto=re.compile(expresion)
for match in archivo:
    if match_texto.search(match):
        print("Se encontró la siguiente coincidencia en el texto: " + match)

# se hace un contador para saber el número de coincidencias en el archivo de texto
for match in archivo:
    match  = match + 1
    print(match)

input()