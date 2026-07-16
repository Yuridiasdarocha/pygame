#Solicita valores ao usuário
maca = float(input("Quantos kg de maça você comprou? "))
morango = float(input("Quantos kg de morango você comprou? "))
#Faz a condição
if morango <= 5:
    precomorango = morango * 2.50
else:
    precomorango = morango * 2.20
if maca <= 5:
    precomaca = maca * 1.80
else:
    precomaca = maca * 1.50
subtotal = precomaca + precomorango
totalkg = maca + morango
if (totalkg > 8) or (subtotal > 25):
    desconto = subtotal * 0.10
else:
    desconto = 0
totalapagar = subtotal - desconto
print (f"Total a pagar: {totalapagar}.")
print (f"Desconto: {desconto}.")
