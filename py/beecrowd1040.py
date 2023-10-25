nota_1, nota_2, nota_3, nota_4 = map(float, input().split())

media = ((nota_1*2) + (nota_2*3) + (nota_3*4) + (nota_4*1))/(2+3+4+1)

if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
else:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    n_prova = float(input())
    media_final = (media+n_prova)/2
    print(f"Nota do exame: {n_prova:.1f}")
    if n_prova >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {media_final:.1f}")
