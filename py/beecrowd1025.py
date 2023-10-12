n = str(input())



def ler_soma (n):
    numeros = n.split(" ")
    n1 = int(numeros[0])
    n2 = int(numeros[1])
    n1_bin = bin(n1)
    n2_bin = bin(n2)
    print(f"{n1_bin} + {n2_bin}")


ler_soma(n)