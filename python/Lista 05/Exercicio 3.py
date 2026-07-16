anonascido = int (input("Qual seu ano de nascimento? "))
anoentrou = int (input("Em qual ano você entrou na empresa? "))
idade = 2026 - anonascido
anostrabalhados = 2026 - anoentrou
if (idade >= 65) or (anostrabalhados >= 25):
    print ("Requerer aposentadoria.")
elif anostrabalhados >= 30:
    print ("Requerer aposentadoria.")
elif (idade >= 60) and (anostrabalhados >= 25):
    print ("Requerer aposentadoria.")
else:
    print ("Não requerer aposentadoria.")
