idade = int(input("Qual a sua idade? "))
meses = int(input("Quantos meses? "))
dias = int(input("Quantos dias ?"))
anosemdias = idade * 365
mesesemdias = meses * 30
resultado = anosemdias + mesesemdias + dias
print (f"Sua idade apenas em dias é: {resultado}.")