_, dia_inicio = input().split()

hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))

segundos_totais_inicio = 0
segundos_totais_inicio += int(dia_inicio) * (60*60*24)
segundos_totais_inicio += hora_inicio * (60*60)
segundos_totais_inicio += minuto_inicio * (60)
segundos_totais_inicio += segundo_inicio

_, dia_fim = input().split()

hora_fim, minuto_fim, segundo_fim = map(int, input().split(" : "))

segundos_totais_fim = 0
segundos_totais_fim += int(dia_fim) * (60*60*24)
segundos_totais_fim += hora_fim * (60*60)
segundos_totais_fim += minuto_fim * (60)
segundos_totais_fim += segundo_fim

segundos_passados = segundos_totais_fim - segundos_totais_inicio

dia_contado = segundos_passados // (60*60*24)
hora_contado = (segundos_passados % (60*60*24)) // (60*60)
minuto_contado = ((segundos_passados % (60*60*24)) % (60*60)) // (60)
segundos_contado = ((segundos_passados % (60*60*24)) % (60*60)) % (60)


print(f"{dia_contado} dia(s)")
print(f"{hora_contado} hora(s)")
print(f"{minuto_contado} minuto(s)")
print(f"{segundos_contado} segundo(s)")