def impares_6(num, cont):
    if cont >= 6: return 0
    elif num%2 != 0:
        print(num)
        impares_6(num+1, cont+1)
    else: impares_6(num+1, cont)

impares_6(int(input()), cont=0)