contdivisores = 0
divisores = [] 
numero = int(input("Digite um número inteiro positivo: "))
if numero <= 1:
    print (f"O número {numero} não é primo.")
else:
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    if len(divisores) == 2:
        print (f"O número {numero} é primo!")
    else:
        print (f"O número {numero} não é primo!")
        print (f"Ele é divisível por: {divisores}.")

