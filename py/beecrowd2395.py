a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

largura = x // a
comprimento = y // b
altura = z // c

total_conteineres = (largura * comprimento) * altura
print(total_conteineres)