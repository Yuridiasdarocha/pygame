time1 = str(input("Qual nome do primeiro time? "))
gols1 = int(input(f"Quantos gols {time1} fez? "))
time2 = str(input("Qual nome do primeiro time? "))
gols2 = int(input(f"Quantos gols {time2} fez? "))
if gols1 == gols2:
    print (f"A partida de {time1} e {time2} ficou empatada!")
elif gols1 > gols2:
    print (f"O {time1} foi o vencedor!")
else:
    print (f"O {time2} foi o vencedor!")