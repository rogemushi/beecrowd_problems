import math


def ler():
    raizes = input()
    raizes_lista = raizes.split()

    lista = [float(i) for i in raizes_lista]
    return lista

def delta(lista):
    a = lista[0]
    b = lista[1]
    c = lista[2]

    del_p1 = b **2
    del_p2 = -4*(a)*(c)

    delta_nm = del_p1 + del_p2
    return delta_nm

def bhaskara(lista):
    a = lista[0]
    b = lista[1]
    c = lista[2]

    upper_eq1 = -b + math.sqrt(delta(lista))
    upper_eq2 = -b - math.sqrt(delta(lista))
    lower_eq = 2 * a

    eq_1 = upper_eq1/lower_eq
    eq_2 = upper_eq2/lower_eq

    resultado = [eq_1, eq_2]
    return resultado


def validade(lista, delta):
    x
    
    if lista[0] == 0:
        x = "Impossivel calcular"
    if delta <= 0:
        x = "Impossivel calcular"
    else: 
        x = bhaskara(lista)
    
    return x
    
lista = ler()
print(validade(lista, delta(lista)))

# def raiz(zap):
#     delta = (float(zap[1])**2) - (4 * (float(zap[0]))*(float(zap[2])))
#     raiz_delta = math.sqrt(delta)
#     x1 = (-float(zap[1]) + raiz_delta)/(2*float(zap[0]))
#     x2 = (-float(zap[1]) - raiz_delta)/(2*float(zap[0]))


#     print(f"R1 = {x1:.5f}")
#     print(f"R2 = {x2:.5f}")


# for i in raizes_lista:
#     if float(i) == 0:
#         print("Impossivel calcular")
#         pode = False
#         break

# if pode == True:
#     raiz(raizes_lista)


# # terminar de fazer o algorítmo