# Escribir un programa que permita leer una frase u oración y un carácter; mostrar la frase u 
#oración leída, reemplazar los espacios en blanco por el caracter y mostrar la frase u 
#La*clase*de*Introducción*a*la*Programación*es*a*las*6*p.m.

frase = input ("Escribe una frase u oracion:")
espacio = (" ")
caracter = input("Ingresa el caracter para sustituir por los espacios:")
for space in espacio:
 frase = frase.replace(space,caracter)
print(frase)
input()