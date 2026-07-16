valor1 = float (input("Qual o primeiro valor? "))
valor2 = float (input("Qual o segundo valor? "))
if valor2 == 0:
    valor2 = float (input("O segundo valor não pode ser 0: "))

resultado = valor1 / valor2

print (f"Valor1 / valor2: {resultado:.2f}")