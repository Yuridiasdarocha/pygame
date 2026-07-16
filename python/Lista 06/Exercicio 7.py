salariobase = 2500.00
comissao = 200.00
nome = str(input("Qual o seu nome? "))
imoveis = int(input("Quantos imóveis você vendeu? "))
vendas = float(input("Qual o valor total de suas vendas? "))
pvendas = vendas * 0.05
cimoveis = imoveis * 200.00
salariofinal = salariobase + pvendas + cimoveis
print (f"O valor final do seu salário é: {salariofinal}.")