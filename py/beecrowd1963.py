valor_1, valor_2 = map(float, input().split())

diferenca = valor_2 - valor_1
porcentagem = diferenca / (valor_1 / 100) 

print(f'{porcentagem:.2f}%')
