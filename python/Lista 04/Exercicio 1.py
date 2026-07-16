saldo = float (input("Qual o seu saldo? "))
debito = float (input("Quanto de debito você tem? "))
credito = float (input("Quantos de crédito você tem? "))
resultado = saldo - debito + credito
if resultado >= 0:
    print (f"O seu saldo é positivo! Saldo: {resultado}")
else:
    print (f"O seu saldo é negativo! Saldo: {resultado}")