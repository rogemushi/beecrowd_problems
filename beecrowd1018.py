notas = (100, 50, 20, 10, 5, 2, 1)

entrada = int(input())

def contar(j):
    if j != 0:
        for i in notas:
            qnt = j // i
            print(f"{qnt} nota(s) de R$ {i},00")
            j = j - (qnt * i)
            
    else:
        return 0
        
contar(entrada)
