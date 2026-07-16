deposito = float(input("Qual o valor do deposito? "))
depositomensal = float(input("Qual o valor de deposito mensal? "))
taxa = float(input("Qual a porcentagem da taxa? "))
mes = 1
totalinvestido = deposito
saldo = deposito
taxadecimal = taxa / 100
while mes <=24:
   saldo = saldo + depositomensal
   totalinvestido = totalinvestido + depositomensal
   saldo = saldo + (saldo * taxadecimal)
   print (f"Mês {mes} saldo {saldo:.2f}")
   mes = mes + 1
juros = saldo - deposito
print (f"O total de lucro foi: {juros:.2f}")