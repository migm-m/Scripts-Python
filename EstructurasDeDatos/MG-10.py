"""
10. En cada opción del primer menú llamar a una función que permita solicitar 
los N valores de la lista (mínimo 15, máximo 25), regresar, mostrar la lista 
desordenada y llamar a la función para que realice ordenación de acuerdo a 
cada algoritmo, al regresar mostrar la lista ordenada.

Para el segundo menú llamar a una función que permita solicitar los N 
valores de la lista (mínimo 15, máximo 25), regresar, solicitar el valor a 
buscar y llamar a la función para que realice la búsqueda de acuerdo a cada 
algoritmo, mostrar si el valor se encuentra en la lista y cuantas veces esta, 
de lo contrario mostrar mensaje que no esta.

"""
# definir función que genera la lista de elementos ingresados
def listanum():
    lista = []
    while True:
        try:
            n = int(input("Ingresa el numero de elementos en la lista, entre 15 y 25: "))  
            if n >= 15 and n <= 25: 
                for i in range(0, n):
                    print("Ingresa valor", i+1,":")
                    e = input()
                    lista.append(e)
                print("La lista es: {}" .format(lista))
                break;
            else:
                print("valor inválido, vuelva a intentarlo. el número de elementos debe estar entre 15 y 25")      
        except ValueError:
            print("Valor Inválido, sólo se aceptan números")
            continue
    return lista

# función de salida del menú 
def salida():
   regreso = input("Quieres probar otro algoritmo? (si/no): ")
   if regreso == ("si"):
      regreso_menu= True
   elif regreso == ("no"):
      print("Gracias por ejecutar el programa, adiós")
      input()
   return(salida)

