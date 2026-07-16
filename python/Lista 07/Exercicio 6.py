qntdkwh = float(input("Quantidade de kWh consumida: "))
tipoinstalacao = str(input("Tipo de instalação: (R) para residência (C) para comércio (I) para indústrias: "))
if (tipoinstalacao == "R") or (tipoinstalacao == "r"):
    if qntdkwh <= 500:
        valorkwh = 0.40
    else:
        valorkwh = 0.65
    valorapagar = qntdkwh * valorkwh

elif (tipoinstalacao == "C") or (tipoinstalacao == "c"):
    if qntdkwh <= 1000:
        valorkwh = 0.55
    else:
        valorkwh = 0.60
    valorapagar = qntdkwh * valorkwh

elif (tipoinstalacao == "I") or (tipoinstalacao == "i"):
    if qntdkwh <= 500:
        valorkwh = 0.55
    else:
        valorkwh = 0.60
    valorapagar = qntdkwh * valorkwh
else:
    print ("Tipo inválido")
    valorapagar = 0
print (f"Valor a pagar: {valorapagar}.")
