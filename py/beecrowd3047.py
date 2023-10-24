idade_monica = int(input())
idade_f1 = int(input())
idade_f2 = int(input())

idade_f3 = idade_monica - idade_f1 - idade_f2

if idade_f1 > idade_f2 and idade_f1 > idade_f3:
    maior = idade_f1
elif idade_f2 > idade_f1 and idade_f2 > idade_f3:
    maior = idade_f2
else:
    maior = idade_f3

print(maior)  