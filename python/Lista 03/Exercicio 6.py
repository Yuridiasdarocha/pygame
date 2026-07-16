salariofixo = float (input("Qual o seu salário fixo por mês? "))
comissaocarrovendido = float (input("Qual a comissão por cada carro vendido? "))
vendas = int (input("Quantos carros você vendeu? "))
valorvendas = float (input("Qual valor total de suas vendas? "))
resultado1 = comissaocarrovendido * vendas
resultado2 = valorvendas * 0.05
resultadofinal = salariofixo + resultado1 + resultado2
print (f"O seu salário final é de {resultadofinal}.")
