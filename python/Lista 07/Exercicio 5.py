valorcasa = float(input("Qual o valor da casa? "))
valorsalario = float(input("Qual o seu salário? "))
quantidadeanos = float(input("Em quantos anos você pretende pagar a casa? "))
meses = quantidadeanos * 12
valorprestacao = valorcasa / meses
trintasalario = valorsalario * 0.30
if valorprestacao < trintasalario:
    print (f"Conceder empréstimo")
else:
    print (f"Não conceder empréstimo") 