numero_digitado = int(input())
quociente = 1
lista = []
while quociente >= 1:
    resto = numero_digitado % 2
    lista.insert(0, resto)
    quociente = numero_digitado // 2
    
