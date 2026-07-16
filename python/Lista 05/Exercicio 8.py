nomevencedora = ""
maiornota = -1.0
for i in range(1, 17):
    print (f"Canditada {i}º ")
    nome = input(str("Nome da canditada: "))
    nota = float(input("Digite a nota (0 a 10): "))
    
    while nota < 0 or nota > 10:
        print ("Nota inválida digite uma nota (0 a 10)")
        nota = float(input("Digite a nota (0 a 10): "))

    if nota > maiornota:
        maiornota = nota
        nomevencedora = nome

print (f"A vencedora foi {nomevencedora} com a nota de {maiornota:.2f}")