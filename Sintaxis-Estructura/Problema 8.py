menu = """
Porfavor, teclee una opcion para calcular el volumen de la figura o salir del menu.

a) Cono recto
b) Cubo
c) Cilindro recto
d) Prisma recto
e) Esfera
f) Terminar

"""
print(menu)
opcion = input('Digite una letra entre la a y la f: ')
if opcion == 'a':
    import math    
    radio = float(input("Ingrese el radio del cono: "))
    altura = float(input("Ingrese la altura del cono: "))
    base= math.pi * radio**2
    volumen_conorecto = (base * altura)/3
    print ("El volumen del cono recto es", volumen_conorecto)
elif opcion == 'b':
    lado = float(input("Ingrese el valor de los lados del cubo: "))
    volumen_cubo = lado**3
    print ("El volumen de el cubo es", volumen_cubo)
elif opcion == 'c':
    import math
    radiocr = float(input("Ingrese el radio del cilindro: "))
    alturacr = float(input("Ingrese la altura del cono: "))
    volumencr = math.pi * radiocr**2 * alturacr
    print ("El volumen del cilindro recto es", volumencr)
elif opcion == 'd':
    lado1 = float(input("Ingresa el valor de un lado del prisma: "))
    lado2 = float(input("Ingresa el valor de un lado diferente del prisma: "))
    alturap = float(input("Ingrese la altura del prisma: "))
    basepr = lado1 * lado2
    volumenpr = basepr * alturap
    print ("El volumen de el cubo es", volumenpr)
elif opcion == 'e':
    import math
    radioe = float (input("Ingresa el radio de tu esfera: "))
    volumene = (4/3) * math.pi * radioe**3
    print ("El volumen de la esfera es", volumene)
elif opcion == 'f':
    pass