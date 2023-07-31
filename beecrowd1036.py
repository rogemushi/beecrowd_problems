import math
raizes = input()
raizes_lista = raizes.split(" ")
pode = True

def raiz(zap):
    delta = (float(zap[1])**2) - 4 * (float(zap[0]))*(float(zap[2]))
    x1 = (-float(zap[1]) + math.sqrt(delta))/(2*float(zap[0]))
    x2 = (-float(zap[1]) - math.sqrt(delta))/(2*float(zap[0]))


    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")


for i in raizes_lista:
    if float(i) == 0:
        print("Impossivel calcular")
        pode = False
        break

if pode == True:
    raiz(raizes_lista)