km = float(input("Quantos km você pecorreu? "))
dias = float(input("Quantos dias o carro ficou alugado? "))
valordia = dias * 120
valorkm = km * 0.15
valorfinal = valordia + valorkm
print (f"Valor dos dias: {valordia}")
print (f"Valor dos km: {valorkm}")
print (f"Valor a pagar: {valorfinal}")