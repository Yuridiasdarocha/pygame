mercadoria = float(input("Qual é o valor da mercadoria? "))
percentual = float(input("Qual o percentual de desconto? "))
desconto = mercadoria * percentual
valorfinal = mercadoria + desconto
print (f"Valor do desconto: {desconto}.")
print (f"Valor final a pagar {valorfinal}.")