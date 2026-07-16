soma = 0
quantidade = 0
while True:
    numero = int (input("Digite um número inteiro ou 0 para sair: "))
    if numero == 0:
        break
    soma = numero + soma
    quantidade = quantidade + 1
    if quantidade > 0:
        media = soma / quantidade
        print (f"Quantidade de números {quantidade}: ")
        print (f"Soma dos números: {soma:.2f}.")
        print (f"Média aritmética: {media:.2f}")
    else:
        print (f"Nenhum número além de 0 foi digitado.")