L, C, X, Y = map(int, input().split())

if X == Y:
    print("Direita")
elif ((X+1) % (Y+1)) == 0 or ((Y+1) % (X+1)) == 0:
    print("Direita")
elif ((X+1) % (Y+1)) != 0:
    print("Esquerda")