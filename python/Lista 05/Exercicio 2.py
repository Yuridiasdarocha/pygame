nota1 = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual sua segunda nota? "))
nota3 = float(input("Qual sua terceira nota? "))
mediaexercicio = float(input("Qual sua média dos exercicios? "))

media = (nota1 + (nota2 * 2) + (nota3 * 3) + mediaexercicio) / 7
print (f"Sua média é: {media:.2f}")
if media >= 9:
    print ("Conceito A")
elif (media >= 7.5) and (media < 9):
    print ("Conceito B")
elif (media >= 6) and (media < 7.5):
    print ("Conceito C")
elif media < 6:
    print ("Conceito D")