somaprimos = 0
for numero in range (1, 101):
    if numero >1:
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        if len(divisores) == 2:
            somaprimos += numero

print (f"A soma de todos os números primos é: {somaprimos}")

