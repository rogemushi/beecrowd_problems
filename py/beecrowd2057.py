hora_inicial, tempo_viagem, fuso = map(int, input().split())
tempo= hora_inicial + tempo_viagem + fuso
if tempo > 24:
    tempo = tempo % 24
elif tempo < 0:
    tempo = tempo + 24
print(tempo)
    