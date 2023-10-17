valor_inicial = float(input())

def contar_notas (entrada_valor):
    notas = [100,50,20,10,5,2]
    moedas = [1,0.5,0.25,0.10,0.05,0.01]

    caixa = entrada_valor

    print("NOTAS:")
    for i in range(len(notas)):
        nota = caixa // notas[i]
        caixa = caixa % notas[i]
        print(f"{int(nota)} nota(s) de R$ {notas[i]:.2f}")
    
    print("MOEDAS:")
    for i in range(len(moedas)):
        moeda = caixa // moedas[i]
        caixa = caixa % moedas[i]
        print(f"{int(moeda)} moeda(s) de R$ {moedas[i]:.2f}")

contar_notas(valor_inicial)