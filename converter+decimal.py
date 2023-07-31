dividendo = int(input())
numero_digitado = dividendo
quociente = 1
lista = []
sep = []
while quociente >= 1:
    resto = numero_digitado % 2
    lista.insert(0, resto)
    quociente = dividendo // 2
    dividendo = quociente

binario = "".join(lista)
print(binario)