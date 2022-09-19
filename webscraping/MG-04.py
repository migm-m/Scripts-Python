"""
4. Escribe una (o mas) expresión regular para 
obtener la fecha, hora y el usuario (si lo muestra) 
de los intentos de logeo de un sistema Linux (si 
tienes un sistema Linux, el archivo auth.log lo 
encuentras en /var/log)

"""

import re
from io import open

fecha=re.compile(r"(\w{3} )([12][0-9]|3[01]| [0-9])")
hora=re.compile(r"([01][1-9]|2[0-3])(:)([0-5][0-9])(:)([0-5][0-9])")
usuarios=re.compile(r"user=\w+")
users=list()
authlog=open(r"C:\Users\mariel\Documents\UANL\2\2._Introducción_a_la_Programación\Programas\3er_Parcial\1_lab\mariel\bitacora.txt", "r", encoding = "utf-8")
c=0
for linea in authlog:       
    linea=linea.rstrip("\\n")
    u=usuarios.findall(linea)
    if u!="None":   
        users.append(u)
        c=c+1
    else:
        users.append(" ")
authlog.close()
authlog=open(r"C:\Users\mariel\Documents\UANL\2\2._Introducción_a_la_Programación\Programas\3er_Parcial\1_lab\mariel\bitacora.txt", "r", encoding = "utf-8")
logs=authlog.read()
dates=fecha.findall(logs)
hours=hora.findall(logs)
c=len(dates)
for i in range (0,c):
    print("fecha: ",dates[i]," hora: ",hours[i]," ",users[i])
authlog.close()
