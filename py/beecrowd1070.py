numero_inicial = int(input())
iteracoes = 6

while iteracoes > 0:
    if (numero_inicial) % 2 != 0:
        print(numero_inicial)
        iteracoes -= 1
    else:
        pass
    numero_inicial += 1