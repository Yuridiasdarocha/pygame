# Pergunta quantas pizzas serão pedidas
pizzas = int(input("Quantas pizzas? "))
# Pergunta quantos chopps devem ser consumidos
chopp = int(input("Quantos chopps? "))
# Pergunta quantas coberturas a mais serão usadas
coberturas = int(input("Quantas coberturas? "))
# Pergunta para quantas pessoas será dividido o valor
pessoas = int(input("Quantas pessoas? "))

# Calcula o custo das pizzas
valorpizza = pizzas * 50.00
# Calcula o custo dos chopps
valorchopp = chopp * 5.00
# Calcula o custo das coberturas
valorcobertura = coberturas * 2.50
# Soma todos os custos antes da taxa
valorbruto = valorpizza + valorchopp + valorcobertura
# Calcula a taxa de serviço de 10%
taxagarcom = valorbruto * 0.10
# Valor total com a taxa
valorfinal = valorbruto + taxagarcom
# Divide o total pelo número de pessoas
valorporpessoa = valorfinal / pessoas

# Mostra o valor total e o valor por pessoa
print (f"Valor a pagar: {valorfinal:.2f}.")
print (f"Valor por pessoa: {valorporpessoa:.2f}.")
