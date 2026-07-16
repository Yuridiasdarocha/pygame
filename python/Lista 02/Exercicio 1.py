nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
nota3 = float(input("Qual a terceira nota? "))
media = (nota1 + nota2 + nota3) / 2
if media >= 7:
    print (f"Você foi aprovado! Média: {media}")
else:
    print (f"Você foi reprovado! Média: {media}")