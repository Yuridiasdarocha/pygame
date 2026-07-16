tipo = str(input("(A) de alcool (G) gasolina."))
litros = float(input("Quantos litros você abasteceu? "))
precolitro = 0
desconto = 0

valido = True

if (tipo == ("A")) or (tipo == ("a")):
    precolitro = 3.90
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

elif (tipo == ("G")) or (tipo == ("g")):
    precolitro = 6.30
    if  litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

else:
        print ("Tipo inválido!")
        valido = False

precobruto = precolitro * litros
valordesconto = precobruto * desconto
valorfinal = precobruto - valordesconto
print (f"Preço bruto: {precobruto}")
print (f"Desconto: {valordesconto}")
print (f"Valor final: {valorfinal}")
