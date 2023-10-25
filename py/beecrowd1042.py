n1, n2, n3 = map(int, input().split())

if n1 > n2 and n1 > n3:
    maior = n1 
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1 
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

if n1 > menor and n1 < maior:
    meio = n1
elif n2 > menor and n2 < maior:
    meio = n2
elif n3 > menor and n3 < maior:
    meio = n3

print(menor)
print(meio)
print(maior)
print("")
print(n1)
print(n2)
print(n3)