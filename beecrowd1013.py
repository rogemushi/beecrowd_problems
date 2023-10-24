numeros = str(input())
numeros = numeros.split(" ")

def maioral(numeros):
    n = 0
    maior = 0
    for num in numeros:
        num = int(num)
        if maior < num:
            maior = num
        else: 
            break   
            
    n += 1

    return maior

print(f"{maioral(numeros)} eh o maior")