x = int(input())
y = int(input())

def soma_impares_intervalo(x,y):
    
    if x > y:
        max = x
        min = y
    else: 
        max = y
        min = x

    somador = 0
    
    for i in range((min+1), max):
        if ((i%2) != 0):
            somador += i
    return somador

print(soma_impares_intervalo(x,y))