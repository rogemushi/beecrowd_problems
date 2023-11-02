x = 0

def pares(x):
    if x<100:
        print(x+2)
        pares(x+2)
    else:
        pass
pares(x)