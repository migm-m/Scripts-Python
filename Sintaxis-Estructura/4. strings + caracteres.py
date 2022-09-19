# PROGRAMA 4
# Escribir un programa que permita leer una cadena de caracteres y un carácter;
# mostrar la cadena leída, inserta el caracter entre cada letra de la cadena y mostrar la cadena resultante. 
# Por ejemplo, si se dan como entrada: algoritmo y * deberá mostrar: "a*l*g*o*r*i*t*m*o"

# INICIO DEL PROGRAMA
cadena = input("Escribe la cadena: ")
caracter = input("Escribe el caracter: ")
print("La cadena original es: " + cadena)
ncadena = caracter.join(cadena[i:i + 1] for i in range(0, len(cadena), 1))
print("La cadena nueva después de agregar un caracter entre cada elemento es: " + ncadena)
input()
# FIN DEL PROGRAMA