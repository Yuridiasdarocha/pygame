comeco = float (input("Hora de inicio: "))
fim = float (input("Hora do fim: "))
if fim >= comeco:
    duracao = fim - comeco
else:
    duracao = 24 - comeco + fim
print (f"Duração do jogo: {duracao} horas.")