# algoritmos de ordenación
# 1 algoritmo de burbuja
def burbuja(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                temp= l[j]
                l[j]= l[j+1]
                l[j+1]= temp
    return l


# 2 algoritmo de inserción
def insercion(l):
    x=len(l)
    aux=0
    for i in range (0,x):
        for j in range(i,0,-1):
            if l[j-1]>l[j]:
                aux=l[j]
                l[j]=l[j-1]
                l[j-1]=aux
    return l
   
#3  algoritmo de selección
def seleccion(l):
    x=len(l)
    for i in range (0, x-1):
        for j in range (i+1, x):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l

# 4 algoritmo shell
def shell(l):
    x=len(l)
    aux=0
    z=x//2
    while z>0:
        for i in range(z,x):
            j=i
            aux=l[i]
            while(j>=z and l[j-z]>aux):
                l[j]=l[j-z]
                j=j-z
            l[j]=aux
        z=z//2

# 5  algoritmo de ordenación rápida
def quicksort(l):
    x=len(l)
    cen=[]
    de=[]
    iz=[]
    if x>1:
        pi=l[0]
        for i in l:
            if i<pi:
                iz.append(i)
            elif i==pi:
                cen.append(i)
            else:
                de.append(i)
        return quicksort(iz)+cen+quicksort(de)
    else:
        return l

# algoritmos de busqueda
# 1 algoritmo de búsqueda secuencial 
def secuencial(lista, valor):
    pos= 0
    enc= False
    while pos < len(lista) and not enc:
        if lista[pos] == valor:
            enc= True
        else:
            pos += 1
    return enc, pos

# 3 algoritmo de búsqueda binaria 
def binaria(arr, x, n):
    lo = 0
    hi = n - 1
    mid = 0

    while lo <= hi:
        mid = (hi + lo) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1

# mensaje de bienvenida
print("Programa 10 para probar algoritmos de búsqueda y ordenación")

# codigo para regresar a menu principal
regreso_menu = True
while regreso_menu == True:
   menu="""
   MENU PRINCIPAL
   1. Ordenación
   2. Búsqueda
   3. Terminar
   """
   print(menu)
   # input para escoger opción
   opcion = input ("Seleccione una opción de la 1 a la 3: ")
   # codigo si se escoge el menú de ordenación
   if opcion == "1":
   
      menu="""
      MENU ORDENACIÓN
      1. Burbuja
      2. Inserción
      3. Selección
      4. Shell
      5. Rápida
      6. Regresar
      """
      print(menu)
      opcion = input ("Seleccione una opción de la 1 a la 6: ")
      print("\n")
      #codigo si se escoge algoritmo burbuja
      if opcion == "1":
         print ("Escogiste Algoritmo de Burbuja")
         print("\n")
         lista = []
         while True:
            try:
               n = int(input("Ingresa el numero de elementos en la lista, entre 15 y 25: "))  
               if n >= 15 and n <= 25: 
                  for i in range(0, n):
                     print("Ingresa valor", i+1,":")
                     e = input()
                     lista.append(e)
                  print("La lista es: {}" .format(lista))
                  break;
               else:
                  print("valor inválido, vuelva a intentarlo. el número de elementos debe estar entre 15 y 25")      
            except ValueError:
               print("Valor Inválido, sólo se aceptan números")
               continue
         print("La lista ordenada es:")
         print(burbuja(lista))
         salida()
      # codigo si se escoge algoritmo de insercion
      elif opcion == "2":
         print("Escogiste Algoritmo de Inserción")
         print("\n")
         lista = []
         while True:
            try:
               n = int(input("Ingresa el numero de elementos en la lista, entre 15 y 25: "))  
               if n >= 15 and n <= 25: 
                  for i in range(0, n):
                     print("Ingresa valor", i+1,":")
                     e = input()
                     lista.append(e)
                  print("La lista es: {}" .format(lista))
                  break;
               else:
                  print("valor inválido, vuelva a intentarlo. el número de elementos debe estar entre 15 y 25")      
            except ValueError:
               print("Valor Inválido, sólo se aceptan números")
               continue
         print("La lista ordenada es:")
         print(insercion(lista))
         salida()
      # codigo si se escoge algoritmo de selección
      elif opcion == "3":
         print ("Escogiste Algoritmo de Selección")
         print("\n")
         lista = []
         while True:
            try:
               n = int(input("Ingresa el numero de elementos en la lista, entre 15 y 25: "))  
               if n >= 15 and n <= 25: 
                  for i in range(0, n):
                     print("Ingresa valor", i+1,":")
                     e = input()
                     lista.append(e)
                  print("La lista es: {}" .format(lista))
                  break;
               else:
                  print("valor inválido, vuelva a intentarlo. el número de elementos debe estar entre 15 y 25")      
            except ValueError:
               print("Valor Inválido, sólo se aceptan números")
               continue
         print("La lista ordenada es:")
         print(seleccion(lista))
         salida()
      # codigo si se escoge algoritmo shell
      elif opcion == "4":
         print ("Escogiste Algoritmo Shell")
         print("\n")
         lista = []
         while True:
            try:
               n = int(input("Ingresa el numero de elementos en la lista, entre 15 y 25: "))  
               if n >= 15 and n <= 25: 
                  for i in range(0, n):
                     print("Ingresa valor", i+1,":")
                     e = input()
                     lista.append(e)
                  print("La lista es: {}" .format(lista))
                  break;
               else:
                  print("valor inválido, vuelva a intentarlo. el número de elementos debe estar entre 15 y 25")      
            except ValueError:
               print("Valor Inválido, sólo se aceptan números")
               continue
         print("La lista ordenada es:")
         print(shell(lista))
         salida()
      #codigo si se escoge algoritmo ordenación rápido
      elif opcion == "5":
         print ("Escogiste Algoritmo de Quick Sort")
         print("\n")
         lista = []
         while True:
            try:
               n = int(input("Ingresa el numero de elementos en la lista, entre 15 y 25: "))  
               if n >= 15 and n <= 25: 
                  for i in range(0, n):
                     print("Ingresa valor", i+1,":")
                     e = input()
                     lista.append(e)
                  print("La lista es: {}" .format(lista))
                  break;
               else:
                  print("valor inválido, vuelva a intentarlo. el número de elementos debe estar entre 15 y 25")      
            except ValueError:
               print("Valor Inválido, sólo se aceptan números")
               continue
         print("La lista ordenada es:")
         print(quicksort(lista))
         salida()
      # codigo si se escoge regresar 
      elif opcion == "6":
            regreso_menu= True
   # codigo si se escogió menú de búsqueda
   elif opcion == "2":
      menu="""
      MENU ORDENACIÓN
      1. Secuencial
      2. Interpolación
      3. Binaria
      4. Regresar
      """
      print(menu)
      opcion = input ("Seleccione una opción de la 1 a la 4: ")
      #codigo si se escoge algoritmo secuencial
      if opcion == "1":
         print ("Escogiste Algoritmo de Búsqueda Secuencial")
         print("\n")
         lista = []
         l=int(input("Escribe la cantidad de numeros que tiene tu lista (minimo 15 y maximo 25): "))
         while l < 15 or l > 25:
            print("valor incorrecto... intenta de nuevo ")
            l=int(input("Escribe la cantidad de numeros que tiene tu lista (minimo 15 y maximo 25): "))
         for i in range(0,l):
            d= int(input("Ingresa el valor " + str(i+1) + ": "))
            lista.append(d)
         v= int(input("Escribe el valor a buscar: "))
         print("valor en la lista, posicion: " + str(secuencial(lista, v)))
         input()
         salida()
      # codigo si se escoge algoritmo de búsqueda de interpolación
      elif opcion == "2":
         print("Escogiste Algoritmo de Búsqueda de Interpolación")
         print("\n")
         lista = []
         while True:
            try:
               n = int(input("Ingresa el numero de elementos en la lista, entre 15 y 25: "))  
               if n >= 15 and n <= 25: 
                  for i in range(0, n):
                     print("Ingresa valor", i+1,":")
                     e = input()
                     lista.append(e)
                  print("La lista es: {}" .format(lista))
                  break;
               else:
                  print("valor inválido, vuelva a intentarlo. el número de elementos debe estar entre 15 y 25")      
            except ValueError:
               print("Valor Inválido, sólo se aceptan números")
               continue
         salida()
      # codigo si se escoge algoritmo de búsqueda binaria
      elif opcion == "3":
         print ("Escogiste Algoritmo de Búsqueda Binaria")
         print("\n")
         listan = []
         l=int(input("Escribe la cantidad de numeros que tiene tu lista (minimo 15 y maximo 25): "))
         while l < 15 or l > 25:
            print("valor incorrecto... intenta de nuevo ")
            l=int(input("Escribe la cantidad de numeros que tiene tu lista (minimo 15 y maximo 25): "))
         for i in range(0,l):
            d= int(input("Ingresa el valor " + str(i+1) + ": "))
            listan.append(d)
         n= len(listan)
         v= int(input("Escribe el valor a buscar: "))

         print("valor en la lista, posicion: " + str(binaria(listan, v, n)))
         salida()
      # codigo si se escoge regresar
      elif opcion == "4":
            regreso_menu = True
   # codigo si se escogió terminar programa
   elif opcion == "3":
      print("Gracias por ejecutar el programa, adiós")
      input()



