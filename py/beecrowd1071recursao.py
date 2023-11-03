
def maior(n1, n2):
    if n1 > n2: return n1
    else: return n2

def menor(n1, n2):
    if n1 > n2: return n2
    else: return n1

def intervalo():
    x = int(input())
    y = int(input())

    return maior(x,y)+menor(x,y)

def impares_6(num, cont, int):      
    soma = 0 

    if cont >= int: return 0
    elif num%2 != 0:
        soma += num
        impares_6(num+1, cont+1)
    else: impares_6(num+1, cont)

impares_6(intervalo(), cont=0)