nome = str(input("Qual o nome do produto ?"))
quantidade = int(input("Qual a quantidade adquirida? "))
preco = float(input("Qual o preço unitário? "))
if quantidade <= 5:
    desconto = 0.02
elif (quantidade > 5) and quantidade <= 10:
    desconto = 0.03
elif quantidade > 10:
    desconto = 0.05

total = quantidade * preco
valordesconto = total * desconto
valorfinal = total - valordesconto

print (f"Preço bruto: {total:.2f}.")
print (f"Desconto: {valordesconto:.2f}.")
print (f"Total a pagar: {valorfinal:.2f}.")