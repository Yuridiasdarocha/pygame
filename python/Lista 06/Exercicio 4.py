#Solicita a velocidade em km para o usuário
velocidadekm = float(input("Qual a velocidade em kmh? "))
#Faz a conversão
velocidadems = velocidadekm / 3.6
#Imprime o resultado
print (f"{velocidadekm} em m/s é: {velocidadems:.2f}.")