numero1 = float (input("Qual o primeiro número? "))
numero2 = float (input("Qual o segundo número? "))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
print (f"Soma: {soma}")
print (f"Subtração: {subtracao}")
print (f"Multiplicação: {multiplicacao}")
if numero2 == 0:
    print ("Não é possível efetuar a divisão")
else:
    divisao = numero1 / numero2
    print (f"Divisão: {divisao}")
