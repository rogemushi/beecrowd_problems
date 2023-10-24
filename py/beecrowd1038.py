produto, quantidade = map(int, input().split())

if produto == 1:
    price = 4
elif produto == 2:
    price = 4.50
elif produto == 3:
    price = 5
elif produto == 4:
    price = 2
elif produto == 5:
    price = 1.50
valor = price*quantidade

print(f"Total: R$ {valor:.2f}")