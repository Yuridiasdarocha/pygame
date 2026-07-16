velocidadecarro = int(input("Qual a velocidade do carro? "))
if velocidadecarro > 80:
    acima = velocidadecarro - 80
    valormulta = acima * 50
    print (f"Você foi multado, Valor da multa: {valormulta}")
elif velocidadecarro <= 0:
    print ("A velocidade tem que ser maior que 0")
else:
    print ("Você não foi multado")