valor1 = int(input("Qual o primeiro valor? "))
valor2 = int(input("Qual o segundo valor? "))
valor3 = int(input("Qual o terceiro valor? "))
if (valor1 > valor2 and valor2 > valor3 and valor1 > valor3):
    print (f"Ordem decrescente:{valor1} {valor2} {valor3}")
elif (valor1 > valor2 and valor3 > valor2 and valor1 > valor3):
    print (f"Ordem decrescente: {valor1} {valor3} {valor2}")
elif (valor2 > valor1 and valor2 > valor3 and valor1 > valor3):
    print (f"Ordem decrescente: {valor2} {valor1} {valor3}")
elif (valor2 > valor1 and valor2 > valor3 and valor3 > valor1):
    print (f"Ordem decrescente: {valor2} {valor3} {valor1}")
elif (valor3 > valor1 and valor3 > valor2 and valor1 > valor2):
    print (f"Ordem decrescente: {valor3} {valor1} {valor2}")
elif (valor3 > valor1 and valor3 > valor2 and valor2 > valor1):
    print (f"Ordem decrescente: {valor3} {valor2} {valor1}")
    