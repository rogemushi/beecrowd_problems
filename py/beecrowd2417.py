c_vitorias, c_empates, c_gols, f_vitorias, f_empates, f_gols = map(int, input().split())

c_pontos = (c_vitorias*3)+(c_empates)
f_pontos = (f_vitorias*3)+(f_empates)

if c_pontos > f_pontos:
    print("C")
elif c_pontos < f_pontos:
    print("F")
else:
    if c_gols > f_gols:
        print("C")
    elif c_gols < f_gols:
        print("F")
    else: 
        print("=")