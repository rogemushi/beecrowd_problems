

age = int(input())

anos = age // 365
resto = age % 365
meses = resto // 30
dias = resto % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
