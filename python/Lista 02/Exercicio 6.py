valor1 = float (input("Qual o primeiro valor? "))
valor2 = float (input("Qual o segundo valor? "))
valor3 = float (input("Qual o terceiro valor? "))
if valor1 > valor2 and valor1 > valor3:
    print (f"O primeiro valor é o maior: {valor1} ")
elif valor2 > valor1 and valor2 > valor3:
    print (f"O segundo valor é o maior: {valor2} ")
elif valor3 > valor1 and valor3 > valor2:
    print (f"O terceiro valor é o maior: {valor3}")