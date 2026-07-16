lado1 = float(input("Qual o comprimento do primeiro lado? "))
lado2 = float(input("Qual o comprimento do segundo lado? "))
lado3 = float(input("QUal o comprimento do terceiro lado? "))
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print ("Os valores podem formar um triângulo!")
if lado1 == lado2 == lado3:
    print ("O triângulo é Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print ("O triângulo é Isósceles")
elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print ("O triângulo é Escaleno")
else:
    print ("Esses valores não formam um triângulo")