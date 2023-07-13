notas = (100, 50, 20, 10, 5, 2, 1)
entrada = int(input())
j = entrada

if j != 0:
        for i in notas:
            
            print("{} nota(s) de R$ {},00".format(int(j/i), i))
            aux = (j%i)
            j = aux


