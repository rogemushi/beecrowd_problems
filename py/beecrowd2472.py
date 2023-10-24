comprimento_l, quantidade_n = map(int, input().split())
fator_tapetes_menores = quantidade_n-1
fator_maior = comprimento_l - fator_tapetes_menores
valor_total = (fator_maior**2) + fator_tapetes_menores
print(valor_total)
