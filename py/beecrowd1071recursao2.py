x = int(input())
y = int(input())


def percorrer(n1, n2, x):
    operador = n1
    fim = n2
    somador = x

    if operador > n2:
        print(somador)
    else:
        if operador%2 != 0:
            somador += operador
        else:
            pass
        operador+=1
        percorrer(operador, fim, somador)

percorrer(min(x,y), max(x,y)-1,0)