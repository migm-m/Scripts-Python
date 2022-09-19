"""
5. Hagamos una simulación de la población de lobos y conejos de un ecosistema. Los
conejos comen hierba y los lobos comen conejos. Supongamos que hay suficiente hierba
en el ecosistema, por lo que el único obstáculo para que crezca la población de conejos es
la población de lobos y sabemos que la población de lobos incrementa con la población
de conejos.
Los cambios diarios en la población de conejos (C) y la población de lobos (L), se
pueden expresar mediante las siguientes fórmulas, donde (mañana) es el cálculo de la
población del día siguiente y (hoy) es la población actual:
C (mañana) = (1 + a) * C(hoy) - c * C(hoy) * L (hoy)
L(mañana) = (1 - b) * L(hoy) + c * d * C(hoy)*L(hoy)
a = 0.01
b = 0.005
c = 0.00001
d = 0.01
En donde:
- a es el aumento fraccional de la población de conejos sin amenaza de lobos
- b es la disminución fraccional de la población de lobos sin conejos que comer
- c es la probabilidad de que un lobo se encuentre y coma un conejo
- d es el aumento fraccional en la población de lobos atribuido a un conejo devorado
Supongamos que inicialmente hay 10,000 conejos y 1,000 lobos.
Escriba un programa con una función que permita calcular las poblaciones de conejos y lobos en un
período de 1000 días. Haga que el programa imprima las poblaciones cada 25 días
"""

# mensaje de bienvenida
print("Programa 5 para sa calcular las poblaciones de conejos y lobos en un período de 1000 días.")
print("\n")

#declarar función
def pob(con, lob):

    # declarar variables
    a = 0.01      # a es el aumento fraccional de la población de conejos sin amenaza de lobos
    b = 0.005     # b es la disminución fraccional de la población de lobos sin conejos que comer
    c = 0.00001   # c es la probabilidad de que un lobo se encuentre y coma un conejo
    d = 0.01      # d es el aumento fraccional en la población de lobos atribuido a un conejo devorado

    # ciclo para calcular población por día 
    for i in range(0, 1001):
        # se declaran las fórmulas para calcular la población por día
        pcm = (1 + a) * con - c * con * lob         # población conejos mañana     
        plm = (1 - b) * lob + c * d * con * lob     # población lobos mañana
        con = pcm
        lob = plm


        # se hace el modulo del iterador para imprimir la población total de conejos y lobos cada 25 días
        if i %25 ==0:
            print("Dia: ", i)
            print("La población de conejos es de: {:.2f}" .format(con))
            print("La población de lobos es de: {:.2f} " .format(lob))
            print("\n")

# declarar población inicial 
pc = 10000  # población de conejos hoy
pl = 1000   # población de lobos hoy

# regresa la lista y la imprime
pob(pc, pl)

# fin del programa
#para que no se cierre automaticamente el programa después de la ejecución
input()