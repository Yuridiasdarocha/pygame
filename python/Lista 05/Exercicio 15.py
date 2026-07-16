import random
sorteados = []
acimadecinco = 0
divisivelpor3 = 0
for i in range(20):
    numero = random.randint(0, 10)
    sorteados.append(numero)
    if numero > 5:
        acimadecinco += 1
    if numero % 3 == 0 and numero != 0:
        divisivelpor3 += 1

print (f"Números sorteados: {sorteados}")
print (f"Números acima de 5: {acimadecinco}")
print (f"Números divisíveis por 3: {divisivelpor3}")
